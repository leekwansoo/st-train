# streamlit_app.py

import streamlit as st
import pandas as pd 
import csv
from pages.trace_train import trace_train

st.markdown("<body style='background-color: White;'>",unsafe_allow_html=True)

#client = init_connection()
from database import coll, client
cursor = coll.find()

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.


def get_data():
    items = []
    for doc in cursor:
        items.append(doc)
    return items

trains = get_data()

# st.write(trains)   

# store items into a csv file 
to_csv = trains
keys = to_csv[0].keys()
field_names =["_id", "date", "user", "pushup", "stomach","squat", "arm", "uplift", "upheel"]
with open('./trains.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=field_names)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)

df = pd.read_csv("trains.csv")
st.write(df)

st.button('trace_train', on_click=trace_train )
