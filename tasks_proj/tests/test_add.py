"""Test the tasks.add() API function."""

import pytest
from tasks import Task, TasksDB


# given, when, then
# or
# arrange, acct, assert

def test_add_first_attempt(tmpdir):
    # GIVEN an empty db
    db_path = tmpdir.join('.tasks_db.json')
    db = TasksDB(db_path)
    assert 0 == db.count()

    # WHEN I add something
    new_task = Task('do something')
    new_id = db.add(new_task)

    # THEN count() return 1
    # AND list_tasks() will return new task
    # AND list_tasks() will return 1 item
    # AND get() will return new task
    # (choice of side effects, but this is overkill)
    assert 1 == db.count()
    assert new_task == db.list_tasks()[0]
    assert 1 == len(db.list_tasks())
    assert new_task == db.get(new_id)


