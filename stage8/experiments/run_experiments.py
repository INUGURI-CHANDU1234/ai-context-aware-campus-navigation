import csv
import os
import statistics
import matplotlib.pyplot as plt

# ============================================================
# STAGE 8 - EXPERIMENT 1
# Crowd Impact Analysis
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
CHART_DIR = os.path.join(BASE_DIR, "charts")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(CHART_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


# ------------------------------------------------------------
# Actual Stage 7 evaluation results
# ------------------------------------------------------------

scenarios = [
    {
        "scenario": "Low Crowd - Open",
        "crowd": "LOW",
        "blocked": "none",
        "cost": 308.00,
        "confidence": 84,
        "risk": 10,
        "route_changed": False
    },
    {
        "scenario": "Medium Crowd - Open",
        "crowd": "MEDIUM",
        "blocked": "none",
        "cost": 455.64,
        "confidence": 84,
        "risk": 35,
        "route_changed": False
    },
    {
        "scenario": "High Crowd - Open",
        "crowd": "HIGH",
        "blocked": "none",
        "cost": 619.70,
        "confidence": 88,
        "risk": 50,
        "route_changed": False
    },
    {
        "scenario": "Low Crowd - Engineering Blocked",
        "crowd": "LOW",
        "blocked": "engineering-east",
        "cost": 316.00,
        "confidence": 92,
        "risk": 70,
        "route_changed": True
    },
    {
        "scenario": "Medium Crowd - Engineering Blocked",
        "crowd": "MEDIUM",
        "blocked": "engineering-east",
        "cost": 471.75,
        "confidence": 92,
        "risk": 95,
        "route_changed": True
    },
    {
        "scenario": "High Crowd - Engineering Blocked",
        "crowd": "HIGH",
        "blocked": "engineering-east",
        "cost": 644.79,
        "confidence": 96,
        "risk": 100,
        "route_changed": True
    },
    {
        "scenario": "High Crowd - Different Destination",
        "crowd": "HIGH",
        "blocked": "none",
        "cost": 309.15,
        "confidence": 88,
        "risk": 50,
        "route_changed": True
    },
    {
        "scenario": "High Crowd - Central Blocked",
        "crowd": "HIGH",
        "blocked": "central-approach",
        "cost": 1135.90,
        "confidence": 96,
        "risk": 100,
        "route_changed": True
    }
]


# ------------------------------------------------------------
# 1. Filter open-road scenarios
# ------------------------------------------------------------

open_routes = [
    s for s in scenarios
    if s["blocked"] == "none"
    and "Different Destination" not in s["scenario"]
]

crowd_order = ["LOW", "MEDIUM", "HIGH"]

crowd_costs = {}

for crowd in crowd_order:
    values = [
        s["cost"]
        for s in open_routes
        if s["crowd"] == crowd
    ]

    if values:
        crowd_costs[crowd] = round(statistics.mean(values), 2)


# ------------------------------------------------------------
# 2. Calculate percentage increase
# ------------------------------------------------------------

low_cost = crowd_costs["LOW"]
medium_cost = crowd_costs["MEDIUM"]
high_cost = crowd_costs["HIGH"]

low_to_medium = ((medium_cost - low_cost) / low_cost) * 100
medium_to_high = ((high_cost - medium_cost) / medium_cost) * 100
low_to_high = ((high_cost - low_cost) / low_cost) * 100


# ------------------------------------------------------------
# 3. Save experiment CSV
# ------------------------------------------------------------

experiment_csv = os.path.join(
    DATA_DIR,
    "crowd_impact_analysis.csv"
)

with open(experiment_csv, "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Crowd Level",
        "Average Route Cost"
    ])

    for crowd in crowd_order:
        writer.writerow([
            crowd,
            crowd_costs[crowd]
        ])

    writer.writerow([])
    writer.writerow([
        "LOW to MEDIUM Increase (%)",
        round(low_to_medium, 2)
    ])

    writer.writerow([
        "MEDIUM to HIGH Increase (%)",
        round(medium_to_high, 2)
    ])

    writer.writerow([
        "LOW to HIGH Increase (%)",
        round(low_to_high, 2)
    ])


# ------------------------------------------------------------
# 4. Generate chart
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    crowd_order,
    [crowd_costs[c] for c in crowd_order],
    marker="o",
    linewidth=2
)

plt.title("Impact of Crowd Density on Route Cost")
plt.xlabel("Campus Crowd Level")
plt.ylabel("Average Route Cost")
plt.grid(True, alpha=0.3)

for crowd in crowd_order:
    plt.annotate(
        f"{crowd_costs[crowd]:.2f}",
        (crowd, crowd_costs[crowd]),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center"
    )

chart_path = os.path.join(
    CHART_DIR,
    "crowd_impact_route_cost.png"
)

plt.tight_layout()
plt.savefig(chart_path, dpi=150)
plt.close()


# ------------------------------------------------------------
# 5. Generate experiment report
# ------------------------------------------------------------

report_path = os.path.join(
    REPORT_DIR,
    "experiment1_crowd_impact.txt"
)

with open(report_path, "w", encoding="utf-8") as f:

    f.write("STAGE 8 - EXPERIMENT 1\n")
    f.write("CROWD IMPACT ANALYSIS\n")
    f.write("=" * 55 + "\n\n")

    f.write("Objective:\n")
    f.write(
        "Evaluate whether increasing campus crowd density "
        "causes the navigation system to increase route cost.\n\n"
    )

    f.write("Results:\n")
    f.write(f"LOW crowd average cost    : {low_cost:.2f}\n")
    f.write(f"MEDIUM crowd average cost : {medium_cost:.2f}\n")
    f.write(f"HIGH crowd average cost   : {high_cost:.2f}\n\n")

    f.write("Percentage Changes:\n")
    f.write(
        f"LOW -> MEDIUM : {low_to_medium:.2f}% increase\n"
    )
    f.write(
        f"MEDIUM -> HIGH : {medium_to_high:.2f}% increase\n"
    )
    f.write(
        f"LOW -> HIGH : {low_to_high:.2f}% increase\n\n"
    )

    f.write("Conclusion:\n")
    f.write(
        "The experiment demonstrates that the navigation system "
        "adapts route cost according to campus crowd density. "
        "As crowd density increases from LOW to MEDIUM to HIGH, "
        "the average route cost increases accordingly. "
        "This supports the context-aware routing objective of "
        "the proposed multi-agent campus navigation system.\n"
    )


# ------------------------------------------------------------
# 6. Console output
# ------------------------------------------------------------

print()
print("=" * 60)
print("STAGE 8 - EXPERIMENT 1")
print("CROWD IMPACT ANALYSIS")
print("=" * 60)

print()
print("Average Route Cost:")
print(f"LOW     : {low_cost:.2f}")
print(f"MEDIUM  : {medium_cost:.2f}")
print(f"HIGH    : {high_cost:.2f}")

print()
print("Percentage Increase:")
print(f"LOW -> MEDIUM  : {low_to_medium:.2f}%")
print(f"MEDIUM -> HIGH : {medium_to_high:.2f}%")
print(f"LOW -> HIGH    : {low_to_high:.2f}%")

print()
print("Conclusion:")
print(
    "Higher campus crowd density results in higher route cost, "
    "demonstrating context-aware route adaptation."
)

print()
print("Files generated:")
print(experiment_csv)
print(chart_path)
print(report_path)

print()
print("EXPERIMENT 1 COMPLETE")
print("=" * 60)