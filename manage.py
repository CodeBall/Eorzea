from eorzea import create_app
from flask_script import Manager, Server


app = create_app()
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=5000))


@manager.command
def init():
    """
    init db
    """
    from eorzea.scripts import init_category
    init_category()


if __name__ == '__main__':
    manager.run()

