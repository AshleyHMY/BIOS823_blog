import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title(""" 
 BIOS823 HW4 
 ## Is there life after graduate school? A report on doctorate recipients in the USA.
 ### by Mengyi Ashley Hu
""")

st.write("""
Use two pie plots to represent the differences in study fields of male doctorate recipients and female doctorate recipients in 2017.
The table used to draw these two pie plots is the award_by_state.xlsx table.
""")
award_state = pd.read_excel('award_by_state.xlsx')

by_state = award_state[3:]

by_state = by_state.rename(columns={'Table 6':'state', 'Unnamed: 1':'All field M',
                         'Unnamed: 2':'All field F', 'Unnamed: 3':'Life science M',
                         'Unnamed: 4':'Life science F', 'Unnamed: 5':'Physical sciences and earth sciences M',
                         'Unnamed: 6':'Physical sciences and earth sciences F', 'Unnamed: 7': 'Mathematics and computer sciences M',
                         'Unnamed: 8':'Mathematics and computer sciences F', 'Unnamed: 9': 'Psychology and social sciences M',
                         'Unnamed: 10':'Psychology and social sciences F', 'Unnamed: 11': 'Engineering M',
                         'Unnamed: 12': 'Engineering F', 'Unnamed: 13': 'Education M',
                         'Unnamed: 14':'Education F', 'Unnamed: 15': 'Humanities and Arts M',
                         'Unnamed: 16': 'Humanities and Arts F', 'Unnamed: 17': 'Other M',
                         'Unnamed: 18': 'Other F'})

#D in the data frame indicates that the result is suppressed to avoid disclosure of confidential information.
by_state = by_state.replace('D', np.NaN)

#To create a data frame for degree awarded for male
male = by_state.set_index('state').filter(regex=(".M$"), axis=1)
#To create a data frame for degree awarded for female
female = by_state.set_index('state').filter(regex=(".F$"), axis=1)

fig1 = px.pie(values=male.loc['United Statesd'].iloc[1:9],
             names=["Life sciences","Physical sciences and earth sciences",
                      "Mathematics and computer science", "Psycholofy and social sciences",
                      "Engineering", "Education", "Humanities and Arts", "Other"],
             color_discrete_sequence=px.colors.sequential.Teal,
             title="Proportion of doctorate recipients study field in 2017 male")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(values=female.loc['United Statesd'].iloc[1:9],
             names=["Life sciences","Physical sciences and earth sciences",
                      "Mathematics and computer science", "Psycholofy and social sciences",
                      "Engineering", "Education", "Humanities and Arts", "Other"],
             color_discrete_sequence=px.colors.sequential.Burgyl,
             title="Proportion of doctorate recipients study field in 2017 female")
st.plotly_chart(fig2, use_container_width=True)

st.write("""
Use a horizontal bar plot to show the ranking of top 50 institutions with the highest number of doctorate recipients
""")
top_institution = pd.read_excel('top_50_institution.xlsx', skiprows=3)

fig3 = px.bar(top_institution, x = 'Doctorate recipients', y = 'Rank', orientation='h',
             color='Doctorate recipients', text='Institution', template='plotly_white',
             labels={'Doctorate recipients': 'Number of Doctorate recipients'},
              width=800, height=400)

fig4 = fig3.update_yaxes(autorange="reversed")
st.plotly_chart(fig4, use_container_width=True)

st.write("""
Choropleth map to show the number of doctorate recipients ranked by state in 2017
""")
num_state = pd.read_excel('num_state.xlsx', skiprows=3)
code = {'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'}

num_state['Code'] = num_state['State or location'].map(code)

fig5 = go.Figure(data=go.Choropleth(
                 locations=num_state['Code'], # Spatial coordinates
                 z = num_state['Doctorate recipients'].astype(float), # Data to be color-coded
                 locationmode = 'USA-states', # set of locations match entries in `locations`
                 colorscale = 'ylorbr',
                 colorbar_title = "Number of doctorate recipients",
))

fig5.update_layout(
    title_text = 'State ranked by number of doctrate recipients in 2017',
    geo_scope='usa', # limite map scope to USA
)
st.plotly_chart(fig5, use_container_width=True)