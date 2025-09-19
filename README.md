# INCLUDED ALL THE WEEKS SHORT EXPLAINATION DOWN
# Week-03 – Decision Tree (ID3)

PES2UG24CS823

This folder contains all the files for **Week 3 Lab: ID3 Decision Tree Algorithm and Its Explaination**.

Everything is already organized and structured for easy navigation.  
Go through the files in this folder to understand the implementation and datasets.

---

## Folder Structure
- **EC_F_823_Lab3.py** – My implementation of the ID3 helper functions
- **student_lab.py** – Original lab skeleton (for reference)
- **test.py** – Testing and evaluation script (provided)
- **mushroom.csv** – Dataset 1
- **tictactoe.csv** – Dataset 2
- **Nursery.csv** – Dataset 3
- **README.md** – This file
- **temp.txt** – Temporary/extra notes (if any)
- **.gitignore** – Git ignore rules

---

## How to Use
Just open this folder and run the **test.py** script with the required dataset.

Example:
```bash
python test.py --ID EC_F_823_Lab3 --data mushroom.csv
```

---

# WEEK-04 – Model Selection & Comparative Analysis   

---

## Highlights  
- Compared Manual Grid Search vs GridSearchCV  
- Datasets: Wine Quality, HR Attrition, Banknote Authentication, QSAR Biodegradation  
- Pipeline: StandardScaler → SelectKBest → Classifier  
- Models: Decision Tree, k-Nearest Neighbors, Logistic Regression  
- Both methods gave consistent results; GridSearchCV was faster  
- Generated confusion matrices and ROC curves  
- Key learnings: pipelines, hyperparameter tuning, cross-validation  

---

## Tools  
Python, scikit-learn, pandas, numpy, matplotlib, seaborn  
---

## Full explained inside the folder
## Feel Free To Fork this Repository

---
# WEEK-06 Neural Network Function Approximation 
---

## 📌 Overview
Implemented a **neural network from scratch** to approximate a polynomial dataset generated from my SRN. Learned how activation functions, initialization, and hyperparameters affect training.

---
## 🔑 Key Learnings
- **ReLU > Sigmoid** → ReLU gave much better results.  
- **Xavier initialization** prevented vanishing/exploding gradients.  
- **Learning rate (0.005)** and **batch size (32)** worked best.  
- Best model achieved **R² ≈ 0.86** on test data.  
- Low training loss ≠ good generalization → balance is key.  

---

## 📊 Best Result
- **Config:** ReLU, LR=0.005, Batch=32, Epochs=500  
- **Final Test Loss:** ~0.137  
- **R² Score:** ~0.867  

---
