# UE23CS352A - Machine Learning Lab (Week 12)
## PES2UG24CS823 [SHARATH GOWDA GR]
## Naive Bayes Classifier - PubMed RCT Sentence Classification

### Overview
This lab focuses on classifying biomedical research abstract sentences into their respective research paper sections using Naive Bayes based classification models.

Target Classes:
- BACKGROUND
- METHODS
- RESULTS
- OBJECTIVE
- CONCLUSIONS

Dataset: Subset of PubMed 200k RCT dataset (Train / Dev / Test provided).

---

### Objectives Completed
- Implemented Multinomial Naive Bayes **from scratch** (Part A)
- Used Scikit-learn MultinomialNB + TF-IDF + hyperparameter tuning (Part B)
- Approximated Bayes Optimal Classifier using posterior weighted **soft voting ensemble** (Part C)

---

### Final Results Summary

| Part | Model Type | Feature | Accuracy | Macro F1 |
|------|------------|----------|----------|----------|
| A | Scratch Multinomial NB | CountVectorizer | **0.7337** | **0.6655** |
| B | Sklearn MultinomialNB (initial) | TF-IDF | 0.7266 | 0.5877 |
| B | Sklearn MNB (best tuned - GridSearchCV) | TF-IDF + bigrams | CV F1 = **0.6567** | — |
| C | Bayes Optimal Soft Voting Ensemble | TF-IDF | 0.6988 | 0.5958 |

Best Grid Search Params (Part B):  
```python
{'nb__alpha': 0.1, 'tfidf__ngram_range': (1, 2)}
