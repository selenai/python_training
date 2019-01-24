from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", lastname="lastname1", address="address1", home="home1", mobile="mobile1", work="work1",
            email="email-1", email2="email2-1", email3="email3-1", phone2="phone2-1"),
    Contact(firstname="firstname2", lastname="lastname2", address="address2", home="home2", mobile="mobile2", work="work2",
            email="email-2", email2="email2-2", email3="email3-2", phone2="phone2-2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", home="", mobile="", work="", email="", email2="", email3="",
                 phone2="")] + [
    Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20),
            address=random_string("address", 20), home=random_string("home", 20), mobile=random_string("mobile", 20),
            work=random_string("work", 20), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20), phone2=random_string("phone2", 20))
    for i in range(5)
    ]
