# ID3 Decision Tree Classifier – Lab 3

## Author
**Sharath Gowda G R**  
**PES2UG24CS823**

---

## Overview
This project implements the **ID3 Decision Tree Algorithm** from scratch using **PyTorch (with optional NumPy)** for educational purposes.  
The project was developed as part of **Lab 3 (Decision Trees)** for the Machine Learning course.

### Features
- Implementation of **ID3 Decision Tree** algorithm
- Supports **PyTorch** and **sklearn-compatible (NumPy)** frameworks
- Works with **categorical datasets** without hardcoding
- Calculates:
  - **Entropy**
  - **Information Gain**
  - **Weighted Average Information**
  - **Best Attribute Selection**
- Evaluates:
  - Accuracy, Precision, Recall, F1-score
  - Tree depth, number of nodes, leaves
- Supports **tree visualization** via CLI flags

---

## Datasets
The project has been tested on three datasets:
1. **Mushroom Classification**  
   Predict whether a mushroom is edible (0) or poisonous (1).

2. **Tic-Tac-Toe Endgame**  
   Predict the outcome of a tic-tac-toe game (win/loss).

3. **Nursery School Admissions**  
   Predict the recommendation level for nursery school admission.

---

## Files in the Repository
- `EC_F_823_Lab3.py` – Implementation of ID3 helper functions:
  - `get_entropy_of_dataset`
  - `get_avg_info_of_attribute`
  - `get_information_gain`
  - `get_selected_attribute`
  
- `test.py` – Testing and evaluation framework (provided by faculty).

- `mushroom.csv`, `tictactoe.csv`, `nursery.csv` – Sample datasets.

---

## How to Run
### **Basic Testing (PyTorch)**
```bash
python test.py --ID EC_F_823_Lab3 --data mushroom.csv
```

## For Other Datasets
```
python test.py --ID EC_F_823_Lab3 --data tictactoe.csv
python test.py --ID EC_F_823_Lab3 --data nursery.csv
```
## Tree Visualization
```
python test.py --ID EC_F_823_Lab3 --data mushroom.csv --print-tree
```

## Using sklearn-Compatible (NumPy) Version
```
python test.py --ID EC_F_823_Lab3 --data mushroom.csv --framework sklearn
```

