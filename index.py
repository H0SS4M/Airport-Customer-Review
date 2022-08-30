import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from dash import Dash, Input, Output, callback


air = pd.read_csv('airport_data.csv')

count_total_satisfied = air[air['satisfaction'] == 'satisfied']['satisfaction'].count()
count_total_dissatisfied = air[air['satisfaction'] == 'neutral or dissatisfied']['satisfaction'].count()

count_total_satisfied_male = air[(air['satisfaction'] == 'satisfied') & (air['Gender'] == 'Male')]['satisfaction'].count()
percent_satisfied_male = (count_total_satisfied_male / count_total_satisfied) * 100

count_total_dissatisfied_male = air[(air['satisfaction'] == 'neutral or dissatisfied') & (air['Gender'] == 'Male')]['satisfaction'].count()
percent_dissatisfied_male = (count_total_dissatisfied_male / count_total_satisfied) * 100

count_total_satisfied_female = air[(air['satisfaction'] == 'satisfied') & (air['Gender'] == 'Female')]['satisfaction'].count()
percent_satisfied_female = (count_total_satisfied_female / count_total_satisfied) * 100

count_total_dissatisfied_female = air[(air['satisfaction'] == 'neutral or dissatisfied') & (air['Gender'] == 'Female')]['satisfaction'].count()
percent_dissatisfied_female = (count_total_dissatisfied_female / count_total_dissatisfied) * 100

count_class = air['Class'].nunique()
count_travel = air['Type of Travel'].nunique()
count_customer_type = air['Customer Type'].nunique()


count_60 = air[air['Age'] >= 60]['Age'].count()
count___60 = air[air['Age'] < 60]['Age'].count()

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}], suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

main_page = html.Div((
    html.Div((

        html.Div([
            #html.A(href = 'https://google.com',children = [html.Img(src=app.get_asset_url('airport1.png'))]),
            
            html.Img(src=app.get_asset_url('airport1.png')),
            html.Div([
                html.H1('Airport Customer Review', style={'margin-top': '10px',
                                                                    'text-align': 'center'}),
                html.P('View below airport customer review', style={'margin-top': '-8px',
                                                                    'text-align': 'center'})

            ], className='main_greeting')

        ], className='main_title'),

        html.Div((
            html.Div([
                html.Img(src=app.get_asset_url('like2.png'),
                         className='set_img',
                         style={'aria-hidden': True, 'margin-left': '-5px'}),
                html.Div([
                    html.P('Satisfied', className='text-primary-p1', ),
                    html.Span('{0:,.0f}'.format(count_total_satisfied), className='font-bold text-title',
                              style={'textAlign': 'center', 'margin-top': '-15px'}),

                ], className="card_inner"),
            ], className="create_container two columns"),

            html.Div([
                html.Img(src=app.get_asset_url('dislike1.png'),
                         className='set_img',
                         style={'aria-hidden': True, 'margin-left': '-10px'}),
                html.Div([
                    html.P('Dissatisfied', className='text-primary-p2', style={'textAlign': 'center'}),
                    html.Span('{0:,.0f}'.format(count_total_dissatisfied), className='font-bold text-title',
                              style={'textAlign': 'center', 'margin-top': '-15px'}),

                ], className="card_inner"),
            ], className="create_container two columns"),

            html.Div([
                html.Img(src=app.get_asset_url('male.png'),
                         className='set_img',
                         style={'aria-hidden': True, 'margin-left': '-20px'}),
                html.Div([
                    html.P('Male Satisfied', className='text-primary-p', style={'textAlign': 'center'}),
                    html.Span('{0:,.0f}'.format(count_total_satisfied_male), className='font-bold text-title',
                              style={'textAlign': 'center', 'margin-top': '-15px'}),
                    html.P('(' + '{0:,.2f}%'.format(percent_satisfied_male) + ')', className='font-bold text-title',
                           style={'textAlign': 'center', 'margin-top': '-8px'}),

                ], className="card_inner"),
            ], className="create_container two columns"),

            html.Div([
                html.Img(src=app.get_asset_url('male.png'),
                         className='set_img',
                         style={'aria-hidden': True, 'margin-left': '-20px'}),
                html.Div([
                    html.P('Male Dissatisfied', className='text-primary-p', style={'textAlign': 'center'}),
                    html.Span('{0:,.0f}'.format(count_total_dissatisfied_male), className='font-bold text-title',
                              style={'textAlign': 'center', 'margin-top': '-15px'}),
                    html.P('(' + '{0:,.2f}%'.format(percent_dissatisfied_male) + ')', className='font-bold text-title',
                           style={'textAlign': 'center', 'margin-top': '-8px'}),

                ], className="card_inner"),
            ], className="create_container two columns"),

            html.Div([
                html.Img(src=app.get_asset_url('woman.png'),
                         className='set_img',
                         style={'aria-hidden': True, 'margin-left': '-20px'}),
                html.Div([
                    html.P('Female Satisfied', className='text-primary-p', style={'textAlign': 'center'}),
                    html.Span('{0:,.0f}'.format(count_total_satisfied_female), className='font-bold text-title',
                              style={'textAlign': 'center', 'margin-top': '-15px'}),
                    html.P('(' + '{0:,.2f}%'.format(percent_satisfied_female) + ')', className='font-bold text-title',
                           style={'textAlign': 'center', 'margin-top': '-8px'}),

                ], className="card_inner"),
            ], className="create_container two columns"),

            html.Div([
                html.Img(src=app.get_asset_url('woman.png'),
                         className='set_img',
                         style={'aria-hidden': True, 'margin-left': '-20px'}),
                html.Div([
                    html.P('Female Dissatisfied', className='text-primary-p', style={'white-space': 'nowrap'}),
                    html.Span('{0:,.0f}'.format(count_total_dissatisfied_female), className='font-bold text-title',
                              style={'textAlign': 'center', 'margin-top': '-15px'}),
                    html.P('(' + '{0:,.2f}%'.format(percent_dissatisfied_female) + ')',
                           className='font-bold text-title',
                           style={'textAlign': 'center', 'margin-top': '-8px'}),

                ], className="card_inner"),
            ], className="create_container two columns"),

        ), className="row flex-display"),

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H1('Total Review'),
                        html.P('Review by class type and travel type', style={'margin-top': '-18px'})
                    ]),
                    html.A(href='/page-1',
                        children = [html.Img(src=app.get_asset_url('airplane.png'),
                        style={'aria-hidden': True})]),

                ], className='charts_left_title'),

                dcc.RadioItems(id='radio_items',
                               labelStyle={"display": "inline-block"},
                               value='Satisfied & Dissatisfied (Class)',
                               options=[{'label': 'Satisfied & Dissatisfied (Class)',
                                         'value': 'Satisfied & Dissatisfied (Class)'},
                                        {'label': 'Satisfied & Dissatisfied (Travel)',
                                         'value': 'Satisfied & Dissatisfied (Travel)'}],
                               style={'text-align': 'center', 'color': '#2e4a66'}),
                dcc.Graph(id='chart1'),

            ], className="charts_left six columns"),

            html.Div([
                html.Div([
                    html.Div([
                        html.H1('Stats Reports'),
                        html.P('Class type, Travel type, Customer type, Age wise review by customer', style={'margin-top': '-18px'})
                    ]),
                    html.A(href = '/page-2',
                        children = [html.Img(src=app.get_asset_url('airplane.png'),
                        style={'aria-hidden': True})]),

                ], className='charts_right_title'),
                html.Div([
                    html.Div([
                        html.P('Class Type', style={'font-size': '15px',
                                                    'font-weight': 700,
                                                    'margin-top': '5px'}),
                        html.P('{0:,.0f}'.format(count_class), style={'font-weight': 700,
                                                                      'font-size': '20px',
                                                                      'margin-top': '-15px'}),

                    ], className='card1'),

                    html.Div([
                        html.P('Travel Type', style={'font-size': '15px',
                                                     'font-weight': 700,
                                                     'margin-top': '5px'}),
                        html.P('{0:,.0f}'.format(count_travel), style={'font-weight': 700,
                                                                       'font-size': '20px',
                                                                       'margin-top': '-15px'}),

                    ], className='card2'),

                    html.Div([
                        html.H6('Customer Type', style={'font-size': '15px',
                                                        'font-weight': 700,
                                                        'margin-top': '5px'}),
                        html.P('{0:,.0f}'.format(count_customer_type), style={'font-weight': 700,
                                                                              'font-size': '20px',
                                                                              'margin-top': '-15px'}),

                    ], className='card3'),

                    html.Div([
                        html.H6('Number of Services', style={'font-size': '15px',
                                                          'font-weight': 700,
                                                          'margin-top': '5px'}),
                        html.P('{0:,.0f}'.format(13), style={'font-weight': 700,
                                                                   'font-size': '20px',
                                                                   'margin-top': '-15px'}),

                    ], className='card4'),

                    html.Div([
                        html.P('Most Effective Service', style={'font-size': '15px',
                                                         'font-weight': 700,
                                                         'margin-top': '5px'}),
                        html.P('Online boarding', style={'font-weight': 700,
                                                                   'font-size': '15px',
                                                                   'margin-top': '-15px'}),

                    ], className='card1'),

                    html.Div([
                        html.P('Most Ineffective Service', style={'font-size': '15px',
                                                         'font-weight': 700,
                                                         'margin-top': '5px'}),
                        html.P('Dep./Arr. time convenient', style={'font-weight': 700,
                                                                   'font-size': '15px',
                                                                   'margin-top': '-15px'}),

                    ], className='card2'),

                    html.Div([
                        html.H6('Customer Age < 60', style={'font-size': '15px',
                                                          'font-weight': 700,
                                                          'margin-top': '5px'}),
                        html.P('{0:,.0f}'.format(count___60), style={'font-weight': 700,
                                                                   'font-size': '20px',
                                                                   'margin-top': '-15px'}),

                    ], className='card3'),

                    html.Div([
                        html.H6('Customer Age > 60', style={'font-size': '15px',
                                                          'font-weight': 700,
                                                          'margin-top': '5px'}),
                        html.P('{0:,.0f}'.format(count_60), style={'font-weight': 700,
                                                                   'font-size': '20px',
                                                                   'margin-top': '-15px'}),

                    ], className='card4')

                ], className='charts_right_cards')
            ], className='charts_left six columns')
        ], className="row flex-display"),

    ), className='main_container'),

), className='main')

@app.callback(Output('chart1', 'figure'),
             [Input('radio_items', 'value')])
def update_graph(radio_items):
        # Class
        eco_satisfied = air[(air['Class'] == 'Eco') & (air['satisfaction'] == 'satisfied')]['satisfaction'].count()
        business_satisfied = air[(air['Class'] == 'Business') & (air['satisfaction'] == 'satisfied')]['satisfaction'].count()
        eco_plus_satisfied = air[(air['Class'] == 'Eco Plus') & (air['satisfaction'] == 'satisfied')]['satisfaction'].count()
        eco_dissatisfied = air[(air['Class'] == 'Eco') & (air['satisfaction'] == 'neutral or dissatisfied')]['satisfaction'].count()
        business_dissatisfied = air[(air['Class'] == 'Business') & (air['satisfaction'] == 'neutral or dissatisfied')]['satisfaction'].count()
        eco_plus_dissatisfied = air[(air['Class'] == 'Eco Plus') & (air['satisfaction'] == 'neutral or dissatisfied')]['satisfaction'].count()

        # Type of Travel
        business_travel_satisfied = air[(air['Type of Travel'] == 'Business travel') & (air['satisfaction'] == 'satisfied')]['satisfaction'].count()
        personal_travel_satisfied = air[(air['Type of Travel'] == 'Personal Travel') & (air['satisfaction'] == 'satisfied')]['satisfaction'].count()
        business_travel_dissatisfied = air[(air['Type of Travel'] == 'Business travel') & (air['satisfaction'] == 'neutral or dissatisfied')]['satisfaction'].count()
        personal_travel_dissatisfied = air[(air['Type of Travel'] == 'Personal Travel') & (air['satisfaction'] == 'neutral or dissatisfied')]['satisfaction'].count()

        colors = ['#30C9C7', '#7A45D1', 'orange', '#EC5333', '#4133EC', '#2C3E50']

        if radio_items == 'Satisfied & Dissatisfied (Class)':

         return {
            'data': [go.Pie(labels = ['Satisfied (Eco)', 'Satisfied (Business)', 'Satisfied (Eco Plus)',
                                      'Dissatisfied (Eco)', 'Dissatisfied (Business)', 'Dissatisfied (Eco Plus)'],
                            values = [eco_satisfied, business_satisfied, eco_plus_satisfied, eco_dissatisfied,
                                      business_dissatisfied, eco_plus_dissatisfied],
                            marker = dict(colors = colors),
                            hoverinfo = 'label+value+percent',
                            textinfo = 'label+value',
                            textfont = dict(size = 13),
                            texttemplate = '%{label} <br>%{value:,.0f}',
                            textposition = 'auto',
                            hole = .7,
                            rotation = 160,
                            insidetextorientation='radial',

                            )],

            'layout': go.Layout(
                margin=dict(l=129, r=122),
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                hovermode = 'x',
                title = {'text':'',

                    'y': 0.93,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont = {
                    'color': 'white',
                    'size': 15},
                legend = {
                    'orientation': 'h',
                    'bgcolor': 'rgba(255, 255, 255, 0)',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.15},

                font = dict(
                    family = "sans-serif",
                    size = 12,
                    color = '#2e4a66')
            ),

        }

        elif radio_items == 'Satisfied & Dissatisfied (Travel)':

         return {
            'data': [go.Pie(labels = ['Satisfied (Business)', 'Satisfied (Personal)',
                                      'Dissatisfied (Business)', 'Dissatisfied (Personal)'],
                            values = [business_travel_satisfied, personal_travel_satisfied, business_travel_dissatisfied,
                                      personal_travel_dissatisfied],
                            marker = dict(colors = colors),
                            hoverinfo = 'label+value+percent',
                            textinfo = 'label+value',
                            textfont = dict(size = 13),
                            texttemplate = '%{label} <br>%{value:,.0f}',
                            textposition = 'auto',
                            # hole = .7,
                            rotation = 190,
                            insidetextorientation='radial',

                            )],

            'layout': go.Layout(
                margin=dict(l=129, r=122),
                plot_bgcolor='rgba(255, 255, 255, 0)',
                paper_bgcolor='rgba(255, 255, 255, 0)',
                hovermode = 'x',
                title = {'text': '',

                    'y': 0.93,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont = {
                    'color': 'white',
                    'size': 15},
                legend = {
                    'orientation': 'h',
                    'bgcolor': 'rgba(255, 255, 255, 0)',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.15},

                font = dict(
                    family = "sans-serif",
                    size = 12,
                    color = '#2e4a66')
            ),

        }

page_1_layout = html.Div((
    html.Div((

        html.Div([
            html.A(href = '/',children = [html.Img(src=app.get_asset_url('airport1.png'))]),
            html.Div([
                html.H1('Airport Customer Review', style={'margin-top': '10px',
                                                                    'text-align': 'center'}),
                html.P('View below airport customer review', style={'margin-top': '-8px',
                                                                    'text-align': 'center'})
            ], className='main_greeting')

        ], className='main_title'),

        html.Div((            
            html.Div([
                html.P('Select a Factor: ', className='fix_lable'),
                dcc.Dropdown(id='factor',
                    options = ['Type of Travel', 'Class', 'Flight Distance' ,'Age', 'Customer Type'],
                    #placeholder="Select a Service",
                    value = 'Type of Travel',
                    clearable=False,
                    style={'width': '100%'}
                ),
                
            ], className="create_container four columns"),

        ), className="row flex-display"),

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H1('Satisfaction With different factors'),
                    ]),

                ], className='charts_mid1_title'),
                
                dcc.Graph(id='graph2'),

            ], className="charts_mid1 ten columns"),

        ], className="row flex-display"),

    ), className='main_container'),

), className='main')

@app.callback(
    Output("graph2", "figure"),
    Input("factor", "value"), 
    )
def generate_chart(factor):
    df = pd.read_csv('airport_data.csv')
    if factor == 'Flight Distance':
        fig = px.histogram(df, x = factor, color = 'satisfaction' ,nbins= 10, barmode = 'group', title = 'Flight Distance by Satisfaction', histfunc='count')
    elif factor == 'Age':
        fig = px.histogram(df, x = factor, color = 'satisfaction' ,nbins= 20, barmode = 'group', title = 'Age by Satisfaction', histfunc='count')
    else:
        fig = px.histogram(df, x = factor, color = 'satisfaction' , barmode = 'group', title = f'{factor} by Satisfaction', histfunc='count')
    
    return fig


page_2_layout = html.Div((
    html.Div((

        html.Div([
            html.A(href = '/',children = [html.Img(src=app.get_asset_url('airport1.png'))]),
            html.Div([
                html.H1('Airport Customer Review', style={'margin-top': '10px',
                                                                    'text-align': 'center'}),
                html.P('View below airport customer review', style={'margin-top': '-8px',
                                                                    'text-align': 'center'})

            ], className='main_greeting')

        ], className='main_title'),

        html.Div((            
            html.Div([
                html.P('Select a Service: ', className='fix_lable'),
                dcc.Dropdown(id='features',
                    options = ['Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking' ,'Gate location', 'Food and drink','Online boarding', 'Seat comfort', 'Inflight entertainment', 'On-board service' ,'Leg room service', 'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness', 'All'],
                    #placeholder="Select a Service",
                    value = 'Inflight wifi service',
                    clearable=False,
                    style={'width': '100%'}
                ),
                
            ], className="create_container four columns"),

        ), className="row flex-display"),

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H1('Satisfaction of each Service'),
                    ]),

                ], className='charts_mid_title'),
                
                dcc.Graph(id='graph'),
                html.Br(),
                dcc.Slider(id='rates',
                    marks={
                    1: '1',
                    2: '2',
                    3: '3',
                    4: '4',
                    5: '5',
                    6: 'All',
                },
                    min = 1, max = 6, value = 6, step = 1,
                ),

            ], className="charts_mid ten columns"),

        ], className="row flex-display"),

    ), className='main_container'),

), className='main')
@app.callback(
    Output("graph", "figure"),
    #Input('gender', 'value'),
    Input("features", "value"),
    Input("rates", "value"), 
    )
def generate_chart(feature, rates):
    df = pd.read_csv('airport_data.csv')

    '''if gender != 'Both':
        df = df[df['Gender'] == gender]'''

    if feature == 'All':
        df_staisfaied =  df[df['satisfaction'] == 'satisfied']
        df_unstaisfaied =  df[df['satisfaction'] == 'neutral or dissatisfied']

        percentage = {i : [df_staisfaied[i].sum()/df_staisfaied.shape[0] , df_unstaisfaied[i].sum()/df_unstaisfaied.shape[0]] for i in df_staisfaied.iloc[:,8:22].columns.to_list()}
        #sorting
        percentage = {k: v for k, v in sorted(percentage.items(), key=lambda item: (item[1][0] / item[1][1]), reverse=True)}

        df_percentage = pd.DataFrame.from_dict(percentage, orient='index', columns = ['satisfied', 'unsatisfied'])
        df_percentage.reset_index(inplace=True)

        return px.bar(df_percentage, x="index", y=['satisfied', 'unsatisfied'], title='AVG Rate of each Service', barmode='group',
            labels={'index': 'Service', 'value': 'AVG Rate'})

    
    if rates != 6:
        df = df[df[feature] == rates]
        stars = rates
    else:
        stars = 'All'
    
    fig = px.pie(df, values=feature, names='satisfaction', hole=.3, color = 'satisfaction',
        color_discrete_map={'satisfied': '#636efa ', 'neutral or dissatisfied': '#ef553b'},
        title= f'{feature} Satisfaction With {stars} Stars')
    
    return fig


# Update the index
@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-2':
        return page_1_layout
    elif pathname == '/page-1':
        return page_2_layout
    else:
        return main_page


if __name__ == '__main__':
    app.run_server(debug=True)