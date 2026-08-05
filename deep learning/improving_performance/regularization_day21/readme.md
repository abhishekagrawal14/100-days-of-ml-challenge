# L2 Regularization in Deep Learning using TensorFlow

## 📌 Overview

This project demonstrates the implementation of **L2 Regularization (Weight Decay)** in a neural network using TensorFlow/Keras. It compares a baseline model with a regularized model to illustrate how L2 regularization helps reduce overfitting and improves generalization on a binary classification dataset.

---

## 🚀 Open in Google Colab

You can run the notebook directly in Google Colab:

**Notebook Link:**  
https://colab.research.google.com/drive/1uKcYHQ-SdM7PnBLyfivX_Om83NDJ-PhI?usp=drive_link

---

## 🎯 Objectives

- Understand the concept of overfitting in neural networks.
- Build a baseline neural network using TensorFlow/Keras.
- Apply L2 Regularization to hidden layers.
- Compare the performance of regularized and non-regularized models.
- Visualize decision boundaries and loss curves.

---

## 📂 Dataset

The project uses a synthetic binary classification dataset generated with Scikit-learn's `make_moons()` function.

- **Samples:** 100
- **Noise:** 0.25
- **Random State:** 2

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras
- mlxtend

---

## 📖 Workflow

1. Import the required libraries.
2. Generate a noisy binary classification dataset.
3. Visualize the dataset.
4. Build and train a baseline neural network.
5. Plot the decision boundary and training history.
6. Apply L2 regularization to the hidden layers.
7. Retrain the model.
8. Compare the performance of both models using decision boundaries and loss curves.

---

## 📊 Results

The notebook demonstrates that:

- The baseline model tends to overfit the training data.
- L2 Regularization penalizes large weights during training.
- The regularized model produces a smoother decision boundary.
- Validation performance improves with reduced overfitting.
- The model generalizes better to unseen data.

---

## 📷 Visualizations

The notebook includes:

- Dataset Scatter Plot
- Decision Boundary (Without Regularization)
- Decision Boundary (With L2 Regularization)
- Training Loss Curve
- Validation Loss Curve

---

## ▶️ Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### Install the required libraries

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow mlxtend
```

### Run the notebook

```bash
jupyter notebook regularization.ipynb
```

Or simply open it using the Google Colab link above.

---

## 📚 Learning Outcomes

After completing this notebook, you will understand:

- Overfitting in deep learning
- Why regularization is important
- How L2 Regularization works
- Implementing L2 Regularization in TensorFlow/Keras
- Comparing model performance before and after regularization

---

## 📖 References

- TensorFlow Documentation
- Scikit-learn Documentation
- Keras Documentation
- *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*