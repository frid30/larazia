from faker import Faker

fake = Faker()

class Feed:
    def __init__(self) -> None:
        pass
    def name(self):
        return fake.first_name()
    def password(self):
        return fake.password()
    def firstname(self):
        return fake.first_name()
class Email:
    def __init__(self) -> None:
        pass
    def get_email(self):
        return 