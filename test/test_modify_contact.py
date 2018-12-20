# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="1TestContact"))
    app.contact.modify_first_contact(Contact(firstname="New first name"))


def test_modify_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="1TestContact"))
    app.contact.modify_first_contact(Contact(nickname="New nickname"))
