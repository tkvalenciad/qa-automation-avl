from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CATALOG_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "products screen")
LOGIN_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "login screen")
MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "open menu")
CATALOG_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item catalog")
DIALOG_OK_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("OK")',
)
AUTOFILL_LOCATORS = (
    (AppiumBy.ID, "android:id/autofill_save_never_allow"),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Never")'),
    (AppiumBy.ID, "android:id/autofill_save_no"),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cancelar")'),
)


def wait_for_app_ready(driver, timeout=45):
    wait = WebDriverWait(driver, timeout, poll_frequency=0.5)
    wait.until(
        EC.any_of(
            EC.presence_of_element_located(CATALOG_SCREEN),
            EC.presence_of_element_located(LOGIN_SCREEN),
            EC.presence_of_element_located(MENU_BUTTON),
            EC.presence_of_element_located(CATALOG_MENU_ITEM),
        )
    )


def wait_for_catalog(driver, timeout=30):
    wait = WebDriverWait(driver, timeout, poll_frequency=0.5)

    if driver.find_elements(*LOGIN_SCREEN):
        return

    if driver.find_elements(*CATALOG_SCREEN):
        return

    if driver.find_elements(*CATALOG_MENU_ITEM):
        wait.until(EC.element_to_be_clickable(CATALOG_MENU_ITEM)).click()
        wait.until(EC.presence_of_element_located(CATALOG_SCREEN))
        return

    wait.until(EC.element_to_be_clickable(MENU_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(CATALOG_MENU_ITEM)).click()
    wait.until(EC.presence_of_element_located(CATALOG_SCREEN))


def dismiss_system_prompts(driver):
    short_wait = WebDriverWait(driver, 2, poll_frequency=0.5)

    for locator in AUTOFILL_LOCATORS:
        try:
            short_wait.until(EC.element_to_be_clickable(locator)).click()
            return
        except TimeoutException:
            continue

    try:
        short_wait.until(EC.element_to_be_clickable(DIALOG_OK_BUTTON)).click()
    except TimeoutException:
        pass
