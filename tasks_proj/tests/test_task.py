"""Test the Task data type."""
from tasks import Task

def test_member_access():
    t = Task('do something', 'Brian', True, 12)
    assert (t.summary, t.owner, t.done, t.id) == \
           ('do something', 'Brian', True, 12)


def test_defaults():
    t = Task()
    assert (t.summary, t.owner, t.done, t.id) == \
           (None, None, None, None)


def test_equal():  # id isn't used for equality
    t1 = Task('do something', 'Brian', True, 1)
    t2 = Task('do something', 'Brian', True, 456)
    assert t1 == t2


def test_unequal():
    t1 = Task('do something', 'Brian', True, 1)
    t2 = Task('do something', 'Not Brian', True, 1)
    assert t1 != t2


def test_to_dict():
    t = Task('do something', 'Brian', True, 1)
    d = t.to_dict()
    expected = {'summary': 'do something',
                'owner': 'Brian', 'done': True, 'id': 1}
    assert expected == d


def test_from_dict():
    expected = Task('do something', 'Brian', True, 12)
    d = {'summary': 'do something',
         'owner': 'Brian', 'done': True, 'id': 12}
    t = Task.from_dict(d)
    assert expected == t
    assert expected.id == t.id
