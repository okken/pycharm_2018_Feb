"""
tasksdb : Storing tasks for people to do.

Interface

class Task(): # used to pass info between CLI and TasksDB
    summary: str attribute, defaults to None
    owner: str attribute, defaults to None
    done: bool attribute, defaults to None
    id: int attribute, defaults to None, filled in by TasksDB, not by CLI

    # helper funcs
    def from_dict(cls, d):
    def to_dict(self):

class TasksDB():
    # main interface
    def __init__(self, db_path):
    def add(self, task: Task) -> int:
    def get(self, task_id: int) -> Task:
    def list_tasks(self) -> List[Task]:
    def count(self) -> int:
    def update(self, task_id: int, task_mods: Task) -> None:
    def delete(self, task_id: int) -> None:

"""

import attr
from typing import List
import tinydb


# --- Task data type
# see http://www.attrs.org/

@attr.s
class Task(object):
    summary: str = attr.ib(default=None)
    owner: str = attr.ib(default=None)
    done: bool = attr.ib(default=None)
    id: int = attr.ib(default=None, cmp=False)

    @classmethod
    def from_dict(cls, d):
        return Task(**d)  # dictionary unpacking as of Python 3.5, PEP 448

    def to_dict(self):
        return attr.asdict(self)

# --- actions on db


class TasksDB():

    def __init__(self, db_path):
        self._db = tinydb.TinyDB(db_path)

    def add(self, task: Task) -> int:
        """Add a task to the db."""
        task.id = self._db.insert(task.to_dict())
        self._db.update(task.to_dict(), doc_ids=[task.id])
        return task.id

    def get(self, task_id: int) -> Task:
        """Return a task with a matching id."""
        return Task.from_dict(self._db.get(doc_id=task_id))

    def list_tasks(self) -> List[Task]:
        """Return a list of all tasks."""
        return [Task.from_dict(t) for t in self._db]

    def count(self) -> int:
        """Return the number of tasks in db."""
        return len(self._db)

    def update(self, task_id: int, task_mods: Task) -> None:
        """Update a task with modifications."""
        d = task_mods.to_dict()
        changes = {k: v for k, v in d.items() if v is not None}
        self._db.update(changes, doc_ids=[task_id])

    def delete(self, task_id: int) -> None:
        """Remove a task from db with given task_id."""
        self._db.remove(doc_ids=[task_id])


