class WhatsappHomeConfig:
    SEARCH_BOX_XPATH = '//div[@contenteditable="true"][@data-tab="3"]'
    MSG_INPUT_XPATH = '//div[@contenteditable="true"][@data-tab="10"]'
    SEND_MSG_BTN_XPATH = '//button[@aria-label="Enviar"]'
    ATTACH_BTN_XPATH = '//div[@aria-label="Anexar"]'
    IMG_VIDEO_INPUT_XPATH = '//input[@type="file"][@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
    SEND_IMG_VIDEO_BTN_XPATH = '//div[@aria-label="Enviar"]'

    @staticmethod
    def get_group_xpath(group_title: str) -> str:
        return f'//span[@title="{group_title}"]'
