"""工作定时打卡"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import my_email


def go_home():
    # 无头浏览，不用显示出来
    options = Options()
    options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0')
    options.add_argument('--headless')
    my_browser = webdriver.Firefox(options=options)

    # options = Options()
    # options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0')
    # my_browser = webdriver.Firefox(options=options)
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
    #
    my_browser.find_element_by_id("SpentRecords").find_element_by_tag_name("a").click()
    time.sleep(3)
    # 花费+按钮
    my_browser.find_element_by_class_name("action-bar").find_element_by_tag_name("a").find_element_by_tag_name(
        "i").click()
    # my_browser.find_element_by_class_name("font font-add").click()
    # 切换进弹窗
    my_browser.switch_to.frame("tdialog-iframe")
    time.sleep(3)
    # 永远滴神！！！！css
    my_browser.find_element_by_css_selector("#TimesheetTimespent").clear()
    my_browser.find_element_by_css_selector("#TimesheetTimespent").send_keys("1")

    # my_browser.find_element_by_xpath("//*[@id="TimesheetTimespent"]").send_keys("1")
    my_browser.find_element_by_class_name("tui-timeedit__description").clear()
    my_browser.find_element_by_class_name("tui-timeedit__description").send_keys(
        "1.都江堰砂石平台2.重车出场未密闭3.市场问题处理")
    # 回到主界面 此元素在主界面就离谱
    my_browser.switch_to.default_content()
    my_browser.find_element_by_id("tdialog-buttonwrap").find_element_by_tag_name("a").click()
    time.sleep(10)
    # 截图
    my_browser.get_screenshot_as_file(
        r'C:\Users\Administrator\Pictures\{}.png'.format(time.strftime("%Y_%m_%d %H_%M_%S")))
    print("打卡成功")
    my_browser.quit()
    my_email.my_email()


if __name__ == '__main__':
    go_home()
