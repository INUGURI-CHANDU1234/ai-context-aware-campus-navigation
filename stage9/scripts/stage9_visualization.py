import csv
import os
import matplotlib.pyplot as plt


# ============================================================
# STAGE 9 - FINAL RESULTS VISUALIZATION
# AI-BASED CONTEXT-AWARE CAMPUS NAVIGATOR
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

CHART_DIR = os.path.join(BASE_DIR, "stage9", "charts")
DATA_DIR = os.path.join(BASE_DIR, "stage9", "data")
REPORT_DIR = os.path.join(BASE_DIR, "stage9", "reports")

os.makedirs(CHART_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


# ============================================================
# VERIFIED STAGE 7 / STAGE 8 RESULTS
# ============================================================

crowd_levels = ["LOW", "MEDIUM", "HIGH"]
route_costs = [308.00, 455.64, 619.70]

blocked_scenarios = 4
successful_reroutes = 4
rerouting_success_rate = 100.00

decision_scenarios = 7
correct_decisions = 7
decision_accuracy = 100.00

confidence_levels = ["Open Road", "Blocked Road"]
confidence_values = [85.33, 94.00]

risk_values = [31.67, 91.25]


# ============================================================
# 1. SAVE FINAL METRICS CSV
# ============================================================

metrics = [
    ["Metric", "Value"],
    ["Low Crowd Route Cost", 308.00],
    ["Medium Crowd Route Cost", 455.64],
    ["High Crowd Route Cost", 619.70],
    ["Low to High Cost Increase (%)", 101.20],
    ["Blocked Road Scenarios", blocked_scenarios],
    ["Successful Reroutes", successful_reroutes],
    ["Rerouting Success Rate (%)", rerouting_success_rate],
    ["Decision Evaluation Scenarios", decision_scenarios],
    ["Correct Decisions", correct_decisions],
    ["Decision Accuracy (%)", decision_accuracy],
    ["Open Road Confidence (%)", 85.33],
    ["Blocked Road Confidence (%)", 94.00],
    ["Open Road Risk Score", 31.67],
    ["Blocked Road Risk Score", 91.25],
]

metrics_file = os.path.join(DATA_DIR, "stage9_final_metrics.csv")

with open(metrics_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(metrics)


# ============================================================
# 2. CROWD VS ROUTE COST
# ============================================================

plt.figure(figsize=(8, 5))
plt.plot(crowd_levels, route_costs, marker="o", linewidth=2)
plt.title("Campus Crowd Density vs Route Cost")
plt.xlabel("Campus Crowd Density")
plt.ylabel("Average Route Cost")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "crowd_vs_route_cost.png"),
    dpi=200
)
plt.close()


# ============================================================
# 3. REROUTING SUCCESS RATE
# ============================================================

plt.figure(figsize=(7, 5))

labels = ["Successful Reroutes", "Unsuccessful Reroutes"]
values = [successful_reroutes, blocked_scenarios - successful_reroutes]

plt.bar(labels, values)

plt.title("Blocked Road Rerouting Performance")
plt.ylabel("Number of Scenarios")
plt.ylim(0, blocked_scenarios + 1)

for i, value in enumerate(values):
    plt.text(i, value + 0.05, str(value), ha="center")

plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "rerouting_success.png"),
    dpi=200
)
plt.close()


# ============================================================
# 4. DECISION ACCURACY
# ============================================================

plt.figure(figsize=(7, 5))

labels = ["Correct Decisions", "Incorrect Decisions"]
values = [correct_decisions, decision_scenarios - correct_decisions]

plt.bar(labels, values)

plt.title("Explainable AI Decision Accuracy")
plt.ylabel("Number of Evaluated Scenarios")
plt.ylim(0, decision_scenarios + 1)

for i, value in enumerate(values):
    plt.text(i, value + 0.05, str(value), ha="center")

plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "decision_accuracy.png"),
    dpi=200
)
plt.close()


# ============================================================
# 5. CONFIDENCE VS RISK
# ============================================================

plt.figure(figsize=(8, 5))

x = range(len(confidence_levels))

plt.plot(
    x,
    confidence_values,
    marker="o",
    linewidth=2,
    label="Confidence (%)"
)

plt.plot(
    x,
    risk_values,
    marker="s",
    linewidth=2,
    label="Risk Score"
)

plt.xticks(list(x), confidence_levels)
plt.ylabel("Score")
plt.title("Confidence vs Risk Under Different Road Conditions")
plt.ylim(0, 100)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "confidence_vs_risk.png"),
    dpi=200
)
plt.close()


# ============================================================
# 6. CROWD COST INCREASE
# ============================================================

low_cost = 308.00
high_cost = 619.70

increase = ((high_cost - low_cost) / low_cost) * 100

plt.figure(figsize=(7, 5))

labels = ["LOW Crowd", "HIGH Crowd"]
values = [low_cost, high_cost]

plt.bar(labels, values)

plt.title("Impact of Crowd Density on Route Cost")
plt.ylabel("Average Route Cost")

for i, value in enumerate(values):
    plt.text(i, value + 10, f"{value:.2f}", ha="center")

plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "crowd_cost_impact.png"),
    dpi=200
)
plt.close()


# ============================================================
# 7. FINAL RESEARCH REPORT
# ============================================================

report_file = os.path.join(
    REPORT_DIR,
    "stage9_final_evaluation.txt"
)

with open(report_file, "w", encoding="utf-8") as f:

    f.write("STAGE 9 - FINAL EVALUATION REPORT\n")
    f.write("=" * 60 + "\n\n")

    f.write("PROJECT: AI-Based Context-Aware Campus Navigator\n\n")

    f.write("1. CROWD ADAPTATION\n")
    f.write("-" * 40 + "\n")
    f.write(f"LOW crowd route cost    : {low_cost:.2f}\n")
    f.write(f"MEDIUM crowd route cost : 455.64\n")
    f.write(f"HIGH crowd route cost   : {high_cost:.2f}\n")
    f.write(f"LOW -> HIGH increase    : {increase:.2f}%\n\n")

    f.write("Finding: Route cost increases as campus crowd density ")
    f.write("increases, demonstrating context-aware adaptation.\n\n")

    f.write("2. BLOCKED ROAD REROUTING\n")
    f.write("-" * 40 + "\n")
    f.write(f"Blocked-road scenarios : {blocked_scenarios}\n")
    f.write(f"Successful reroutes    : {successful_reroutes}\n")
    f.write(f"Rerouting success rate : {rerouting_success_rate:.2f}%\n\n")

    f.write("Finding: The navigation system successfully generated ")
    f.write("alternative routes for all blocked-road scenarios.\n\n")

    f.write("3. EXPLAINABLE AI DECISION QUALITY\n")
    f.write("-" * 40 + "\n")
    f.write(f"Evaluated scenarios : {decision_scenarios}\n")
    f.write(f"Correct decisions   : {correct_decisions}\n")
    f.write(f"Decision accuracy   : {decision_accuracy:.2f}%\n\n")

    f.write("Finding: The decision agent produced context-consistent ")
    f.write("routing decisions across the evaluated scenarios.\n\n")

    f.write("4. CONFIDENCE ANALYSIS\n")
    f.write("-" * 40 + "\n")
    f.write("Open-road confidence    : 85.33%\n")
    f.write("Blocked-road confidence : 94.00%\n\n")

    f.write("5. RISK ANALYSIS\n")
    f.write("-" * 40 + "\n")
    f.write("Open-road risk score    : 31.67\n")
    f.write("Blocked-road risk score : 91.25\n\n")

    f.write("6. OVERALL CONCLUSION\n")
    f.write("-" * 40 + "\n")
    f.write(
        "The experimental evaluation demonstrates that the "
        "AI-based campus navigation system can adapt its route "
        "selection according to changing campus context. "
        "The system responds to crowd density, detects blocked "
        "road conditions, performs dynamic rerouting, and "
        "provides explainable routing decisions.\n\n"
    )

    f.write(
        "The results support the effectiveness of the proposed "
        "context-aware multi-agent navigation architecture.\n"
    )


# ============================================================
# COMPLETE
# ============================================================

print("=" * 60)
print("STAGE 9 - FINAL VISUALIZATION COMPLETE")
print("=" * 60)

print("\nCharts generated:")
print("1. crowd_vs_route_cost.png")
print("2. rerouting_success.png")
print("3. decision_accuracy.png")
print("4. confidence_vs_risk.png")
print("5. crowd_cost_impact.png")

print("\nData generated:")
print("stage9_final_metrics.csv")

print("\nReport generated:")
print("stage9_final_evaluation.txt")

print("\nLOW -> HIGH route cost increase: {:.2f}%".format(increase))
print("Rerouting success rate: {:.2f}%".format(rerouting_success_rate))
print("Decision accuracy: {:.2f}%".format(decision_accuracy))

print("\nSTAGE 9 STEP 2 COMPLETE")
print("=" * 60)