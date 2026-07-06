from api_tests.config.endpoints import JSONPLACEHOLDER_POSTS, jsonplaceholder_post
from api_tests.helpers.assertions import assert_json_response, assert_within_sla
from api_tests.payloads.post_payload import UPDATE_POST_PAYLOAD, create_post_payload
from api_tests.schemas.post_schema import POST_SCHEMA


def test_create_post_returns_201(jsonplaceholder_api):
    response = jsonplaceholder_api.request(
        "POST",
        JSONPLACEHOLDER_POSTS,
        create_post_payload(),
    )
    assert_json_response(response, 201, schema=POST_SCHEMA)


def test_update_post_returns_200(jsonplaceholder_api):
    response = jsonplaceholder_api.request(
        "PUT",
        jsonplaceholder_post(1),
        UPDATE_POST_PAYLOAD,
    )
    body = assert_json_response(response, 200, schema=POST_SCHEMA)

    assert body["title"] == UPDATE_POST_PAYLOAD["title"]


def test_get_post_matches_json_schema(jsonplaceholder_api):
    response = jsonplaceholder_api.request("GET", jsonplaceholder_post(1))
    assert_json_response(response, 200, schema=POST_SCHEMA)


def test_list_posts_response_time_under_sla(jsonplaceholder_api):
    response = jsonplaceholder_api.request("GET", JSONPLACEHOLDER_POSTS)

    assert_json_response(response, 200)
    assert_within_sla(response)
