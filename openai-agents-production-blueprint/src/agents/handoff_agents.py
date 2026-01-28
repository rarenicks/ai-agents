from agents import Agent, handoff
from config.settings import settings

# Define specialized agents
def create_technical_agent():
    return Agent(
        name="TechnicalAgent",
        instructions="You are an expert technical support engineer. Help the user with complex technical issues. If the issue is about billing, hand off to the BillingAgent.",
    )

def create_billing_agent():
    return Agent(
        name="BillingAgent",
        instructions="You are a billing specialist. Help the user with invoices and payments. If they ask a technical question, hand off to the TechnicalAgent.",
    )

def create_triage_agent():
    # Triage agent decides where to send the user
    tech_agent = create_technical_agent()
    billing_agent = create_billing_agent()
    
    return Agent(
        name="TriageAgent",
        instructions="You are a triage coordinator. Determine if the user needs technical help or billing support and hand off to the appropriate agent.",
        handoffs=[
            handoff(tech_agent),
            handoff(billing_agent),
        ],
    )
