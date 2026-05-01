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
**Objective:** Split the dataset into training and testing sets. Fit a linear regression model using scikit-learn. Interpret the coefficients and evaluate the model using metrics such as R-squared and mean squared error. 

**Phase 1: Linear Regression (The Baseline)**
* Initially implemented a Linear Regression model.
* **The Insight:** While the model achieved an **R-squared of 0.6690**, the error margin was concerningly high (over $5,400 off for our test case). I wasn't fully confident in this 67% accuracy as it seemed to oversimplify the market dynamics.

**Phase 2: Random Forest (The Optimization)**
* To verify the accuracy and push the performance, I pivoted to a **Random Forest Regressor** (an ensemble method using 100 decision trees).
* **The Breakthrough:** This model captured the non-linear complexities of the data, boosting the **R-squared to 0.8993**.
* **Result:** Reduced the prediction error from $5,414 down to just **$895**, a significant improvement that validates the model's reliability for real-world application.

**Tools Used:** Python, Pandas, Scikit-Learn (LinearRegression, RandomForestRegressor, train_test_split)

### Task 4: Time Series Analysis & Trend Detection
**Dataset:** `stock_prices_dataset.csv`  
**Objective:** Analyse historical stock data to isolate trends and validate market momentum using statistical testing.

**Key Insights Derived:**
1. **Trend Isolation:** Used **Seasonal Decomposition** to strip away market "noise," revealing a consistent long-term bullish trend where the price grew from ~$77 to ~$98.
2. **Volatility Smoothing:** Applied a **3-month rolling mean** to identify that the early 2016 dip was a temporary market correction rather than a structural trend reversal.
3. **Statistical Validation:** Conducted an **Augmented Dickey-Fuller (ADF) test**. The resulting **p-value of 0.993** statistically confirmed the series is **Non-Stationary**, providing mathematical proof of persistent momentum.

**Tools Used:** Python, Pandas, Matplotlib, Statsmodels (ADF Test, seasonal_decompose)

---
## ⚙️ Level 3: Advanced Tasks

### Task 5: Customer Churn Prediction (Advanced Classification)
**Dataset:** `churn-bigml-80.csv`, `churn-bigml-20.csv`  
**Objective:** Build a system to predict which customers are likely to leave a company (Churn).

**Executive Summary:**  
Data science is often about spotting the human frustration hidden in the numbers before a customer walks away. This project was highly relatable; I remembered my own experience in the UK, calling a service provider four times with no resolution before finally quitting. Seeing that exact "frustration threshold" appear as a statistical pattern in my code transformed this from a technical task into a mission to solve real-world churn.

**Phase 1: Logistic Regression (The Baseline)**
* Implemented a baseline model to separate "Churners" from "Loyalists.".
* **The Insight:** This model was too simple and missed 76% of actual churners (Low Recall). It proved that human behavior is rarely a straight line.

**Phase 2: Random Forest & Grid Search (The Optimization)**
* Pivoted to a **Random Forest** classifier and used **GridSearchCV** to fine-tune the "brains" of the model (tree depth and split points).
* **The Breakthrough:** Boosted the "catch rate" (Recall) by **2.5x** compared to the baseline.
* **Actionable Output:** Generated a "High-Risk" list of **62 specific customers** for the sales team to prioritize for retention.

**Key Insights Derived:**
1. **The "Power of 4" Trigger:** Customers reaching 4 support calls were almost guaranteed to leave. I proposed a "Safety Net" trigger at the **3rd call** to intervene before the customer quits.
2. **Precision Over Guesswork:** Achieved **95% Precision**, meaning the model is right 19 out of 20 times when it flags a customer.
3. **From Math to Action:** Successfully isolated **62 high-risk individuals** from the testing pool, turning abstract data into a literal to-do list for marketing.

**Tools Used:** Python, Pandas, Scikit-Learn (RandomForestClassifier, LogisticRegression, GridSearchCV), StandardScaler, OneHotEncoder.

---

## ⚙️ How to Run
1. Clone this repository: 
   `git clone https://github.com/emmanuelgharteykb/codveda-data-analysis-internship.git`
2. Activate Virtual Environment:
   `source venv/bin/activate`
3. Install dependencies:
   `pip install pandas matplotlib seaborn scikit-learn statsmodels`
4. Run the scripts:
```bash
   # Level 1
   python level-1-basic/task1_cleaning.py
   python level-1-basic/task2_eda.py

   # Level 2
   python level-2-intermediate/task3_housing/task3_model.py
   python level-2-intermediate/task3_housing/task3_random_forest.py
   python level-2-intermediate/task4_time_series/task4_analysis.py
   python level-2-intermediate/task4_time_series/task4_analysis_phase2.py

# Level 3
   python level-3-advanced/task5_predictive_modeling/task5_model.py
   python level-3-advanced/task5_predictive_modeling/task5_model_phase2.py
```
---

## 👤 Author
**Emmanuel Kobina Bondzie Ghartey** *Aspiring Data/Business Analyst | Business Intelligence Developer*
