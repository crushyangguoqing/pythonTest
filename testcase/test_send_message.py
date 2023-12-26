import os
import pytest


from webtest.SendMessage import SendMessage


class TestSendMessage:
    def test_01_sendmessage(self):

        SendMessage.sendMessage()



if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./temp -o ./reports")