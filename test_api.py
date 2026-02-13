"""
Lab 6 - API Testing Script
Tests the deployed Wine Quality Prediction API
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("=" * 70)
    print("Testing Health Endpoint")
    print("=" * 70)
    
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")
    print()

def test_root():
    """Test root endpoint"""
    print("=" * 70)
    print("Testing Root Endpoint")
    print("=" * 70)
    
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")
    print()

def test_metrics():
    """Test metrics endpoint"""
    print("=" * 70)
    print("Testing Metrics Endpoint")
    print("=" * 70)
    
    response = requests.get(f"{BASE_URL}/metrics")
    print(f"Status Code: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")
    print()

def test_prediction():
    """Test prediction endpoint"""
    print("=" * 70)
    print("Testing Prediction Endpoint")
    print("=" * 70)
    
    # Sample wine features
    sample_data = {
        "alcohol": 13.2,
        "malic_acid": 2.77,
        "ash": 2.51,
        "alcalinity_of_ash": 18.5,
        "magnesium": 96.0,
        "total_phenols": 2.45,
        "flavanoids": 2.53,
        "nonflavanoid_phenols": 0.29,
        "proanthocyanins": 1.54,
        "color_intensity": 4.6,
        "hue": 1.04,
        "od280_od315": 2.77,
        "proline": 562.0
    }
    
    print("Request Data:")
    print(json.dumps(sample_data, indent=2))
    print()
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=sample_data
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")
    print()

def main():
    """Run all tests"""
    print("\n" + "🧪 " * 35)
    print(" " * 20 + "API TESTING SUITE")
    print("🧪 " * 35 + "\n")
    
    try:
        test_root()
        test_health()
        test_metrics()
        test_prediction()
        
        print("=" * 70)
        print("✅ All tests completed successfully!")
        print("=" * 70)
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API")
        print("   Make sure the container is running on port 8000")
        print("   Run: docker run -d -p 8000:8000 --name wine-api <image-name>")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
