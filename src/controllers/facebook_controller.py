import os
import sys
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from src.configs.facebook_config import login, password, FacebookLoginPagePaths, FacebookHomePagePaths


class FacebookController:
    _WEBSITE_URL = 'https://www.facebook.com/'
    _web_driver: WebDriver = None

    def __init__(self, web_driver: WebDriver) -> None:
        self._web_driver = web_driver

    def open_website(self) -> None:
        self._web_driver.get(self._WEBSITE_URL)
        while (
            len(self._web_driver.find_elements(By.XPATH, FacebookLoginPagePaths.LOGIN_INPUT_XPATH)) < 1
            and len(self._web_driver.find_elements(By.XPATH, FacebookHomePagePaths.ADD_PICTURE_BUTTON_XPATH)) < 1
        ):
            sleep(1)
        sleep(2)

    def auth(self) -> None:
        login_input = self._web_driver.find_element(By.XPATH, FacebookLoginPagePaths.LOGIN_INPUT_XPATH)
        password_input = self._web_driver.find_element(By.XPATH, FacebookLoginPagePaths.PASSWORD_INPUT_XPATH)
        if not login_input or not password_input:
            return

        login_input.send_keys(login)
        password_input.send_keys(password)
        sleep(1)

        sign_in_button = self._web_driver.find_element(By.XPATH, FacebookLoginPagePaths.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click()

        while len(self._web_driver.find_elements(By.XPATH, FacebookHomePagePaths.IMG_POST_INPUT_BUTTON_XPATH)) < 1:
            sleep(1)
        sleep(2)

    def public_image_post(self, image_path: str, message: str) -> None:
        project_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
        absolute_image_path = os.path.join(project_directory, image_path)

        img_post_button = self._web_driver.find_element(By.XPATH, FacebookHomePagePaths.IMG_POST_INPUT_BUTTON_XPATH)
        img_post_button.click()
        sleep(2)

        post_input = self._web_driver.find_element(By.XPATH, FacebookHomePagePaths.POST_INPUT_XPATH)
        post_input.send_keys(message)
        sleep(2)

        input_file = self._web_driver.find_element(By.XPATH, FacebookHomePagePaths.FILE_INPUT_XPATH)
        input_file.send_keys(absolute_image_path)
        sleep(2)
