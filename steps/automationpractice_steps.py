from behave import given, when, then
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
# TODO:
# MOVE ADDITIONAL METHODS TO UTILS ETC. OR SOME FIXTURE

email = 'paw.kuznik+99@gmail.com'
password = '123456'


def generate_unique_email():
    number = random.randint(0, 999999)
    random_email = 'paw.kuznik' + '+' + str(number) + '@gmail.com'
    print(random_email)
    return random_email


@given(u'User is on the Home Page')
def user_on_home_page(context):
    context.driver.get("http://automationpractice.com/index.php")


@when(u'User enters the {item_name}')
def step_impl(context, item_name):
    context.driver.find_element(By.CSS_SELECTOR,  u"#search_query_top").send_keys(item_name)


@when(u'User chooses item from drop-down list')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, u"//*[contains(@class, 'ac_even')]")))
    context.driver.find_element(By.XPATH, u"//*[contains(@class, 'ac_even')]").click()


@when(u'User changes color')
def step_impl(context):
    context.driver.find_element(By.XPATH, u"//*[@id='color_14']").click()


@when(u'User click Add to cart button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='Add to cart']").click()


@then(u'Item is added to the cart')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, u"//span[contains(text(),'There is 1 item in your cart.')]")


@when(u'User chooses Women category')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR,  u"[title='Women']")
    webdriver.ActionChains(context.driver).move_to_element(element).perform()


@when(u'User chooses {subcategory} subcategory')
def step_impl(context, subcategory):
    context.driver.find_element(By.CSS_SELECTOR,  u"[title='" + subcategory + "']").click()


@when(u'User add to cart first item from list')
def step_impl(context):
    context.driver.find_element(By.XPATH, u"//span[text()='Add to cart']").click()


@when(u'User chooses Sign In button')
def step_impl(context):
    context.driver.find_element(By.XPATH, u"//a[contains(text(),'Sign in')]").click()
    assert context.driver.find_element(By.XPATH, "//h1[contains(text(),'Authentication')]")


@when(u'User fills in email address on create account area')
def step_impl(context):
    context.driver.find_element(By.XPATH, u"//input[@id='email_create']").send_keys(generate_unique_email())


@when(u'User fills in already used email address on create account area')
def step_impl(context):
    context.driver.find_element(By.XPATH, u"//input[@id='email_create']").send_keys(email)


@when(u'User chooses Create and account button')
def step_impl(context):
    context.driver.find_element(By.XPATH, u"//*[@id='SubmitCreate']/span").click()
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, u"//h3[text()='Your personal information']")))


@when(u'User fills all necessary information in sign up form')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, u"#customer_firstname").send_keys('test')
    context.driver.find_element(By.CSS_SELECTOR, u"#customer_lastname").send_keys('test')
    context.driver.find_element(By.CSS_SELECTOR, u"#passwd").send_keys('123456')
    context.driver.find_element(By.CSS_SELECTOR, u"#address1").send_keys('test')
    context.driver.find_element(By.CSS_SELECTOR, u"#city").send_keys('test')
    state = Select(context.driver.find_element(By.CSS_SELECTOR,  u"#id_state"))
    state.select_by_index(1)
    context.driver.find_element(By.CSS_SELECTOR, u"#postcode").send_keys('12345')
    context.driver.find_element(By.CSS_SELECTOR, u"#phone_mobile").send_keys('123456789')


@when(u'User chooces Register button')
def step_impl(context):
    context.driver.find_element(By.XPATH, u"//span[text()='Register']").click()


@then(u'User is sign in')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, u"[title='Log me out']")


@then(u'User get information about already registered email')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, u"//*[@id='create_account_error']")


@when(u'User fills in email address and password on sign in area')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#email').send_keys(email)
    context.driver.find_element(By.CSS_SELECTOR, '#passwd').send_keys(password)


@when(u'User fills in email address and invalid password on sign in area')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#email').send_keys(email)
    context.driver.find_element(By.CSS_SELECTOR, '#passwd').send_keys('qwerty')


@then(u'User gets message about failed authentication')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, u"//li[text()='Authentication failed.']")


@when(u'User chooses Sign In padlock button')
def step_impl(context):
    context.driver.find_element(By.XPATH, u"//*[@id='SubmitLogin']/span").click()
