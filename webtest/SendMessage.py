from webtest.Login import LoginWeb
from selenium.webdriver.common.keys import Keys
import time

class SendMessage(LoginWeb):
    def sendMessage(self):
        # 调用登录
        self.loginWeb()
        # 点击九点
        self.click_element('class', '_pp-product-container')
        # 点击消息
        self.click_element('xpath', '/html/body/div[3]/div/div/div/div/div[1]/ul/li[1]/div/i')
        self.driver.implicitly_wait(5)
        # 点击通讯录
        self.click_element('xpath', '//*[@id="app"]/section/div/section/section/section[5]/div')
        # 点击tester2
        self.click_element('xpath', '//*[@id="root-contacts"]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]')
        # 输入消息
        self.input_text('xpath', '//*[@id="root-userCardModal"]/div/div[1]/div/div/div/div[2]/div/input', 'hello')
        time.sleep(5)
        # 回车发送
        Keys.ENTER()



if __name__ == '__main__':
    ll = SendMessage()
    ll.sendMessage()