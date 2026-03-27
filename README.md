# XGBoost Phishing Detection Model

## Project Overview
This project implements a phishing detection model using XGBoost. The goal is to accurately classify websites as phishing or legitimate to enhance online safety and combat phishing attacks.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Deikazen/PhishGuard.git
   cd PhishGuard
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Prepare the dataset as per the provided structure.
2. Run the model training script:
   ```bash
   python train_model.py
   ```
3. After training, use the prediction script to classify new websites:
   ```bash
   python predict.py --url <website_url>
   ```

## Model Information
The model employs XGBoost, a gradient boosting framework that is efficient and effective for various classification tasks. It utilizes various techniques such as regularization and sparsity awareness for better performance.

## Dataset Source
The dataset used for training and testing the model is sourced from [Mendeley Data](https://data.mendeley.com/datasets/gdx3pkwp47/2).

## Requirements
- Python 3.6+
- XGBoost
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Project Structure
```
PhishGuard/
├── data/
│   └── dataset.csv           # The dataset used for training
├── models/
│   └── model.pkl             # The trained model
├── scripts/
│   ├── train_model.py        # Script to train the model
│   └── predict.py            # Script to make predictions
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```
