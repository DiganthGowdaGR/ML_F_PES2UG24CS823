# SHARATH GOWDA GR
# PES2UG24CS823
# Support Vector Machine (SVM) Classifier - Learning Lab 10

## Overview
This project focuses on understanding and implementing **Support Vector Machines (SVM)** with different kernel functions. It includes experiments on synthetic and real-world datasets, visualizations of decision boundaries, and analysis of hard vs soft margins.

---

## Objectives
- Learn the working principles of Support Vector Machines.
- Explore how different kernel functions affect classification performance.
- Visualize decision boundaries for better understanding of decision regions.
- Analyze the impact of the regularization parameter **C** (hard and soft margins).

---

## 1. Setup and Imports
The following libraries are used in this project:
- **numpy**, **pandas** – for data manipulation and analysis  
- **matplotlib**, **seaborn** – for visualization  
- **scikit-learn (sklearn)** – for data generation, preprocessing, and SVM implementation  

---

## 2. Visualization Helper Function
A helper function `plot_decision_boundaries()` is implemented to:
- Create a grid of points in the feature space.
- Predict class labels for each grid point using a trained SVM model.
- Plot the decision boundary and data points for visual understanding.

---

## 3. Experiment 1: Moons Dataset

### Data Generation and Preparation
- The **make_moons()** function from `sklearn.datasets` is used to create a non-linear dataset.
- Data is split into training and testing sets using **train_test_split**.
- Features are scaled using **StandardScaler** for consistent SVM performance.

### Training and Evaluation
- SVM models are trained using three different kernels:
  - **linear**
  - **rbf**
  - **poly**
- Model performance is evaluated using **classification_report** (Precision, Recall, F1-score).

### Visualization
- The **plot_decision_boundaries()** function is used to visualize how each kernel separates the moon-shaped data.

---

## 4. Experiment 2: Banknote Authentication Dataset

### Data Loading and Preparation
- The **Banknote Authentication Dataset** is loaded using `pandas.read_csv` from a provided URL.
- Two features (`variance`, `skewness`) and the target variable (`class`) are selected.
- The dataset is split and scaled similar to the Moons dataset.

### Training and Evaluation
- SVM models are trained using **linear**, **rbf**, and **poly** kernels.
- Results are displayed using **classification_report** with labels:
  - **Forged**
  - **Genuine**

### Visualization
- Decision boundaries are visualized for all kernels to observe differences in classification behavior.

---

## 5. Experiment 3: Hard vs Soft Margins

### Data Generation
- A linearly separable dataset is created using **make_blobs()**.
- Outliers are added manually to demonstrate the effect of margin flexibility.

### Training and Visualization
- Two linear SVM models are trained:
  - **C = 0.1** → Soft Margin (allows some misclassifications)
  - **C = 100** → Hard Margin (tries to classify all points correctly)
- Decision boundaries show how **C** controls model flexibility and margin width.

---

## 6. Results and Observations
- **Linear kernel:** Suitable for linearly separable data.  
- **RBF kernel:** Handles complex non-linear decision boundaries effectively.  
- **Polynomial kernel:** Captures non-linear relationships but may overfit small datasets.  
- **C parameter:**  
  - Small **C** → soft margin, more tolerance for errors.  
  - Large **C** → hard margin, strict separation.  

---

## Technologies Used
- Python 3.x  
- NumPy  
- Pandas  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

   git clone https://github.com/yourusername/svm-learning-lab.git
   cd svm-learning-lab
