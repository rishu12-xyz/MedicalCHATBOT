from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="medical-chatbot",
    version="1.0.0",
    author="Rishi",
    author_email="rishi@example.com",
    description="A medical information chatbot built with Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rishu12-xyz/MedicalCHATBOT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "python-dateutil>=2.8.2",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "medical-chatbot=medical_chatbot:main",
        ],
    },
    package_data={
        "": ["data/*.json"],
    },
    include_package_data=True,
)
