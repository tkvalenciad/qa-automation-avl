from jsonschema import validate

from api_tests.config.settings import MAX_RESPONSE_TIME_SECONDS


def assert_json_response(response, expected_status, schema=None):
    assert response.status_code == expected_status, (
        f"Expected HTTP {expected_status}, got {response.status_code}"
    )

    content_type = response.headers.get("Content-Type", "")
    assert content_type.startswith("application/json"), (
        f"Expected JSON response, got Content-Type: {content_type!r}"
    )

    body = response.json()

    if schema is not None:
        validate(instance=body, schema=schema)

    return body


def assert_within_sla(response, max_seconds=MAX_RESPONSE_TIME_SECONDS):
    elapsed = response.elapsed.total_seconds()
    assert elapsed < max_seconds, (
        f"Response took {elapsed:.2f}s, SLA is {max_seconds}s"
    )
