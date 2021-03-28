from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import FindPet


faker = Faker()


def test_by_pet_id():
    """ Testing by_pet_id method """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_pet.by_pet_id(pet_id=attributes["id"])

    # Testing inputs
    assert pet_repo.select_pet_params["pet_id"] == attributes["id"]

    # Testing Outputs
    assert response["Success"]
    assert response["Data"]


def test_by_user_id():
    """ Testing by_user_id method """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = find_pet.by_user_id(user_id=attributes["user_id"])

    # Testing inputs
    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    # Testing Outputs
    assert response["Success"]
    assert response["Data"]


def test_by_id_and_name():
    """ Testing by_pet_id_and_user_id method """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }
    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["id"], user_id=attributes["user_id"]
    )

    # Testing inputs
    assert pet_repo.select_pet_params["pet_id"] == attributes["id"]
    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    # Testing Outputs
    assert response["Success"]
    assert response["Data"]
