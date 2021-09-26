from selenium import webdriver
import time
my_browser = webdriver.Firefox()
url = "https://www.tapd.cn/30152737/prong/stories/view/1130152737001000581"
my_browser.get(url)
my_browser.implicitly_wait(10)
my_browser.maximize_window()
# 输入我的账号名密码
my_browser.find_element_by_id("username").send_keys("13608031941")
my_browser.find_element_by_id("password_input").send_keys("youfei123!")
my_browser.find_element_by_id("tcloud_login_button").click()
print("当前时间为：", time.ctime())
# 等待其反应
time.sleep(3)
# # 点击过滤按钮
# my_browser.find_element_by_id("search-keyword").send_keys("游飞")
# my_browser.find_element_by_id("main_search_hover").click()
my_browser.find_element_by_id("SpentRecords").find_element_by_tag_name("a").click()
time.sleep(10)
# 截图
my_browser.get_screenshot_as_file(r'C:\Users\Administrator\Pictures\{}.png'.format(time.strftime("%Y_%m_%d %H_%M_%S")))
print("截图成功")
my_browser.quit()