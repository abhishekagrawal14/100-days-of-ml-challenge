# Day 17 — Vanishing Gradient Problem

Part of my **100 Days of ML** challenge.

📓 **Notebook:** [Open in Google Colab](https://colab.research.google.com/drive/174r3skfiWqibppvtygzrrXdw1avP4Mys?usp=drive_link)

## 🎯 Objective
Reproduce the vanishing gradient problem hands-on with a deep sigmoid network, and confirm it by directly inspecting how little the weights move after training.

## 📊 Dataset
`make_moons` from `sklearn.datasets` — 250 samples, noise = 0.05, split 80/20 into train/test.

## 🧠 Setup
Built a deliberately deep `Sequential` model to stress-test gradient flow:

- 12 hidden `Dense(10)` layers, all with **sigmoid** activation
- 1 output `Dense(1)` layer, sigmoid activation
- Loss: `binary_crossentropy`, Optimizer: `adam`
- Trained for 100 epochs

## 🔬 Method
1. Captured the first layer's weights *before* training (`old_weights`).
2. Trained the model.
3. Captured the first layer's weights *after* training (`new_weights`).
4. Computed `gradient = (old_weights - new_weights) / learning_rate` and the percentage change per weight to see how much (or little) each weight actually moved.

## 📉 Observations
- Training accuracy stayed flat around **~50%** (basically a coin flip) for all 100 epochs.
- Loss barely moved, hovering around **~0.693** (≈ `ln(2)`, i.e. the loss of an untrained binary classifier).
- The first layer's weights changed by only a few percent after 100 epochs — the gradient signal from the loss essentially never reached the earliest layers because it got squashed to near-zero passing back through 12 stacked sigmoid layers.

**This is the vanishing gradient problem in action:** each sigmoid layer's derivative is at most 0.25, so backpropagating through 12 of them multiplies the gradient by a factor that shrinks toward zero — the deeper (earlier) layers barely learn anything.

## 🛠️ What helps (noted, not the main run)
- **Shrinking the network** (e.g. 3 sigmoid layers instead of 12) lets gradients flow again — but this defeats the purpose if the problem actually needs a deep/complex model.
- **Switching to ReLU** activation in the hidden layers helps a lot, since ReLU's derivative is 1 for all positive inputs and doesn't saturate the way sigmoid does.

## ✅ Takeaway
Depth + saturating activations (sigmoid/tanh) is a bad combination — it silently kills learning in early layers even though the model *looks* fine architecturally. Activation choice (ReLU and friends) is one of the simplest fixes.

---
*Day 17/100 — 100 Days of ML*