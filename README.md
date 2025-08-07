# 🏥 MediBot - Medical Assistant Chatbot

A comprehensive medical information chatbot built with Streamlit that provides symptom analysis, health information, and emergency detection.

## ⚠️ Medical Disclaimer

**IMPORTANT:** This chatbot is for informational purposes only and does not provide medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns. In case of emergency, contact emergency services immediately.

## 🌟 Features

- **Symptom Analysis**: Analyzes common symptoms and provides possible causes
- **Emergency Detection**: Identifies emergency situations and provides immediate guidance
- **Health Information**: Provides educational content on various health topics
- **Red Flag Warnings**: Identifies symptoms requiring immediate medical attention
- **Interactive Chat Interface**: User-friendly conversational interface
- **Chat History**: Maintains conversation context with clear/reset functionality

## 🚀 Quick Start

### Local Development

1. **Clone or download the project files**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   streamlit run medical_chatbot.py
   ```
4. **Open your browser** and go to `http://localhost:8501`

### Streamlit Cloud Deployment

1. **Push your code to GitHub**
2. **Go to [share.streamlit.io](https://share.streamlit.io)**
3. **Connect your GitHub repository**
4. **Deploy with main file:** `medical_chatbot.py`

## 📁 Project Structure

```
medical-chatbot/
├── medical_chatbot.py          # Main application file
├── requirements.txt            # Python dependencies
├── README.md                  # Project documentation
├── .streamlit/
│   └── config.toml           # Streamlit configuration
├── .gitignore                # Git ignore file
└── setup.py                  # Setup configuration (optional)
```

## 🔧 Configuration

The app includes pre-configured settings in `.streamlit/config.toml`:
- Custom theme colors
- Server configuration for deployment
- Privacy settings

## 📋 Supported Symptoms & Topics

### Symptoms Covered:
- Fever and temperature-related issues
- Headaches and migraines
- Cough and respiratory symptoms
- Stomach pain and digestive issues
- Sore throat and throat problems

### Health Topics:
- Nutrition and diet guidance
- Exercise and fitness recommendations
- Sleep hygiene and disorders
- Stress management techniques
- Preventive care information

### Emergency Detection:
- Chest pain and heart-related emergencies
- Stroke symptoms
- Severe allergic reactions
- Breathing difficulties
- Severe injuries and trauma

## 🛡️ Safety Features

- **Emergency keyword detection** with immediate response protocols
- **Medical disclaimers** prominently displayed
- **Red flag symptom identification** for urgent care needs
- **Professional referral guidance** in all responses
- **No diagnostic or prescription capabilities** by design

## 🔒 Privacy & Security

- **No data storage**: Chat history is session-based only
- **No personal information collection**
- **HIPAA-conscious design** (though not HIPAA compliant)
- **Local processing**: No external API calls for core functionality

## 🚫 Limitations

This chatbot **CANNOT**:
- Provide medical diagnoses
- Prescribe medications
- Replace professional medical consultation
- Handle actual medical emergencies
- Store or analyze personal health data
- Provide treatment recommendations

## 🤝 Contributing

This is a basic implementation that can be extended with:
- More comprehensive symptom database
- Integration with medical APIs
- Multi-language support
- Voice interaction capabilities
- Appointment scheduling features

## 📞 Emergency Contacts

- **United States**: 911
- **India**: 102 (Medical Emergency)
- **United Kingdom**: 999
- **Australia**: 000
- **European Union**: 112

## 📚 Resources

- [World Health Organization](https://www.who.int)
- [Centers for Disease Control](https://www.cdc.gov)
- [NHS Health Information](https://www.nhs.uk)
- [Mayo Clinic](https://www.mayoclinic.org)

## 📄 License

This project is provided for educational and informational purposes. Please ensure compliance with local healthcare regulations and laws when deploying or modifying this application.

---

**Remember: When in doubt, always consult a healthcare professional!**
