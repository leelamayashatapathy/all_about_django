from faker import Faker

fake = Faker("en_IN")
import random
from .models import CollegeFaker, StudentFaker,Author,Book,Person


def College_Fake_data():
    indian_universities = [
        "Indian Institute of Technology Bombay (IIT Bombay)",
        "Indian Institute of Science (IISc) Bangalore",
        "Indian Institute of Technology Delhi (IIT Delhi)",
        "Indian Institute of Technology Madras (IIT Madras)",
        "Indian Institute of Technology Kharagpur (IIT Kharagpur)",
        "University of Delhi",
        "Jawaharlal Nehru University (JNU)",
        "Indian Institute of Technology Kanpur (IIT Kanpur)",
        "Indian Institute of Technology Roorkee (IIT Roorkee)",
        "Banaras Hindu University (BHU)",
    ]
    for i in indian_universities:
        address = fake.address()
        CollegeFaker.objects.create(college_name = i , college_address = address)

def Student_fake_data(c=10)->None:
    colleges = CollegeFaker.objects.all()
    for i in range(c):
        gender_choices = ["Male", "Female"]
        college = random.choice(colleges)
        gender_choice = random.choice(gender_choices)
        name = fake.name()
        phone =  fake.phone_number()
        email = fake.email()
        gender = gender_choice
        age = random.randint(18,35)
        dob = fake.date()
        bio = fake.text()
        StudentFaker.objects.create(
            college=college,
            name = name,
            phone= phone,
            email= email,
            gender = gender,
            age= age,
            dob = dob,
            bio=bio
        )


def fakedata_author(c=20)->None:
    for i in range(c):
        author_name = fake.name()
        Author.objects.create(author_name=author_name)
        
def fake_data_book(c=100)->None:
    authors = Author.objects.all()
    for i in range (c):
        author = random.choice(authors)
        book_name =fake.sentence(nb_words=5)
        price = round(random.uniform(10,100),2)
        publish_date = fake.date_between(start_date='-2y',end_date='today')
        Book.objects.create(
            author = author,
            book_name = book_name,
            price = price,
            publish_date = publish_date
        )
        
        
def person_fake_data(c=30)->None:
    for i in range (c):
        person_name = fake.name()
        skill = fake.sentence(nb_words=5)
        
        Person.objects.create(person_name=person_name, skill=skill)
        