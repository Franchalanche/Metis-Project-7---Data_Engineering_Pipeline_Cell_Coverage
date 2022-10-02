import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import random
import datetime


df = pd.read_csv("df_no_nan.csv")
df_list = np.array_split(df,50)

dataset_number = random.choice(range(0,49,1))

sql_df = df_list[dataset_number]


beginning, end = st.slider("Date Range", min_value=pd.to_datetime(sql_df["date"].min()), max_value=pd.to_datetime(sql_df["date"].max()))

mask = (sql_df['date'] >= beginning) & (sql_df['date'] <= end)

new_df = sql_df.loc[mask]

st.write('''
## Coverage in Catalonia
Everything you need to know /n about cell service in Spain's Capitol
''')


st.write(
'''
#### Google Cloud was the [datasource](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=catalonian_mobile_coverage_eu&page=dataset&project=catalonian-coverage-project&ws=!1m5!1m4!4m3!1sbigquery-public-data!2scatalonian_mobile_coverage_eu!3smobile_data_2015_2017!1m0).
'''
)

st.dataframe(new_df.head())

st.write('''Network Demand by Time of Day''')
fig, ax = plt.subplots()
ax.plot(np.unique(new_df["hour"]), new_df["hour"].value_counts().sort_index(), linewidth=2.0)
fig.set_size_inches(30, 10.5, forward=True)
st.pyplot(fig)

## PART 4 - Graphing and Buttons
#

metric = st.select_slider("Select Metric",options=("signal","speed","precission","satellites"))

st.write(
'''
#### Network  Distribution
#'''
)

fig1, ax1 = plt.subplots()
ax1.pie(new_df["Top_Networks"].value_counts(),explode = (0.1,0.2,.3,.4),labels=new_df["Top_Networks"].value_counts().index.values, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)


fig2, ax2 = plt.subplots()
ax2.plot(new_df["Top_Networks"].unique(), new_df[metric], linewidth=2.0)
fig2.set_size_inches(30, 10.5, forward=True)
st.pyplot(fig2)



st.write(
'''
#### Activity Performance
#'''
)
#
fig3, ax3 = plt.subplots()
ax3.plot(new_df["activity"].unique(), new_df[metric], linewidth=2.0)
fig3.set_size_inches(30, 10.5, forward=True)
st.pyplot(fig3)


fig4, ax4 = plt.subplots()
ax4.pie(new_df["activity"].value_counts(),labels=new_df["activity"].value_counts().index.values, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig4)

#

