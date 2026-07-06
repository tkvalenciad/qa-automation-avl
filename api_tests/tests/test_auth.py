from api_tests.config.endpoints import DUMMYJSON_LOGIN
from api_tests.helpers.assertions import assert_json_response, assert_within_sla
from api_tests.payloads.auth_payload import INVALID_LOGIN_PAYLOAD, VALID_LOGIN_PAYLOAD
from api_tests.schemas.auth_schema import LOGIN_ERROR_SCHEMA, LOGIN_SUCCESS_SCHEMA


def test_login_with_valid_credentials(dummyjson_api):
    response = dummyjson_api.request("POST", DUMMYJSON_LOGIN, VALID_LOGIN_PAYLOAD)
    body = assert_json_response(response, 200, schema=LOGIN_SUCCESS_SCHEMA)

    assert body["username"] == VALID_LOGIN_PAYLOAD["username"]


def test_login_with_invalid_credentials(dummyjson_api):
    response = dummyjson_api.request("POST", DUMMYJSON_LOGIN, INVALID_LOGIN_PAYLOAD)
    body = assert_json_response(response, 400, schema=LOGIN_ERROR_SCHEMA)

    assert "invalid" in body["message"].lower()


def test_login_response_time_under_sla(dummyjson_api):
    response = dummyjson_api.request("POST", DUMMYJSON_LOGIN, VALID_LOGIN_PAYLOAD)

    assert_json_response(response, 200)
    assert_within_sla(response)
