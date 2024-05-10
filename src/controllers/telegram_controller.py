from time import sleep

from selenium.webdriver.common.by import By

from src.configs import telegram_config

website_url='https://web.telegram.org/k/'


class TelegramController:
    _web_driver = None
    _is_opened = False
    
    def __init__(self, web_driver) -> None:
        self._web_driver = web_driver
        
    def start(self) -> None:
        self._web_driver.get(website_url)
        while len(self._web_driver.find_elements(By.CLASS_NAME, telegram_config.message_list_classname)) < 1:
            sleep(1) 
        sleep(2)