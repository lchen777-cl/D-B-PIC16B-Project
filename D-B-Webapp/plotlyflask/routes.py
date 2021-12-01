#learn from: https://hackersandslackers.com/plotly-dash-with-flask/
#access document from: https://github.com/toddbirchard/plotlydash-flask-tutorial/tree/master/plotlyflask_tutorial

"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template


@app.route("/")
def home():
    """Landing homepage."""
    return render_template(
        "index.jinja2",
        title="TAX&Transfer Project",
        description="Analysis of Tax Policy for States",
        template="home-template",
        body="This is a homepage served with Flask.",
    ) #render template with title, description
