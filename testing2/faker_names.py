from faker import Faker  # could generate inconsistent data in terms of formatation (e.g. phone number, names with abbreviation, etc.)


faker = Faker(locale="es_AR")  # you don't need to specify the locale, it will generate fake data in English by default


print(f"Fake last name: {faker.last_name()}")
print(f"Fake email: {faker.email()}")
print(f"Fake password: {faker.password()}")
print(f"Fake url: {faker.url()}")
print(f"Fake license plate: {faker.license_plate()}")
print(f"Fake phone number: {faker.phone_number()}")
print(f"Fake credit card number: {faker.credit_card_number()}")
