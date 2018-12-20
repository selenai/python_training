# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New first name"))


def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(Contact(nickname="New nickname"))
