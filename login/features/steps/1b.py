from behave import *
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)

@given("a user accesses a login page (1b)")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'))
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user fills in the fields with incorrect username and/or password (1b)")
def when(context):
    username = context.driver.find_element_by_id("login")
    username.send_keys("marayahaluna")
    password = context.driver.find_element_by_id("password")
    password.send_keys("aaaaaaaa")
    context.driver.find_element_by_id("login-btn").click()

@then("it should see “Invalid username and/or password. Please check the username and password and try again.” (1b)")
def then(context):
    try:
        warning = ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-login/html/body/form/div[1]'))
        WebDriverWait(context.driver, 10).until(warning)
    except TimeoutException:
        print('Timed out waiting for page to load')
    finally:
        time.sleep(1)
        context.driver.close()
    