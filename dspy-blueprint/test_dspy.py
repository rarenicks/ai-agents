from src.modules.fact_checker import get_module
import sys
import os

# Add project root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_fact_checker():
    print("Testing DSPy Module...")
    
    checker = get_module()
    
    context = "Apollo 11 was the spaceflight that first landed humans on the Moon. Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed the American crew that landed the Apollo Lunar Module Eagle on July 20, 1969, at 20:17 UTC."
    
    true_claim = "Neil Armstrong stepped on the moon in 1969."
    false_claim = "Buzz Aldrin was the first person to step on the moon."
    
    print(f"\nContext: {context[:50]}...")
    
    print(f"\nChecking True Claim: '{true_claim}'")
    pred_true = checker.forward(context=context, claim=true_claim)
    print(f"Reasoning: {pred_true.reasoning}")
    print(f"Verdict: {pred_true.assessment}")
    
    print(f"\nChecking False Claim: '{false_claim}'")
    pred_false = checker.forward(context=context, claim=false_claim)
    print(f"Reasoning: {pred_false.reasoning}")
    print(f"Verdict: {pred_false.assessment}")

if __name__ == "__main__":
    test_fact_checker()
