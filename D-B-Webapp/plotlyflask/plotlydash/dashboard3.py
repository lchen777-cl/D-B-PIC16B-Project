"""Instantiate a Dash app."""
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
from plotly.subplots import make_subplots
import pathlib
from .layout3 import html_layout



def init_dashboard(server):


    dash_app = Dash(
        server=server,
        routes_pathname_prefix="/dashapp3/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
        )
    
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("../plotlydash/data").resolve()

    dash_app.index_string = html_layout

    def p2f(x):
        return float(x.strip('%'))/100

# -- Import and clean data (importing csv into pandas)
    EITC2021 = pd.read_csv(DATA_PATH.joinpath('State EITC Rule.csv'), converters={'EITC':p2f})
    EITC = pd.read_csv(DATA_PATH.joinpath('State EITC Share of Return.csv'))
    Family = pd.read_csv(DATA_PATH.joinpath('State EITC Family.csv'))


    # ------------------------------------------------------------------------------
# App layout
    dash_app.layout = html.Div(
        [
                html.Div(
                [
                    html.Div(
                        [
                            html.H2(
                                ["Introduction"], className="subtitle padded"
                            ),
                            html.P(
                                [
                                    "Launched in the 1970s and expanded in the 1990s, Earned Income Tax Credit (EITC) is the largest poverty alleviation program. \
                                    Through offsetting taxes, EITC aims for low-income working families with children and, in theory, \
                                    encourages labor force participation."
                                ],
                                style={"color": "#7A7A7A"},
                            ),
                        ],
                        className="twelve columns",
                    )
                ],
                className="row ",
            ),

            html.Div(
                [
                    html.Div(
                        [
                            html.Br([]),
                            html.H2(
                                ["EITC Rule by States"],
                                className="subtitle tiny-header padded",
                            ),
                            html.P(
                                [
                                    "Besides federal EITC, more than half of the states have refundable \
                                    or non-refundable EITC. The below graph shows the present state EITC policies.\
                                    We've noticed that California and South Carolina have a particularlly high EITC \
                                    percentage and states in the northeast tend to have in-state EITC."
                                ],
                                style={"color": "#7A7A7A"},
                            ),
                            html.Div(
                                [
                                    dcc.Graph(id='state_tax_credits', figure={}),
                                ],
                                style={"overflow-x": "auto"},
                            ),
                        ],
                        className="twelve columns",
                    )
                ],
                className="row ",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Br([]),
                            html.H2(
                                ["Share of Returns with EITC"],
                                className="subtitle tiny-header padded",
                            ),
                            html.P(
                                [
                                    "Besides EITC, there are also other types of tax credits, including \
                                    Child Tax Credits, Premium Tax Credits, and so on. The below graph shows the proportion \
                                    of EITC take in the overall tax credits. We can see each state rely on EITC differently."
                                ],
                                style={"color": "#7A7A7A"},
                            ),
                            html.Div(
                                [
                                        dcc.Graph(id='state_share', figure={}),

                                        html.Br(),

                                        dcc.Slider(
                                            id = 'year',
                                            min=1997,
                                            max=2018,
                                            value = 2018,
                                            step = None,
                                            marks={i: '{}'.format(i) for i in range(1997,2019)},
                                        ),
                                ],
                                style={"overflow-x": "auto"},
                            ),
                        ],
                        className="twelve columns",
                    )
                ],
                className="row ",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Br([]),
                            html.H2(
                                ["Family Benefited from EITC"],
                                className="subtitle tiny-header padded",
                            ),
                            html.P(
                                [
                                    "Only working poor families are eligible for EITC. The below graphs show the number of families \
                                    receiving EITC in 2016. We observe that California, Texas, New York and Florida have the highest number \
                                    of recipients."
                                ],
                                style={"color": "#7A7A7A"},
                            ),
                            html.Div(
                                [
                                       dcc.Graph(id='state_family', figure={}),

                                ],
                                style={"overflow-x": "auto"},
                            ),
                        ],
                        className="twelve columns",
                    )
                ],
                className="row ",
            ),

            ],
            className="page")

    @dash_app.callback(
    [
     Output(component_id='state_tax_credits', component_property='figure'),
     Output(component_id='state_share', component_property='figure'),
     Output(component_id='state_family', component_property='figure'),],
    [Input(component_id='year', component_property='value'),]
    )
    def update_graph(year):
    #figure1

        EITC2021['text'] = EITC2021['State'] + '<br>' +'Year Enacted: ' + EITC2021['Year'] + '<br>' +\
                             'Refundable: '+ EITC2021['Refundable'] + '<br>' +EITC2021['Note'] 

        fig1 = go.Figure(data=go.Choropleth(
            locations=EITC2021['Code'],
            z=EITC2021['EITC'],
            text = EITC2021['text'],
            locationmode='USA-states',
            colorscale='blues',
            autocolorscale=False,
            marker_line_color='white', # line markers between states
            colorbar_title="EITC<br>Percentage"
            ))

        fig1.update_layout(
            width=800, height=400,
            title_text='2021 Earned Income Tax Credit by States',
            geo = dict(
                scope='usa',
                projection=go.layout.geo.Projection(type = 'albers usa')
            ),
            annotations = [dict(
                x=0.5,
                y=-0.1,
                xref='paper',
                yref='paper',
                text='Source: <a href="https://www.taxcreditsforworkersandfamilies.org/state-tax-credits/">\
                    State Tax Credits</a>',
                showarrow = False
            )]
            )
    
        fig1.add_scattergeo(
            locations=EITC2021['Code'],    ###codes for states,
            locationmode='USA-states',
            text=EITC2021['Code'],
            mode='text',
            hoverinfo='skip')

    #figure 2
        fig2 = go.Figure(data=go.Choropleth(
            locations=EITC['Code'],
            z=EITC[str(year)],
            locationmode='USA-states',
            colorscale='Blues',
            autocolorscale=False,
            marker_line_color='white', # line markers between states
            colorbar_title="Share of Returns<br>Percentage"
            ))

        fig2.update_layout(
            width=800, height=400,
            title_text=str(year) + ' Share of Returns with EITC by States',
            geo = dict(
            scope='usa',
            projection=go.layout.geo.Projection(type = 'albers usa')
            ),
            annotations = [dict(
                x=0.5,
                y=-0.1,
                xref='paper',
                yref='paper',
                text='Source: <a href="https://www.taxpolicycenter.org/statistics/eitc-claims-state">\
                    Tax Policy Center</a>',
                showarrow = False
            )]
            )

        fig2.add_scattergeo(
            locations=EITC['Code'],    ###codes for states,
            locationmode='USA-states',
            text=EITC['Code'],
            mode='text',
            hoverinfo='skip')

    #fig3
        Family['text'] = Family['State'] + '<br>' +'Proportion to nation total: ' + Family['Proportion']

        fig3 = go.Figure(data=go.Choropleth(
            locations=Family['Code'],
            z=Family['Family'],
            text = Family['text'],
            locationmode='USA-states',
            colorscale='Blues',
            autocolorscale=False,
            marker_line_color='white', # line markers between states
            colorbar_title="Number of<br>Families"
        ))

        fig3.update_layout(
            width=800, height=400,
            title_text='2016 Working Families Benefited from the EITC by State',
            geo = dict(
                scope='usa',
                projection=go.layout.geo.Projection(type = 'albers usa')
            ),
            annotations = [dict(
                x=0.5,
                y=-0.1,
                xref='paper',
                yref='paper',
                text='Source: <a href="https://www.cbpp.org/fact-sheets-eitc-usage-by-congressional-district-and-state">\
                    Center on Budget adn Policy Priorities</a>',
                showarrow = False
            )]
        )

        fig3.add_scattergeo(
            locations=Family['Code'],    ###codes for states,
            locationmode='USA-states',
            text=Family['Code'],
            mode='text',
            hoverinfo='skip')

        return fig1, fig2, fig3

    return dash_app.server



