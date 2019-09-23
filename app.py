import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('daily-inmates-in-custody.csv')
mental_obs_custody = df[(df.BRADH == 'Y') & (df.INFRACTION == 'Y')]
mental_custody = mental_obs_custody['CUSTODY_LEVEL'].value_counts(normalize=False).to_frame()
label = mental_custody.index.tolist()
value = mental_custody['CUSTODY_LEVEL'].tolist()

df = df.replace(to_replace='W',value='White')
df = df.replace(to_replace='B',value='Black')
df = df.replace(to_replace='O',value='Other Pacific Islander')
df = df.replace(to_replace='A',value='Asian')
df = df.replace(to_replace='I',value='Indian')
df = df.replace(to_replace='U',value='Alaska Native')


mental = df[(df['BRADH'] == 'Y') & (df['CUSTODY_LEVEL'])]
mental_custody_level = mental['CUSTODY_LEVEL'].value_counts(normalize=False).to_frame()
mlabel = mental_custody_level.index.tolist()
mvalue = mental_custody_level['CUSTODY_LEVEL'].tolist()

gender = df['GENDER'].value_counts(normalize=False).to_frame()
glabel = gender.index.tolist()
gvalue = gender['GENDER'].tolist()

age = df['AGE'].value_counts(normalize=False).to_frame()
alabels = age.index.tolist()
avalues = age['AGE'].tolist()

date = df['SRG_FLG'].value_counts(normalize=False).to_frame()
slabels = date.index.tolist()

svalues = date['SRG_FLG'].tolist()


race = df['RACE'].value_counts(normalize=False).to_frame()
rlabels = race.index.tolist()
rvalues = race['RACE'].tolist()

race_age = df[(df['SRG_FLG']=='Y') & (df['RACE'])]
race = race_age['RACE'].value_counts(normalize=False).to_frame()
ralabels = race.index.tolist()
ravalues = race['RACE'].tolist()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H1(children='NYC Inmates'),

    html.Div(children='''
        Data from all prisons in New York City was collected. In this dashboard 
        we explore which groups are dominant in these prisons in order deduce the safety levels in prison.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': label, 'y': value, 'type': 'bar', 'name': 'Inmates'},
                
            ],
            'layout': {
                'title': 'Custody Levels of Inmates Under Mental Observation With Infractions'
            }
        }
    ),

    html.Div(children='''
        Custody levels were measured against being under mental observation to 
        see where most inmates are concentrated.
    '''),

    dcc.Graph(
        id='graph',
        figure={
            'data': [
                {'x': mlabel, 'y': mvalue, 'type': 'bar', 'name': 'Inmates'},
                
            ],
            'layout': {
                'title': 'Custody Levels of Inmates Under Mental Observation '
            }
        }
    ),

    html.Div(children='''
        Which gender dominates NYC prisons?
    '''),

    dcc.Graph(id='device_usage',
                           figure=go.Figure(
                               data=[go.Pie(labels=glabel,
                                            values=gvalue)],
                               layout=go.Layout(
                                   title='Gender')
                           )),

    dcc.Graph(
        id='age-graph',
        figure={
            'data': [
                {'x': alabels, 'y': avalues, 'type': 'bar', 'name': 'Age'},
                
            ],
            'layout': {
                'title': 'Age'
            }
        }
    ),

    dcc.Graph(id='gang',
                           figure=go.Figure(
                               data=[go.Pie(labels=slabels,
                                            values=svalues)],
                               layout=go.Layout(
                                   title='Inmates with a Gang Affiliation')
                           )),
    html.Div(children='''
        From the percentage of inmates affiliated with a gang, a graph showing the percentages of each race group that is affiliated with a gang.
    '''),
  dcc.Graph(id='race_age',
                           figure=go.Figure(
                               data=[go.Pie(labels=ralabels,
                                            values=ravalues)],
                               layout=go.Layout(
                                   title='Inmates with a Gang Affiliation According to Race')
                           )),
  dcc.Graph(
        id='race-graph',
        figure={
            'data': [
                {'x': rlabels, 'y': rvalues, 'type': 'line', 'name': 'Race'},
                {'x': ralabels, 'y': ravalues, 'type': 'line', 'name': 'Races in Gangs'},
                
            ],
            'layout': {
                'title': 'Representation of Races in Prison and in Gangs',
                'tickformat': '%'
                
            }
        }
    ),

])

if __name__ == '__main__':
	app.run_server(debug=True)