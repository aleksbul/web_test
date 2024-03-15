import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'img.jpg')

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(email_input, password_input, submit, error, error_result, site):
    input1 = site.find_element("xpath", email_input)
    input1.send_keys("test")
    input2 = site.find_element("xpath", password_input)
    input2.send_keys("test")
    btn = site.find_element("css", submit)
    btn.click()
    error_label = site.find_element("xpath", error)
    assert error_label.text == error_result


def test_step2(email_input, password_input, submit, error, error_result, site):
    input1 = site.find_element("xpath", email_input)
    input1.send_keys(testdata['email'])
    input2 = site.find_element("xpath", password_input)
    input2.send_keys(testdata['password'])
    btn = site.find_element("css", submit)
    btn.click()
    hello_text = site.find_element("xpath", '//*[@id="app"]/main/nav/ul/li[3]/a').text
    assert f"Hello, {testdata['email']}" == hello_text


def test_user_can_create_post(site, email_input, password_input, submit):
    site.find_element("xpath", email_input).send_keys(testdata['email'])
    site.find_element("xpath", password_input).send_keys(testdata['password'])
    site.find_element("css", submit).click()
    WebDriverWait(site.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#create-btn")))
    site.find_element("css", "#create-btn").click()
    site.find_element("xpath", '//*[@id="create-item"]/div/div/div[1]/div/label').send_keys(testdata['title'])
    site.find_element("xpath", '//*[@id="create-item"]/div/div/div[2]/div/label').send_keys(testdata['description'])
    site.find_element("xpath", '//*[@id="create-item"]/div/div/div[3]/div/label').send_keys(testdata['content'])
    site.find_element("xpath", '//*[@id="create-item"]/div/div/div[6]/div/div/label/input').send_keys(file_path)
    site.find_element("xpath", '//*[@id="create-item"]/div/div/div[7]/div/button/span').click()
    WebDriverWait(site.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
    post_name = site.find_element("xpath", '//*[@id="app"]/main/div/div[1]/h1').text
    assert testdata['title'] == post_name, "The post wasn't created"
