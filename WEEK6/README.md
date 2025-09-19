# UE23CS352A: MACHINE LEARNING WEEK-06
## Neural Network Function Approximation  
### SRN: PES2UG24CS823  

---

## 📌 Overview
This project was completed as part of the **Artificial Neural Networks (ANN) lab**.  
The main objective was to **implement a neural network from scratch** (without using high-level frameworks like TensorFlow or PyTorch) and train it to approximate a synthetic polynomial dataset generated based on my SRN.  

---

## 🚀 Tasks Completed
- Implemented **core components** of a neural network:  
  - **Activation functions** → ReLU and its derivative.  
  - **Loss function** → Mean Squared Error (MSE).  
  - **Weight Initialization** → Xavier (Glorot) initialization with `std = sqrt(2/(fan_in + fan_out))`; biases set to zero.  
- Implemented **forward propagation**:  
  - Input → Hidden1 (ReLU) → Hidden2 (ReLU) → Output (Linear).  
- Implemented **backpropagation** using the chain rule to compute gradients for all layers.  
- Built a **training loop** with:  
  - Gradient descent updates.  
  - Early stopping (with patience).  
  - Train and test loss tracking.  
- Added **visualizations**:  
  - Loss curves.  
  - Predictions vs Actual comparison.  
  - Residual analysis.  
- Conducted **multiple experiments** by varying learning rate, batch size, activation function, and epochs.  

---

## 🔑 Key Learnings
1. **Activation Functions**  
   - ReLU worked significantly better than Sigmoid for this architecture.  
   - Sigmoid led to poor performance (low R² and high loss).  

2. **Weight Initialization**  
   - Xavier initialization stabilized training and prevented vanishing/exploding gradients.  
   - Provided much smoother convergence compared to random initialization.  

3. **Hyperparameter Impact**  
   - Learning rate was critical: 0.005 (with ReLU) performed best.  
   - Batch size 32 was more stable than 64.  
   - More epochs improved performance slightly but also increased the risk of overfitting.  

4. **Model Performance**  
   - Best configuration achieved **R² ≈ 0.86** on test data.  
   - Predictions closely matched the polynomial ground truth.  

5. **Generalization vs Overfitting**  
   - Learned that low training loss does not always mean a better model.  
   - Proper initialization combined with balanced hyperparameters leads to better generalization.  

---

## 📊 Results Summary
| Experiment | Learning Rate | Batch Size | Epochs | Activation | Final Train Loss | Final Test Loss | R² Score |
|------------|--------------|------------|--------|------------|------------------|-----------------|----------|
| Exp1       | 0.005        | 32         | 500    | ReLU       | 0.1296           | 0.1370          | 0.8677   |
| Exp2       | 0.001        | 64         | 500    | ReLU       | 0.2637           | 0.2631          | 0.7356   |
| Exp3       | 0.001        | 32         | 1000   | ReLU       | 0.1932           | 0.1942          | 0.8041   |
| Exp4       | 0.001        | 32         | 500    | Sigmoid    | 0.9448           | 0.9449          | 0.0552   |

**Best Run → Exp1 (ReLU, LR=0.005, Batch=32, Epochs=500).**

---

## 📝 Conclusion
From this assignment, I learned:  
- How to **design, implement, and train** a neural network completely from scratch.  
- The importance of **proper weight initialization (Xavier)** in stabilizing training.  
- How **activation functions** influence convergence and performance.  
- The strong impact of **hyperparameters** like learning rate, batch size, and epochs.  
- The difference between **fitting training data** and achieving good **generalization**.  

This lab gave me **hands-on experience** in the fundamentals of neural networks, which will help me understand and use higher-level deep learning frameworks more effectively in the future.  

---
