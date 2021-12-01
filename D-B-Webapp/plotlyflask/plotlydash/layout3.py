# reference from: https://hackersandslackers.com/plotly-dash-with-flask/
# access from: https://github.com/toddbirchard/plotlydash-flask-tutorial/tree/master/plotlyflask_tutorial

"""Plotly Dash HTML layout override."""

html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body class="dash-template">
            <header>
              <div class="nav-wrapper">
                <a href="/">
                    <img src="/static/img/name.png" class="logo" />
                    <h1>EITC Rules&Effects</h1>
                  </a>
                <nav>
                </nav>
            </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
"""
