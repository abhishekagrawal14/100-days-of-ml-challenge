# Day 19 — Feature Normalization in Deep Learning

Part of my **100 Days of ML** challenge.

📓 Notebook: [Open in Colab](https://colab.research.google.com/drive/1kSoMU5XT3gbmB4lBSXvpEUdRUfusRwcQ?usp=drive_link)

## 🎯 Goal

Demonstrate — visually and empirically — why feature normalization matters when training neural networks with gradient descent.

## 📊 Dataset

**Breast Cancer Wisconsin** dataset (from `sklearn.datasets`), using two numeric features with very different scales:

| Feature | Approx. Range |
|---|---|
| `mean area` | 140 – 2500 |
| `mean smoothness` | 0.05 – 0.16 |

Target: `target` (binary classification — malignant vs. benign)

## 🧪 Experiment Setup

- **Model:** Simple 2-layer feedforward network (`Dense(32, relu)` → `Dense(1, sigmoid)`)
- **Optimizer:** Plain SGD (chosen deliberately over Adam, since Adam's per-parameter adaptive learning rates can mask scaling issues)
- **Loss:** Binary cross-entropy
- **Epochs:** 250
- Trained the **same architecture** twice:
  1. On raw, unscaled features
  2. On features scaled with `MinMaxScaler`

## 📈 Results

| | Unscaled | Scaled |
|---|---|---|
| `val_loss` behavior | Oscillates wildly (~0.4 – 0.9), never stabilizes even after 250 epochs | Smooth, steady descent to a low, stable value |
| Training stability | Poor — large gradient steps on the high-magnitude feature dominate | Stable — both features contribute comparably to gradients |

**Unscaled val_loss curve:**
Loss jumps around chaotically across all 250 epochs — no clear convergence.

**Scaled val_loss curve:**
Loss decreases smoothly and converges to a noticeably lower, more stable value.

## 🔑 Key Takeaway

When features are on very different scales, gradient descent (especially plain SGD) struggles because:
- The loss surface has very different curvature along each feature's axis
- Steps that are appropriate for the small-scale feature are either too large or too small for the large-scale feature
- This causes oscillation, slow convergence, or instability

**Normalization (Min-Max scaling / Standardization)** puts all features on a comparable scale, giving gradient descent a much smoother, more symmetric loss surface to optimize — resulting in faster, more stable convergence.

> Note: This effect is much more visible with plain SGD than with adaptive optimizers like Adam, which partially self-correct for scale differences.

## 🛠️ Tech Stack

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn` (dataset + `MinMaxScaler`)
- `TensorFlow` / `Keras`
