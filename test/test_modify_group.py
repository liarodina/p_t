from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group")) # передаем в качестве пвараметра обьект типа групп

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))  # передаем в качестве пвараметра обьект типа групп
