import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from Utilities.test_data import TestData


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()

    request.cls.driver = driver
    # Load the AUT
    driver.get(TestData.base_url)
    driver.maximize_window()
    # transfer control to the test scripts
    yield
    driver.close()


# 1st Step: Declare Variables For Setting Up LambdaTest
user_name = "pranav_naik"
access_token = "KtFvmwaUCKQQfPRpPmh1YAW2RvHfsysJGUlV0roFQBZY3AQcnm"
remote_url = "https://" + user_name + ":" + access_token + "@hub.lambdatest.com/wd/hub"

# 2nd Step: Define The Desired Capabilities (3 Caps)
chrome_caps = {
    "build": "1.0",
    "name": "LambdaTest Grid On Chrome and Windows 10",
    "platform": "Windows 10",
    "browserName": "Chrome",
    "version": "88.0"
}

edge_caps = {
    "build": "2.0",
    "name": "LambdaTest Grid On Edge and macOS Sierra",
    "platform": "macOS Sierra",
    "browserName": "Edge",
    "version": "87.0"
}

firefox_caps = {
    "build": "3.0",
    "name": "LambdaTest Grid On Firefox and Windows 7",
    "platform": "Windows 7",
    "browserName": "Firefox",
    "version": "82.0"
}

ie_caps = {
    "build": "4.0",
    "name": "LambdaTest Grid On Internet Explorer and Windows 10",
    "platform": "Windows 10",
    "browserName": "Internet Explorer",
    "version": "11.0"
}


# 3rd Step: Connect To LambdaTest Using A Fixture & RemoteConnection
@pytest.fixture(params=["chrome", "firefox", "edge", "ie"])
def driver_initialization(request):
    """
  Initialize Driver For Selenium Grid On LambdaTest
  :param request:
  """
    desired_caps = {}

    if request.param == "chrome":
        desired_caps.update(chrome_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            desired_capabilities=desired_caps
        )
    elif request.param == "firefox":
        desired_caps.update(firefox_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            desired_capabilities= desired_caps
        )
    elif request.param == "edge":
        desired_caps.update(edge_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            desired_capabilities=desired_caps
        )
    elif request.param == "ie":
        desired_caps.update(ie_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            desired_capabilities=desired_caps
        )
    request.cls.driver = driver
    yield
    driver.close()
