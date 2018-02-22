"""Command Line Interface (CLI) for tasks project."""

import click
from tasks.tasksdb import Task, TasksDB
import pathlib


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.1.1')
def tasks_cli():
    """Run the tasks application."""
    pass


@tasks_cli.command(help="add a task")
@click.argument('summary')
@click.option('-o', '--owner', default=None,
              help='set the task owner')
def add(summary, owner):
    """Add a task to db."""
    tasks_db().add(Task(summary, owner))


@tasks_cli.command(help="delete a task")
@click.argument('task_id', type=int)
def delete(task_id):
    """Remove task in db with given id."""
    tasks_db().delete(task_id)


@tasks_cli.command(name="list", help="list tasks")
def list_tasks():
    """
    List tasks in db.

    If owner given, only list tasks with that owner.
    """
    formatstr = "{: >4} {: >10} {: >5} {}"
    print(formatstr.format('ID', 'owner', 'done', 'summary'))
    print(formatstr.format('--', '-----', '----', '-------'))
    for t in tasks_db().list_tasks():
        done = ' x ' if t.done else ''
        owner = '' if t.owner is None else t.owner
        print(formatstr.format(
              t.id, owner, done, t.summary))


@tasks_cli.command(help="update task")
@click.argument('task_id', type=int)
@click.option('-o', '--owner', default=None,
              help='change the task owner')
@click.option('-s', '--summary', default=None,
              help='change the task summary')
@click.option('-d', '--done', default=None,
              type=bool,
              help='change the task done state (True or False)')
def update(task_id, owner, summary, done):
    """Modify a task in db with given id with new info."""
    tasks_db().update(task_id, Task(summary, owner, done))


@tasks_cli.command(help="list count")
def count():
    """Return number of tasks in db."""
    print(tasks_db().count())


def tasks_db():
    # just put it in users home dir for now
    db_path = str(pathlib.Path().home() / '.tasks_db.json')
    return TasksDB(db_path)


if __name__ == '__main__':
    tasks_cli()
