## Who is this Brian person?

* Author of [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)
* Host of [Test & Code](http://testandcode.com) podcast
* Host of [Python Bytes](https://pythonbytes.fm) podcast
* Blogs at [pythontesting.net](http://pythontesting.net)
* Works with electronic test equipment at Rohde & Schwarz

## the code man, where is the code

It's here: https://github.com/okken/pycharm_2018_Feb

(well, at least our starting point code is there)

## why this webinar

Python developers love writing code. Tests? Not so much.
Whether it’s the concepts of testing, or the interface of testing tools, testing is a chasm not all cross.

This webinar aims to bring Python testing to the masses, taking a new approach to first contact with Python testing:

Visual testing using PyCharm
Driven by the popular pytest framework
Real-world scenario during the live building of a simple Python application


* pytest is
    * the easiest framework to start using
    * way more powerful than we will cover today
    * grows with you and your projects
    * is extendable, pluggable
    * active community
    * blah, blah, blah, we know! it's awesome!
* PyCharm is like a booster rocket ( or two or three )
    * develop tests faster
    * debug tests
    * debug code
    * re-run easily
    * coverage and all
    * ...
* We aren't going to be able to cover everything cool.
    * But hopefully enough to get you more productive
    * And inspire you to learn more

## Plan for today

* setup PyCharm to run pytest
    * interpreter from venv
    * pytest for tests
    * yep, I think that's it. Unless we need to hide some stuff.
* hello world tests
    * different ways to run tests
    * run configurations
    * default pytest settings (Drop the dot!)
    * extected vs actual
    * diffs
    * continuous testing
    * adding flags via PyCharm
    * adding flags via pytest.ini

< interlude:  quick demo of tasks project >

* fixtures
    * making temp files
    * connecting to a database
    * sharing fixtures within the project
    * fixtures using fixtures
    * using test_add.py and something else
* parametrized testing
    * parametrize tests
    * multiple params
    * stacking params to matrix test
    * parametrize fixtures (probably won't get to that)
* keywords
* markers
    * and maybe marking parametrizations
* tox
* coverage
* TDD
    * did we want talk about TDD?
    * if not, how about...
* testing strategies
    * tracer bullet testing
    * code coverage and what to do about it
    * feature coverage
    * deciding how deep to go with each feature
    * RCRCRC
    * behavior coverage
    *

## startup

This is what I did before we started:

    $ git clone https://github.com/okken/pycharm_2018_Feb
    $ cd pycharm_2018_Feb/
    $ cd tasks_proj/
    $ python3.6 -m venv venv --prompt tasks_proj
    $ source venv/bin/activate
    (tasks_proj) $ pip install -e .
    (tasks_proj) $ pycharm .
    # (or open it some other way)



