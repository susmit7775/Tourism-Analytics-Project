# 🌍 Tourism Experience Analytics
**Classification, Prediction, and Recommendation System**

Welcome to the **Tourism Experience Analytics** project! This repository contains an end-to-end Machine Learning pipeline and interactive web application designed to help travel agencies personalize customer experiences, predict user satisfaction, and classify travel behaviors.

---

## 🚀 Project Overview
Tourism platforms aim to enhance user experiences by leveraging data to provide personalized recommendations. This project analyzes user preferences, travel patterns, and attraction features to achieve three primary objectives:

1. **Rating Prediction (Regression):** Predicts the 1-5 star rating a user will give an attraction before they visit.
2. **Trip Classification (Classification):** Determines the context of a trip (e.g., Business, Family, Solo) based on user demographics and behaviors.
3. **Personalized Recommendations (Collaborative Filtering):** Suggests new hidden gems and attractions using User-Item similarity matrices.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest Regressor & Classifier, Collaborative Filtering)
* **Web Framework:** Streamlit
* **Deployment:** GitHub & Streamlit Community Cloud

---

## 📁 Repository Structure
```text
Tourism-Analytics-Project/
│
├── models/                     # Pre-trained Machine Learning models (.pkl)
│   ├── rating_model.pkl
│   ├── mode_classifier.pkl
│   ├── rec_matrix.pkl
│   ├── le_continent.pkl
│   ├── le_category.pkl
│   └── le_mode.pkl
│
├── app.py                      # The main Streamlit web application
├── train_models.ipynb          # Jupyter Notebook with data cleaning and model training
├── requirements.txt            # Python dependencies
├── Project_Report.docx         # Detailed project methodology and insights
└── README.md                   # Project documentation


💻 How to Run Locally
If you want to run this application on your own machine, follow these steps:

1. Clone the repository
git clone [https://github.com/YourUsername/Tourism-Analytics-Project.git](https://github.com/YourUsername/Tourism-Analytics-Project.git)
cd Tourism-Analytics-Project

2. Install required libraries
pip install -r requirements.txt

3.Run the Streamlit app
streamlit run app.py


📊 Key Business Use Cases
Risk Management: Prevent bad user experiences by filtering out attractions with low predicted ratings.

Targeted Marketing: Offer tailored deals (e.g., family packages) by instantly classifying the user's trip type.

Customer Retention: Keep users engaged by suggesting highly accurate, personalized destinations.

Author: Susmit Sarkar
