# Import dependencies
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Build app
# -------------------------------------------

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# Data source
df = pd.read_csv('flights_complete_sample.csv')

# Dict of colours
colors = {
    'background': '#1B6F93',
    'text': '#7FDBFF',
    'header': '#D3D3D3',
    'paragraph': '#9BECFA',
    'plot': '#9BECFA',
    'plot2': '#B0B0B0'
}

# Airlines list of dicts, formatted using pandas and excel concat
airlines_options=[{'label': 'Choose', 'value': 0},{'label': 'WN', 'value': 1},{'label': 'DL', 'value': 2},{'label': 'AA', 'value': 3},{'label': 'UA', 'value': 4},{'label': 'US', 'value': 5},{'label': 'B6', 'value': 6},{'label': 'OO', 'value': 7},{'label': 'AS', 'value': 8},{'label': 'EV', 'value': 9},{'label': 'NK', 'value': 10},{'label': 'F9', 'value': 11},{'label': 'VX', 'value': 12},{'label': 'MQ', 'value': 13},{'label': 'HA', 'value': 14}]

# Airports list of dicts, formatted using pandas and excel concat
airport_options=[{'label': 'Choose', 'value': 0},{'label': 'ATL', 'value': 1},{'label': 'ORD', 'value': 2},{'label': 'DFW', 'value': 3},{'label': 'DEN', 'value': 4},{'label': 'LAX', 'value': 5},{'label': 'PHX', 'value': 6},{'label': 'SFO', 'value': 7},{'label': 'IAH', 'value': 8},{'label': 'LAS', 'value': 9},{'label': 'MSP', 'value': 10},{'label': 'SEA', 'value': 11},{'label': 'MCO', 'value': 12},{'label': 'DTW', 'value': 13},{'label': 'BOS', 'value': 14},{'label': 'CLT', 'value': 15},{'label': 'EWR', 'value': 16},{'label': 'SLC', 'value': 17},{'label': 'LGA', 'value': 18},{'label': 'JFK', 'value': 19},{'label': 'BWI', 'value': 20},{'label': 'MDW', 'value': 21},{'label': 'FLL', 'value': 22},{'label': 'DCA', 'value': 23},{'label': 'SAN', 'value': 24},{'label': 'MIA', 'value': 25},{'label': 'PHL', 'value': 26},{'label': 'TPA', 'value': 27},{'label': 'DAL', 'value': 28},{'label': 'HOU', 'value': 29},{'label': 'PDX', 'value': 30},{'label': 'BNA', 'value': 31},{'label': 'STL', 'value': 32},{'label': 'HNL', 'value': 33},{'label': 'OAK', 'value': 34},{'label': 'AUS', 'value': 35},{'label': 'MSY', 'value': 36},{'label': 'MCI', 'value': 37},{'label': 'SJC', 'value': 38},{'label': 'SMF', 'value': 39},{'label': 'SNA', 'value': 40},{'label': 'CLE', 'value': 41},{'label': 'IAD', 'value': 42},{'label': 'RDU', 'value': 44},{'label': 'SAT', 'value': 45},{'label': 'MKE', 'value': 46},{'label': 'RSW', 'value': 48},{'label': 'IND', 'value': 49},{'label': 'SJU', 'value': 50},{'label': 'PIT', 'value': 51},{'label': 'CMH', 'value': 52},{'label': 'PBI', 'value': 53},{'label': 'OGG', 'value': 55}]


# Header
app.layout = html.Div(
        style={
            'backgroundColor': colors['background'], 
            'padding-left':'3%', 
            'padding-right':'3%',
            'marginTop':25,
            'marginBottom':25            
            }, 
        children=[
            html.Img(id='panda', 
                src='https://image.shutterstock.com/image-vector/little-panda-super-hero-flies-260nw-650591155.jpg', 
                style={
                    'height':'10%', 
                    'width':'10%', 
                    'display':'inline-block',
                    'marginTop':15
                    },
                ),
            html.H1(children='Flying Pandas', 
                style={
                    'textAlign': 'center',
                    'font-size': '30px',
                    'color': colors['header'],
                    'display':'inline-block',
                    'padding-left':'3%',
                    'font-weight':'bold'
                }),    
            
            html.H2(
                children='How late will your flight be?',
                style={
                    'textAlign': 'left',
                    'font-size': '22px',
                    'color': colors['header']
                }
            ),
        # Background and Images
        # ----------------------------

        # Intro
            html.Div(html.P(['Late flights are a pain, ruining schedules and delaying plans. Use our app to help regain control over your time by planning for your flight delays before they happen.', html.Br(), html.Br()],
                style={
                    'textAlign': 'left',
                    'font-size': '18px',
                    'color': colors['paragraph']
                })),

                html.Div(html.P(['We analysed a dataset of billions of rows of data on flights in the United States during 2015 to determine if we could predict flight delays based on the given information. We visualized and evaluated the data to determine its spread based on various factors, as shown below.', html.Br(), html.Br()],
                style={
                    'textAlign': 'left',
                    'font-size': '18px',
                    'color': colors['paragraph']
                })),
            
            # Delays by Airline Graph
            dcc.Graph(
                id='delays',
                figure={
                    'data': [
                        {'x':df['airline_name'], 'y': df['departure_delay'], 'type':'box', 'name': 'Departure',
                        'marker' : { "color" : colors['plot']}},
                        {'x':df['airline_name'], 'y': df['arrival_delay'], 'type':'box', 'name': 'Arrival',
                        'marker' : { "color" : colors['plot2']}}
                    ],
                    'layout' : {
                        'title': 'Departure and Arrival Delays by Airline',
                        'yaxis':{
                            'title':'Delay in Minutes'
                        },
                        'plot_bgcolor':colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        }
                    }
                },
                style={'padding-left':'3%', 
                    'padding-right':'1%'}
            ),

        # Images
            html.Br(),
            html.Br(),

            html.Img(id='dept_delay_by_month', 
                    src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/month_departure_delay.png?raw=true',
                style={'width': '45%',
                        'padding-left':'3%', 
                        'padding-right':'1%', 
                        'display': 'inline-block'
                        } 
                    ),

            html.Img(id='arr_delay_by_time', 
                    src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/time_arrival_delay.png?raw=true',
                style={'width': '45%',
                        'padding-left':'3%', 
                        'padding-right':'1%',
                        'display': 'inline-block'
                        }
                    ), 

        # Machine Learning Images
            html.Br(),
            html.Br(),
            html.H3(
                children='Arrival Delay',
                style={
                    'textAlign': 'left',
                    'color': colors['text'],
                    'font-size': '20px',            
                    'width': '45%', 
                    'display': 'inline-block'
                }
            ),    

            html.Div(html.P(['For our machine learning model we used both a neural network model and a random forest model. Their accuracies are depicted below.'],
                style={
                    'textAlign': 'left',
                    'font-size': '18px',
                    'color': colors['paragraph']
                })),

            html.Br(),

            html.Img(id='ml_dnn', 
                    src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/prediction_plot.PNG?raw=true',
                style={'width': '45%',
                        'padding-left':'3%', 
                        'padding-right':'1%', 
                        'display': 'inline-block'
                        } 
                    ),

            html.Img(id='ml_rf', 
                    src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/prediction_forest_plot.PNG?raw=true',
                style={'width': '45%',
                        'padding-left':'3%', 
                        'padding-right':'1%',
                        'display': 'inline-block'
                        }
                    ), 
        # Dropdown boxes
        # ------------------------------------------
                html.Br(),
                html.Br(),

                # Intro to Dropdown section
                html.Div(html.P(['An sklearn linear regression machine learning model was also used to generate a simple formula to predict how late your flight may arrive at its destination. Interestingly, airline and airport have negligible effects on delay time in our model. As expected, departure delay has the largest impact on arrival delay.'],
                style={
                    'textAlign': 'left',
                    'font-size': '18px',
                    'color': colors['paragraph']
                })),

                # Formula

                # Arrival_Delay = 
                # -1.36684786e-01*month 
                # + -1.40802847e-02*day 
                # + -1.79483261e-01*day_of_week 
                # + -4.21771859e-04*scheduled_departure
                # + 1.01375182e+00*departure_delay 
                # + -2.68430838e-03*distance 
                # + 2.40652401e-04*scheduled_arrival 
                # + 1.13694581e-08*arrival_airport
                # + 1.13694581e-08*departure_airport
                # + 6.85911322e-09*airline
            
                # Note: The biggest predictor of 

                
                html.H3(
                    children='Enter Information Below:',
                    style={
                        'textAlign': 'left',
                        'color': colors['header'],
                        'font-size': '20px',            
                        'width': '45%', 
                        'display': 'inline-block'
                    }
                ), 
                
                html.Br(),
                # Build dropdowns
                # -----
                    
                    # Text Row
                    html.Div(children='Choose Airline', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }),  
                    html.Br(),
                    
                    # Input Row
                    dcc.Dropdown(id="airline",
                        options=airlines_options,
                        value=0,
                        style={'width': '45%', 
                            'display': 'inline-block'}),

                    html.Br(),
                    html.Br(),

                    # Text Row
                    html.Div(children='Departure Airline (code)', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }),   
                    html.Div(children='Arrival Airport (code)', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }),         
                    html.Br(),   

                    # Input row
                    dcc.Dropdown(id="departure_airport",
                        options=airport_options,
                        value=0,
                        style={'width': '45%', 
                            'display': 'inline-block'}),
                    dcc.Dropdown(id="arrival_airport",
                        options=airport_options,
                        value=0,
                        style={'width': '45%', 
                            'display': 'inline-block'}),

                    html.Br(),
                    html.Br(),                                     

                    # Text Row
                    html.Div(children='Choose Month', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }),   
                    html.Div(children='Choose Day of the Week', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }),         
                    html.Br(),

                    # Input Row
                    dcc.Dropdown(id="month",
                        options=[
                            {'label': 'Choose', 'value': 0},
                            {'label': 'January', 'value': 1},
                            {'label': 'February','value': 2},
                            {'label': 'March', 'value': 3},
                            {'label': 'April', 'value': 4},
                            {'label': 'May', 'value': 5},
                            {'label': 'June', 'value': 6},
                            {'label': 'July', 'value': 7},
                            {'label': 'August', 'value': 8},
                            {'label': 'September', 'value': 9},
                            {'label': 'October', 'value': 10},
                            {'label': 'November', 'value': 11},
                            {'label': 'December', 'value': 12}
                        ],
                        value=0,
                        style={'width': '45%', 'display': 'inline-block'}
                    ),
                    
                    dcc.Dropdown(id="day_of_week",
                        options=[
                            {'label': 'Choose', 'value': 0},
                            {'label': 'Monday', 'value': 1},
                            {'label': 'Tuesday', 'value': 2},
                            {'label': 'Wednesday', 'value': 3},
                            {'label': 'Thursday', 'value': 4},
                            {'label': 'Friday', 'value': 5},
                            {'label': 'Saturday', 'value': 6},
                            {'label': 'Sunday', 'value': 7}
                        ],
                        value=0,
                        style={'width': '45%', 'display': 'inline-block'}
                    ), 
                    html.Br(),
                    html.Br(),

                    # Text row
                    html.Div(children='Day of the Month', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }), 
                    html.Div(children='Departure Delay (minutes, if applicable)', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }), 
                    html.Br(),

                    # Input row
                    dcc.Input(id="day",type="number",value=0, min=0,max=31,
                                style={'width': '44%', 
                                'display': 'inline-block'}),
                    dcc.Input(id="departure_delay",type="number",value=0,
                                style={'width': '44%', 
                                'display': 'inline-block'}),

                    html.Br(),
                    html.Br(),

                    # Text row
                    html.Div(children='Scheduled Departure Time (four digits, no punctuation)', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }), 
                    html.Div(children='Scheduled Arrival Time (four digits, no punctuation)', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }), 

                    # Input row
                    dcc.Input(id="scheduled_departure",type="number",value=0,
                                style={'width': '44%', 
                                'display': 'inline-block'}),
                    dcc.Input(id="scheduled_arrival",type="number",value=0,
                                style={'width': '44%', 
                                'display': 'inline-block'}),
                    html.Br(),
                    html.Br(),

                    # Text Row
                    html.Div(children='Enter distance (miles)', style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'width': '45%', 
                        'display': 'inline-block'
                    }),    

                    html.Br(),        
                    # Input Row
                    dcc.Input(id="distance",type="number",value=0,
                                style={'width': '44%', 
                                'display': 'inline-block'}),
                    # Text Row
                    html.Br(),
                    html.Br(),


                # Output Div
                html.Br(),
                html.Br(),
                html.Div(id="prediction", style={
                        'textAlign': 'center',
                        'font-size': '22px',
                        'color': colors['header']
                    }),
                
                # Footer space
                html.Div(html.P(['. . .'],
                style={
                    'textAlign': 'center',
                    'font-size': '30px',
                    'color': colors['paragraph']
                })) 
                
            ])

@app.callback(
    Output("prediction", "children"),
    [Input("month", "value"),
    Input("day", "value"), 
    Input("day_of_week", "value"),
    Input("scheduled_departure", "value"),
    Input("departure_delay","value"),
    Input("distance","value"),
    Input("scheduled_arrival","value"),
    Input("arrival_airport","value"),
    Input("departure_airport","value"),    
    Input("airline", "value")
    ]
)

def predict_delay(month,day,day_of_week,scheduled_departure,departure_delay,distance,scheduled_arrival,arrival_airport,departure_airport,airline):
    predict = -1.36684786e-01*month + -1.40802847e-02*day + -1.79483261e-01*day_of_week + -4.21771859e-04*scheduled_departure + 1.01375182e+00*departure_delay + -2.68430838e-03*distance + 2.40652401e-04*scheduled_arrival + 1.13694581e-08*arrival_airport + 1.13694581e-08*departure_airport + 6.85911322e-09*airline
    prediction = round(predict,4)
    return "Your flight's arrival will be {} minutes delayed.".format(prediction)

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
