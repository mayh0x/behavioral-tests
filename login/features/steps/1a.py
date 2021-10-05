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

@given("a user accesses a login page (1a)")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'))
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user submits their data with correct username and password (1a)")
def when(context):
    context.driver.find_element_by_id('enUS').click()
    username = context.driver.find_element_by_id("login")
    username.send_keys("marayahalunaaudment")
    password = context.driver.find_element_by_id("password")
    password.send_keys("abcd1234")
    context.driver.find_element_by_id("login-btn").click()

@then("it must be redirected to a logged area (1a)")
def then(context):
    try:
        element = ec.presence_of_element_located((By.ID, 'nav-item-3'))
        WebDriverWait(context.driver, 10).until(element)
    except TimeoutException:
        print('Timed out waiting for page to load')
    finally:
        time.sleep(1)
        context.driver.close()
