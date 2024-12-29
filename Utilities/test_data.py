from selenium.webdriver.common.by import By


class TestData:
    """
    This class stores all the test data and locators required for the test scenario automation
    """

    baseUrl = "https://www.lambdatest.com/"
    integrationsTabUrl = "https://www.lambdatest.com/integrations"
    urlToBeUpdated = "https://www.lambdatest.com/blog/"

    # New
    exploreAllIntegrationsLink = (By.XPATH, '//a[text()="Explore all Integrations"]')
    # exploreAllIntegrationsLink = (By.XPATH, '//div[@class="wrapper"]/section[9]')

    codelessAutomationLink = (By.XPATH, '//a[text()="Codeless Automation"]')
    testingWhizLink = (By.XPATH, '//a[text()="Integrate Testing Whiz with LambdaTest"]')
    testingWhizPageTitle = (By.XPATH, '//h1')
    communityLink = (By.XPATH, '//div[@class="menu-menu-1-container"]//a[text()="Community"]')

    communityPageUrl = "https://community.lambdatest.com/"