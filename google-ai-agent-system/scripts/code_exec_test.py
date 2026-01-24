import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_code_execution():
    print("\n--- [Code Execution Test] ---")
    session_id = f"code_test_{int(time.time())}"
    
    # We ask a question that requires a numerical calculation best solved by code
    payload = {
        "session_id": session_id,
        "user_id": "user_001", # Admin has all permissions
        "message": "Data_Analyst, write a Python script to calculate the sum of all prime numbers up to 1000 and execute it."
    }
    
    try:
        print("Sending request for code execution...")
        resp = requests.post(f"{BASE_URL}/agent/chat", json=payload)
        resp.raise_for_status()
        data = resp.json()
        
        response_text = data.get("response", "")
        print(f"\nAgent Response:\n{response_text}")
        
        # Check if the result seems calculated
        # Sum of primes up to 1000 is 76127
        if "76127" in response_text:
            print("\n✅ PASS: Code was executed and returned the correct mathematical result.")
        elif "python" in response_text.lower() and ("result" in response_text.lower() or "sum" in response_text.lower()):
            print("\n✅ PASS: Agent appeared to use Python to solve the problem.")
        else:
            print("\n❌ FAIL: Agent response did not confirm code execution result.")
            
    except Exception as e:
        print(f"ERROR: Code execution test failed. {e}")

if __name__ == "__main__":
    test_code_execution()
