import time
from types import SimpleNamespace

import pytest

from event_tests.client.kafka_client import (
    KafkaUnavailable,
    TelemetryConsumer,
    TelemetryProducer,
)
from event_tests.config.settings import (
    GPS_RAW_EVENTS_TOPIC,
    KAFKA_BOOTSTRAP_SERVERS,
)
from event_tests.helpers.evidence import (
    attach_last_event_evidence,
    record_event_exchange,
)


@pytest.fixture
def telemetry_topic():
    """Topic de telemetria (gps-raw-events por defecto, como pide la prueba)."""
    return GPS_RAW_EVENTS_TOPIC


@pytest.fixture
def producer():
    try:
        client = TelemetryProducer()
    except KafkaUnavailable as exc:
        pytest.skip(
            f"Kafka no disponible en {KAFKA_BOOTSTRAP_SERVERS}: {exc}. "
            "Levanta el broker con `docker compose up -d` e instala "
            "`pip install -r event_tests/requirements-events.txt`."
        )
        return
    yield client
    client.close()


@pytest.fixture
def consumer_factory(telemetry_topic):
    """Crea consumidores del topic y los cierra al finalizar el test."""
    created = []

    def _make(topic=None, group_id=None):
        try:
            client = TelemetryConsumer(topic or telemetry_topic, group_id=group_id)
        except KafkaUnavailable as exc:
            pytest.skip(f"Kafka no disponible: {exc}")
        created.append(client)
        return client

    yield _make

    for client in created:
        client.close()


@pytest.fixture
def publish_and_consume(producer, consumer_factory, telemetry_topic):
    """Publica un evento, lo consume filtrando por vehicleId y registra evidencia.

    Devuelve un objeto con `.records`, `.latency` y `.metadata`, encapsulando el
    ciclo produce -> consume que comparten los tests de telemetria.
    """

    def _roundtrip(event, key=None):
        vehicle_id = event.get("vehicleId")
        consumer = consumer_factory()

        started = time.time()
        metadata = producer.publish(telemetry_topic, event, key=key or vehicle_id)
        records = consumer.consume(match=lambda value: value.get("vehicleId") == vehicle_id)
        latency = time.time() - started

        record_event_exchange(
            topic=telemetry_topic,
            produced=event,
            consumed=records[0]["value"] if records else None,
            metadata=metadata,
            latency_seconds=latency,
        )
        return SimpleNamespace(records=records, latency=latency, metadata=metadata)

    return _roundtrip


@pytest.fixture(autouse=True)
def event_evidence(request):
    yield

    report = getattr(request.node, "rep_call", None)
    if report is None:
        return

    if report.passed:
        attach_last_event_evidence(request.node.name, status="passed")
    elif report.failed:
        attach_last_event_evidence(request.node.name, status="failed")
