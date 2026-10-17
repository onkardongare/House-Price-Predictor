# House Price Predictor MVP

A simplified machine learning project to predict California housing prices.

## Setup

### 1. Set up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Download the Data

```bash
curl -o data/01/housing.csv https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv
```

## Usage

### Train the Model

```bash
python train.py
```

### Make Predictions

**Option 1: Web Interface**

```bash
streamlit run app.py
```

**Option 2: Command Line**

```bash
python predict.py
```
