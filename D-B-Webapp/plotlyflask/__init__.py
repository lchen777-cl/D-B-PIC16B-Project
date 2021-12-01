#reference from: https://hackersandslackers.com/plotly-dash-with-flask/

"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment



def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False) #initialize flask app
    app.config.from_object("config.Config") #construct config
    #register asset with app
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
        
        app = init_dashboard(app) #add plotly dashboard to corresponsing subpage/dashapp/
        app = init_dashboard2(app) #add plotly dashboard to corresponsing subpage/dashapp2/
        app = init_dashboard3(app) #add plotly dashboard to corresponsing subpage/dashapp3/

        compile_static_assets(assets)  # Compile static assets

        return app


