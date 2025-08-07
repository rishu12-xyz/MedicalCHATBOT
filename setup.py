from setuptools import setup

setup(
    name="medical-chatbot",
    version="1.0.0",
    author="Rishi",
    description="A medical information chatbot built with Streamlit",
    url="https://github.com/rishu12-xyz/MedicalCHATBOT",
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "python-dateutil>=2.8.2",
    ],
)
