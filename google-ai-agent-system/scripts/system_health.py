import requests
import json
import time

BASE_URL = "http://localhost:8000"

def check_health():
    print("--- [Health Check] ---")
    try:
        resp = requests.get(f"{BASE_URL}/health")
        resp.raise_for_status()
        data = resp.json()
        print(f"Server Status: {data['status']}")
        print(f"Active Agents: {[a['name'] for a in data['agents']]}")
        return True
    except Exception as e:
        print(f"ERROR: Server is not healthy. {e}")
        return False

def test_agent_roundtrip():
    print("\n--- [Agent Roundtrip Test] ---")
    session_id = f"test_{int(time.time())}"
    payload = {
        "session_id": session_id,
        "message": "Who are you and what are your capabilities?"
    }
    try:
        resp = requests.post(f"{BASE_URL}/agent/chat", json=payload)
        resp.raise_for_status()
        data = resp.json()
        print(f"Agent Response: {data['response'][:200]}...")
        if data['response']:
            print("PASS: Agent responded successfully.")
            return True
        else:
            print("FAIL: Agent returned empty response.")
            return False
    except Exception as e:
        print(f"ERROR: Roundtrip test failed. {e}")
        return False

def test_mcp_access():
    print("\n--- [MCP Integration Test] ---")
    session_id = f"mcp_test_{int(time.time())}"
    payload = {
        "session_id": session_id,
        "message": "Researcher, get system metrics via MCP."
    }
    try:
        resp = requests.post(f"{BASE_URL}/agent/chat", json=payload)
        resp.raise_for_status()
        data = resp.json()
        print(f"Agent Response: {data['response'][:200]}...")
        if "metrics" in data['response'].lower() or "cpu" in data['response'].lower() or "mcp" in data['response'].lower():
            print("PASS: Agent accessed MCP tools successfully.")
            return True
        else:
            print("FAIL: Agent did not seem to use MCP tools.")
            return False
    except Exception as e:
        print(f"ERROR: MCP integration test failed. {e}")
        return False

if __name__ == "__main__":
    s1 = check_health()
    if s1:
        s2 = test_agent_roundtrip()
        s3 = test_mcp_access()
        
        if s1 and s2 and s3:
            print("\n✅ ALL SYSTEMS FUNCTIONAL")
        else:
            print("\n❌ SYSTEM ISSUES DETECTED")
