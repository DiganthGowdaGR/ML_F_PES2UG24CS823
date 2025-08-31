# Lab 4 – Model Selection and Comparative Analysis  

**Name:** SHARATH GOWDA GR  
**SRN:** PES2UG24CS823  
**Course:** Machine Learning  
**Lab:** WEEK 4  

---
as mentioned in class only code file pushed
---

## 📖 Introduction  
In this lab, I explored **model selection and hyperparameter tuning** for different classifiers. The experiment was divided into two key parts:  

1. 🔄 **Manual Grid Search** – Implementing grid search using loops and cross-validation.  
2. ⚡ **Automated Grid Search (GridSearchCV)** – Using scikit-learn’s built-in method.  

The main goal was to understand **how grid search works internally** and then compare it with the **efficient automated version**.  

---

## 📊 Datasets Used  
The datasets were preprocessed (scaling, feature selection, encoding if needed) and split into training/testing sets:  

- 🍷 **Wine Quality** → Predicting good/bad quality wine.  
- 🧑‍💼 **HR Attrition** → Predicting employee attrition.  
- 💵 **Banknote Authentication** → Predicting genuine vs forged banknotes.  
- ⚗️ **QSAR Biodegradation** → Predicting chemical biodegradability.  

---

## ⚙️ Methodology  

🔗 **Pipeline Used:**  

- 📏 **StandardScaler** → Normalized the features.  
- ✂️ **SelectKBest** → Selected best features (parameter `k` tuned).  
- 🤖 **Classifiers applied:**  
  - 🌳 Decision Tree  
  - 👥 k-Nearest Neighbors (kNN)  
  - ➗ Logistic Regression  

---

## 🛠️ Part 1: Manual Grid Search  

- Defined parameter grids for each classifier:  
  - Decision Tree → `max_depth`  
  - kNN → `n_neighbors`  
  - Logistic Regression → `C`  

- Performed **5-fold Stratified Cross-Validation**.  
- Trained pipeline → predicted probabilities → calculated **ROC-AUC**.  
- Stored mean scores → selected **best parameters**.  
- Retrained best pipeline on full training set.  

---

## ⚡ Part 2: GridSearchCV  

- Built the same pipeline.  
- Used **GridSearchCV** with:  
  - Parameter grid  
  - `cv=5` (Stratified)  
  - `scoring="roc_auc"`  

- Reported **best parameters, best score, and best estimator**.  

---

## 📈 Results & Observations  

- ✅ Both **manual grid search** and **GridSearchCV** gave **consistent results**.  
- ⚡ GridSearchCV was **faster and more convenient**.  
- 🧠 Manual grid search improved my **understanding of hyperparameter tuning**.  
- 📊 Plotted **Confusion Matrices** and **ROC Curves** for final models.  

*(Add screenshots/plots here if available)*  

---

## 🏁 Conclusion  

Key learnings from this lab:  

✔️ Use **pipelines** to prevent data leakage.  
✔️ Apply **hyperparameter tuning** to improve performance.  
✔️ Use **cross-validation** for robust evaluation.  
✔️ **Manual methods** help learning, but **GridSearchCV** is best for real-world projects.  

---

## 🚀 Tech Stack  

- 🐍 Python  
- 📦 scikit-learn  
- 📊 matplotlib / seaborn (for visualization)  
- 🔢 numpy / pandas  


---

## 📌 Author  
**👤 SHARATH GOWDA GR**  
SRN: PES2UG24CS823  
