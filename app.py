import os

import dash
import dash_core_components as dcc
import dash_html_components as html
#import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# Data source
df = pd.read_csv('flights_complete_sample.csv')

# Dict of colours
colors = {
    'background': '#1B6F93',
    'text': '#7FDBFF',
    'header': '#FFFFFF',
    'paragraph': '#9BECFA',
    'plot': '#9BECFA',
    'plot2': '#B0B0B0'
}

# Header
app.layout = html.Div(style={'backgroundColor': colors['background'], 'padding-left':'3%', 
            'padding-right':'3%'}, children=[
    html.Img(id= 'panda', src='https://image.shutterstock.com/image-vector/little-panda-super-hero-flies-260nw-650591155.jpg', style={'height':'10%', 'width':'10%', 'display':'inline-block'}),
    html.H1(
        children='Flying Pandas',
        style={
            'textAlign': 'center',
            'color': colors['header'],
            'display':'inline-block'
        }
    ),
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

        html.Div(html.P(['We analysed a dataset of millions of rows of data on flights in the United States during 2015 to determine if we could predict flight delays based on the given information. We visualized and evaluated the data to determine its spread based on various factors, as shown below.', html.Br(), html.Br()],
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

    html.Img(id= 'dept_delay_by_month', 
            src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/month_departure_delay.png?raw=true',
           style={'width': '45%',
                'padding-left':'3%', 
                'padding-right':'1%', 
                'display': 'inline-block'
                } 
            ),

    html.Img(id= 'arr_delay_by_time', 
            src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/time_arrival_delay.png?raw=true',
           style={'width': '45%',
                'padding-left':'3%', 
                'padding-right':'1%',
                'display': 'inline-block'
                }
            ), 

# Machine Learning Images
    html.Br(),
    html.H3(
        children='Arrival Delay',
        style={
            'textAlign': 'left',
            'color': colors['text'],            
            'width': '45%', 
            'display': 'inline-block'
        }
    ),    

    html.Div(html.P(['For our machine learning model we used a neural network. Its accuracy is depicted below.'],
        style={
            'textAlign': 'left',
            'font-size': '18px',
            'color': colors['paragraph']
        })),

    html.Img(id= 'ml_arrival_graph', 
            src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/arrival_predictions.png?raw=true',
            style={'Align': 'center',
                'width': '45%',
                'padding-left':'30%', 
                'padding-right':'30%'
                } 
            ),
# Dropdown boxes
# ------------------------------------------
        html.Br(),

        # Intro to Dropdown section
        html.Div(html.P(['A random forest machine learning model was also used to evaluate the importance of each feature, for the purpose of creating this interactable menu. Test it out by entering your flight data and letting it predict how late your flight will arrive at its destination.'],
        style={
            'textAlign': 'left',
            'font-size': '18px',
            'color': colors['paragraph']
        })),

            # Text row
            html.Div(children='Day of the Month', style={
                'textAlign': 'left',
                'color': colors['text'],
                'width': '45%', 
                'display': 'inline-block'
            }), 
            html.Div(children='Scheduled Arrival Time', style={
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

            dcc.Input(id="scheduled_arrival",type="number",value=0,
                        style={'width': '44%', 
                        'display': 'inline-block'}),
            html.Br(),
            html.Br(),

            # Text row
            html.Div(children='Departure Delay (minutes, if applicable)', style={
                'textAlign': 'left',
                'color': colors['text'],
                'width': '45%', 
                'display': 'inline-block'
            }),
            html.Div(children='Scheduled Departure Time (four digits, no punctuation)', style={
                'textAlign': 'left',
                'color': colors['text'],
                'width': '45%', 
                'display': 'inline-block'
            }), 

            # Input row
            dcc.Input(id="departure_delay",type="number",value=0,
                        style={'width': '44%', 
                        'display': 'inline-block'}),
            dcc.Input(id="scheduled_departure",type="number",value=0,
                        style={'width': '44%', 
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
                    {'label': 'Choose', 'value': '0'},
                    {'label': 'January', 'value': '1'},
                    {'label': 'February','value': '2'},
                    {'label': 'March', 'value': '3'},
                    {'label': 'April', 'value': '4'},
                    {'label': 'May', 'value': '5'},
                    {'label': 'June', 'value': '6'},
                    {'label': 'July', 'value': '7'},
                    {'label': 'August', 'value': '8'},
                    {'label': 'September', 'value': '9'},
                    {'label': 'October', 'value': '10'},
                    {'label': 'November', 'value': '11'},
                    {'label': 'December', 'value': '12'}
                ],
                value=0,
                style={'width': '45%', 'display': 'inline-block'}
            ),
            
            dcc.Dropdown(id="day_of_week",
                options=[
                    {'label': 'Choose', 'value': '0'},
                    {'label': 'Monday', 'value': '1'},
                    {'label': 'Tuesday', 'value': '2'},
                    {'label': 'Wednesday', 'value': '3'},
                    {'label': 'Thursday', 'value': '4'},
                    {'label': 'Friday', 'value': '5'},
                    {'label': 'Saturday', 'value': '6'},
                    {'label': 'Sunday', 'value': '7'}
                ],
                value=0,
                style={'width': '45%', 'display': 'inline-block'}
            ), 
            html.Br(),
            html.Br(),

            # Text Row
            html.Div(children='Choose distance', style={
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

            html.Div(children='Choose Airline', style={
                'textAlign': 'left',
                'color': colors['text'],
                'width': '45%', 
                'display': 'inline-block'
            }),  
            html.Br(),

            # Input Row
            dcc.Dropdown(id="airline",
                options=[
                    {'label': 'Choose', 'value': '0'},
                    {'label': 'United Air Lines Inc.', 'value': 0.005348358975268569},
                    {'label': 'American Airlines Inc.', 'value': 0.008028661993477714},
                    {'label': 'US Airways Inc.', 'value': 0.00438836446916319},
                    {'label': 'Frontier Airlines Inc.', 'value': 0.0024388397635945274},
                    {'label': 'JetBlue Airways', 'value': 0.003844877415727794},
                    {'label': 'Skywest Airlines Inc.', 'value': 0.0034624647984771604},
                    {'label': 'Alaska Airlines Inc.', 'value': 0.0025787244542513706},
                    {'label': 'Spirit Air Lines', 'value': 0.002630639117114348},
                    {'label': 'Southwest Airlines Co.', 'value': 0.00568087848579114},
                    {'label': 'Delta Air Lines Inc.', 'value': 0.006072474892492146},
                    {'label': 'Atlantic Southeast Airlines', 'value': 0.002616016399733442},
                    {'label': 'Hawaiian Airlines Inc.', 'value': 0.00044869258052845305},
                    {'label': 'American Eagle Airlines Inc.', 'value': 0.0014036373942613492},
                    {'label': 'Virgin America', 'value': 0.002178998873948589}	
                ],
                value=0,
                style={'width': '45%', 'display': 'inline-block'}
            ),

        # Output Div
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
    [Input("day", "value"), 
    Input("scheduled_arrival","value"),
    Input("departure_delay","value"),
    Input("scheduled_departure", "value"),
    Input("month", "value"),
    Input("day_of_week", "value"),
    Input("distance","value"),
    Input("airline", "value")
    ]
)

def predict_delay(d, sa, dd, sd, m, dw, di, a):
    predict = d*0.11048671263154038 + sa*0.10619959174532308 + dd*0.1040270876376712 + sd*0.10189558360762008 + m*0.08462700920684066 + dw*0.08313113520744703 + di*0.06509603467532205 + a*1
    prediction = round(predict,4)
    return "Your flight's arrival will be {} minutes delayed.".format(prediction)
    prediction = 0


if __name__ == '__main__':
    app.run_server(debug=True)
