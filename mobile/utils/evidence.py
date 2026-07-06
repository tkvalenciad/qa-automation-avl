from datetime import datetime

import allure

from config.reporting import SCREENSHOTS_DIR, ensure_report_dirs


def attach_mobile_screenshot(driver, test_name, status="passed", label="Screenshot"):
    ensure_report_dirs()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = test_name.replace("/", "_").replace("\\", "_")
    screenshot_path = SCREENSHOTS_DIR / f"{safe_name}_{status}_{timestamp}.png"

    try:
        driver.save_screenshot(str(screenshot_path))
    except Exception:
        # Session/instrumentation may have crashed; skip evidence rather than
        # turning a test result into an additional teardown error.
        return None

    try:
        allure.attach.file(
            str(screenshot_path),
            name=label,
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception:
        pass

    return screenshot_path


def attach_mobile_page_source(driver, label="Page Source"):
    try:
        source = driver.page_source
    except Exception:
        return

    try:
        allure.attach(
            source,
            name=label,
            attachment_type=allure.attachment_type.XML,
        )
    except Exception:
        pass
