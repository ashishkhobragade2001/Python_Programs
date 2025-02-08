from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
action = ActionChains(driver)

def right_click():
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Practice']")

    action.context_click(element).perform()
    time.sleep(5)

#right_click()

def double_click_test():
    driver.get("https://doubleclicktest.com/")
    driver.maximize_window()
    
    action.double_click().perform()
    time.sleep(5)
    
double_click_test()
   
    