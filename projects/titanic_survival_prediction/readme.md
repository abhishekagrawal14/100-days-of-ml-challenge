# 🚢 Titanic Survival Prediction

> **An end-to-end Machine Learning web application that predicts whether a passenger aboard the RMS Titanic would have survived based on passenger information.**
>
> Built with **Scikit-learn**, **Streamlit**, and **Python**.

<p align="center">
  <img src="assets/demo.gif" alt="Application Demo" width="900">
</p>

---

# 🌐 Live Demo



🔗 **Streamlit Cloud:** `ADD_DEPLOYMENT_LINK_HERE`

---

# 📖 Project Overview

The sinking of the **RMS Titanic** remains one of the most well-known maritime disasters in history. Although numerous factors influenced survival, historical passenger records allow us to build predictive machine learning models.

This project uses passenger information such as:

* Passenger Class
* Gender
* Age
* Fare
* Family Size
* Embarkation Port
* Cabin Availability
* Passenger Title

to estimate whether a passenger would have survived.

The project is not only focused on model training but also demonstrates an end-to-end deployment workflow including preprocessing, feature engineering, model serialization, and a Streamlit-based web application.

---

# ✨ Features

* 🚢 Interactive Streamlit Web Application
* 🤖 Machine Learning Pipeline
* 🧠 Automatic Feature Engineering
* 📊 Survival Probability Prediction
* 📈 Clean and Responsive User Interface
* ⚙️ End-to-End Deployment Ready
* 📦 Serialized Pipeline using Joblib

---

# 📂 Project Structure

```text
titanic-survival-prediction/
│
├── app.py
├── prediction.py
├── feature_engineering.py
├── config.py
├── requirements.txt
├── README.md
│
├── models/
│   └── titanic_pipeline.pkl
│
├── assets/
│   ├── demo.gif
│   └── titanic.gif
│
└── notebooks/
```

---

# 🛠️ Tech Stack

## Programming Language

* Python

## Machine Learning

* Scikit-learn

## Data Processing

* Pandas
* NumPy

## Deployment

* Streamlit

## Model Serialization

* Joblib

---

# 📊 Dataset

The dataset used in this project is the famous **Titanic Dataset**.

It contains passenger information collected from the Titanic disaster.

Features include:

* Passenger Class
* Name
* Sex
* Age
* Number of Siblings/Spouses
* Number of Parents/Children
* Ticket
* Fare
* Cabin
* Embarked Port

Target Variable:

* **Survived**

  * 0 → Did Not Survive
  * 1 → Survived

---

# ⚙️ Machine Learning Pipeline

The application uses a Scikit-learn Pipeline to ensure identical preprocessing during both training and inference.

Pipeline Stages:

1. Feature Engineering
2. Data Preprocessing
3. Model Prediction

Using a pipeline guarantees that the same transformations applied during training are also applied during deployment.

---

# 🧩 Feature Engineering

The project performs several feature engineering steps before prediction.

Examples include:

* Extracting passenger titles from names
* Creating family size
* Identifying passengers travelling alone
* Detecting cabin availability
* Removing unnecessary columns
* Preparing categorical features for encoding

---

# 🚀 How to Run Locally

Clone the repository

```bash
git clone https://github.com/abhishekagrawal14/100-days-of-ml-challenge.git
```

Move into the project

```bash
cd titanic-survival-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m streamlit run app.py
```

---

# 📈 Model Output

The application predicts:

* Survival Prediction
* Survival Probability

Example:

```
Prediction:
Survived

Probability:
82.34%
```

---

# 🖥️ Application Preview

The application allows users to enter passenger details through an interactive interface.

Input includes:

* Passenger Class
* Gender
* Age
* Fare
* Family Information
* Embarkation Port
* Passenger Title
* Cabin Availability

After clicking **Predict Survival**, the application:

* Processes the input
* Performs feature engineering
* Passes the data through the trained pipeline
* Displays prediction and survival probability

---

# 📚 Kaggle Notebook

The complete model development notebook can be found here:

🔗 https://www.kaggle.com/code/superviseddeep/titanic-survival-prediction-main

---

# 🎯 Future Improvements

* Deploy on Streamlit Cloud
* SHAP Explainability
* Feature Importance Visualization
* Model Comparison Dashboard
* Better UI Animations
* Passenger History Cards
* Mobile Responsive Design

---

# 💡 Lessons Learned

This project helped me understand several practical machine learning concepts beyond model training.

Key takeaways include:

* Building reusable ML pipelines
* Feature engineering for real-world datasets
* Saving and loading models with Joblib
* Deploying machine learning models using Streamlit
* Managing project structure for deployment
* Handling Scikit-learn version compatibility
* Debugging deployment-specific issues
* Writing production-friendly code

---

# 🤝 Connect With Me

GitHub:
https://github.com/abhishekagrawal14


LinkedIn:
https://www.linkedin.com/in/abhishek-kumar-agrawal-7b8495398 

---

# ⭐ If you found this project helpful

Please consider giving this repository a ⭐.

It motivates me to continue building more machine learning projects as part of my **100 Days of ML Challenge**.
