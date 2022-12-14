from flask import Flask


def create_app(test_config=None):
    """
    Returns the configured Flask application.
    """
    app = Flask(__name__, instance_relative_config=True)

    from flaskr.views import ping, disk, cpu
    app.register_blueprint(ping.bp)
    app.register_blueprint(cpu.bp)
    app.register_blueprint(disk.bp)

    return app
