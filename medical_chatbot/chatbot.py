"""
Medical Chatbot Core Module

Contains the main MedicalChatbot class with all chatbot functionality.
"""

import json
import os
from typing import Dict, List, Optional
from .utils import EmergencyDetector, SymptomAnalyzer, HealthTopics


class MedicalChatbot:
    """Main Medical Chatbot class handling all interactions and responses."""
    
    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize the Medical Chatbot.
        
        Args:
            data_path (str, optional): Path to data directory containing JSON files
        """
        self.data_path = data_path or os.path.join(os.path.dirname(__file__), '..', 'data')
        
        # Initialize components
        self.emergency_detector = EmergencyDetector()
        self.symptom_analyzer = SymptomAnalyzer()
        self.health_topics = HealthTopics()
        
        # Load configuration
        self._load_config()
    
    def _load_config(self):
        """Load chatbot configuration and settings."""
        self.config = {
            'max_response_length': 1000,
            'emergency_priority': True,
            'include_disclaimers': True,
            'log_interactions': False
        }
    
    def process_message(self, user_message: str, user_context: Optional[Dict] = None) -> Dict:
        """
        Process user message and generate appropriate response.
        
        Args:
            user_message (str): User's input message
            user_context (dict, optional): Additional user context
            
        Returns:
            dict: Response containing message, type, and metadata
        """
        if not user_message.strip():
            return self._get_default_response()
        
        # Check for emergency first (highest priority)
        if self.emergency_detector.detect_emergency(user_message):
            return self._get_emergency_response()
        
        # Try symptom analysis
        symptom_matches = self.symptom_analyzer.analyze_symptoms(user_message)
        if symptom_matches:
            return self._format_symptom_response({'possible_causes': [m['condition'] for m in symptom_matches]})
        
        # Try health topic information
        health_info = self.health_topics.get_topic_info(user_message)
        if health_info:
            return self._format_health_response({'info': health_info})
        
        # Default general response
        return self._get_general_response(user_message)
    
    def _get_emergency_response(self) -> Dict:
        """Generate emergency response."""
        return {
            'message': """🚨 **EMERGENCY DETECTED** 🚨
            
If this is a medical emergency, please:
• Call emergency services immediately (911 in US, 102 in India)
• Go to the nearest emergency room
• Contact your local emergency number

This chatbot cannot provide emergency medical care. Please seek immediate professional medical attention.""",
            'type': 'emergency',
            'priority': 'urgent',
            'metadata': {
                'emergency_contacts': {
                    'US': '911',
                    'India': '102',
                    'UK': '999',
                    'Australia': '000',
                    'EU': '112'
                }
            }
        }
    
    def _format_symptom_response(self, symptom_data: Dict) -> Dict:
        """Format symptom analysis response."""
        response = f"""**Symptom Analysis: {symptom_data.get('symptom', '').title()}**

**🔍 Possible Causes:**
{chr(10).join(f'• {cause}' for cause in symptom_data.get('possible_causes', []))}

**💡 General Advice:**
{symptom_data.get('advice', 'Consult a healthcare professional.')}

**⏱️ Typical Duration:**
{symptom_data.get('duration', 'Varies depending on the cause.')}

**⚠️ Warning Signs - Seek Medical Care If You Experience:**
{chr(10).join(f'• {flag}' for flag in symptom_data.get('red_flags', []))}

**👨‍⚕️ When to See a Doctor:**
{symptom_data.get('when_to_see_doctor', 'Consult a healthcare provider if symptoms persist or worsen.')}

**📋 Disclaimer:**
This information is for educational purposes only and does not replace professional medical advice. Always consult a healthcare provider for diagnosis and treatment."""
        
        return {
            'message': response,
            'type': 'symptom_analysis',
            'priority': 'normal',
            'metadata': symptom_data
        }
    
    def _format_health_response(self, health_data: Dict) -> Dict:
        """Format health information response."""
        response = f"**Health Information:**\n\n{health_data.get('info', '')}\n\n**Note:** Consult healthcare providers for personalized advice."
        
        return {
            'message': response,
            'type': 'health_info',
            'priority': 'normal',
            'metadata': health_data
        }
    
    def _get_general_response(self, user_message: str) -> Dict:
        """Generate general chatbot response."""
        return {
            'message': """I'm a medical information chatbot designed to provide basic health information and symptom guidance.

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

**In case of emergency, call emergency services immediately!**""",
            'type': 'general',
            'priority': 'normal',
            'metadata': {'user_input': user_message}
        }
    
    def _get_default_response(self) -> Dict:
        """Get default welcome response."""
        return {
            'message': "Hello! I'm your medical information assistant. How can I help you today?",
            'type': 'welcome',
            'priority': 'normal',
            'metadata': {}
        }
    
    def get_chat_history(self, session_id: str) -> List[Dict]:
        """
        Get chat history for a session (if logging is enabled).
        
        Args:
            session_id (str): Session identifier
            
        Returns:
            list: Chat history messages
        """
        # This would connect to a database or storage system in production
        return []
    
    def clear_chat_history(self, session_id: str) -> bool:
        """
        Clear chat history for a session.
        
        Args:
            session_id (str): Session identifier
            
        Returns:
            bool: Success status
        """
        # This would clear from database or storage system in production
        return True
