from selenium import webdriver

chroopt = webdriver.ChromeOptions()

chroopt.add_argument("--start-maximized")
chroopt.add_argument("headless")
chroopt.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="D:\\PyCharm Community Edition 2019.3.3\\chromedriver.exe",options=chroopt)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)