# CNN Image Classification – Rock Paper Scissors  
PES University – ML Lab Week 14

Name: Sharath Gowda GR  
SRN: PES2UG24CS823  
Section: F  

---

## 1. Introduction  
This project involves designing and training a Convolutional Neural Network (CNN) using the PyTorch deep learning framework to classify hand gesture images into three categories: rock, paper, and scissors.  
The model was trained on the Rock–Paper–Scissors dataset containing over 2,000 images and evaluated on an unseen test set.  
After training, the final model was used to make predictions on test images.

---

## 2. Model Architecture  

The CNN model (RPS_CNN) consists of two main components:

### A. Convolutional Feature Extractor  
This block is responsible for extracting hierarchical spatial features. It contains three repeated sequences of Conv2d → ReLU → MaxPool2d layers.

| Layer Type | In Channels | Out Channels | Kernel | Stride | Description |
|------------|-------------|--------------|--------|--------|-------------|
| Conv2d | 3 | 16 | 3×3 | 1 | Processes the RGB image |
| ReLU | - | - | - | - | Non-linear activation |
| MaxPool2d | - | - | 2×2 | 2 | Reduces spatial dimensions |
| Conv2d | 16 | 32 | 3×3 | 1 | Extracts higher-level features |
| MaxPool2d | - | - | 2×2 | 2 | Downsamples feature maps |
| Conv2d | 32 | 64 | 3×3 | 1 | Deep feature extraction |
| MaxPool2d | - | - | 2×2 | 2 | Final reduction to 16×16×64 |

Final output shape: 64 × 16 × 16  
Flattened size: 16,384 features

### B. Fully Connected Classifier  
1. Flatten (16,384 features)  
2. Linear: 16,384 → 256  
3. ReLU  
4. Dropout (p = 0.3)  
5. Linear: 256 → 3 (rock, paper, scissors)

---

## 3. Training and Performance  

### Hyperparameters  
| Parameter | Value | Description |
|----------|--------|-------------|
| Optimizer | Adam | Adaptive optimization algorithm |
| Loss Function | CrossEntropyLoss | For multi-class classification |
| Learning Rate | 0.001 | Step size for weight updates |
| Epochs | 10 | Number of passes over the dataset |
| Batch Size | 32 | Number of samples per batch |
| Device | CUDA | Training on GPU |

### Final Test Accuracy  
The model was evaluated on 438 unseen test images.

Final Test Accuracy: **97.95%**

---

## 4. Conclusion and Analysis  

The CNN performed exceptionally well, achieving a test accuracy of 97.95%.  
The use of 3×3 convolutions, ReLU activations, and 2×2 MaxPooling helped the network extract strong, scale-invariant features.  
The Adam optimizer and a stable learning rate contributed to smooth convergence.  
The dropout layer added during the classification phase improved the generalization ability and reduced overfitting.

---

## 5. Potential Improvements  

### 1. Data Augmentation  
Applying transformations such as random rotations, shifts, brightness variations, or shearing can increase dataset variability. This may further improve robustness to real-world variations.

### 2. Transfer Learning  
Instead of training a CNN from scratch, a pre-trained model like ResNet or VGG (trained on ImageNet) can be fine-tuned.  
This approach often yields higher accuracy, especially for smaller datasets, and can potentially push performance close to 100%.

---

## Project Summary  
- Built a convolutional neural network using PyTorch  
- Trained on a dataset of rock–paper–scissors hand gesture images  
- Achieved 97.95% accuracy on the test set  
- Discussed performance, architecture, and potential improvements  

---

