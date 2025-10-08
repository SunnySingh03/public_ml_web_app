🧠 Multiple Disease Prediction Web Application
Overview

Our Multiple Disease Prediction Web Application uses advanced Machine Learning algorithms to predict the likelihood of a person having Diabetes, Heart Disease, or Parkinson’s Disease based on user-provided health parameters.

The web app is developed using Python, Streamlit, and pre-trained ML models. It provides a clean, interactive, and responsive interface for users to get instant health predictions.

📚 Table of Contents

Features

Installation

Usage

Machine Learning Models Used

Contributing

License

Contact

⚙️ Features

✅ Predicts three major diseases:

Diabetes Prediction based on glucose level, BMI, age, etc.

Heart Disease Prediction based on cholesterol, blood pressure, heart rate, etc.

Parkinson’s Disease Prediction based on vocal and frequency parameters.

✅ Built using Streamlit for easy deployment and fast performance
✅ Modern UI with navigation using streamlit-option-menu
✅ Supports real-time predictions through pre-trained ML models
✅ Completely open-source and easy to modify
✅ Can be deployed on Streamlit Cloud or local environment

🧩 Installation

To run the Multiple Disease Prediction Web Application locally, follow these steps:

1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/Multiple-Disease-Prediction.git


Or download the ZIP and extract it.

2️⃣ Navigate to the Project Directory
cd Multiple-Disease-Prediction

3️⃣ Install Required Libraries

Make sure Python is installed (version ≥ 3.8), then run:

pip install -r requirements.txt


This installs:

streamlit

scikit-learn

pandas, numpy

streamlit-option-menu

and other dependencies

4️⃣ Run the Application
streamlit run Multiple_disease_prediction.py

5️⃣ Access the App

Open your browser and go to:
👉 http://localhost:8501

🧠 Usage

Open the application in your browser.

Select the disease you want to predict from the sidebar (Diabetes, Heart, or Parkinson’s).

Enter the required medical values in the input fields.

Click on the “Predict” button to view the result.

The model will show whether the person is likely affected or not.

🧮 Machine Learning Models Used

Each disease prediction uses a trained ML model based on real-world datasets:

Disease	Model Used	Dataset Source
Diabetes	Logistic Regression	PIMA Indian Diabetes Dataset
Heart Disease	Random Forest Classifier	UCI Heart Disease Dataset
Parkinson’s Disease	Support Vector Machine (SVM)	UCI Parkinson’s Dataset

All models are pre-trained and saved as .sav files for fast loading in the app.

🤝 Contributing

We welcome contributions to improve features, UI, or model accuracy.

To contribute:

Fork the repository

Create a new branch for your feature or fix

Commit your changes

Push to your fork and open a Pull Request

Please make sure to follow Python and Streamlit best practices.
