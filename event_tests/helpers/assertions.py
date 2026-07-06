from jsonschema import validate

from event_tests.config.settings import MAX_EVENT_LATENCY_SECONDS


def assert_event_contract(event, schema):
    validate(instance=event, schema=schema)


def assert_message_integrity(sent, received):
    assert received == sent, (
        f"El mensaje recibido no coincide con el enviado.\n"
        f"Enviado:   {sent}\n"
        f"Recibido:  {received}"
    )


def assert_delivered(records, expected_count=1):
    assert len(records) == expected_count, (
        f"Se esperaban {expected_count} evento(s), se consumieron {len(records)}"
    )


def assert_event_within_sla(latency_seconds, max_seconds=MAX_EVENT_LATENCY_SECONDS):
    assert latency_seconds < max_seconds, (
        f"Latencia produce->consume {latency_seconds:.3f}s excede el SLA de {max_seconds}s"
    )
