
from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="1TestGroup"))
    group = random.choice(db.get_group_list())
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="1TestContact"))
    old_contacts_in_group = db.get_contacts_in_group(group)

    contact = random.choice(db.get_contact_list())
    contact_exists_in_group = False

    if len(old_contacts_in_group) > 0:
        for c in old_contacts_in_group:
            if c.id == contact.id:
                contact_exists_in_group = True
            break
    else:
        contact_exists_in_group == False
        app.contact.add_contact_to_group(contact.id, group.id)
        old_contacts_in_group.append(contact)

    new_contacts_in_group = db.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
