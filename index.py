from dotenv import load_dotenv

load_dotenv()

import os
import pandas as pd
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from src.controllers.whatsapp_controller import WhatsappController
from src.controllers.telegram_controller import TelegramController
from src.controllers.facebook_controller import FacebookController


def _get_web_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
    options.add_argument(r"user-data-dir={}".format(profile))
    return webdriver.Chrome(options)


def main() -> None:
    web_driver = _get_web_driver()
    csv_data = pd.read_csv('data.csv')

    whatsapp_controller = WhatsappController(web_driver)

    whatsapp_controller.open_website()
    whatsapp_controller.auth()
    for index, row in csv_data.iterrows():
        whatsapp_controller.send_message_to_group(row['whatsapp_group'], row['link'], row['image_path'])
        web_driver.save_screenshot('screenshots/{}.png'.format(index))


main()
