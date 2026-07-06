import pytest
from jsonschema import ValidationError

from event_tests.helpers.assertions import (
    assert_delivered,
    assert_event_contract,
    assert_event_within_sla,
    assert_message_integrity,
)
from event_tests.payloads.telemetry_events import build_gps_event, random_gps_event
from event_tests.schemas.telemetry_schema import GPS_EVENT_SCHEMA


@pytest.mark.events
def test_gps_telemetry_event_is_delivered_intact(publish_and_consume):
    event = random_gps_event()
    result = publish_and_consume(event)

    assert_delivered(result.records, expected_count=1)
    assert_message_integrity(event, result.records[0]["value"])
    assert result.records[0]["key"] == event["vehicleId"]


@pytest.mark.events
def test_consumed_event_matches_json_schema(publish_and_consume):
    result = publish_and_consume(random_gps_event())

    assert_delivered(result.records, expected_count=1)
    assert_event_contract(result.records[0]["value"], GPS_EVENT_SCHEMA)


@pytest.mark.events
def test_delivery_latency_within_sla(publish_and_consume):
    result = publish_and_consume(random_gps_event())

    assert_delivered(result.records, expected_count=1)
    assert_event_within_sla(result.latency)


@pytest.mark.events
def test_invalid_gps_event_is_rejected_by_schema():
    invalid_event = build_gps_event(lat=999, lng=-74.08, speed=-5)

    with pytest.raises(ValidationError):
        assert_event_contract(invalid_event, GPS_EVENT_SCHEMA)
