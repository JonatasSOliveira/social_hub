from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from src.configs.whatsapp_config import WhatsappHomeConfig
from src.utils.file_utils import FileUtils


class WhatsappController:
    _WEBSITE_URL = 'https://web.whatsapp.com/'

    _is_opened = False

    def __init__(self, web_driver: WebDriver) -> None:
        self._web_driver = web_driver

    def open_website(self) -> None:
        self._web_driver.get(self._WEBSITE_URL)

    def auth(self):
        while len(self._web_driver.find_elements(By.ID, 'side')) < 1:
            sleep(1)
        sleep(2)

    def send_message_to_group(self, group_title: str, message: str, image_path: str) -> None:
        search_box = WebDriverWait(self._web_driver, 500).until(
            EC.presence_of_element_located((By.XPATH, WhatsappHomeConfig.SEARCH_BOX_XPATH))
        )
        search_box.send_keys(group_title)
        sleep(2)

        group = self._web_driver.find_element(By.XPATH, WhatsappHomeConfig.get_group_xpath(group_title))
        group.click()
        sleep(2)

        msg_input = self._web_driver.find_element(By.XPATH, WhatsappHomeConfig.MSG_INPUT_XPATH)
        msg_input.send_keys(message)
        sleep(2)

        send_btn_xpath = WhatsappHomeConfig.SEND_MSG_BTN_XPATH
        if image_path:
            send_btn_xpath = WhatsappHomeConfig.SEND_IMG_VIDEO_BTN_XPATH
            attach_btn = self._web_driver.find_element(By.XPATH, WhatsappHomeConfig.ATTACH_BTN_XPATH)
            attach_btn.click()
            sleep(2)

            absolute_image_path = FileUtils.absolute_file_path(image_path)
            file_input = self._web_driver.find_element(By.XPATH, WhatsappHomeConfig.IMG_VIDEO_INPUT_XPATH)
            file_input.send_keys(absolute_image_path)
            sleep(2)

        self._web_driver.find_element(By.XPATH, send_btn_xpath).click()
        sleep(2)
