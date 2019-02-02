# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="1TestGroup"))
    old_groups = db.get_group_list()
    modified_group = random.choice(old_groups)
    index = old_groups.index(modified_group)
    group = Group(name="New group")
    group.id = modified_group.id
    app.group.modify_group_by_id(modified_group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
