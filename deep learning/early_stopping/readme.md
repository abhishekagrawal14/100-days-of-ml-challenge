# Early Stopping in Neural Networks

A hands-on demo of **overfitting** and how **early stopping** helps prevent it, using a simple binary classification problem (`make_circles` from scikit-learn).

**Open in Colab:** https://colab.research.google.com/drive/1jj36-M5VOEVfQiA7XnOCAvTZAj4LUeIH?usp=drive_link

## Overview

This notebook trains a small feedforward neural network on a synthetic, non-linearly separable dataset (two concentric circles) and compares two training runs:

1. **Without early stopping** — the model trains for the full 1000 epochs, clearly overfitting to the training data.
2. **With early stopping** — training halts once the validation loss stops improving, preventing further overfitting.

## Dataset

- Generated with `sklearn.datasets.make_circles` (100 samples, noise = 0.1)
- Split into 80% train / 20% test using `train_test_split`
- Visualized with a scatter plot colored by class label

## Model Architecture

A simple dense neural network built with `tensorflow.keras`:

```python
model = Sequential()
model.add(Dense(56, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
```

- **Loss:** binary crossentropy
- **Optimizer:** Adam
- **Metric:** accuracy

## Workflow

| Step | Description |
|------|-------------|
| 1 | Import libraries (`pandas`, `numpy`, `matplotlib`, `tensorflow`, `mlxtend`, `seaborn`, etc.) |
| 2 | Generate and visualize the `make_circles` dataset |
| 3 | Split data into train/test sets |
| 4 | Train a baseline model for 1000 epochs (no early stopping) and plot train vs. validation loss |
| 5 | Visualize decision boundary with `mlxtend.plotting.plot_decision_regions` |
| 6 | Rebuild the same model and train it again, this time with an `EarlyStopping` callback |
| 7 | Compare the loss curves and decision boundary with early stopping applied |

## Early Stopping Configuration

```python
callback = EarlyStopping(
    monitor='val_loss',
    min_delta=0.001,
    patience=50,
    verbose=1,
    mode='auto',
    baseline=None,
    restore_best_weights=False
)
```

- **`monitor='val_loss'`** — tracks validation loss as the stopping criterion
- **`patience=50`** — stops training if validation loss doesn't improve for 20 consecutive epochs
- **`min_delta=0.001`** — minimum change to count as an improvement

## Key Takeaways

- The unconstrained model overfits quickly given its size (256 hidden units) relative to the small dataset (100 samples total).
- Early stopping halts training once the validation loss plateaus, avoiding further overfitting.
- Because the validation set is small (only 20 samples), `val_loss` can be noisy — worth keeping in mind when interpreting how early the callback triggers.

## Suggested Improvements

- Set `restore_best_weights=True` so the final model reflects the best validation performance rather than the weights at the moment training stopped.
- Reduce the hidden layer size (e.g., 8–16 units) for a more gradual, illustrative overfitting curve.
- Use a larger dataset or cross-validation for a more stable validation signal.

## Requirements

```
pandas
numpy
matplotlib
scikit-learn
tensorflow
mlxtend
seaborn
```

## How to Run

1. Open the notebook in [Google Colab](https://colab.research.google.com/drive/1jj36-M5VOEVfQiA7XnOCAvTZAj4LUeIH?usp=drive_link) or Jupyter.
2. Install any missing dependencies (`pip install mlxtend seaborn` if needed).
3. Run all cells in order to reproduce the dataset, baseline training, and early-stopped training runs.