from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 替换为你的chromedriver路径
CHROMEDRIVER_PATH = 'chromedriver'  # 或完整路径 'C:/tools/chromedriver.exe'

# 打开Chrome
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

url = "https://19870310.xyz"

# 循环10次
for i in range(10):
    driver.get(url)
    # 等待页面加载完毕（可根据实际网站调整等待条件）
    time.sleep(5)  # 简单等待5秒；可用WebDriverWait设置更智能
    print(f"第 {i+1} 次加载完成")

# 关闭浏览器
driver.quit()
