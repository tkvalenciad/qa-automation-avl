import time

from appium import webdriver
from appium.options.android import UiAutomator2Options

from config.settings import (
    APP_ACTIVITY,
    APP_PACKAGE,
    APP_PATH,
    APPIUM_SERVER,
    AUTOMATION_NAME,
    DEVICE_NAME,
    PLATFORM_NAME,
    UDID,
)


def _build_options():
    options = UiAutomator2Options()

    options.platform_name = PLATFORM_NAME
    options.automation_name = AUTOMATION_NAME
    options.device_name = DEVICE_NAME
    options.app_wait_duration = 30000
    options.new_command_timeout = 120

    # Stability on real devices: give UiAutomator2 server more time to install
    # and launch, tolerate slow adb, disable animations and auto-grant perms so
    # the instrumentation process is less likely to be killed mid-session.
    options.uiautomator2_server_launch_timeout = 60000
    options.uiautomator2_server_install_timeout = 60000
    options.adb_exec_timeout = 60000
    options.set_capability("disableWindowAnimation", True)
    options.set_capability("autoGrantPermissions", True)
    options.set_capability("ignoreHiddenApiPolicyError", True)
    options.set_capability("forceAppLaunch", True)
    options.set_capability("shouldTerminateApp", True)

    if UDID:
        options.udid = UDID

    if APP_PATH.exists():
        options.app = str(APP_PATH)
    else:
        options.app_package = APP_PACKAGE
        options.app_activity = APP_ACTIVITY

    options.no_reset = False

    return options


def get_driver(max_attempts=2):
    last_error = None

    for attempt in range(max_attempts):
        try:
            driver = webdriver.Remote(APPIUM_SERVER, options=_build_options())
            driver.implicitly_wait(5)
            return driver
        except Exception as exc:  # noqa: BLE001 - retry on flaky session start
            last_error = exc
            if attempt < max_attempts - 1:
                time.sleep(5)

    raise last_error
