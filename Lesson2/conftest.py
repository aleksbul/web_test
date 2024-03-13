import pytest
from module import Site
import yaml

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

@pytest.fixture
def email_input():
    return '//*[@id="login"]/div[1]/label/input'

@pytest.fixture
def password_input():
    return '//*[@id="login"]/div[2]/label/input'

@pytest.fixture
def error():
    return '//*[@id="app"]/main/div/div/div[2]/h2'

@pytest.fixture
def submit():
    return "button"

@pytest.fixture
def error_result():
    return "401"

@pytest.fixture
def site():
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.close()
