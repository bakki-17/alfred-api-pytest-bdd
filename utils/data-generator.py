from faker import Faker

class DataGenerator:
    def __init__(self) -> None:
        self.fake = Faker()

    def generate_pet_data_with_faker(self):
        return{
            "id": self.fake.random_int(min=1, max=1000),
            "category": {
                "id": self.fake.random_int(min=1, max=100),
                "name": self.fake.word()
            },
            "name": self.fake.first_name(),
            "photoUrls": [self.fake.url],
            "tags": [
                {
                    "id": self.fake.random_int(min=1, max=100),
                    "name": self.fake.word()
                }
            ],
            "status": self.fake.random_element(elements=("available", "pending", "sold"))
        }
    
    def generate_oder_data_with_faker(self):
        return{
            "id": self.fake.random_int(min=1, max=100),
            "petId": self.fake.random_int(min=1, max=100),
            "quantity": self.fake.random_int(min=1, max=100),
            "shipDate": self.fake.iso8601()
        }
    
    def generat_user_data(self):
        return[
            {
                "id": 0,
                "username": "string",
                "firstName": "string",
                "lastName": "string",
                "email": "string",
                "password": "string",
                "phone": "string",
                "userStatus": 0
            }
        ]