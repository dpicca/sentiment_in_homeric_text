import streamlit as st
import pandas as pd

# Create session state to store the values of the text inputs
ss= st.session_state
st.set_page_config(page_title="Homer", page_icon=":black_nib:", layout="wide", initial_sidebar_state="expanded")


# Create a sidebar to navigate through the app
with st.sidebar:    
    # Create a text element to manipulate the data
    st.title("Edit the data")
    
    st.subheader("Get a specific value for sentiment")
    st.text_input("Enter the value for positive", key="positive")
    st.text_input("Enter the value for negative", key="negatives")
    st.text_input("Enter the value for neutral", key="neutre")
    
    #get a specific value for the column 'narrator' from the dataframe
    st.subheader("Get a specific value for the column 'narrator'")
    st.text_input("Enter the value for the column 'narrator'", key="narrator")
    
    # get a specific entry from the dataframe
    st.subheader("Get a specific entry")
    st.text_input("Enter the value for the index", key="index")
    
 

    
    
    

# read the data csv and create a dataframe to show it in streamlit
# Show the original    dataframe in streamlit
st.subheader("Original Data")
df = pd.read_csv("ib1_sentiment_probs_french.csv")
df.drop(columns=['Unnamed: 0'], inplace=True)
df.drop(columns=['y'], inplace=True)


edited_df = st.experimental_data_editor(df, key="original_data_editor")
# get only values of the dataframe corresponding to state of the text inputs 'positive', 'negatives' and 'neutre' in the sidebar
if ss.positive != '' and ss.negatives != '' and ss.neutre !='':
    edited_df = edited_df[edited_df['positive'] == float(ss.positive)]
    edited_df = edited_df[edited_df['negative'] == float(ss.negatives)]
    edited_df = edited_df[edited_df['neutral'] == float(ss.neutre)]
        # put some space between the two dataframes
    st.write("-----------")

    #show the edited dataframe in streamlit
    st.subheader("Edited Data for sentiment")
    st.experimental_data_editor(edited_df, key="edited_data_editor")

#get the value of the text input 'narrator' in the sidebar
narrator = ss.narrator
# get only values of the dataframe corresponding to the value of the text input 'narrator' in the sidebar
if narrator != '':
    edited_df = edited_df[edited_df['narrator'] == int(narrator)]
    # put some space between the two dataframes
    st.write("-----------")

    #show the edited dataframe in streamlit
    st.subheader("Edited Data for narrator")
    st.experimental_data_editor(edited_df)
    
# get the value of the text input 'index' in the sidebar
index = ss.index
# get the row corresponding to the index
if index != '':
    edited_df = edited_df.iloc[[int(index)]]
    # put some space between the two dataframes
    st.write("-----------")

    #show the edited dataframe in streamlit
    st.subheader("Edited Data for index")
    st.experimental_data_editor(edited_df)
    


