# Environment and Dependencies

This document describes the computational environment used to run the simulations and generate the results reported in the thesis.

## Hardware Configuration

Simulations were executed on a standard research workstation with the following specifications:

- CPU: Intel Core i7 (8 cores, 2.6–3.4 GHz)
- RAM: 16 GB DDR4
- Storage: 512 GB SSD
- GPU: Not required (CPU-based training)

The experiments were designed to be reproducible on standard mid-range hardware without specialized acceleration.

---

## Software Environment

- Operating System: Ubuntu 22.04 LTS (64-bit)
- Python Version: 3.10
- Virtual Environment: Python venv

### Core Libraries

- NumPy (for numerical computations)
- Pandas (for data handling)
- Matplotlib (for visualization)
- Scikit-learn (for evaluation metrics)
- TensorFlow / PyTorch (for DQN implementation)
- Stable-Baselines3 (for reinforcement learning framework, if applicable)

---

## Security and Logging Tools

- ELK Stack (Elasticsearch, Logstash, Kibana) – version 8.x
- Custom SOAR orchestration scripts
- JSON/CSV-based log generation for simulated attack scenarios

---

## Simulation Configuration

- Number of simulation runs per scenario: 30
- Episodes per run (for RL training): 500
- Replay buffer size: 10,000
- Batch size: 64
- Learning rate: 0.001
- Discount factor (gamma): 0.99
- Exploration strategy: Epsilon-greedy with linear decay

---

## Reproducibility Notes

- A fixed random seed (42) was used where applicable to ensure experimental consistency.
- All required Python dependencies can be installed using a `requirements.txt` file located in the `code/` directory.
- The repository includes all simulation outputs necessary to reproduce the reported evaluation metrics.
