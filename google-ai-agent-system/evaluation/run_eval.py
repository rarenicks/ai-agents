import requests
import json
import sys

# Mock Evaluation Set
TEST_SET = [
    {"input": "What is the length of 'Google DeepMind'?", "expected_tool": "calculate_length"},
    {"input": "Search for the latest news on Gemini AI", "expected_tool": "web_search", "requires_search": True},
    {"input": "Hi there!", "expected_tool": None}
]

def run_evaluation(endpoint="http://localhost:8000/agent/chat"):
    print("Starting Evaluation Run...")
    results = []
    
    for i, test_case in enumerate(TEST_SET):
        print(f"Running Test Case {i+1}: {test_case['input']}")
        try:
            payload = {
                "session_id": f"eval_run_{i}",
                "message": test_case['input']
            }
            response = requests.post(endpoint, json=payload)
            response.raise_for_status()
            data = response.json()
            
            resp_text = data.get("response", "")
            print(f"  -> Agent Response: {resp_text[:100]}...")
            
            # Simple heuristic check
            passed = True
            if not resp_text:
                passed = False
                
            results.append({
                "input": test_case['input'],
                "response": resp_text,
                "passed": passed
            })
            
        except Exception as e:
            print(f"  -> Test Failed: {e}")
            results.append({"input": test_case['input'], "error": str(e), "passed": False})
            
    print("\nEvaluation Summary:")
    passed_count = sum(1 for r in results if r['passed'])
    print(f"Passed: {passed_count}/{len(results)}")
    
    # In a real scenario, we would upload 'results' to Vertex AI Evaluation service here.
    with open("evaluation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Results saved to evaluation_results.json")

if __name__ == "__main__":
    run_evaluation()
