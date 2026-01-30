# Agentic AI for Finance Transaction Approval
# Inspired by Microsoft Discovery Hour

transactions = [
    {"id": 1, "amount": 5000, "risk_score": 0.2},
    {"id": 2, "amount": 75000, "risk_score": 0.85},
    {"id": 3, "amount": 20000, "risk_score": 0.4}
]

def agent_decision(tx):
    if tx["risk_score"] > 0.7:
        return "ESCALATE_TO_HUMAN"
    elif tx["amount"] > 50000:
        return "FLAG_FOR_REVIEW"
    else:
        return "AUTO_APPROVE"

def human_review(tx):
    return "APPROVED_BY_HUMAN"

print("Agentic AI Finance Decision System\n")

for tx in transactions:
    decision = agent_decision(tx)
    if decision == "ESCALATE_TO_HUMAN":
        decision = human_review(tx)
    print(f"Transaction {tx['id']} -> {decision}")
