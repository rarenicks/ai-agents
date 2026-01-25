from typing import Dict, List, Any

class MemoryStore:
    def __init__(self):
        self._conversations: Dict[str, List[Dict[str, str]]] = {}
        self._artifacts: Dict[str, List[Dict[str, Any]]] = {}

    def get_history(self, session_id: str) -> List[Dict[str, str]]:
        return self._conversations.get(session_id, [])

    def add_message(self, session_id: str, role: str, content: str):
        if session_id not in self._conversations:
            self._conversations[session_id] = []
        self._conversations[session_id].append({"role": role, "content": content})

    def get_artifacts(self, session_id: str) -> List[Dict[str, Any]]:
        return self._artifacts.get(session_id, [])

    def add_artifact(self, session_id: str, artifact: Dict[str, Any]):
        if session_id not in self._artifacts:
            self._artifacts[session_id] = []
        self._artifacts[session_id].append(artifact)

    def clear(self, session_id: str):
        self._conversations.pop(session_id, None)
        self._artifacts.pop(session_id, None)

