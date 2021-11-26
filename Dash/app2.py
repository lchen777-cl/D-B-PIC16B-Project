import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
from plotly.subplots import make_subplots


def p2f(x):
    return float(x.strip('%'))/100

app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
EITC2021 = pd.read_csv('State EITC Rule.csv', converters={'EITC':p2f})
EITC = pd.read_csv('State EITC Share of Return.csv')
Family = pd.read_csv('State EITC Family.csv')

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("EITC by States", style={'text-align': 'center'}),

    #html.H2("States EITC Rule", style={'text-align': 'left'}),

    dcc.Graph(id='state_tax_credits', figure={}),

    html.Br(),

    #html.H2("EITC Amounts by States", style={'text-align': 'left'}),

    dcc.Graph(id='state_share', figure={}),

    html.Br(),

    dcc.Slider(
        id = 'year',
        min=1997,
        max=2018,
        value = 2018,
        step = None,
        marks={i: 'Y{}'.format(i) for i in range(1997,2019)},
    ),

    html.Br(),

    dcc.Graph(id='state_family', figure={}),

    html.Div(id='output_container', children=[]),
    html.Br(),


])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='state_tax_credits', component_property='figure'),
     Output(component_id='state_share', component_property='figure'),
     Output(component_id='state_family', component_property='figure'),],
    [Input(component_id='year', component_property='value'),]
)
def update_graph(year):


    #figure1

    EITC2021['text'] = EITC2021['State'] + '<br>' +'Year Enacted: ' + EITC2021['Year'] + '<br>' + \
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
        width=1200, height=600,
        title_text='2021 Earned Income Tax Credit by States',
        geo = dict(
            scope='usa',
            projection=go.layout.geo.Projection(type = 'albers usa')
        ),
        annotations = [dict(
            x=0.5,
            y=-0.3,
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
        width=1200, height=600,
        title_text=str(year) + ' Share of Returns with EITC by State',
        geo = dict(
           scope='usa',
           projection=go.layout.geo.Projection(type = 'albers usa')
        ),
        annotations = [dict(
            x=0.5,
            y=-0.3,
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
        width=1200, height=600,
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

    #container
    container = ""


    return container, fig1, fig2, fig3

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)