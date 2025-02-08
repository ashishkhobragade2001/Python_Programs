from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
x = By.XPATH
import time

filename = "C://Ashish_python_Programms//ashish_k.xlsx"
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    return driver



def login_functionality_check(filename):
    data = pd.read_excel(filename)
    print(data)
         
    for i, row in data.iterrows():
        
        username = row["username"]
        password = row["password"]
        
        driver = setup_browser()
        time.sleep(5)
        
        driver.find_element(x, "//input[@placeholder='Username']").send_keys(username)
        driver.find_element(x, "//input[@placeholder='Password']").send_keys(password)
        
        driver.find_element(x, "//button[@type='submit']").click()
        time.sleep(3)
        
        try:
            driver.find_element(x, "//span[normalize-space()='Admin']")  
            data.iloc[i, 2] = "PASS"
        except:
            data.iloc[i, 2] = "FAIL"
        
        data.to_excel(filename, index=False)
        driver.quit()
    
login_functionality_check(filename)