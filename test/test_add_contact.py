# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


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


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
