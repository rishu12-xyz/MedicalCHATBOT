"""
Streamlit Application for Medical Chatbot

Main Streamlit app that provides the web interface for the medical chatbot.
"""

import streamlit as st
import json
from datetime import datetime
from .chatbot import MedicalChatbot

# Configure the Streamlit page
st.set_page_config(
    page_title="MediBot - Medical Assistant",
    page_icon="🏥",
    layout="wide"
)

def main():
    # Initialize the chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = MedicalChatbot()
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # App header
    st.title("🏥 MediBot - Medical Assistant")
    st.markdown("*Your AI-powered health information companion*")
    
    # Sidebar with information
    with st.sidebar:
        st.header("ℹ️ Important Information")
        st.warning("""
        **Medical Disclaimer:**
        - This chatbot provides general health information only
        - It does not diagnose or treat medical conditions
        - Always consult healthcare professionals for medical advice
        - In emergencies, call emergency services immediately
        """)
        
        st.header("🔧 Features")
        st.info("""
        • Symptom checker and guidance
        • Health information and tips
        • Emergency detection
        • When to seek medical care
        • Preventive health advice
        """)
        
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

    # Main chat interface
    st.header("💬 Chat with MediBot")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Describe your symptoms or ask a health question..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display bot response
        with st.chat_message("assistant"):
            response = st.session_state.chatbot.generate_response(prompt)
            st.markdown(response)
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Footer with additional resources
    st.markdown("---")
    st.markdown("""
    **🆘 Emergency Contacts:**
    - US: 911
    - India: 102 (Medical Emergency)
    - UK: 999
    - Australia: 000
    
    **🔗 Helpful Resources:**
    - [WHO Health Topics](https://www.who.int/health-topics)
    - [CDC Health Information](https://www.cdc.gov)
    - [NHS Health A-Z](https://www.nhs.uk/conditions)
    """)

if __name__ == "__main__":
    main()


def main():
    """Main application function."""
    # Initialize session state
    initialize_session_state()
    
    # Render UI components
    render_sidebar()
    render_main_interface()
    render_analytics_dashboard()
    render_footer()


if __name__ == "__main__":
    main()
