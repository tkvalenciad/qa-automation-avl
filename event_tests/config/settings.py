import os

# Broker Kafka. Por defecto apunta al Kafka local del docker-compose.
# Para un broker en la nube (Confluent Cloud, Upstash, Redpanda Cloud) basta con
# sobreescribir esta variable y las de SASL de abajo.
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

# Topic de telemetria cruda tal como lo pide la prueba tecnica.
GPS_RAW_EVENTS_TOPIC = os.getenv("GPS_RAW_EVENTS_TOPIC", "gps-raw-events")

# Tiempos de espera del flujo produce -> consume.
PRODUCE_TIMEOUT_SECONDS = float(os.getenv("EVENTS_PRODUCE_TIMEOUT", "10"))
CONSUME_TIMEOUT_SECONDS = float(os.getenv("EVENTS_CONSUME_TIMEOUT", "15"))

# SLA de latencia extremo a extremo (produce -> consume) del evento.
MAX_EVENT_LATENCY_SECONDS = float(os.getenv("EVENTS_MAX_LATENCY", "2.0"))

# Seguridad opcional para brokers gestionados en la nube (SASL_SSL, etc.).
# Si se dejan vacias, el cliente usa PLAINTEXT (broker local sin auth).
KAFKA_SECURITY_PROTOCOL = os.getenv("KAFKA_SECURITY_PROTOCOL")
KAFKA_SASL_MECHANISM = os.getenv("KAFKA_SASL_MECHANISM")
KAFKA_SASL_USERNAME = os.getenv("KAFKA_SASL_USERNAME")
KAFKA_SASL_PASSWORD = os.getenv("KAFKA_SASL_PASSWORD")
