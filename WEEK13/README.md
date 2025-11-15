## PES2UG24CS823
# ML Lab Week 13 Clustering Lab Instructions
## 1. Objective
The objective of this lab is to implement customer segmentation using clustering techniques, specifically K-means and Recursive Bisecting K-means. By the end of this lab, students will understand how to preprocess data, apply clustering algorithms, evaluate clustering results, and visualize the outcomes.
# Enhanced K-Means Clustering Analysis (K-means++ + Manhattan Distance)

This repository documents the complete workflow of enhancing standard K-means clustering using K-means++ initialization and Manhattan (L1) distance, followed by visualization, evaluation, cluster profiling, outlier detection, and correlation analysis.

---

## Step 1: Implementing K-means++ Initialization

**Action:**  
The `_initialize_centroids` method in the `KMeansClustering` class was modified to use the K-means++ algorithm instead of random initialization.  
This involved:
- Selecting the first centroid randomly.
- Choosing subsequent centroids based on probability proportional to the squared distance from existing centroids.

**Output:**  
Execution confirmed: KMeansClustering class updated with K-means++ initialization.

---

## Step 2: Implementing Manhattan Distance

**Action:**  
The `_assign_clusters` method was modified to compute distances using the Manhattan (L1) metric:

```np.sum(np.abs(x - centroid))```

instead of Euclidean (L2) distance.

**Output:**  
Execution confirmed: KMeansClustering class updated to use Manhattan distance for cluster assignment.

---

## Step 3: Re-running K-means with Enhancements and Evaluating Results

**Action:**  
The clustering process was re-executed using the upgraded model:

1. Ran `plot_elbow_curve` on PCA-transformed data (`X_pca`), confirming 3 clusters.
2. Fit the enhanced KMeans model with `n_clusters = 3`.
3. Generated multiple visualizations and evaluation metrics.

### Plots Generated:
- Elbow Method Plot (Inertia for k = 1–10)
- Silhouette Score Plot (k = 2–10, peak at k = 3)
- PCA Scatter Plot colored by cluster with centroids
- Cluster Size Bar Plot
- Silhouette Score Distribution Box Plots per cluster

### Numerical Results:

```
Inertia: 49146.46
Silhouette Score: 0.38
```

---

## Step 4: Cluster Characteristic Analysis

**Action:**  
To interpret clusters:

- Added cluster labels to the original DataFrame (`data_with_clusters`).
- Computed mean and standard deviation for each feature grouped by cluster.
- Built bar plots for important features such as:
  - age
  - balance
  - campaign
  - housing
  - loan
  - y
  - education
  - marital
  - job

**Output:**  
- Displayed head of `data_with_clusters`.
- Provided cluster-wise mean and standard deviation summaries.
- Generated nine bar charts showing feature differences across clusters.

---

## Step 5: Outlier Detection

**Action:**

1. Calculated Manhattan distance of each point to its cluster centroid.
2. Added a new column: `distance_to_centroid`.
3. For each cluster, defined outliers using:

```mean_distance + 3 * std_distance```

4. Extracted outliers into a new DataFrame (`outliers_df`).

**Output:**
- Updated dataset with distance values.
- Identified 639 total outliers across all clusters.
- Displayed head of the outlier dataset.

---

## Step 6: Feature Correlation Matrix

**Action:**  
Generated a heatmap showing pairwise feature correlations for all numeric variables.

**Output:**  
A heatmap titled "Feature Correlation Matrix" and confirmation that the correlation matrix was successfully generated.

---

## Step 7: Final Summary

A comprehensive markdown summary was created including:

### Comparison with Original K-means
- K-means++ improved stability.
- Manhattan distance produced better cluster shape handling.
- Silhouette and inertia scores were compared.

### Cluster Descriptions

**Cluster 0: Financially Less Affluent**  
Younger group, lowest balance, lowest subscription rate.

**Cluster 1: Financially Secure Older**  
Highest balance, older age, highest subscription rate.

**Cluster 2: Working-Class Younger**  
Moderate age, moderate balance, dominated by working-class jobs.

### Outlier Importance
- Outliers represent customers with unusual combinations of behavior, balance, or campaign interactions.

### Business Insights
- Prioritize Cluster 1 for premium offerings.
- Provide retention/engagement strategies for Cluster 0.
- Investigate outliers for potential niche customer segments.

---

## Conclusion

This project demonstrates how enhancing K-means with K-means++ initialization and Manhattan distance improves clustering performance and interpretability.  
The workflow includes evaluation, visualization, cluster profiling, outlier detection, and correlation analysis, offering a complete analytical understanding of the dataset.

---
