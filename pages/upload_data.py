import streamlit as st
import pandas as pd
from database import coll, client

# Define a function to upload data to MongoDB
def upload_to_mongodb(data):
    # Insert data into MongoDB
    result = coll.insert_many(data.to_dict('records'))
    # Display result
    st.write(f'{len(result.inserted_ids)} documents uploaded to MongoDB')
    return result


# Define the Streamlit app
def main():
    # Page title
    st.title('Upload Data')

    # Getting user input
with st.form(key='columns_in_form'):
    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
    with c1:
        date = st.text_input('date')
    with c2:
        user = st.text_input('user')
    with c3:
        pushup = st.number_input('pushup', value = 0)
    with c4:
        stomach = st.number_input('stomach', value = 0)
    with c5:
        squat = st.number_input('squat', value = 0)
    with c6:
        arm = st.number_input('arm', value = 0)
    with c7:
        uplift = st.number_input('uplift', value = 0)
    with c8:
        upheel = st.number_input('upheel', value = 0)

    submitButton = st.form_submit_button(label = 'Submit Data')

# Create dataframe for new_record with user input

new_record = pd.DataFrame({
    'date': date,
    'user': user,
    'pushup':pushup,
    'stomach': stomach,
    'squat': squat,
    'arm':arm, 
    'uplift': uplift,
    'upheel':upheel,   
}, index=[0])  #ValueError("If using all scalar values, you must pass an index")

st.dataframe(new_record)  
    
# Upload data to MongoDB
if st.button('Upload to MongoDB'):
    # Upload data to MongoDB
    upload_to_mongodb(new_record)
    st.success('Data uploaded to MongoDB.')

    # Display the uploaded data in a table
    st.write(pd.DataFrame(new_record))

# Download data in CSV format
st.download_button('Download CSV',
                    new_record.to_csv(),
                    file_name='new_record.csv',
                    mime="text/csv")

# Download data in JSON format
st.download_button('Download JSON',
                    new_record.to_json(),
                    file_name='new_record.json',
                    mime="text/json")


if __name__ == '__main__':
    main()