﻿
# 📚 Grade Prediction Web App
# Overview
This project is a Django-based web application that predicts student grades based on key factors such as socio-economic score, study hours, sleep hours, and attendance percentage. It provides a simple yet interactive web interface where users can input their details and get an estimated grade prediction instantly.

# Features
✅ Web-based UI built with Django, HTML, CSS, and JavaScript

✅ Backend powered by Django and scikit-learn

✅ Predicts student grades using machine learning models

✅ Interactive form for real-time user input

✅ Responsive and modern design

# Tech Stack
1. Backend: Django (Python), scikit-learn (Machine Learning)
   
2. Frontend: HTML, CSS, JavaScript
   
3. Database: SQLite (or PostgreSQL/MySQL if needed)
   
4. Deployment: Can be hosted on DigitalOcean, Heroku, or any cloud platform
   
5. Dataset from kaggle.com

# The dataset consists of the following features:

1. Socio-Economic Score: A numeric value representing a student’s economic background
   
2. Study Hours: Average number of hours spent studying daily
   
3. Sleep Hours: Average number of hours slept per day
   
4. Attendance Percentage: Percentage of attended classes
   
5. Grade (Target Variable): The final predicted grade

# Installation & Setup
# 1️⃣ Clone the repository

git clone https://github.com/rillhancho/grade_prediction_model.git
cd gradepredictor

# 2️⃣ Create and activate a virtual environment

python -m venv venv  
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3️⃣ Install dependencies

pip install -r requirements.txt

# 4️⃣ Apply migrations and start the Django server

python manage.py migrate  
python manage.py runserver

# The web app will be available at: http://127.0.0.1:8000/

# Usage
  * Open the web app in your browser
  * Enter socio-economic score, study hours, sleep hours, and attendance percentage
  * Click the "Predict Grade" button
  * View the predicted grade instantly on the screen

# Frontend
The frontend is built using HTML, CSS, and JavaScript, ensuring a clean and responsive user interface.

1. HTML: Structure of the form and results display
   
2. CSS: Styling for a modern and user-friendly experience
   
3. JavaScript: Handles user input, sends AJAX requests to Django backend, and updates results dynamically

# Backend (Django + ML Model)
Django View (views.py) handles user input and calls the ML model
Machine Learning Model (ml_model/train_model.py) is trained using scikit-learn and saved as linera_regression_model.pkl

# Future Improvements
🚀 Enhance UI with Bootstrap or Tailwind CSS

🚀 Improve prediction accuracy using deep learning models

🚀 Add authentication & user history tracking

🚀 Deploy the app on DigitalOcean or Heroku

# Contributing
Feel free to fork this repository, make improvements, and submit a pull request!

# License
This project is licensed and copyrighted to Michael Rill Okanda.




