# Identity Management & RBAC

The Google AI Agent System features a built-in **Identity Management** layer that enables **Role-Based Access Control (RBAC)** across the entire agent fleet. This ensures that sensitive tools and data are only accessible to authorized personnel.

## 👤 Identity Model

**File**: `engine/identity.py`

The system uses a `UserIdentity` model to track user profiles. In a production environment, this would integrate with Google Cloud Identity or an OAuth2 provider.

### Mock Identities:
| User ID | Username | Role | Key Permissions |
| :--- | :--- | :--- | :--- |
| `user_001` | Avdhesh | **Admin** | Full system access, bypass checks. |
| `user_003` | Analyst | **Researcher** | Read internal docs, web search. |
| `user_002` | Guest_User | **Guest** | Web search only. |

---

## 🛡 Policy Enforcement

**File**: `engine/policy.py`

The `AgentPolicyPlugin` acts as the enforcement engine. It intercepts actions before they reach tools or models.

### 1. Tool Interception
When an agent attempts to call a sensitive tool (e.g., `mcp_read_document`), the plugin verifies the user's identity:
- **Permission Check**: Does the user have `read_internal`?
- **Level Check**: Is the user an `Admin` for `write` operations?

If unauthorized, the plugin returns a `SECURITY_BLOCK` error which the agent is instructed to report to the user.

### 2. Identity Context Injection
The plugin dynamically injects the user's identity into the LLM's system instruction for every turn.

**Example Instruction:**
> `[IDENTITY CONTEXT]: You are currently assisting Avdhesh (Role: admin). Tailor your responses to their technical level and clearance.`

---

## 🧪 Testing RBAC

We provide a diagnostic script to verify that identity-based blocks are working correctly:

```bash
./venv/bin/python3 scripts/identity_rbac_test.py
```

### Script Scenarios:
- **Scenario A**: Admin requests an internal document → **Allowed**.
- **Scenario B**: Guest requests an internal document → **Blocked** with security alert.
- **Scenario C**: Researcher requests 'write' access → **Blocked** (Admin only).

---

## 🔒 Security Logs
Every interception is recorded in `agent_trace.log`:
```text
[POLICY] Intercepted sensitive tool: mcp_read_document for user: Guest_User (guest)
```
