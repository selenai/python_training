# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="aa", middlename="xx", lastname="cc", nickname="vv", title="bb", company="nn",
                        address="mm", home="aa", mobile="ss", work="dd", fax="ff", email="gg", email2="hh", email3="jj",
                        homepage="kk", bday="18", bmonth="December", byear="1980", aday="18", amonth="December",
                        ayear="1990", address2="qwe", phone2="df", notes="gg")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
#                        home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="",
#                        bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="")
#    app.contact.create_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
