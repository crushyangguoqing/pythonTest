from selenium import webdriver

class Basepage:
    def __init__(self):
        self.driver = webdriver.Chrome()

    # 元素定位
    def locater(self, locater_type, value):
        if locater_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
            return el
        elif locater_type == 'id':
            el = self.driver.find_element_by_id(value)
            return el
        elif locater_type == 'name':
            el = self.driver.find_element_by_name(value)
            return el
        elif locater_type == 'class':
            el = self.driver.find_element_by_class_name(value)
            return el

    # 输入
    def input_text(self, locater_type, value, text):
        self.locater(locater_type, value).send_keys(text)

    # 点击
    def click_element(self, locater_type, value):
        self.locater(locater_type, value).click()