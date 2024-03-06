import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(login, title):
    response = requests.get(data['website2'], headers={'X-Auth-Token': login},
                            params={"owner": "notMe", "order": "ASC"})
    titles = [i["title"] for i in response.json()['data']]
    assert response.status_code == 200 and title in titles


def test_step2(login):
    response = requests.post(data['website3'], headers={'X-Auth-Token': login}, data={'title': data['title1'],
                                                                                      'description': data[
                                                                                          'description1'],
                                                                                      'content': data['content1']})
    response2 = requests.get(data['website2'], headers={'X-Auth-Token': login})
    descriptions = [i["description"] for i in response2.json()['data']]
    if response.status_code == response2.status_code == 200:
        assert data['description1'] in descriptions
