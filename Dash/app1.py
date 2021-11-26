import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
from plotly.subplots import make_subplots




app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
df = pd.read_csv("tax_unemployment.csv")
df2 = pd.read_csv("eitc_unemployment.csv")
states = pd.read_csv("states.csv")

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Taxation and Unemployment", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_state",
                 options=[
                     #{"label": "United States", "value": 52},
                     {'label':states['States'].iloc[i], 'value':i+1} for i in range(0,52)
                 ],
                 multi=False,
                 value=52,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='tax_unemployment', figure={}),
    dcc.Graph(id='eitc_unemployment', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='tax_unemployment', component_property='figure'),
     Output(component_id='eitc_unemployment', component_property='figure'),],
    [Input(component_id='slct_state', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    #container = "The state chosen by user was: {}".format(option_slctd)
    container = " "

#figure1

    # Create figure with secondary y-axis
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    plotly = df[df['state']== option_slctd]

    # Add traces
    fig.add_trace(
        go.Scatter(
        x=plotly['year'],
        y=plotly['rate'],
        name = "unemployment rate"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
        x=plotly['year'],
        y=plotly['C_avg'],
        name = "average tax rate"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text=plotly['State'].iloc[15]+" Unemployment and Average Tax Rate",
        annotations = [dict(
            x=0.5,
            y=-0.3,
            xref='paper',
            yref='paper',
            text='Source: <a href="http://users.nber.org/~taxsim/allyup/ally.html">\
                Marginal and Average Tax Rates and Elasticities for the US 1960-2019 </a><br><a href="https://www.icip.iastate.edu/tables/employment/unemployment-states">\
                Annual Unemployment Rates by State</a>',
            showarrow = False
        )]
    )

    fig.add_vrect(x0=1992, x1=1997, 
                  annotation_text="State<br>Welfare<br>Waivers", annotation_position="top",
                  fillcolor="green", opacity=0.25, line_width=0
                 )

    fig.add_vline(x=1986, line_width=2, line_dash="dash", line_color="green",annotation_text = "Tax Reform<br>Act of 1986",annotation_position="top left")


    # Set x-axis title
    fig.update_xaxes(title_text="Year")

    # Set y-axes titles
    fig.update_yaxes(title_text="Unemployent Rate", secondary_y=False)
    fig.update_yaxes(title_text="Average Tax Rate", secondary_y=True)


#figure 2
    # Create figure with secondary y-axis
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    plotly2 = df2[df2['Code']== option_slctd]

    # Add traces
    fig2.add_trace(
        go.Scatter(
        x=plotly2['Year'],
        y=plotly2['rate'],
        name = "unemployment rate"),
        secondary_y=False,
    )

    fig2.add_trace(
        go.Scatter(
        x=plotly2['Year'],
        y=plotly2['Amount'],
        name = "eitc amount"),
        secondary_y=True,
    )

    # Add figure title
    fig2.update_layout(
        title_text=plotly2['States'].iloc[15]+" Unemployment and Amount of EITC",
        annotations = [dict(
            x=0.5,
            y=-0.3,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://www.icip.iastate.edu/tables/employment/unemployment-states">\
                Annual Unemployment Rates by State</a><br><a href="https://www.taxpolicycenter.org/statistics/eitc-claims-state">\
                Tax Policy Center</a>',
            showarrow = False
        )]
    )

    fig2.add_vline(x=2008, line_width=2, line_dash="dash", line_color="green",annotation_text = "Financial Crisis",annotation_position="top left")

    # Set x-axis title
    fig2.update_xaxes(title_text="Year")

    # Set y-axes titles
    fig2.update_yaxes(title_text="Unemployent Rate", secondary_y=False)
    fig2.update_yaxes(title_text="Amount of EITC", secondary_y=True)

    return container, fig, fig2


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)