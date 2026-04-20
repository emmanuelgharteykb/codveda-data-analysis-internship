# Codveda Data Analysis Internship 🚀📊

This repository contains my completed tasks for the **Codveda Technologies Data Analysis Internship**. The goal of this internship is to apply data analysis, machine learning, and visualization techniques to real-world datasets.

## 📁 Project Structure
The internship is divided into three levels:
* **Level 1: Basic** - Data Cleaning and Exploratory Data Analysis (EDA).
* **Level 2: Intermediate** - Machine Learning Modeling (Regression), Benchmarking, and Evaluation.
* **Level 3: Advanced** - Predictive Modeling, Dashboards, and NLP.

---

## 🛠️ Level 1: Basic Tasks

### Task 1: Data Cleaning and Preprocessing
**Dataset:** `house Prediction Data Set.csv`  
**Objective:** Handle missing values, remove duplicates, and standardize data formats.  

**Key Actions Taken:**
1. **Loading:** Used Pandas to load raw housing data.
2. **Missing Values:** Identified null entries and used mean imputation to fill gaps in numerical columns.
3. **Duplicates:** Removed redundant rows to ensure data integrity.
4. **Export:** Generated `cleaned_house_data.csv` for further analysis.

**Tools Used:** Python, Pandas


### Task 2: Exploratory Data Analysis (EDA)
**Dataset:** `cleaned_house_data.csv`  
**Objective:** Identify patterns, calculate summary statistics, and visualize relationships between housing features and prices.

**Key Insights Derived:**
1. **Statistical Profile:** Found that 50% of the houses in the dataset are priced below **$21,200**, indicating a market primarily composed of affordable/middle-class housing.
2. **Primary Price Drivers:** Identified a strong positive correlation (0.70) between the **number of rooms (RM)** and the house price.
3. **Environmental/Social Impact:** Discovered that **Neighborhood Status (LSTAT)** and **Pupil-Teacher Ratios (PTRATIO)** have significant negative correlations with price, proving that location and school quality are major valuation factors.
4. **Data Distribution:** Used histograms to identify "luxury outliers" at the $50k mark that deviate from the normal market distribution.

**Tools Used:** Python, Pandas, Matplotlib, Seaborn

---
## 🚀 Level 2: Intermediate Tasks

### Task 3: Predictive Modeling & Benchmarking
**Dataset:** `cleaned_house_data.csv`  
**Objective:** Build a predictive "engine" to estimate house prices and verify accuracy using multiple machine learning algorithms.

**Phase 1: Linear Regression (The Baseline)**
* Initially implemented a Linear Regression model.
* **The Insight:** While the model achieved an **R-squared of 0.6690**, the error margin was concerningly high (over $5,400 off for our test case). I wasn't fully confident in this 67% accuracy as it seemed to oversimplify the market dynamics.

**Phase 2: Random Forest (The Optimization)**
* To verify the accuracy and push the performance, I pivoted to a **Random Forest Regressor** (an ensemble method using 100 decision trees).
* **The Breakthrough:** This model captured the non-linear complexities of the data, boosting the **R-squared to 0.8993**.
* **Result:** Reduced the prediction error from $5,414 down to just **$895**, a significant improvement that validates the model's reliability for real-world application.

**Tools Used:** Python, Scikit-Learn (LinearRegression, RandomForestRegressor, train_test_split)

---

## ⚙️ How to Run
1. Clone this repository: 
   `git clone https://github.com/emmanuelgharteykb/codveda-data-analysis-internship.git`
2. Activate Virtual Environment:
   `source venv/bin/activate`
3. Install dependencies:
   `pip install pandas matplotlib seaborn scikit-learn`
4. Run the scripts:
```bash
   # Level 1
   python level-1-basic/task1_cleaning.py
   python level-1-basic/task2_eda.py

   # Level 2
   python level-2-intermediate/task3_model.py
   python level-2-intermediate/task3_random_forest.py
```
---

## 👤 Author
**Emmanuel Kobina Bondzie Ghartey** *Aspiring Data/Business Analyst | Business Intelligence Developer*
