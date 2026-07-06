import pytest

from mobile.utils.app_helpers import wait_for_app_ready, wait_for_catalog
from mobile.utils.driver_factory import get_driver
from mobile.utils.evidence import attach_mobile_page_source, attach_mobile_screenshot


@pytest.fixture
def driver():
    driver = get_driver()
    wait_for_app_ready(driver, timeout=45)
    wait_for_catalog(driver)
    yield driver
    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture(autouse=True)
def mobile_test_evidence(request, driver):
    yield

    report = getattr(request.node, "rep_call", None)
    if report is None:
        return

    test_name = request.node.name

    if report.passed:
        attach_mobile_screenshot(
            driver,
            test_name,
            status="passed",
            label="Success screenshot",
        )
        return

    if report.failed:
        attach_mobile_screenshot(
            driver,
            test_name,
            status="failed",
            label="Failure screenshot",
        )
        attach_mobile_page_source(driver, label="Failure page source")
