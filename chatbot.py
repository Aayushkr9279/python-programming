import streamlit as st
import google.generativeai as genai


genai.configure(api_key="your api key")  

model = genai.GenerativeModel("gemini-2.5-flash")


st.title("chat bot")
st.write("ai-bot")


if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Type your message…")


if st.button("Send") and user_input.strip() != "":
    try:
        response = model.generate_content(user_input)
        bot_reply = response.text

        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", bot_reply))

    except Exception as e:
        st.error(f"Error: {e}")


st.write("Chat History:")
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f" You: {message}")
    else:
        st.markdown(f" Bot: {message}")
