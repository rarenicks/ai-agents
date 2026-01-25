from typing import Dict, List, Optional
from pydantic import BaseModel

class UserIdentity(BaseModel):
    user_id: str
    username: str
    role: str  # e.g., "admin", "researcher", "reviewer", "guest"
    permissions: List[str] = []

# Simulated Identity Provider (IdP)
MOCK_USER_DB = {
    "user_001": UserIdentity(
        user_id="user_001",
        username="Avdhesh",
        role="admin",
        permissions=["read_internal", "write_internal", "search_web", "bypass_policy"]
    ),
    "user_002": UserIdentity(
        user_id="user_002",
        username="Guest_User",
        role="guest",
        permissions=["search_web"]
    ),
    "user_003": UserIdentity(
        user_id="user_003",
        username="Senior_Analyst",
        role="researcher",
        permissions=["read_internal", "search_web"]
    )
}

def get_user_identity(user_id: str) -> UserIdentity:
    """Fetch identity from mock DB."""
    return MOCK_USER_DB.get(user_id, UserIdentity(
        user_id=user_id,
        username="Unknown",
        role="guest",
        permissions=["search_web"]
    ))

def check_permission(identity: UserIdentity, permission: str) -> bool:
    """Check if identity has a specific permission."""
    if identity.role == "admin":
        return True
    return permission in identity.permissions
