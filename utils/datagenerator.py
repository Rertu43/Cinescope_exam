from faker import Faker
class DataGenetator:
    fake = Faker()

    @classmethod
    def email(cls):
        return cls.fake.email()

    @classmethod
    def data_for_film(cls):
        return {
            "name": cls.fake.sentence(nb_words=3),
            "price": cls.fake.random_int(min=100, max=1000),
            "description": cls.fake.text(),
            "imageUrl": "https://placekitten.com/300/300",
            "location": "MSK",
            "published": True,
            "genreId": cls.fake.random_int(min=1, max=10) # TODO: определить жанры
        }

    @classmethod
    def data_for_user(cls):
        email = cls.email()
        name = cls.fake.name()
        password = cls.fake.password()
        return {
            "email": email,
            "fullName": name,
            "password": password,
            "passwordRepeat": password,
        }

    @classmethod
    def random_string(cls):
        return cls.fake.pystr(min_chars=5, max_chars=20)
