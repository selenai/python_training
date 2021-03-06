import re
from model.contact import Contact


def test_phones_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="1TestContact"))
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)

    for contact_from_home_page in contacts_from_home_page:
        for contact_from_db in contacts_from_db:
            if contact_from_home_page.id == contact_from_db.id:
                assert contact_from_home_page.lastname == del_extra_spaces(contact_from_db.lastname)
                assert contact_from_home_page.firstname == del_extra_spaces(contact_from_db.firstname)
                assert contact_from_home_page.address == contact_from_db.address
                assert contact_from_home_page.all_email_from_home_page == merge_emails_like_on_home_page(contact_from_db)
                assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)


def del_extra_spaces(s):
    return re.sub(' +', ' ', s).strip()


def clear(s):
    return re.sub("[()/ -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: del_extra_spaces(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2]))))

#def test_phones_on_home_page(app):
#    contact_list = app.contact.get_contact_list()
#    index = randrange(len(contact_list))
#    contact_from_home_page = app.contact.get_contact_list()[index]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#    assert contact_from_home_page.address == contact_from_edit_page.address
#    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.home == contact_from_edit_page.home
#    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#    assert contact_from_view_page.work == contact_from_edit_page.work
#    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2