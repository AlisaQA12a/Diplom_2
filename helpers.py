import random
import string
from faker import Faker

faker = Faker()

def generate_username():
    return faker.name() + "".join(random.choice(string.ascii_lowercase) for _ in range(12))


def generate_email():
    email = faker.email()
    name, domain = email.split("@")
    name += "".join(random.choice(string.ascii_lowercase) for _ in range(12))
    return f"{name}@{domain}"


def generate_password():
    return faker.password(length=8, digits=True)