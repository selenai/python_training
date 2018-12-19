# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New first name"))
    app.session.logout()


def test_modify_contact_nickname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(nickname="New nickname"))
    app.session.logout()
