"""Initialize Flask app."""
from ddtrace import patch_all
from flask import Flask
from flask_assets import Environment

patch_all()


def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes
        from .assets import compile_static_assets

        # Import Dash application
        from .plotlydash.dashboard import init_dashboard as init_dashboard
        from .plotlydash.dashboard2 import init_dashboard as init_dashboard2
        from .plotlydash.dashboard3 import init_dashboard as init_dashboard3
        
        app = init_dashboard(app)
        app = init_dashboard2(app)
        app = init_dashboard3(app)



        # Compile static assets
        compile_static_assets(assets)

        return app
