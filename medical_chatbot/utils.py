"""
Medical Chatbot Utilities Module

Contains utility classes for emergency detection, symptom analysis, and health topics.
"""

import json
import os
import difflib
from typing import Dict, List, Optional


class EmergencyDetector:
    """Detects emergency situations from user input."""
    
    def __init__(self):
        self.emergency_keywords = [
            'chest pain', 'heart attack', 'stroke', 'bleeding heavily', 'unconscious',
            'difficulty breathing', 'severe allergic reaction', 'poisoning',
            'severe burns', 'broken bone', 'suicide', 'overdose', 'choking',
            'severe headache', 'paralysis', 'seizure', 'can\'t breathe',
            'severe pain', 'losing consciousness', 'anaphylaxis', 'cardiac arrest',
            'blood loss', 'major trauma', 'drug overdose', 'alcohol poisoning'
        ]
    
    def detect_emergency(self, message: str) -> bool:
        """
        Detect if message contains emergency keywords.
        
        Args:
            message (str): User's message
            
        Returns:
            bool: True if emergency detected
        """
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in self.emergency_keywords)
    
    def get_emergency_level(self, message: str) -> str:
        """
        Determine emergency severity level.
        
        Args:
            message (str): User's message
            
        Returns:
            str: Emergency level (critical, high, medium, low)
        """
        critical_keywords = ['unconscious', 'not breathing', 'cardiac arrest', 'overdose']
        high_keywords = ['chest pain', 'stroke', 'severe bleeding', 'choking']
        medium_keywords = ['difficulty breathing', 'severe pain', 'allergic reaction']
        
        message_lower = message.lower()
        
        if any(keyword in message_lower for keyword in critical_keywords):
            return 'critical'
        elif any(keyword in message_lower for keyword in high_keywords):
            return 'high'
        elif any(keyword in message_lower for keyword in medium_keywords):
            return 'medium'
        else:
            return 'low'


class SymptomAnalyzer:
    """Analyzes symptoms and provides medical information."""
    
    def __init__(self, data_path: Optional[str] = None):
        """Initialize with optional data path."""
        self.data_path = data_path or os.path.join(os.path.dirname(__file__), '..', 'data')
        self.symptoms_data = self._load_symptoms_data()
    
    def _load_symptoms_data(self) -> Dict:
        """Load symptoms data from JSON file."""
        symptoms_file = os.path.join(self.data_path, 'symptoms.json')
        
        # Default data if file doesn't exist
        default_data = {
            'fever': {
                'possible_causes': ['Common cold', 'Flu', 'Infection', 'COVID-19'],
                'advice': 'Rest, stay hydrated, monitor temperature. Seek medical care if fever exceeds 103°F or persists.',
                'red_flags': ['High fever with severe headache', 'Difficulty breathing', 'Persistent vomiting']
            },
            'headache': {
                'possible_causes': ['Tension headache', 'Migraine', 'Sinus infection', 'Dehydration'],
                'advice': 'Rest in dark room, stay hydrated, consider over-the-counter pain relief.',
                'red_flags': ['Sudden severe headache', 'Headache with fever and stiff neck', 'Vision changes']
            }
        }
        
        try:
            if os.path.exists(symptoms_file):
                with open(symptoms_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        
        return default_data
    
    def analyze(self, message: str) -> Optional[Dict]:
        """
        Analyze user message for symptoms.
        
        Args:
            message (str): User's message
            
        Returns:
            dict or None: Symptom information if found
        """
        message_lower = message.lower()
        
        # Check for exact matches first
        for symptom in self.symptoms_data:
            if symptom in message_lower:
                symptom_data = self.symptoms_data[symptom]
                return {
                    'symptom': symptom,
                    'possible_causes': symptom_data['possible_causes'],
                    'advice': symptom_data['advice'],
                    'red_flags': symptom_data['red_flags'],
                    'duration': symptom_data.get('duration', 'Varies'),
                    'when_to_see_doctor': symptom_data.get('when_to_see_doctor', 'Consult a healthcare provider if symptoms persist or worsen.')
                }
        
        # Try fuzzy matching
        closest_symptom = self._find_closest_symptom(message_lower)
        if closest_symptom:
            symptom_data = self.symptoms_data[closest_symptom]
            return {
                'symptom': closest_symptom,
                'possible_causes': symptom_data['possible_causes'],
                'advice': symptom_data['advice'],
                'red_flags': symptom_data['red_flags'],
                'duration': symptom_data.get('duration', 'Varies'),
                'when_to_see_doctor': symptom_data.get('when_to_see_doctor', 'Consult a healthcare provider if symptoms persist or worsen.')
            }
        
        return None
    
    def _find_closest_symptom(self, user_input: str) -> Optional[str]:
        """Find closest matching symptom using fuzzy matching."""
        symptoms = list(self.symptoms_data.keys())
        matches = difflib.get_close_matches(user_input, symptoms, n=1, cutoff=0.6)
        return matches[0] if matches else None


class HealthTopics:
    """Provides information about general health topics."""
    
    def __init__(self, data_path: Optional[str] = None):
        """Initialize with optional data path."""
        self.data_path = data_path or os.path.join(os.path.dirname(__file__), '..', 'data')
        self.topics_data = self._load_topics_data()
    
    def _load_topics_data(self) -> Dict:
        """Load health topics data from JSON file."""
        topics_file = os.path.join(self.data_path, 'health_topics.json')
        
        # Default data if file doesn't exist
        default_data = {
            'nutrition': {
                'info': 'Eat a balanced diet with fruits, vegetables, whole grains, lean proteins, and healthy fats. Limit processed foods and sugar.',
                'tips': ['Include 5+ servings of fruits/vegetables daily', 'Choose whole grains over refined', 'Stay hydrated'],
                'resources': ['https://www.nutrition.gov', 'https://www.choosemyplate.gov']
            },
            'exercise': {
                'info': 'Adults should aim for at least 150 minutes of moderate aerobic activity weekly, plus strength training twice a week.',
                'tips': ['Start slowly and gradually increase', 'Find activities you enjoy', 'Include both cardio and strength training'],
                'resources': ['https://www.cdc.gov/physicalactivity', 'https://www.acsm.org']
            }
        }
        
        try:
            if os.path.exists(topics_file):
                with open(topics_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        
        return default_data
    
    def get_info(self, message: str) -> Optional[Dict]:
        """
        Get health topic information from user message.
        
        Args:
            message (str): User's message
            
        Returns:
            dict or None: Health topic information if found
        """
        message_lower = message.lower()
        
        for topic in self.topics_data:
            if topic in message_lower or any(word in message_lower for word in topic.split()):
                return self.topics_data[topic]
        
        return None


class ResponseFormatter:
    """Formats chatbot responses for different output formats."""
    
    @staticmethod
    def format_for_streamlit(response_data: Dict) -> str:
        """Format response for Streamlit display."""
        return response_data.get('message', '')
    
    @staticmethod
    def format_for_api(response_data: Dict) -> Dict:
        """Format response for API output."""
        return {
            'message': response_data.get('message', ''),
            'type': response_data.get('type', 'general'),
            'priority': response_data.get('priority', 'normal'),
            'timestamp': response_data.get('timestamp'),
            'metadata': response_data.get('metadata', {})
        }
    
    @staticmethod
    def format_for_json(response_data: Dict) -> str:
        """Format response as JSON string."""
        return json.dumps(response_data, indent=2, ensure_ascii=False)
