"""
Medical Chatbot Application

A comprehensive medical information chatbot built with Streamlit.
"""

import streamlit as st
import json
import re
from datetime import datetime
from typing import Dict, List, Tuple
import difflib

# Configure the Streamlit page
st.set_page_config(
    page_title="MediBot - Medical Assistant",
    page_icon="🏥",
    layout="wide"
)

class MedicalChatbot:
    def __init__(self):
        self.emergency_keywords = [
            'chest pain', 'heart attack', 'stroke', 'bleeding heavily', 'unconscious',
            'difficulty breathing', 'severe allergic reaction', 'poisoning',
            'severe burns', 'broken bone', 'suicide', 'overdose', 'choking',
            'severe headache', 'paralysis', 'seizure'
        ]
        
        # Load symptoms data
        import os
        data_dir = os.path.join(os.path.dirname(__file__), 'data')
        
        with open(os.path.join(data_dir, 'symptoms.json'), 'r') as f:
            self.symptoms_conditions = json.load(f)
            
        # Load health topics data
        with open(os.path.join(data_dir, 'health_topics.json'), 'r') as f:
            self.health_topics = json.load(f)
    
    def detect_emergency(self, message: str) -> bool:
        """Detect if the message contains emergency keywords"""
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in self.emergency_keywords)

    def find_closest_symptom(self, user_input: str) -> str:
        """Find the closest matching symptom using fuzzy matching"""
        symptoms = list(self.symptoms_conditions.keys())
        matches = difflib.get_close_matches(user_input.lower(), symptoms, n=1, cutoff=0.6)
        return matches[0] if matches else None

    def analyze_symptoms(self, symptoms: str) -> Dict:
        """Analyze reported symptoms and provide information"""
        symptoms_lower = symptoms.lower()
        
        # Check for exact matches first
        for symptom in self.symptoms_conditions:
            if symptom in symptoms_lower:
                return self.symptoms_conditions[symptom]
        
        # Try fuzzy matching
        closest_symptom = self.find_closest_symptom(symptoms)
        if closest_symptom:
            return self.symptoms_conditions[closest_symptom]
        
        return None

    def get_health_info(self, topic: str) -> str:
        """Get information about health topics"""
        topic_lower = topic.lower()
        for key, info in self.health_topics.items():
            if key in topic_lower or topic_lower in key:
                return info
        return None

    def generate_response(self, user_message: str) -> str:
        """Generate appropriate response based on user input"""
        
        # Check for emergency
        if self.detect_emergency(user_message):
            return """🚨 **EMERGENCY DETECTED** 🚨
            
If this is a medical emergency, please:
- Call emergency services immediately (911 in US, 102 in India)
- Go to the nearest emergency room
- Contact your local emergency number

This chatbot cannot provide emergency medical care. Please seek immediate professional medical attention."""

        # Check for symptom analysis
        symptom_info = self.analyze_symptoms(user_message)
        if symptom_info:
            response = f"""**Symptom Analysis:**

**Possible causes:** {', '.join(symptom_info['possible_causes'])}

**General advice:** {symptom_info['advice']}

**⚠️ Seek immediate medical attention if you experience:**
{chr(10).join(f'• {flag}' for flag in symptom_info['red_flags'])}

**Disclaimer:** This information is for educational purposes only and does not replace professional medical advice."""
            return response

        # Check for health information
        health_info = self.get_health_info(user_message)
        if health_info:
            return f"**Health Information:**\n\n{health_info}\n\n**Note:** Consult healthcare providers for personalized advice."

        # Default response for general queries
        return """I'm a medical information chatbot designed to provide basic health information and symptom guidance.

**I can help with:**
• Symptom information and basic guidance
• General health topics (nutrition, exercise, sleep, etc.)
• When to seek medical care
• Health education and prevention tips

**I cannot:**
• Diagnose medical conditions
• Prescribe medications
• Replace professional medical advice
• Handle medical emergencies

**Please describe your symptoms or ask about a health topic I can help with.**

**In case of emergency, call emergency services immediately!**"""

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
