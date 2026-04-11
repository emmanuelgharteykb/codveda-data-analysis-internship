# Codveda Data Analysis Internship 🚀📊

This repository contains my completed tasks for the **Codveda Technologies Data Analysis Internship**. The goal of this internship is to apply data analysis, machine learning, and visualization techniques to real-world datasets.

## 📁 Project Structure
The internship is divided into three levels:
* **Level 1: Basic** - Data Cleaning and Exploratory Data Analysis (EDA).
* **Level 2: Intermediate** - Regression, Time Series, and Clustering.
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

## 🚀 How to Run
1. Clone this repository: 
   `git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git`
2. Install dependencies:
   `pip install pandas matplotlib seaborn scikit-learn`
3. Run the scripts:
```bash
   python Level-1-Basic/task1_cleaning.py
   python level-1-basic/task2_eda.py
```
---

## 👤 Author
**Emmanuel Kobina Bondzie Ghartey** *Aspiring Data Analyst | Business Intelligence Developer*
