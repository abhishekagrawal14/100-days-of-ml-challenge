# Day 22 - Weight Initialization Techniques

## What I did today
Explored and compared different weight initialization techniques and their impact on neural network training using `make_moons` dataset (2 features — easy to visualize).

### Notebooks

**1. Random vs Zero Initialization**
- Demonstrated why Zero initialization fails — all neurons learn the same thing (symmetry problem)
- Showed how Random initialization breaks symmetry but can cause vanishing/exploding gradients in deep networks

**2. Vanishing & Exploding Gradients**
- Visualized how gradients vanish or explode as they propagate through layers
- Showed why poor initialization makes training unstable or impossible

**3. Xavier (Glorot) & He Initialization**
- **Xavier/Glorot** — designed for sigmoid/tanh activations, scales weights by `sqrt(1/n)`
- **He Initialization** — designed for ReLU activations, scales weights by `sqrt(2/n)`
- Compared convergence speed across all three initialization methods

## Google Colab Notebooks
- [Random vs Zero Initialization](https://colab.research.google.com/drive/1PGqpH1CrgRSzBPcU-yocvp36yQB_dd_H?usp=drive_link)
- [Vanishing & Exploding Gradients](https://colab.research.google.com/drive/1hLOIKcDFY3xyCYcjZe7R7YDtSAu-_krv?usp=drive_link)
- [Xavier & He Initialization](https://colab.research.google.com/drive/1BeaEvVwe9tZwNWZZIEqYpH1TShtRAhM3?usp=drive_link)

## Dataset
`make_moons` — sklearn built-in, 2 features, easy to visualize decision boundaries

## Tech Stack
- Python, NumPy, Matplotlib
- TensorFlow / Keras

## Key Learnings
- Zero initialization = symmetry problem → all neurons identical → model fails to learn
- Random initialization = breaks symmetry but unstable for deep networks
- Xavier init = best for sigmoid/tanh activations
- He init = best for ReLU activations (accounts for dead neurons)
- Right initialization → faster convergence, stable training

## Part of
[100 Days of ML Challenge](https://github.com/abhishekagrawal14/100-days-of-ml-challenge)