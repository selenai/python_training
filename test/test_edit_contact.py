# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstname="1z", middlename="1x", lastname="1c", nickname="1v", title="1b", company="1n",
                        address="1m", home="1a", mobile="1s", work="1d", fax="1f", email="1g", email2="1h", email3="1j",
                        homepage="1k", bday="1", bmonth="November", byear="1979", aday="2", amonth="October",
                        ayear="1989", address2="1qwe", phone2="1df", notes="1gg"))

    app.session.logout()