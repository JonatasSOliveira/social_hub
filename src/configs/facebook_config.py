import os

login = os.getenv("FACEBOOK_LOGIN")
password = os.getenv("FACEBOOK_PASSWORD")


class FacebookLoginPagePaths:
    LOGIN_INPUT_XPATH = '//input[@id="email"]'
    PASSWORD_INPUT_XPATH = '//input[@id="pass"]'
    SIGN_IN_BUTTON_XPATH = '//button[@name="login"]'


class FacebookHomePagePaths:
    IMG_POST_INPUT_BUTTON_XPATH = (
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div'
        + '/div/div[2]/div[2]'
    )
    POST_INPUT_XPATH = (
        '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div'
        + '/div[2]/div[1]/div[1]/div[1]/div/div/div[1]'
    )
    FILE_INPUT_XPATH = '//input[@type="file"]'
