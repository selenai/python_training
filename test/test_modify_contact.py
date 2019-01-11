# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="1FN", lastname="2LN"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="1FN", lastname="2LN")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_nickname(app):
#    if app.contact.count() == 0:
#        app.contact.create_contact(Contact(firstname="1TestContact"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(nickname="New nickname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
