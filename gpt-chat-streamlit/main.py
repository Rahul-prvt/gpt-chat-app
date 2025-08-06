import streamlit as st
from openai import OpenAI, OpenAIError

# app configuration
st.set_page_config(page_title="OpenAI API Example", page_icon=":robot_face:")
st.title("CHAT WITH GPT")
st.markdown("Paste your open AI API key below to start chatting with GPT-3.5.")

#api key input
api_key = st.text_input("OpenAI API Key", type="password")

# Model selection 
model = st.selectbox(
    "Select Model",
    ["gpt-3.5-turbo", "gpt-4"]
)

# Intitalize chat history 

if "message" not in st.session_state:
    st.session_state.messages=[]
    
# display chat history 
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# chat input
if api_key:
    user_input = st.chat_input("Type your message here...")
    if user_input:
        st.session_state.messages.append({'role':'user','content':user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        try:
            openai = OpenAI(api_key=api_key)
            response = openai.chat.completions.create(
                model=model,
                messages=st.session_state.messages
            )
            bot_response = response.choices[0].message.content
            
            st.session_state.messages.append({'role':'assistant','content':bot_response})
            with st.chat_message("assistant"):
                st.markdown(bot_response)
        except OpenAIError as e:
            st.error(f"An error occurred: {e}")
else:
    st.warning("Please enter your OpenAI API key to start chatting.")