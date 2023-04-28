import datetime
import time
from selenium import webdriver

# 定义保存网页为图片的函数
def save_webpage_as_image(url, filename):
    # 创建一个 Chrome WebDriver 实例
    driver = webdriver.Chrome()
    # 最大化浏览器窗口
    driver.maximize_window()
    # 打开指定的网页
    driver.get(url)
    # 等待页面加载完成
    time.sleep(5)
    # 将网页内容保存为图片
    driver.save_screenshot(filename)
    # 关闭浏览器窗口
    driver.quit()

# 设置保存图片的时间间隔
save_interval = 5 * 60  # 5分钟

# 保存第一个网页
url1 = "https://www.163.com/"
filename1 = "webpage_163_" + str(int(datetime.datetime.now().strftime("%Y%m%d"))) + ".png"
save_webpage_as_image(url1, filename1)

# 等待指定的时间间隔
time.sleep(save_interval)

# 保存第二个网页
url2 = "https://www.google.com/finance?hl=zh"
filename2 = "webpage_google_" + str(int(time.time())) + ".png"
save_webpage_as_image(url2, filename2)
