import requests

def test_all_breeds_status_code():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    assert response.status_code == 200



import requests
import pytest

@pytest.mark.parametrize("breed_name, status_code", [("bichon", 200)])
def test_random_dog_image(breed_name, status_code):
    response = requests.get(f'https://dog.ceo/api/breed/{breed_name}/images/random')
    assert response.status_code == status_code



import requests

def test_all_hound_subbreeds():
    response = requests.get('https://dog.ceo/api/breed/hound/list')
    assert len(response.json()["message"]) > 1


import requests
import pytest

@pytest.mark.parametrize("breed_name, image_size, status_code", [("poodle", "thumb", 200)])
def test_dog_image_by_size(breed_name, image_size, status_code):
    response = requests.get(f'https://dog.ceo/api/breed/{breed_name}/images/{image_size}/random')
    assert response.status_code == status_code



