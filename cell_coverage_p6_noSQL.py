import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import random
import datetime


df = pd.read_csv("df_no_nan_small.csv",parse_dates=["date"])
#df_list = np.array_split(df,50)

#dataset_number = random.choice(range(0,49,1))

#sql_df = df_list[dataset_number]

#df["date"] = pd.to_datetime(df["date"])
df["date"] = df["date"].dt.strftime("%Y-%m-%d %H:%M:%S")

[beginning, end] = st.slider("Date Range", min_value=pd.datetime.to_pydatetime(df["date"].min()), max_value=pd.datetime.to_pydatetime(df["date"].max()))

mask = (df['date'] >= beginning) & (df['date'] <= end)

new_df = df.loc[mask]

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
ax.plot(np.unique(df["hour"]), df["hour"].value_counts().sort_index(), linewidth=2.0)
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
ax1.pie(df["Top_Networks"].value_counts(),explode = (0.1,0.2,.3,.4),labels=df["Top_Networks"].value_counts().index.values, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)


fig2, ax2 = plt.subplots()
ax2.plot(df["Top_Networks"].unique(), df[metric], linewidth=2.0)
fig2.set_size_inches(30, 10.5, forward=True)
st.pyplot(fig2)



st.write(
'''
#### Activity Performance
#'''
)
#
fig3, ax3 = plt.subplots()
ax3.plot(df["activity"].unique(), df[metric], linewidth=2.0)
fig3.set_size_inches(30, 10.5, forward=True)
st.pyplot(fig3)


fig4, ax4 = plt.subplots()
ax4.pie(df["activity"].value_counts(),labels=df["activity"].value_counts().index.values, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig4)

#

