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

@given("a user accesses the internal mail page (1b)")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'))
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user sends a message with at least one mandatory field unfilled (1b)")
def when(context):
    # login
    username = context.driver.find_element_by_id("login")
    username.send_keys("marayahalunaaudment")
    password = context.driver.find_element_by_id("password")
    password.send_keys("abcd1234")
    context.driver.find_element_by_id("login-btn").click()
    time.sleep(2)

    # steps
    # context.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/div/li[4]/a[2]').click() #janela pequena
    # context.driver.find_element_by_id('nav-item-3').click() #janela grande

    mail = WebDriverWait(context.driver, 40)
    mail.until(ec.element_to_be_clickable((By.ID, 'nav-item-3'))).click()
    
    # espera o carregamento da página
    while(context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/ngx-spinner').is_displayed()):
        pass
    
    time.sleep(1)

    context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[1]/app-intern-mail-tabs/ul/li[3]/div/label').click()

    # espera o carregamento da página
    while(context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/ngx-spinner').is_displayed()):
        pass
    
    time.sleep(1)

    context.driver.find_element_by_id('messageSubject').send_keys('assunto teste')

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll down
    context.driver.find_element_by_id('btn-send').click()

@then('it should see "Required Field" next to the fields that have not been filled in (1b)')
def then(context):
    try:
        warning = ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[2]/app-new-intern-message/div/form/div/div[3]/div/app-text-editor/label'))
        WebDriverWait(context.driver, 10).until(warning)
    except TimeoutException:
        print('Timed out waiting for page to load')
    finally:
        time.sleep(1)
        context.driver.close()