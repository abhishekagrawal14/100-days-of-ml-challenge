# Day 16 - Backpropagation from Scratch | Regression + Classification

## What I did today
Built backpropagation completely from scratch using only NumPy — no Keras, no sklearn, pure math implementation for both regression and classification problems.

### Architecture
Both notebooks use a small `2→2→1` neural network:
- Input layer: 2 neurons (features)
- Hidden layer: 2 neurons
- Output layer: 1 neuron

### 1. Backpropagation for Regression
- Dataset: Student placement data (CGPA, IQ → Package)
- Loss function: Mean Squared Error (MSE)
- Output activation: Linear
- Implemented from scratch:
  - `initialize_parameters` — weights and biases initialization
  - `L_layer_forward` — forward pass
  - `update_parameters` — backward pass with gradient descent

### 2. Backpropagation for Classification
- Dataset: Student placement data (CGPA, Profile Score → Placed/Not Placed)
- Loss function: Binary Cross Entropy
- Output activation: Sigmoid
- Implemented from scratch:
  - Same structure as regression but different loss + activation
  - Trained epoch-wise — loss decreasing per epoch confirmed correct implementation

## Google Colab Notebooks
- [Backpropagation - Regression](https://colab.research.google.com/drive/1ixnDqq2zYQzqiF_u1XQ8OXgLNOeEiuIZ?usp=drive_link)
- [Backpropagation - Classification](https://colab.research.google.com/drive/1QIuTaQyYI08I6lz3NHS8VlJnsl8a5iiK?usp=drive_link)

## Tech Stack
- Python
- NumPy only (no ML libraries)

## Key Learnings
- Backpropagation = chain rule applied layer by layer from output to input
- Regression vs Classification mein sirf loss function aur output activation change hota hai — backprop logic same rehta hai
- Weight update formula: `W = W - lr * dW`
- Loss decreasing per epoch = correct gradient flow
- Keras andar yahi sab automatically karta hai — ab pata hai andar kya hota hai

## Part of
[100 Days of ML Challenge](https://github.com/abhishekagrawal14/100-days-of-ml-challenge)