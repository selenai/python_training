# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="1FN", lastname="2LN"))
    old_contacts = db.get_contact_list()
    modified_contact = random.choice(old_contacts)
    index = old_contacts.index(modified_contact)
    contact = Contact(firstname="1FN", lastname="2LN")
    contact.id = modified_contact.id
    app.contact.modify_contact_by_id(modified_contact.id, contact)
    new_contacts = db.get_contact_list()
#    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_contact_nickname(app):
#    if app.contact.count() == 0:
#        app.contact.create_contact(Contact(firstname="1TestContact"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(nickname="New nickname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
