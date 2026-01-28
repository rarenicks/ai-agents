import dspy
from config.settings import settings

# 1. Configure the Language Model globally (standard DSPy pattern)
lm = dspy.LM("openai/" + settings.openai_model_name, api_key=settings.openai_api_key)
dspy.configure(lm=lm)

# 2. Define the Signature (The Interface)
# Instead of a prompt string, we define Inputs and Outputs.
class FactChecker(dspy.Signature):
    """Assess the factual accuracy of a claim and provide a reasoning."""
    context = dspy.InputField(desc="The reference context to verify against.")
    claim = dspy.InputField(desc="The statement to check.")
    reasoning = dspy.OutputField(desc="Explanation of why the claim is true or false.")
    assessment = dspy.OutputField(desc="Final verdict: TRUE or FALSE.")

# 3. Define the Module (The Logic)
# Modules are like PyTorch layers. They can learn.
class FactCheckModule(dspy.Module):
    def __init__(self):
        super().__init__()
        # ChainOfThought adds a "reasoning" step automatically before the answer.
        # We map our specific signature to this strategy.
        self.prog = dspy.ChainOfThought(FactChecker)

    def forward(self, context, claim):
        return self.prog(context=context, claim=claim)

# factory function for easy import
def get_module():
    return FactCheckModule()
