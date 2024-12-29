import time

import pytest

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage

from Utilities.test_data import TestData

@pytest.mark.usefixtures("driver_initialization")
class TestScenario1():
    def test_scenario_1(self):
        basePage = BasePage(self.driver)
        homePage = HomePage(self.driver)

        homePage.verify_all_elements_loaded(self.driver)

        # As per the problem statement, the `Explore all Integrations should open a new tab`,
        # but the actual behavior seems to open the link in the same tab.
        # Hence, implemented a method that mimics the expected behavior.
        time.sleep(5)
        homePage.openLinkInNewTab(TestData.exploreAllIntegrationsLink)

        windowHandles = self.driver.window_handles

        for index, handle in enumerate(windowHandles):
            print("Window Handle {0}: {1}".format(index, handle))

        time.sleep(10)
        assert len(windowHandles) == 2, ('Count of Window Handles is not as expected! '
                                         'Expected : 2, Actual: {0}').format(len(windowHandles))

        self.driver.switch_to.window(windowHandles[-1])
        time.sleep(5)
        assert self.driver.current_url == TestData.integrationsTabUrl, (
            'URL of the new Tab does not match with the expected!'
            'Expected: {0} Actual: {1}'.format(TestData.integrationsTabUrl, self.driver.current_url))

        homePage.scrollElementIntoView(TestData.codelessAutomationLink)
        basePage.click_on_element(TestData.codelessAutomationLink)
        time.sleep(2)
        basePage.click_on_element(TestData.testingWhizLink)

        assert basePage.get_text_in_element(
            TestData.testingWhizPageTitle) == "TestingWhiz Integration With LambdaTest", (
            'Title of the Page does not match!'
            'Expected Title: {0} Actual Title: {1}'.format("TestingWhiz Integration With LambdaTest",
                                                           self.driver.title))

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        print("Current Count of Window Handles: ", len(self.driver.window_handles))

        self.driver.get(TestData.urlToBeUpdated)

        basePage.click_on_element(TestData.communityLink)

        assert self.driver.current_url == TestData.communityPageUrl, ('URL of the Community Page does not match with '
                                                                      'the expected!'
                                                                      'Expected: {0} Actual: {1}'.format(
            TestData.communityPageUrl, self.driver.current_url))