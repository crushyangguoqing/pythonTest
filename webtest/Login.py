from selenium import webdriver
import time

from webtest.basePage import Basepage


class LoginWeb(Basepage):
    def loginWeb(self):
        self.driver.get("https://www.feishu.cn")
        self.driver.implicitly_wait(5)
        # 关闭弹窗广告
        self.click_element("xpath", "/html/body/div[2]/div[2]/div/div/div")
        # 点击登录按钮
        self.click_element("xpath", '//*[@id="app"]/div/div[2]/div/div/div/div/a[3]')
        # 点击账号登录
        self.click_element("xpath", '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div')
        # 输入手机号
        self.input_text('class', 'mobile-input-phone', '18995102513')
        # 勾选我已同意
        self.click_element('class', 'ud__checkbox__input')
        # 点击下一步
        self.click_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div/button')
        # 输入密码
        self.input_text('xpath', '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div[2]/div/div/div/div/div[1]/div/div/div/input', 'ruanjianceshi101..')
        # 点击下一步登录
        self.click_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div[3]/div/button')


if __name__ == '__main__':
    ll = LoginWeb()
    ll.loginWeb()
