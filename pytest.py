import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_data():
    return [
    ["Admin","123"],
    ["admin","321"],
    ["ADMIN","999"]]


  
@pytest.mark.parametrize("username,password",get_data())
def test_parametrize(username,password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://seleniumpractise.blogspot.com/")
    driver.find_element(By.XPATH,"//input[@id='user']").send_keys(username)
    driver.find_element(By.XPATH,"//input[@id='pass1']").send_keys(password)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f'C:\\Screenshots\\image{timestamp}.png')
    
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)
    
def test_Login_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://seleniumpractise.blogspot.com/")
    driver.find_element(By.XPATH,"//input[@id='user']").send_keys("username")
    driver.find_element(By.XPATH,"//input[@id='pass1']").send_keys("password")
    driver.save_screenshot("C:\\Screenshots\\image4.png")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)

def test_Login_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://seleniumpractise.blogspot.com/")
    driver.find_element(By.XPATH,"//input[@id='user']").send_keys("Ashish")
    driver.find_element(By.XPATH,"//input[@id='pass1']").send_keys("Khobragade")
    driver.save_screenshot("C:\\Screenshots\\image5.png")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)
    
def test_Login_4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://seleniumpractise.blogspot.com/")
    driver.find_element(By.XPATH,"//input[@id='user']").send_keys("Shaurya")
    driver.find_element(By.XPATH,"//input[@id='pass1']").send_keys("Khobragade")
    driver.save_screenshot("C:\\Screenshots\\image6.png")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)