import csv
import os
import statistics

# ============================================================
# STAGE 8 - EXPERIMENT 3
# EXPLAINABLE DECISION QUALITY ANALYSIS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


# ------------------------------------------------------------
# Stage 7 evaluation results
# ------------------------------------------------------------

scenarios = [
    {
        "name": "Low Crowd - Open",
        "crowd": "LOW",
        "blocked": "none",
        "confidence": 84,
        "risk": 10,
        "route_changed": False
    },
    {
        "name": "Medium Crowd - Open",
        "crowd": "MEDIUM",
        "blocked": "none",
        "confidence": 84,
        "risk": 35,
        "route_changed": False
    },
    {
        "name": "High Crowd - Open",
        "crowd": "HIGH",
        "blocked": "none",
        "confidence": 88,
        "risk": 50,
        "route_changed": False
    },
    {
        "name": "Low Crowd - Engineering Blocked",
        "crowd": "LOW",
        "blocked": "engineering-east",
        "confidence": 92,
        "risk": 70,
        "route_changed": True
    },
    {
        "name": "Medium Crowd - Engineering Blocked",
        "crowd": "MEDIUM",
        "blocked": "engineering-east",
        "confidence": 92,
        "risk": 95,
        "route_changed": True
    },
    {
        "name": "High Crowd - Engineering Blocked",
        "crowd": "HIGH",
        "blocked": "engineering-east",
        "confidence": 96,
        "risk": 100,
        "route_changed": True
    },
    {
        "name": "High Crowd - Different Destination",
        "crowd": "HIGH",
        "blocked": "none",
        "confidence": 88,
        "risk": 50,
        "route_changed": True
    },
    {
        "name": "High Crowd - Central Blocked",
        "crowd": "HIGH",
        "blocked": "central-approach",
        "confidence": 96,
        "risk": 100,
        "route_changed": True
    }
]


# ------------------------------------------------------------
# Decision quality rule
#
# For the core routing evaluation:
#
# 1. Blocked road  -> route should change
# 2. Open road     -> current route should be retained
#
# "Different Destination" is excluded because the destination
# itself changed, so a route change is expected for a different
# reason.
# ------------------------------------------------------------

core_scenarios = [
    s for s in scenarios
    if "Different Destination" not in s["name"]
]


# ------------------------------------------------------------
# Evaluate decision consistency
# ------------------------------------------------------------

evaluated = []

for s in core_scenarios:

    if s["blocked"] != "none":
        expected_change = True
    else:
        expected_change = False

    actual_change = s["route_changed"]

    correct = actual_change == expected_change

    evaluated.append({
        "name": s["name"],
        "crowd": s["crowd"],
        "blocked": s["blocked"],
        "confidence": s["confidence"],
        "risk": s["risk"],
        "expected_route_change": expected_change,
        "actual_route_change": actual_change,
        "decision_correct": correct
    })


# ------------------------------------------------------------
# Overall decision quality
# ------------------------------------------------------------

total = len(evaluated)

correct = sum(
    1 for s in evaluated
    if s["decision_correct"]
)

decision_accuracy = (
    correct / total * 100
    if total
    else 0
)


# ------------------------------------------------------------
# Confidence and risk statistics
# ------------------------------------------------------------

average_confidence = statistics.mean(
    s["confidence"] for s in evaluated
)

average_risk = statistics.mean(
    s["risk"] for s in evaluated
)


blocked_cases = [
    s for s in evaluated
    if s["blocked"] != "none"
]

open_cases = [
    s for s in evaluated
    if s["blocked"] == "none"
]


blocked_confidence = statistics.mean(
    s["confidence"] for s in blocked_cases
)

open_confidence = statistics.mean(
    s["confidence"] for s in open_cases
)

blocked_risk = statistics.mean(
    s["risk"] for s in blocked_cases
)

open_risk = statistics.mean(
    s["risk"] for s in open_cases
)


# ------------------------------------------------------------
# Save CSV
# ------------------------------------------------------------

csv_path = os.path.join(
    DATA_DIR,
    "decision_quality_analysis.csv"
)

with open(
    csv_path,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "Scenario",
        "Crowd",
        "Blocked Path",
        "Confidence",
        "Risk Score",
        "Expected Route Change",
        "Actual Route Change",
        "Decision Correct"
    ])

    for s in evaluated:

        writer.writerow([
            s["name"],
            s["crowd"],
            s["blocked"],
            s["confidence"],
            s["risk"],
            s["expected_route_change"],
            s["actual_route_change"],
            s["decision_correct"]
        ])


# ------------------------------------------------------------
# Generate report
# ------------------------------------------------------------

report_path = os.path.join(
    REPORT_DIR,
    "experiment3_decision_quality.txt"
)

with open(
    report_path,
    "w",
    encoding="utf-8"
) as f:

    f.write("STAGE 8 - EXPERIMENT 3\n")
    f.write("EXPLAINABLE DECISION QUALITY ANALYSIS\n")
    f.write("=" * 60 + "\n\n")

    f.write("Objective:\n")
    f.write(
        "Evaluate whether the Explainable Decision Agent "
        "makes routing decisions consistent with the current "
        "campus context.\n\n"
    )

    f.write("Decision Rule:\n")
    f.write(
        "Blocked road -> alternative route should be selected.\n"
    )
    f.write(
        "Open road -> current route should be retained.\n"
    )
    f.write(
        "Different-destination scenario excluded because the "
        "destination itself changes.\n\n"
    )

    f.write("Overall Results:\n")
    f.write(
        f"Evaluated scenarios : {total}\n"
    )
    f.write(
        f"Correct decisions   : {correct}\n"
    )
    f.write(
        f"Decision accuracy   : {decision_accuracy:.2f}%\n"
    )
    f.write(
        f"Average confidence  : {average_confidence:.2f}%\n"
    )
    f.write(
        f"Average risk score  : {average_risk:.2f}\n\n"
    )

    f.write("Context Comparison:\n")
    f.write(
        f"Open-road average confidence    : "
        f"{open_confidence:.2f}%\n"
    )
    f.write(
        f"Blocked-road average confidence : "
        f"{blocked_confidence:.2f}%\n"
    )
    f.write(
        f"Open-road average risk          : "
        f"{open_risk:.2f}\n"
    )
    f.write(
        f"Blocked-road average risk       : "
        f"{blocked_risk:.2f}\n\n"
    )

    f.write("Scenario Decisions:\n")

    for s in evaluated:

        result = (
            "CORRECT"
            if s["decision_correct"]
            else "INCORRECT"
        )

        f.write(
            f"{s['name']} | "
            f"Expected={s['expected_route_change']} | "
            f"Actual={s['actual_route_change']} | "
            f"{result}\n"
        )

    f.write("\nConclusion:\n")
    f.write(
        "The Explainable Decision Agent produced decisions "
        "consistent with the defined context-aware routing "
        "rules for all evaluated scenarios. Blocked roads "
        "resulted in route changes, while open roads retained "
        "the existing route. This demonstrates decision "
        "consistency within the evaluated scenarios.\n"
    )


# ------------------------------------------------------------
# Console output
# ------------------------------------------------------------

print()
print("=" * 60)
print("STAGE 8 - EXPERIMENT 3")
print("EXPLAINABLE DECISION QUALITY ANALYSIS")
print("=" * 60)

print()

print("Decision Evaluation:")
print(f"Evaluated scenarios : {total}")
print(f"Correct decisions   : {correct}")
print(f"Decision accuracy   : {decision_accuracy:.2f}%")

print()

print("Confidence:")
print(f"Overall average     : {average_confidence:.2f}%")
print(f"Open-road average   : {open_confidence:.2f}%")
print(f"Blocked-road average: {blocked_confidence:.2f}%")

print()

print("Risk:")
print(f"Overall average     : {average_risk:.2f}")
print(f"Open-road average   : {open_risk:.2f}")
print(f"Blocked-road average: {blocked_risk:.2f}")

print()

print("Conclusion:")
print(
    "The Explainable Decision Agent produced context-consistent "
    "routing decisions across the evaluated scenarios."
)

print()

print("Files generated:")
print(csv_path)
print(report_path)

print()

print("EXPERIMENT 3 COMPLETE")
print("=" * 60)