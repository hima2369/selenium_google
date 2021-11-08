from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(r"C:\Users\Manosasi\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")

driver.find_element_by_xpath('(//a[@role="button"])[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//input[@name="firstname"]').send_keys("himabindu")
time.sleep(3)
driver.find_element_by_xpath('//input[@name="lastname"]').send_keys("kollam")
driver.find_element_by_xpath('//input[@name="reg_email__"]').send_keys("himabindureddy45@gmail.com")
driver.find_element_by_xpath('//input[@name="reg_email_confirmation__"]').send_keys("himabindureddy45@gmail.com")
driver.find_element_by_xpath('(//input[@type="password"])[2]').send_keys("Bindureddy@45")
select_day=Select(driver.find_element_by_xpath('//select[@name="birthday_day"]'))
select_day.select_by_value('6')

select_month=Select(driver.find_element_by_xpath('//select[@name="birthday_month"]'))
select_month.select_by_value('4')

select_year=Select(driver.find_element_by_xpath('//select[@name="birthday_year"]'))
select_year.select_by_value("1998")

driver.find_element_by_xpath('//input[@value="1"]').click()
driver.find_element_by_xpath('//button[@name="websubmit"]').click()


