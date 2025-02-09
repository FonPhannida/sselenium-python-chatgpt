# reports/report.py
import unittest
from datetime import datetime

def generate_report(test_results):
    # Simple report structure
    with open(f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", 'w') as file:
        file.write(f"Test Results: {test_results}")
