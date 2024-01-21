import streamlit as st
import pandas as pd
import csv

def trace_train():
    data = pd.read_csv('./trains.csv')
    # st.dataframe(data)
    # open the file in read mode
    filename = open('trains.csv', 'r')

    # creating dictreader object
    file = csv.DictReader(filename)
    
    # creating empty lists
    pushup = []
    stomach = []
    squat = []
    arm = []
    uplift = []
    upheel = []
 
    # iterating over each row and append
    # values to empty list
    for col in file:
        pushup.append(col['pushup'])
        stomach.append(col['stomach'])
        squat.append(col['squat'])
        arm.append(col['arm'])
        uplift.append(col['uplift'])
        upheel.append(col['upheel'])
    
    data = pd.DataFrame(
        {
            "name": ["pushup", "stomach", "squat", "arm", "uplift", "upheel"],
            "daily_history": [pushup,stomach,squat,arm,uplift,upheel],
        }
    )
    st.dataframe(data, hide_index=True)
    st.dataframe(
        data,
        column_config={
            "name": "Train Name",
            "daily_history": st.column_config.LineChartColumn(
                "Daily_Record", y_min=0, y_max=20,
                width = "large"
            ),
        },
        hide_index=True,
    )

trace_train()