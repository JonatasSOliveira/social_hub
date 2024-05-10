from dotenv import load_dotenv

load_dotenv()

from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from src.controllers.whatsapp_controller import WhatsappController
from src.controllers.telegram_controller import TelegramController
from src.controllers.facebook_controller import FacebookController

message = 'Hello from Python'


def _get_web_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    # dir_path = os.getcwd()
    # profile = os.path.join(dir_path, "profile", "wpp")
    # options.add_argument(r"user-data-dir={}".format(profile))
    return webdriver.Chrome(options)


def main() -> None:
    web_driver = _get_web_driver()

    whatsapp_controller = WhatsappController(web_driver)
    telegram_controller = TelegramController(web_driver)
    facebook_controller = FacebookController(web_driver)

    facebook_controller.open_website()
    facebook_controller.auth()
    facebook_controller.public_image_post('pictures\game\img_01.png', message)
    sleep(10)

    pass


main()
