from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser


faker = Faker()


def test_register():
    """ Testing registry method """

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # testing inputs
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # Testing outputs
    assert response["Success"]
    assert response["Data"]


def test_register_fail():
    """ Testing registry method in fail """

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.random_number(digits=2), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # testing inputs
    assert user_repo.insert_user_params == {}

    # Testing outputs
    assert not response["Success"]
    assert response["Data"] is None
