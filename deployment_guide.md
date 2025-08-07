# 🚀 Medical Chatbot Deployment Guide

This guide covers multiple deployment options for the Medical Chatbot application.

## 📁 Complete File Structure

Make sure you have all these files in your project directory:

```
medical-chatbot/
├── medical_chatbot.py          # Main Streamlit app
├── requirements.txt            # Dependencies
├── README.md                  # Documentation
├── DEPLOYMENT_GUIDE.md        # This file
├── setup.py                   # Package setup
├── .gitignore                 # Git ignore rules
└── .streamlit/
    └── config.toml            # Streamlit configuration
```

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended - Free)

**Steps:**
1. Create a GitHub repository and push all files
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository
6. Set main file path: `medical_chatbot.py`
7. Click "Deploy"

**Advantages:**
- Free hosting
- Automatic deployments on git push
- Built-in SSL certificates
- Easy sharing with custom URLs

### 2. Heroku Deployment

**Additional files needed:**
Create `Procfile` (no extension):
```
web: sh setup.sh && streamlit run medical_chatbot.py --server.port=$PORT --server.address=0.0.0.0
```

Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

**Deploy:**
1. Install Heroku CLI
2. `heroku create your-medical-chatbot`
3. `git push heroku main`

### 3. AWS EC2 Deployment

**Steps:**
1. Launch EC2 instance (t2.micro for free tier)
2. SSH into instance
3. Install Python and pip
4. Clone your repository
5. Install requirements: `pip install -r requirements.txt`
6. Run: `streamlit run medical_chatbot.py --server.port=8501 --server.address=0.0.0.0`
7. Configure security groups for port 8501

### 4. Google Cloud Platform (Cloud Run)

**Additional file needed - Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["streamlit", "run", "medical_chatbot.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

**Deploy:**
```bash
gcloud run deploy medical-chatbot --source . --platform managed --region us-central1 --allow-unauthenticated
```

### 5. Local Development

**Quick start:**
```bash
git clone <your-repo>
cd medical-chatbot
pip install -r requirements.txt
streamlit run medical_chatbot.py
```

## 🔧 Environment Variables

For production deployments, you may want to set these environment variables:

```bash
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

## 📊 Performance Optimization

For production deployments:

1. **Resource Limits:**
   - Memory: 512MB minimum
   - CPU: 1 vCPU minimum
   - Storage: 1GB minimum

2. **Caching:**
   - Use `@st.cache_data` for expensive computations
   - Implement session state management efficiently

3. **Security:**
   - Set up HTTPS (handled by most cloud platforms)
   - Implement rate limiting if needed
   - Add input validation and sanitization

## 🔒 Security Considerations

**Important for production:**

1. **Data Privacy:**
   - No chat history is stored persistently
   - Session data is cleared on browser close
   - No personal information is logged

2. **Input Sanitization:**
   - User inputs are processed safely
   - No code execution from user input
   - XSS protection built into Streamlit

3. **Medical Compliance:**
   - Clear disclaimers throughout the app
   - No diagnostic capabilities
   - Appropriate emergency responses

## 🐛 Troubleshooting

**Common Issues:**

1. **Port Issues:**
   - Ensure the correct port is exposed
   - Check firewall settings
   - Verify cloud platform port configuration

2. **Dependencies:**
   - Make sure all packages in requirements.txt are installed
   - Use Python 3.8+ for compatibility

3. **Memory Issues:**
   - Monitor resource usage
   - Implement proper caching
   - Consider upgrading server resources

## 📈 Monitoring & Analytics

**Recommended tools:**
- **Uptime monitoring:** UptimeRobot, Pingdom
- **Performance:** New Relic, DataDog
- **Logs:** Cloud platform native logging
- **Usage analytics:** Google Analytics (if privacy compliant)

## 🔄 Continuous Deployment

**GitHub Actions example** (`.github/workflows/deploy.yml`):
```yaml
name: Deploy to Streamlit Cloud
on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Deploy to Streamlit Cloud
      run: echo "Auto-deploy configured in Streamlit Cloud"
```

## 📞 Support & Maintenance

**Regular maintenance tasks:**
- Update dependencies monthly
- Review and update medical information
- Monitor error logs
- Test emergency detection functionality
- Update emergency contact information

**Support considerations:**
- Provide clear contact information
- Set up error reporting
- Monitor user feedback
- Plan for scalability

---

**Remember:** This is a medical information tool. Ensure compliance with local healthcare regulations and maintain appropriate disclaimers for your jurisdiction.