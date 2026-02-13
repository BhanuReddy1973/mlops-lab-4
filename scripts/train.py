"""
Lab 6 - Model Training Script for Jenkins Pipeline
Trains a wine quality prediction model and saves metrics
"""

import json
import pickle
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, mean_squared_error, accuracy_score, classification_report
import warnings
import os

warnings.filterwarnings('ignore')


def load_data():
    """Load and prepare wine dataset"""
    print("📥 Loading wine dataset...")
    wine = load_wine()
    X, y = wine.data, wine.target
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_model(X_train, y_train):
    """Train Random Forest model"""
    print("🎯 Training Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    print("✅ Model training complete!")
    return model


def evaluate_model(model, X_test, y_test):
    """Evaluate model and calculate metrics"""
    print("📊 Evaluating model performance...")
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    mse = mean_squared_error(y_test, y_pred)
    
    metrics = {
        'accuracy': round(accuracy, 4),
        'f1_score': round(f1, 4),
        'mse': round(mse, 4)
    }
    
    print(f"  • Accuracy: {metrics['accuracy']}")
    print(f"  • F1 Score: {metrics['f1_score']}")
    print(f"  • MSE: {metrics['mse']}")
    
    return metrics


def save_model(model, filepath='../model.pkl'):
    """Save trained model to parent directory"""
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)
    print(f"✅ Model saved to {filepath}")


def save_metrics(metrics, filepath='../metrics.json'):
    """Save metrics to JSON file in parent directory"""
    with open(filepath, 'w') as f:
        json.dump(metrics, f, indent=2)
    print(f"✅ Metrics saved to {filepath}")


def main():
    """Main training pipeline"""
    print("=" * 70)
    print("Lab 6: Jenkins CI/CD - Model Training Pipeline")
    print("=" * 70)
    
    # Load data
    X_train, X_test, y_train, y_test = load_data()
    print(f"📈 Training samples: {len(X_train)}")
    print(f"📈 Test samples: {len(X_test)}\n")
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    metrics = evaluate_model(model, X_test, y_test)
    
    # Save outputs
    save_model(model)
    save_metrics(metrics)
    
    print("\n" + "=" * 70)
    print("✅ Training pipeline completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
