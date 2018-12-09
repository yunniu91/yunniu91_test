from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import unittest
import random

username = "yyx" + str(random.randint(1,1000))
class testWebUI(unittest.TestCase):
    def setUp(self):
        self.username = username
        self.url = "http://39.98.63.132:8040/"
        self.dr = webdriver.Ie()
        self.dr.implicitly_wait(10)

    # 登录
    def test_case_1_dl(self):
        self.dr.get(self.url)
        self.dr.find_element_by_css_selector("input[name='imageField']").click()

    # 公共方法
    def allfound(self):
        self.dr.get(self.url)
        self.dr.find_element_by_css_selector("input[name='imageField']").click()
        sleep(2)
        self.dr.switch_to.frame(1)
        self.dr.find_element_by_css_selector("img[id='ri2']").click()
        self.dr.switch_to.default_content()
        sleep(2)

    # 查询
    def test_case_2_select(self):
        self.allfound()#调用公共方法
        self.dr.switch_to.frame(3)
        self.dr.find_element_by_css_selector("input[id='select-key:useruuid']").clear()
        self.dr.find_element_by_css_selector("input[id='select-key:useruuid']").send_keys("zhangsan")
        self.dr.find_element_by_css_selector("input[name='select-key_submit']").click()
        sleep(2)

    # 新增
    def test_case_3_add(self):
        self.allfound()#调用公共方法
        self.dr.switch_to.frame(3)
        self.dr.find_element_by_css_selector("input[name='record_record_addRecord']").click()
        signal = False
        for i in range(10):  # 该循环只为增加查询成功率
            windowsHandlers = self.dr.window_handles
            for h in windowsHandlers:
                self.dr.switch_to.window(h)
                title = self.dr.title
                if "增加人员维护" == title:
                    signal = True
                    break
            if signal: break
        self.dr.find_element_by_id("record:useruuid").send_keys(username)
        self.dr.find_element_by_id("record:name").send_keys(username)
        self.dr.find_element_by_id("record:department").send_keys("部门")
        s = self.dr.find_element_by_id("record:roleuuid")
        Select(s).select_by_value("软件工程师")
        d = self.dr.find_element_by_id("record:ability")
        Select(d).select_by_value("000000")
        self.dr.find_element_by_css_selector("input[name='record_record_saveAndExit']").click()
        sleep(2)

    # 删除
    def test_case_4_delete(self):
        self.allfound()#调用公共方法
        self.dr.switch_to.frame(3)
        self.dr.find_element_by_css_selector("input[id='select-key:useruuid']").clear()
        self.dr.find_element_by_css_selector("input[id='select-key:useruuid']").send_keys(username)
        self.dr.find_element_by_css_selector("input[name='select-key_submit']").click()
        sleep(2)

        self.dr.find_element_by_css_selector("input[name='record:_flag']").click()
        self.dr.find_element_by_css_selector("input[name='record_record_deleteRecord']").click()
        self.dr.switch_to.alert.accept()  # 确定
        sleep(2)
        self.dr.switch_to.alert.accept()  # 确定
        sleep(2)

    def tearDown(self):
         self.dr.quit()

if __name__ == "__main__":
    unittest.main()