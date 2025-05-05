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
    driver.quit()                                                          # Quits Chrome.


def test_Guvi_login(driver):                                               # A function to test login functionalities.                                              
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")                                     # Opens the main page of the guvi portal.
    driver.execute_script("window.open('https://www.guvi.in/sign-in/')")   # Navigates to the login page.
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])                      # Used to switch between web pages.
    time.sleep(5)

    driver.find_element( By.ID,"email").send_keys("********.com")          # Testing the email using its ID.
    driver.find_element( By.ID,"password").send_keys("*****20003")         # Used to find the passowrd by its ID.
    driver.find_element( By.ID,"login-btn").click()                        # Using click() button to login for the website.
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
        try:                                                                # Using exception handling to continue the workflow of program.

             error = driver.find_element(By. CLASS_NAME, "invalid-feedback") #Throws an error because of the invalid login credentials.
             print(" LOgin failed as expected with message:", error.text) 
        except Exception as e:
             print("erroe element not found")  
   

