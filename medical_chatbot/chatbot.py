"""
Medical Chatbot Core Module

Contains the main MedicalChatbot class with all chatbot functionality.
"""

import json
import re
from typing import Dict, List, Tuple
import difflib


class MedicalChatbot:
    def __init__(self):
        self.emergency_keywords = [
            'chest pain', 'heart attack', 'stroke', 'bleeding heavily', 'unconscious',
            'difficulty breathing', 'severe allergic reaction', 'poisoning',
            'severe burns', 'broken bone', 'suicide', 'overdose', 'choking',
            'severe headache', 'paralysis', 'seizure'
        ]
        
        self.symptoms_conditions = {
            'fever': {
                'possible_causes': ['Common cold', 'Flu', 'Infection', 'COVID-19'],
                'advice': 'Rest, stay hydrated, monitor temperature. Seek medical care if fever exceeds 103°F or persists.',
                'red_flags': ['High fever with severe headache', 'Difficulty breathing', 'Persistent vomiting']
            },
            'headache': {
                'possible_causes': ['Tension headache', 'Migraine', 'Sinus infection', 'Dehydration'],
                'advice': 'Rest in dark room, stay hydrated, consider over-the-counter pain relief.',
                'red_flags': ['Sudden severe headache', 'Headache with fever and stiff neck', 'Vision changes']
            },
            'cough': {
                'possible_causes': ['Common cold', 'Allergies', 'Bronchitis', 'Asthma'],
                'advice': 'Stay hydrated, use humidifier, avoid irritants. Persistent cough needs evaluation.',
                'red_flags': ['Coughing up blood', 'Severe difficulty breathing', 'High fever with cough']
            },
            'stomach pain': {
                'possible_causes': ['Indigestion', 'Gas', 'Food poisoning', 'Gastritis'],
                'advice': 'Eat bland foods, stay hydrated, avoid dairy and spicy foods.',
                'red_flags': ['Severe abdominal pain', 'Vomiting blood', 'Signs of dehydration']
            },
            'sore throat': {
                'possible_causes': ['Viral infection', 'Bacterial infection', 'Allergies', 'Dry air'],
                'advice': 'Gargle with salt water, stay hydrated, use throat lozenges.',
                'red_flags': ['Difficulty swallowing', 'High fever', 'Severe throat pain']
            }
        }
        
        self.health_topics = {
            'nutrition': 'Eat a balanced diet with fruits, vegetables, whole grains, lean proteins, and healthy fats. Limit processed foods and sugar.',
            'exercise': 'Adults should aim for at least 150 minutes of moderate aerobic activity weekly, plus strength training twice a week.',
            'sleep': 'Adults need 7-9 hours of quality sleep nightly. Maintain consistent sleep schedule and good sleep hygiene.',
            'stress management': 'Practice relaxation techniques, regular exercise, adequate sleep, and seek support when needed.',
            'preventive care': 'Regular check-ups, vaccinations, screenings, and healthy lifestyle choices are key to prevention.'
        }
    
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
