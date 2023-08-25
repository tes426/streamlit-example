from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# Import necessary libraries
import streamlit as st
import requests

# Define the API endpoint for your fine-tuned ChatGPT model
GPT_API_ENDPOINT = "http://your_api_endpoint_here.com/predict"

# Streamlit app
def main():
    st.title("Chat with Fine-tuned ChatGPT")
    
    user_input = st.text_input("You: ", "")
    
    if st.button("Send"):
        if user_input:
            # Send the user input to your API and get the response
            response = send_to_gpt(user_input)
            
            # Display the response
            st.write(f"ChatGPT: {response}")
        else:
            st.warning("Please enter a message to send.")

def send_to_gpt(user_input):
    """
    Send the user input to the GPT API and get the response.
    """
    data = {
        "input": user_input
    }
    
    response = requests.post(GPT_API_ENDPOINT, json=data)
    
    if response.status_code == 200:
        return response.json().get("output", "")
    else:
        return "Sorry, I couldn't process that request."

if __name__ == "__main__":
    main()
