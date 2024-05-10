from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from src.configs import whatsapp_config


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
        
    def send_message_to_group(self, message: str, group_title: str) -> None:
        search_box = WebDriverWait(self._web_driver, 500).until(
            EC.presence_of_element_located((By.XPATH, whatsapp_config.search_box_xpath))
        )
        search_box.send_keys(group_title)
        sleep(2)
        group = self._web_driver.find_element(By.XPATH, whatsapp_config.get_group_xpath(group_title))
        group.click()
        sleep(2)
        msg_input = self._web_driver.find_element(By.XPATH, whatsapp_config.msg_input_xpath) 
        msg_input.send_keys(message)
        sleep(2)
        self._web_driver.find_element(By.XPATH, whatsapp_config.send_btn_xpath).click()
        sleep(10)
        