# Cybersecurity-AV-Anomaly-Detection

# AI-Based Anomaly Detection System for Vehicle Cybersecurity

## Project Overview
This project presents a lightweight cybersecurity system designed to detect abnormal behavior in vehicle sensors and smart transportation systems.

The system focuses on protecting modern vehicles and smart city infrastructure in Palestine, where there is a lack of affordable and real-time cybersecurity solutions.

The proposed solution uses the Isolation Forest algorithm to detect anomalies without requiring labeled attack data.

---

## Problem Statement
Modern vehicles rely on sensors such as cameras, radar, and GPS. These sensors can be targeted by cyber attacks (e.g., spoofing or false data injection), which may lead to incorrect system behavior or safety risks.

In Palestine, the use of smart systems is increasing, but cybersecurity protection is still limited. Therefore, there is a need for a simple, low-cost, and real-time detection system.

---

## Proposed Solution
I developed an anomaly detection system based on:

- Unsupervised Machine Learning
- Isolation Forest Algorithm
- Real-time detection capability

The system is trained only on normal data and can detect unknown attacks by identifying unusual patterns.

---

## System Architecture
The system consists of the following components:

1. Data Acquisition Layer (collect sensor data)
2. Preprocessing Layer (normalization and scaling)
3. Anomaly Detection Engine (Isolation Forest model)
4. Decision Module (classify normal or attack)
5. Response Module (alert and logging)

---

## Technologies Used
- Python 3
- scikit-learn
- pandas
- numpy

---

## Dataset
The system was evaluated using the NSL-KDD dataset, which is a standard dataset for intrusion detection systems.

Dataset characteristics:
- 125,000+ samples
- 41 features
- Includes both normal and attack data

---

## Implementation Details

### Preprocessing
- Categorical data encoded using LabelEncoder
- Features scaled using StandardScaler
- Training performed on normal data only

### Model Configuration
- Algorithm: Isolation Forest
- Number of trees: 100
- Contamination: 0.25

---

## Results

The system achieved the following performance:

- Accuracy: 81.5%
- Precision: 78.3%
- Recall: 79.2%
- F1-Score: 78.7%
- False Positive Rate: 8.1%
- Inference Time: 1.2 ms per sample

These results show that the system can detect most attacks while maintaining real-time performance.

---

## Comparison with Existing Work

Compared to other approaches:

- Faster than deep learning models (e.g., CNN)
- Does not require labeled attack data
- Similar performance to SVM with better speed
- More suitable for low-resource environments

---

## How to Run the Project

1. Install required libraries:
2. pip install pandas numpy scikit-learn
3. Place the dataset file in the project folder

4. Run the main script:
   python main.py
   ---

## Limitations
- Tested on NSL-KDD dataset, not real vehicle sensor data
- Only one algorithm used (Isolation Forest)
- Response system is simulated

---

## Future Work
- Test on real-world vehicle sensor data
- Use more advanced models (Autoencoder, LSTM)
- Deploy on embedded devices (e.g., Raspberry Pi)
- Improve accuracy and reduce false positives

---

## Author
[Malak Suleiman]

---

## Notes
This project was developed as a university assignment to demonstrate the use of machine learning in cybersecurity for vehicle systems in a local context.
