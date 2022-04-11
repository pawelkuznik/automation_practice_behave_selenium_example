from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait


def before_scenario(context, feature):
    context.driver = webdriver.Chrome()


def after_scenario(context, feature):
    context.driver.quit()

def after_step(context, feature):
    time.sleep(0.5)