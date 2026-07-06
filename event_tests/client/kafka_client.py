import json
import time
import uuid

from event_tests.config.settings import (
    CONSUME_TIMEOUT_SECONDS,
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_SASL_MECHANISM,
    KAFKA_SASL_PASSWORD,
    KAFKA_SASL_USERNAME,
    KAFKA_SECURITY_PROTOCOL,
    PRODUCE_TIMEOUT_SECONDS,
)

# Import perezoso del cliente kafka-python. Si la libreria no esta instalada no
# rompemos la coleccion de pytest: los tests haran skip con un mensaje claro.
try:
    from kafka import KafkaConsumer, KafkaProducer
    from kafka.errors import KafkaError, NoBrokersAvailable

    _IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover - solo si falta la dependencia
    KafkaProducer = KafkaConsumer = None
    NoBrokersAvailable = KafkaError = Exception
    _IMPORT_ERROR = exc


class KafkaUnavailable(Exception):
    """Se lanza cuando el cliente o el broker Kafka no estan disponibles."""


def _security_config():
    """Config SASL/SSL opcional para brokers gestionados en la nube."""
    if not KAFKA_SECURITY_PROTOCOL:
        return {}

    config = {"security_protocol": KAFKA_SECURITY_PROTOCOL}
    if KAFKA_SASL_MECHANISM:
        config["sasl_mechanism"] = KAFKA_SASL_MECHANISM
        config["sasl_plain_username"] = KAFKA_SASL_USERNAME
        config["sasl_plain_password"] = KAFKA_SASL_PASSWORD
    return config


def _bootstrap_list(bootstrap):
    return [server.strip() for server in bootstrap.split(",") if server.strip()]


class TelemetryProducer:
    """Productor de eventos de telemetria hacia un topico Kafka."""

    def __init__(self, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS):
        if KafkaProducer is None:
            raise KafkaUnavailable(
                f"El cliente kafka-python no esta instalado: {_IMPORT_ERROR}"
            )
        try:
            self._producer = KafkaProducer(
                bootstrap_servers=_bootstrap_list(bootstrap_servers),
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                key_serializer=lambda k: k.encode("utf-8") if k is not None else None,
                acks="all",
                retries=3,
                request_timeout_ms=int(PRODUCE_TIMEOUT_SECONDS * 1000),
                **_security_config(),
            )
        except NoBrokersAvailable as exc:
            raise KafkaUnavailable(
                f"No hay broker Kafka en {bootstrap_servers}: {exc}"
            ) from exc

    def publish(self, topic, event, key=None):
        """Publica un evento JSON y devuelve los metadatos de entrega."""
        future = self._producer.send(topic, value=event, key=key)
        self._producer.flush(timeout=PRODUCE_TIMEOUT_SECONDS)
        metadata = future.get(timeout=PRODUCE_TIMEOUT_SECONDS)
        return {
            "topic": metadata.topic,
            "partition": metadata.partition,
            "offset": metadata.offset,
            "key": key,
        }

    def close(self):
        try:
            self._producer.close(timeout=PRODUCE_TIMEOUT_SECONDS)
        except Exception:
            pass


class TelemetryConsumer:
    """Consumidor que lee eventos de telemetria de un topico Kafka."""

    def __init__(self, topic, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=None):
        if KafkaConsumer is None:
            raise KafkaUnavailable(
                f"El cliente kafka-python no esta instalado: {_IMPORT_ERROR}"
            )
        self.topic = topic
        try:
            self._consumer = KafkaConsumer(
                topic,
                bootstrap_servers=_bootstrap_list(bootstrap_servers),
                group_id=group_id or f"qa-telemetry-{uuid.uuid4().hex[:8]}",
                auto_offset_reset="earliest",
                enable_auto_commit=True,
                value_deserializer=lambda v: json.loads(v.decode("utf-8")),
                key_deserializer=lambda k: k.decode("utf-8") if k is not None else None,
                consumer_timeout_ms=1000,
            )
        except NoBrokersAvailable as exc:
            raise KafkaUnavailable(
                f"No hay broker Kafka en {bootstrap_servers}: {exc}"
            ) from exc

    def consume(self, match=None, timeout=CONSUME_TIMEOUT_SECONDS, limit=200):
        """Consume mensajes hasta cumplir el timeout o el limite.

        Si `match` (callable sobre el value) se entrega, solo retorna los
        registros que lo cumplen. Esto permite aislar el evento producido por el
        test aunque el topico contenga otros mensajes.
        """
        deadline = time.time() + timeout
        records = []
        while time.time() < deadline and len(records) < limit:
            batch = self._consumer.poll(timeout_ms=1000, max_records=limit)
            new_messages = any(batch.values())
            for _partition, messages in batch.items():
                for message in messages:
                    if match is None or match(message.value):
                        records.append(
                            {
                                "value": message.value,
                                "key": message.key,
                                "partition": message.partition,
                                "offset": message.offset,
                            }
                        )
            if match is not None and records:
                break
            if not new_messages and records:
                break
        return records

    def close(self):
        try:
            self._consumer.close()
        except Exception:
            pass
