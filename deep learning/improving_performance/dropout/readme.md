# Dropout Regularization — make_moons Classification

Part of my **100 Days ML Challenge**.

📓 Colab Notebook: [dropout_reg.ipynb](https://colab.research.google.com/drive/1Gp86q-7uBipCMij9IU0Qxo7zIFT7VmHH?usp=drive_link)

## Overview

This notebook explores **Dropout** as a regularization technique in neural networks, using a synthetic non-linear binary classification dataset. The goal is to visually and quantitatively compare a model trained **without** dropout against one trained **with** dropout, and observe the effect on overfitting.

## Dataset

- Generated using `sklearn.datasets.make_moons(n_samples=1000, noise=0.3, random_state=42)`
- Two interleaving crescent-shaped classes, split 80/20 into train and test sets

## Workflow

1. **Data generation & visualization** — created the moons dataset and visualized the train/test split as a scatter plot.
2. **Baseline model (`model_1`)** — a 4-hidden-layer dense network (128 units each, ReLU), no dropout, trained for 100 epochs with Adam (`lr=0.01`) on binary crossentropy.
3. **Loss curves** — plotted training vs validation loss to check for overfitting.
4. **Decision boundary** — visualized `model_1`'s decision regions using `mlxtend.plotting.plot_decision_regions`.
5. **Dropout model (`model_2`)** — same architecture, but with a `Dropout(0.2)` layer after every hidden layer.
6. **Comparison** — plotted `model_2`'s loss curves and decision boundary against the baseline to see how dropout affects the fit.

## Key Takeaway

Adding dropout after each hidden layer smooths out the decision boundary and narrows the gap between training and validation loss, showing dropout's regularizing effect in reducing overfitting on noisy, non-linear data.

## Tech Stack

`TensorFlow / Keras` · `scikit-learn` · `mlxtend` · `NumPy` · `Matplotlib` · `Seaborn`

## Part of

🔗 100 Days of ML Challenge
