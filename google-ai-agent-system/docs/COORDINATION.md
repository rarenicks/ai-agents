# Multi-Agent Coordination & Code Execution

The Google AI Agent System (Enterprise Edition) utilizes a sophisticated team structure to solve complex problems. A key highlight is the **Data Analyst** agent's ability to execute live Python code.

## 👥 The Agent Team (Team Alpha)

The ecosystem is coordinated by a **Supervisor** who delegates tasks according to agent specialties:

| Agent Name | Role | Core Capability |
| :--- | :--- | :--- |
| **Supervisor** | Orchestrator | Analyzes requests and routes to the best worker. |
| **Senior Researcher** | Information Gathering | Web search and internal document retrieval (MCP). |
| **Professional Writer** | Synthesis | Formatting findings into reports. |
| **Data Analyst** | Computation | **Native Python Code Execution**. |

---

## 💻 Native Code Execution

**File**: `engine/agents/analyst.py`

The system integrates the `google.adk.code_executors.UnsafeLocalCodeExecutor` (simulated sandbox) to allow agents to solve mathematical, logical, or data processing problems.

### How it Works:
1. **Request**: User asks for a complex calculation (e.g., "Sum of primes up to 1000").
2. **Delegation**: Supervisor transfers control to the `Data_Analyst`.
3. **Reasoning**: The Analyst writes a Python block in its response.
4. **Execution**: The ADK Runner detects the code block, executes it using the configured executor, and provides the result back to the model.
5. **Synthesis**: The Analyst provides the final answer based on the real execution output.

---

## 🏗 Infrastructure Support

To enable code execution, the platform provides several critical services:

### 1. Artifact Service
Code execution often generates data (files, charts, text output). The system uses an **Artifact Service** (`InMemoryArtifactService`) linked to the ADK `Runner` to capture and manage these outputs.

### 2. Multi-Agent Delegation
The Supervisor is initialized with `sub_agents=[researcher, writer, analyst]`. In ADK, these agents are treated as "Transfer Tools" that the LLM can invoke to hand over the conversation.

### 3. A2A Open Protocol (Agent-to-Agent)
The system supports the **A2A Open Protocol** for communicating with agents outside the immediate team hierarchy.
- **Protocol Definition**: `frameworks/a2a/protocol.py`
- **Capabilities**: Discovery, Negotiation, task assignment, and observations.
- **Mesh Communication**: Handled by the `A2AGateway`, a simulated service mesh for cross-platform agent sync.

---

## 🧪 Testing Coordination

You can verify the multi-agent handoff and code execution using the dedicated test suite:

```bash
./venv/bin/python3 scripts/code_exec_test.py
```

**Success Criteria**:
- The Supervisor correctly identifies that the request needs the Data Analyst.
- The Data Analyst generates valid Python.
- The system returns the exact mathematical result (`76127`).
