from Pages.BasePage import BasePage
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_all_elements_loaded(self, driver):
        WebDriverWait(driver, timeout=10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )

    def scrollElementIntoView(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    def openLinkInNewTab(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        if self.driver.capabilities["platformName"].lower() == "windows":
            actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
        elif self.driver.capabilities["platformName"].lower() == "mac":
            actions.key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
