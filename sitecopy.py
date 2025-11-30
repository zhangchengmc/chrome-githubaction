from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

url = "https://19870310.xyz"

# 循环10次
for i in range(10):
    driver.get(url)
    time.sleep(5)  # 简单等待5秒；可用WebDriverWait更智能
    print(f"第 {i+1} 次加载完成")

driver.quit()