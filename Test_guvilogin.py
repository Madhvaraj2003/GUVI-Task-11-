import pytest                                                               # Importing pytest. 
from selenium.common.exceptions import NoSuchElementException               # Using Selenium modules.
import time
from selenium import webdriver                                              # Importing webdriver. 
from selenium.webdriver.common.by import By


@pytest.fixture                                                            # Using Fixture methods.
def driver():
    driver = webdriver.Chrome()                                            # Using Chrome to test Scripts.
    driver.maximize_window()
    yield driver                                                           # Returns Driver.
    driver.quit()


def test_Guvi_login(driver):                                               # A function to test login functionalities.                                              
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")                                     # Used to get navigate 
    driver.execute_script("window.open('https://www.guvi.in/sign-in/')")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)

    driver.find_element( By.ID,"email").send_keys("madhva3@gmail.com")     # Testing the email using its ID.
    driver.find_element( By.ID,"password").send_keys("Madhvaraj2003")      # USed to find the passowrd by its ID.
    driver.find_element( By.ID,"login-btn").click()                        # Using click() to login for the website.
    print("LOGIN WAS SUCESSFULL")
    time.sleep(5)
def test_invalid_login(driver):                                            # Negative test case to check proper login functionalites.                                                           
        driver.get("https://www.guvi.in/")
        time.sleep(5)
        driver.execute_script("window.open('https://www.guvi.in/sign-in/')")
        time.sleep(4)
        driver.find_element( By.ID,"email").send_keys("wrongmail.com")      # Testing login Functionalities.
        driver.find_element( By.ID,"password").send_keys("wrongpass34") 
        driver.find_element( By.ID,"login-btn").click()
        try:                                                                # USing exception handling to continue the workflow of program.

             error = driver.find_element(By. CLASS_NAME, "invalid-feedback") # Throws an error because of the invalid login credentials.
             print(" LOgin failed as expected with message:", error.text) 
        except Exception as e:
             print("erroe element not found")  
   

