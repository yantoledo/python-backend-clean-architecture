from faker import Faker
from src.domain.models import Pets

faker = Faker()


def mock_pets() -> Pets:
    """ Mocking Pets """

    return Pets(
        id=faker.random_number(digits=5),
        name=faker.name(),
        specie=faker.name(),
        age=faker.random_number(digits=2),
        user_id=faker.random_number(digits=5),
    )
