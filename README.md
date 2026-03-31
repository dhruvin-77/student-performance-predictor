# Student Performance Predictor

## Project Overview

This project is a machine learning-based desktop application that predicts a student’s final academic performance (G3 grade) using various academic, behavioral, and social factors.

Unlike basic ML scripts, this project provides a **fully interactive graphical user interface (GUI)** built using Tkinter, allowing users to input meaningful real-world data and receive predictions along with explanations.

---

## Objectives

* Build a machine learning model to predict student performance
* Convert raw dataset features into a user-friendly system
* Develop a GUI-based application for real-time predictions
* Provide meaningful explanations for predictions
* Bridge the gap between ML models and real-world usability

---

## Problem Statement

Students and educators often struggle to understand how different factors such as study time, attendance, and past performance influence final grades.

This project aims to solve that problem by:

* Predicting final grades
* Explaining influencing factors
* Providing an interactive prediction system

---

## Dataset Information

* Source: Kaggle
* Dataset: Student Performance Dataset

The dataset contains records of students with features related to:

* Academic performance
* Study habits
* Lifestyle factors
* Family background

---

## Features Used

| Feature    | Description                  |
| ---------- | ---------------------------- |
| studytime  | Weekly study time            |
| failures   | Number of past failures      |
| absences   | Number of school days missed |
| G1, G2     | Previous exam grades         |
| health     | Health condition             |
| freetime   | Free time after school       |
| goout      | Social activity level        |
| Medu, Fedu | Parents’ education level     |

---

## Target Variable

| Variable | Description              |
| -------- | ------------------------ |
| G3       | Final grade (0–20 scale) |

---

## Machine Learning Model

* Model Used: **Random Forest Regressor**
* Library: scikit-learn

### Why Random Forest?

* Handles complex relationships better than linear models
* Reduces overfitting
* Produces more realistic predictions

---

## Workflow

1. Data Loading (CSV dataset)
2. Feature Selection (relevant columns)
3. Train-Test Split
4. Model Training
5. Model Saving (`model.pkl`)
6. GUI Input Collection
7. Prediction Generation
8. Result Interpretation

---

## GUI Application (Tkinter)

This project includes a fully interactive desktop application where users can:

* Select meaningful options (no confusing numbers)
* Enter realistic values
* Get predictions instantly
* Understand results with explanations

### Key GUI Features

* Dropdown menus with real-world meanings
* Input validation (prevents incorrect values)
* Clear labels for all fields
* Error handling for invalid inputs
* Clean and simple interface

---

## User Inputs (Human-Friendly)

Instead of raw numbers, the system uses understandable inputs:

* Study Time → "<2 hrs", "2–5 hrs", etc.
* Health → "Very Bad" to "Excellent"
* Parent Education → "Primary", "Higher Education"
* Absences → Number of days missed (validated range)

---

## Output

The system provides:

### Predicted Grade

```
Predicted G3:    / 20
```

### Performance Level

* Excellent
* Good
* Average
* Poor
* Very Poor

### Explanation (Reasoning)

Example:

```
Strong previous academic performance
High absences may reduce performance
Good study time improves results
```

---

## Technologies Used

* Python
* pandas
* numpy
* scikit-learn
* joblib
* Tkinter (GUI)

---

## Project Structure

```
student-performance-project/
│
├── data/
│   └── student.csv
│
├── src/
│   ├── train_model.py
│   └── predict_gui.py
│
├── model.pkl
├── README.md
├── requirements.txt
├── spp_report.pdf
```

---

##  How to Run the Project

### 1️ Install Dependencies

```
pip install -r requirements.txt
```

### 2️ Train the Model

```
python src/train_model.py
```

### 3️ Run the Application

```
python src/predict_gui.py
```

---

## Key Insights

* Previous grades (G1, G2) strongly influence final performance
* Study time has a positive impact on results
* High absences negatively affect performance
* Lifestyle factors also contribute to outcomes

---

## Limitations

* Predictions are based on dataset patterns, not real-world guarantees
* Model may not generalize to all education systems
* Some features are simplified representations

---

## Future Improvements

* Add more features (internet usage, family support, etc.)
* Improve model accuracy with larger datasets
* Build web-based version of the app
* Add visualization dashboards
* Implement advanced ML models

---

## Conclusion

This project successfully demonstrates how machine learning can be used to predict student performance while maintaining usability through a graphical interface.

It transforms a simple ML model into a **real-world application**, making predictions understandable and accessible to users.

---

## Acknowledgement

* Dataset sourced from Kaggle
* Libraries used from open-source Python ecosystem
