import csv
import os

# ============================================================
# STAGE 8 - CONSOLIDATED EVALUATION
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


# ------------------------------------------------------------
# Experiment 1 - Crowd Impact
# ------------------------------------------------------------

crowd_low = 308.00
crowd_medium = 455.64
crowd_high = 619.70

low_to_high = 101.20


# ------------------------------------------------------------
# Experiment 2 - Rerouting
# ------------------------------------------------------------

blocked_scenarios = 4
successful_reroutes = 4
reroute_success = 100.00

additional_costs = [
    8.00,
    16.11,
    25.09,
    516.20
]


# ------------------------------------------------------------
# Experiment 3 - Decision Quality
# ------------------------------------------------------------

evaluated_scenarios = 7
correct_decisions = 7
decision_accuracy = 100.00

overall_confidence = 90.29
open_confidence = 85.33
blocked_confidence = 94.00

overall_risk = 65.71
open_risk = 31.67
blocked_risk = 91.25


# ------------------------------------------------------------
# Create consolidated CSV
# ------------------------------------------------------------

csv_path = os.path.join(
    DATA_DIR,
    "stage8_consolidated_results.csv"
)

rows = [
    ["Experiment", "Metric", "Value"],

    [
        "Experiment 1 - Crowd Impact",
        "LOW average route cost",
        crowd_low
    ],
    [
        "Experiment 1 - Crowd Impact",
        "MEDIUM average route cost",
        crowd_medium
    ],
    [
        "Experiment 1 - Crowd Impact",
        "HIGH average route cost",
        crowd_high
    ],
    [
        "Experiment 1 - Crowd Impact",
        "LOW to HIGH cost increase (%)",
        low_to_high
    ],

    [
        "Experiment 2 - Rerouting",
        "Blocked-road scenarios",
        blocked_scenarios
    ],
    [
        "Experiment 2 - Rerouting",
        "Successful reroutes",
        successful_reroutes
    ],
    [
        "Experiment 2 - Rerouting",
        "Rerouting success rate (%)",
        reroute_success
    ],

    [
        "Experiment 3 - Decision Quality",
        "Evaluated scenarios",
        evaluated_scenarios
    ],
    [
        "Experiment 3 - Decision Quality",
        "Correct decisions",
        correct_decisions
    ],
    [
        "Experiment 3 - Decision Quality",
        "Decision accuracy (%)",
        decision_accuracy
    ],
    [
        "Experiment 3 - Decision Quality",
        "Overall confidence (%)",
        overall_confidence
    ],
    [
        "Experiment 3 - Decision Quality",
        "Open-road confidence (%)",
        open_confidence
    ],
    [
        "Experiment 3 - Decision Quality",
        "Blocked-road confidence (%)",
        blocked_confidence
    ],
    [
        "Experiment 3 - Decision Quality",
        "Overall risk score",
        overall_risk
    ],
    [
        "Experiment 3 - Decision Quality",
        "Open-road risk score",
        open_risk
    ],
    [
        "Experiment 3 - Decision Quality",
        "Blocked-road risk score",
        blocked_risk
    ]
]

with open(
    csv_path,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)
    writer.writerows(rows)


# ------------------------------------------------------------
# Generate consolidated report
# ------------------------------------------------------------

report_path = os.path.join(
    REPORT_DIR,
    "stage8_consolidated_evaluation.txt"
)

with open(
    report_path,
    "w",
    encoding="utf-8"
) as f:

    f.write("=" * 70 + "\n")
    f.write("STAGE 8 - CONSOLIDATED EVALUATION REPORT\n")
    f.write("AI-BASED CONTEXT-AWARE CAMPUS NAVIGATION SYSTEM\n")
    f.write("=" * 70 + "\n\n")

    # --------------------------------------------------------
    # Experiment 1
    # --------------------------------------------------------

    f.write("EXPERIMENT 1 - CROWD IMPACT ANALYSIS\n")
    f.write("-" * 70 + "\n")

    f.write(
        f"LOW crowd average route cost    : {crowd_low:.2f}\n"
    )

    f.write(
        f"MEDIUM crowd average route cost : {crowd_medium:.2f}\n"
    )

    f.write(
        f"HIGH crowd average route cost   : {crowd_high:.2f}\n"
    )

    f.write(
        f"LOW to HIGH increase            : {low_to_high:.2f}%\n\n"
    )

    f.write(
        "Finding: Increasing campus crowd density increases "
        "route cost, demonstrating context-aware adaptation.\n\n"
    )


    # --------------------------------------------------------
    # Experiment 2
    # --------------------------------------------------------

    f.write("EXPERIMENT 2 - BLOCKED ROAD & REROUTING\n")
    f.write("-" * 70 + "\n")

    f.write(
        f"Blocked-road scenarios : {blocked_scenarios}\n"
    )

    f.write(
        f"Successful reroutes    : {successful_reroutes}\n"
    )

    f.write(
        f"Rerouting success rate : {reroute_success:.2f}%\n\n"
    )

    f.write("Additional route costs:\n")

    f.write(
        f"Engineering + LOW    : +{additional_costs[0]:.2f}\n"
    )

    f.write(
        f"Engineering + MEDIUM : +{additional_costs[1]:.2f}\n"
    )

    f.write(
        f"Engineering + HIGH   : +{additional_costs[2]:.2f}\n"
    )

    f.write(
        f"Central blockage     : +{additional_costs[3]:.2f}\n\n"
    )

    f.write(
        "Finding: All blocked-road scenarios were successfully "
        "rerouted, demonstrating adaptive navigation.\n\n"
    )


    # --------------------------------------------------------
    # Experiment 3
    # --------------------------------------------------------

    f.write("EXPERIMENT 3 - EXPLAINABLE DECISION QUALITY\n")
    f.write("-" * 70 + "\n")

    f.write(
        f"Evaluated scenarios : {evaluated_scenarios}\n"
    )

    f.write(
        f"Correct decisions   : {correct_decisions}\n"
    )

    f.write(
        f"Decision accuracy   : {decision_accuracy:.2f}%\n"
    )

    f.write(
        f"Overall confidence  : {overall_confidence:.2f}%\n"
    )

    f.write(
        f"Open-road confidence: {open_confidence:.2f}%\n"
    )

    f.write(
        f"Blocked confidence  : {blocked_confidence:.2f}%\n"
    )

    f.write(
        f"Overall risk        : {overall_risk:.2f}\n"
    )

    f.write(
        f"Open-road risk      : {open_risk:.2f}\n"
    )

    f.write(
        f"Blocked-road risk   : {blocked_risk:.2f}\n\n"
    )

    f.write(
        "Finding: The Explainable Decision Agent produced "
        "context-consistent decisions for all evaluated cases.\n\n"
    )


    # --------------------------------------------------------
    # Overall conclusion
    # --------------------------------------------------------

    f.write("=" * 70 + "\n")
    f.write("OVERALL STAGE 8 CONCLUSION\n")
    f.write("=" * 70 + "\n\n")

    f.write(
        "The Stage 8 evaluation demonstrates three important "
        "properties of the proposed AI-based campus navigation "
        "system:\n\n"
    )

    f.write(
        "1. CONTEXT ADAPTATION\n"
        "   Route cost changes according to campus crowd density.\n\n"
    )

    f.write(
        "2. DYNAMIC REROUTING\n"
        "   The system successfully identifies blocked roads "
        "and selects alternative pedestrian routes.\n\n"
    )

    f.write(
        "3. EXPLAINABLE DECISION MAKING\n"
        "   The decision agent produces context-consistent "
        "routing decisions with measurable confidence and risk.\n\n"
    )

    f.write(
        "Overall, the evaluation supports the feasibility of "
        "multi-agent, context-aware navigation for dynamic "
        "campus environments.\n"
    )


# ------------------------------------------------------------
# Console output
# ------------------------------------------------------------

print()
print("=" * 70)
print("STAGE 8 - CONSOLIDATED EVALUATION")
print("=" * 70)

print()
print("EXPERIMENT 1 - CROWD IMPACT")
print(f"LOW    : {crowd_low:.2f}")
print(f"MEDIUM : {crowd_medium:.2f}")
print(f"HIGH   : {crowd_high:.2f}")
print(f"LOW -> HIGH increase : {low_to_high:.2f}%")

print()
print("EXPERIMENT 2 - REROUTING")
print(f"Blocked scenarios : {blocked_scenarios}")
print(f"Successful reroutes : {successful_reroutes}")
print(f"Success rate : {reroute_success:.2f}%")

print()
print("EXPERIMENT 3 - DECISION QUALITY")
print(f"Evaluated scenarios : {evaluated_scenarios}")
print(f"Correct decisions : {correct_decisions}")
print(f"Decision accuracy : {decision_accuracy:.2f}%")

print()
print("OVERALL FINDING")
print(
    "The Stage 8 experiments demonstrate context adaptation, "
    "dynamic rerouting, and explainable decision making."
)

print()
print("Files generated:")
print(csv_path)
print(report_path)

print()
print("STAGE 8 CONSOLIDATION COMPLETE")
print("=" * 70)