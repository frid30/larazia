from faker import Faker

fake = Faker()

class Name:
    def __init__(self) -> None:
        pass
    def name(self):
        return fake.first_name()
class Email:
    def __init__(self) -> None:
        pass
    def get_email(self):
        return 