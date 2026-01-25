import requests
import uuid
import sys

BASE_URL = "http://localhost:8000"

def chat_session(initial_message=None):
    session_id = str(uuid.uuid4())
    print(f"Starting session: {session_id}")
    
    if initial_message:
        send_message(session_id, initial_message)
        return

    print("Type 'quit' to exit.")
    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            break
            
        if user_input.lower() in ["quit", "exit"]:
            break
        
        send_message(session_id, user_input)

def send_message(session_id, message):
    payload = {
        "session_id": session_id,
        "message": message
    }
    try:
        response = requests.post(f"{BASE_URL}/agent/chat", json=payload)
        response.raise_for_status()
        data = response.json()
        print(f"Agent: {data['response']}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Agent Engine. Is it running?")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else None
    chat_session(msg)
