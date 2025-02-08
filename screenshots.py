from selenium import webdriver
from selenium.webdriver.common.by import By
import time

filename = "C:\\get_screenshot_as_png_method.png"
filename2 = "C:\\save_screenshot_method.png"

def setup():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    return driver
    
def take_screenshot(filename):
    driver = setup()
    driver.find_element(By.XPATH, "//a[@id='opentab']").click()
    time.sleep(5)
    
    select_window = driver.window_handles
    driver.switch_to.window(select_window[-1])  # Switch to the latest opened window
    time.sleep(2)  
    
    ## screenshot 
    binary_data = driver.get_screenshot_as_png()
    with open (filename, "wb") as file:
        file.write(binary_data)
    print(f"file successfully save in {filename} directory")
    
def take_screenshot_method(filename2):
    driver = setup()
    driver.save_screenshot(filename2)
    print(f"save screenshot in {filename2} directory")
    time.sleep(2)
    
take_screenshot(filename)
take_screenshot_method(filename2)