"""
Medical Chatbot Package

A comprehensive medical information chatbot built with Streamlit.
Provides symptom analysis, health information, and emergency detection.

Author: Medical Chatbot Team
Version: 1.0.0
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Medical Chatbot Team"
__email__ = "contact@medicalchatbot.com"
__description__ = "AI-powered medical information chatbot"

from .chatbot import MedicalChatbot
from .utils import EmergencyDetector, SymptomAnalyzer, HealthTopics

__all__ = [
    "MedicalChatbot",
    "EmergencyDetector", 
    "SymptomAnalyzer",
    "HealthTopics"
]
