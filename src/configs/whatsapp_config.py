search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]' # <- "caminho" para a barra de pesquisa
msg_input_xpath='//div[@contenteditable="true"][@data-tab="10"]' # <- "caminho" para o campo de mensagen
send_btn_xpath='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span' # <- "caminho" para o botão de enviar

def get_group_xpath(group_title: str) -> str:
    return f'//span[@title="{group_title}"]'