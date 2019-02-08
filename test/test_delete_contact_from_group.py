from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="1TestGroup"))
    group = random.choice(db.get_group_list())

    contact = random.choice(db.get_contact_list())
    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(contact.id, group.id)

    old_contacts_in_group = db.get_contacts_in_group(group)
    app.contact.delete_contact_from_group(contact.id, group.id)
    old_contacts_in_group.remove(contact)
    new_contacts_from_group = db.get_contacts_in_group(group)

    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_from_group, key=Contact.id_or_max)
