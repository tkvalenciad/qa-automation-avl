from appium.webdriver.common.appiumby import AppiumBy

from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait





class BasePage:



    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 15, poll_frequency=0.5)



    def click(self, locator):

        last_error = None

        for _ in range(3):

            try:

                element = self.wait.until(EC.element_to_be_clickable(locator))

                element.click()

                return

            except StaleElementReferenceException as exc:

                last_error = exc

        raise last_error



    def write(self, locator, text):

        last_error = None

        for _ in range(3):

            try:

                element = self.wait.until(EC.element_to_be_clickable(locator))

                element.click()

                element.clear()

                element.send_keys(text)

                return

            except StaleElementReferenceException as exc:

                last_error = exc

        raise last_error



    def get_text(self, locator):

        return self.wait.until(

            EC.visibility_of_element_located(locator)

        ).text



    def is_present(self, locator):

        return bool(self.driver.find_elements(*locator))



    def is_visible(self, locator):

        if not self.is_present(locator):

            return False

        try:

            WebDriverWait(self.driver, 5, poll_frequency=0.5).until(

                EC.visibility_of_element_located(locator)

            )

            return True

        except Exception:

            return False



    def exists(self, locator):

        return self.is_present(locator)



    def wait_for_visible(self, locator):

        self.wait.until(EC.visibility_of_element_located(locator))



    def hide_keyboard(self):

        try:

            self.driver.hide_keyboard()

        except Exception:

            pass



    def scroll_to(self, locator):

        if locator[0] != AppiumBy.ACCESSIBILITY_ID:

            return



        description = locator[1]

        scroll_selector = (

            AppiumBy.ANDROID_UIAUTOMATOR,

            (

                "new UiScrollable(new UiSelector().scrollable(true))"

                f'.scrollIntoView(new UiSelector().description("{description}"))'

            ),

        )

        self.driver.find_element(*scroll_selector)


