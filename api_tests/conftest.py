import pytest

from api_tests.client.api_client import ApiClient
from api_tests.config.settings import DUMMYJSON_URL, JSONPLACEHOLDER_URL
from api_tests.helpers.evidence import attach_last_api_evidence


def _api_client(base_url):
    with ApiClient(base_url) as client:
        yield client


@pytest.fixture
def jsonplaceholder_api():
    yield from _api_client(JSONPLACEHOLDER_URL)


@pytest.fixture
def dummyjson_api():
    yield from _api_client(DUMMYJSON_URL)


@pytest.fixture(autouse=True)
def api_test_evidence(request):
    yield

    report = getattr(request.node, "rep_call", None)
    if report is None:
        return

    if report.passed:
        attach_last_api_evidence(request.node.name, status="passed")
        return

    if report.failed:
        attach_last_api_evidence(request.node.name, status="failed")
