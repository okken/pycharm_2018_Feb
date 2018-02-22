"""
Sample tests just to get started.
"""


def test_one():
    pass


def test_two():
    expected = (1, 2, 3)
    actual = (1, 2, 3)
    assert expected == actual


class TestSomeStuff():
    def test_three(self):
        assert {1, 2, 2} == {1, 2}
