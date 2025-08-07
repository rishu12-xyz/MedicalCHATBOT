"""
Streamlit Application for Medical Chatbot

Main Streamlit app that provides the web interface for the medical chatbot.
"""

import streamlit as st
import json
from datetime import datetime
from .chatbot import MedicalChatbot
from .utils import ResponseFormatter

# Configure the Streamlit page
st.set_page_config(
    page_title="MediBot - Medical Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = MedicalChatbot()
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'session_id' not in st.session_state:
        st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")


def render_sidebar():
    """Render the sidebar with information and controls."""
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
        
        # Chat controls
        st.header("💬 Chat Controls")
        if st.button("Clear Chat History", type="secondary"):
            st.session_state.messages = []
            st.rerun()
        
        if st.button("Download Chat", type="secondary"):
            chat_data = {
                'session_id': st.session_state.session_id,
                'timestamp': datetime.now().isoformat(),
                'messages': st.session_state.messages
            }
            st.download_button(
                label="📄 Download JSON",
                data=json.dumps(chat_data, indent=2),
                file_name=f"medical_chat_{st.session_state.session_id}.json",
                mime="application/json"
            )
        
        # Settings
        st.header("⚙️ Settings")
        show_metadata = st.checkbox("Show response metadata", value=False)
        st.session_state.show_metadata = show_metadata


def render_main_interface():
    """Render the main chat interface."""
    st.title("🏥 MediBot - Medical Assistant")
    st.markdown("*Your AI-powered health information companion*")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Show metadata if enabled
            if (st.session_state.get('show_metadata', False) and 
                message["role"] == "assistant" and 
                "metadata" in message):
                with st.expander("Response Metadata"):
                    st.json(message["metadata"])

    # User input
    if prompt := st.chat_input("Describe your symptoms or ask a health question..."):
        # Add user message to chat history
        user_message = {"role": "user", "content": prompt, "timestamp": datetime.now().isoformat()}
        st.session_state.messages.append(user_message)
        
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display bot response
        with st.chat_message("assistant"):
            with st.spinner("Analyzing your message..."):
                response_data = st.session_state.chatbot.process_message(prompt)
                response_text = ResponseFormatter.format_for_streamlit(response_data)
                
                # Display response based on type
                if response_data.get('type') == 'emergency':
                    st.error(response_text)
                elif response_data.get('priority') == 'urgent':
                    st.warning(response_text)
                else:
                    st.markdown(response_text)
            
            # Add assistant response to chat history
            assistant_message = {
                "role": "assistant", 
                "content": response_text,
                "timestamp": datetime.now().isoformat(),
                "metadata": response_data.get('metadata', {})
            }
            st.session_state.messages.append(assistant_message)


def render_footer():
    """Render the footer with emergency contacts and resources."""
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🆘 Emergency Contacts:**
        - **US:** 911
        - **India:** 102 (Medical Emergency)
        - **UK:** 999
        - **Australia:** 000
        - **EU:** 112
        """)
    
    with col2:
        st.markdown("""
        **🔗 Helpful Resources:**
        - [WHO Health Topics](https://www.who.int/health-topics)
        - [CDC Health Information](https://www.cdc.gov)
        - [NHS Health A-Z](https://www.nhs.uk/conditions)
        - [Mayo Clinic](https://www.mayoclinic.org)
        """)


def render_analytics_dashboard():
    """Render analytics dashboard (optional feature)."""
    if st.sidebar.checkbox("Show Analytics", value=False):
        st.header("📊 Session Analytics")
        
        if st.session_state.messages:
            total_messages = len(st.session_state.messages)
            user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
            bot_messages = len([m for m in st.session_state.messages if m["role"] == "assistant"])
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Messages", total_messages)
            with col2:
                st.metric("User Messages", user_messages)
            with col3:
                st.metric("Bot Responses", bot_messages)
            
            # Message types
            message_types = {}
            for message in st.session_state.messages:
                if message["role"] == "assistant" and "metadata" in message:
                    msg_type = message["metadata"].get("type", "general")
                    message_types[msg_type] = message_types.get(msg_type, 0) + 1
            
            if message_types:
                st.subheader("Response Types")
                st.bar_chart(message_types)


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
