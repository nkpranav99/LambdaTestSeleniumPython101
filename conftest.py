import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from Utilities.test_data import TestData


@pytest.fixture(params=["edge", "chrome"])
def initialize_driver(request):
    """
    This fixture is for testing on the local development environment.
    For testing on remote i.e. LambdaTest, 'driver_initialization' fixture can be used.
    """
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()

    request.cls.driver = driver
    # Load the AUT
    driver.get(TestData.baseUrl)
    driver.maximize_window()
    # transfer control to the test scripts
    yield
    driver.close()


# 1st Step: Declare Variables For Setting Up LambdaTest
user_name = "pranav_naik"
access_token = "TIip2A6dnYX0RVdW3jMAYtNNFr7O9ZWXljPMQbtrS0QbqqefWW"
remote_url = "http://" + user_name + ":" + access_token + "@hub.lambdatest.com/wd/hub"

# 2nd Step: Define The Desired Capabilities
chrome_caps = {
    "build": "1.0",
    "name": "LambdaTest Grid On Chrome v128.0 and Windows 10",
    "platform": "Windows 10",
    "browserName": "Chrome",
    "version": "128.0",
    "visual": True,
    "video": True,
    "network": True,
    "console": True,
    "idleTimeout": 10
}

edge_caps = {
    "build": "2.0",
    "name": "LambdaTest Grid On Edge v127.0 and macOS Ventura",
    "platform": "MacOS Sequoia",
    "browserName": "MicrosoftEdge",
    "version": "127.0",
    "visual": True,
    "video": True,
    "network": True,
    "console": True,
    "idleTimeout": 10
}

# 3rd Step: Connect To LambdaTest Using A Fixture & RemoteConnection
@pytest.fixture(params=["chrome", "edge"])
def driver_initialization(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("LT:Options", chrome_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            options=chrome_options
        )
    elif request.param == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.set_capability("LT:Options", edge_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            options=edge_options
        )
    request.cls.driver = driver
    driver.get(TestData.baseUrl)
    driver.maximize_window()
    yield
    driver.quit()
