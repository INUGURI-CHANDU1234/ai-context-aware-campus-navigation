import csv
import os

# ============================================================
# STAGE 8 - EXPERIMENT 2
# BLOCKED ROAD & REROUTING ANALYSIS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


# ------------------------------------------------------------
# Stage 7 actual evaluation results
# ------------------------------------------------------------

scenarios = [
    {
        "name": "Low Crowd - Open",
        "crowd": "LOW",
        "blocked": "none",
        "cost": 308.00,
        "route_changed": False
    },
    {
        "name": "Medium Crowd - Open",
        "crowd": "MEDIUM",
        "blocked": "none",
        "cost": 455.64,
        "route_changed": False
    },
    {
        "name": "High Crowd - Open",
        "crowd": "HIGH",
        "blocked": "none",
        "cost": 619.70,
        "route_changed": False
    },
    {
        "name": "Low Crowd - Engineering Blocked",
        "crowd": "LOW",
        "blocked": "engineering-east",
        "cost": 316.00,
        "route_changed": True
    },
    {
        "name": "Medium Crowd - Engineering Blocked",
        "crowd": "MEDIUM",
        "blocked": "engineering-east",
        "cost": 471.75,
        "route_changed": True
    },
    {
        "name": "High Crowd - Engineering Blocked",
        "crowd": "HIGH",
        "blocked": "engineering-east",
        "cost": 644.79,
        "route_changed": True
    },
    {
        "name": "High Crowd - Different Destination",
        "crowd": "HIGH",
        "blocked": "none",
        "cost": 309.15,
        "route_changed": True
    },
    {
        "name": "High Crowd - Central Blocked",
        "crowd": "HIGH",
        "blocked": "central-approach",
        "cost": 1135.90,
        "route_changed": True
    }
]


# ------------------------------------------------------------
# Identify blocked-road scenarios
# ------------------------------------------------------------

blocked_scenarios = [
    s for s in scenarios
    if s["blocked"] != "none"
]

blocked_count = len(blocked_scenarios)

rerouted_count = sum(
    1 for s in blocked_scenarios
    if s["route_changed"]
)

if blocked_count:
    reroute_success_rate = (
        rerouted_count / blocked_count
    ) * 100
else:
    reroute_success_rate = 0


# ------------------------------------------------------------
# Calculate additional cost
#
# Compare each blocked scenario with the corresponding
# open-road scenario having the same crowd level.
# ------------------------------------------------------------

open_costs = {}

for s in scenarios:
    if s["blocked"] == "none":
        if "Different Destination" not in s["name"]:
            open_costs[s["crowd"]] = s["cost"]


for s in blocked_scenarios:
    baseline = open_costs.get(s["crowd"])

    if baseline is not None:
        s["baseline_cost"] = baseline
        s["additional_cost"] = round(
            s["cost"] - baseline,
            2
        )
    else:
        s["baseline_cost"] = None
        s["additional_cost"] = None


# ------------------------------------------------------------
# Save experiment data
# ------------------------------------------------------------

csv_path = os.path.join(
    DATA_DIR,
    "rerouting_analysis.csv"
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
        "Baseline Cost",
        "Rerouted Cost",
        "Additional Cost",
        "Route Changed"
    ])

    for s in blocked_scenarios:
        writer.writerow([
            s["name"],
            s["crowd"],
            s["blocked"],
            s["baseline_cost"],
            s["cost"],
            s["additional_cost"],
            s["route_changed"]
        ])


# ------------------------------------------------------------
# Generate report
# ------------------------------------------------------------

report_path = os.path.join(
    REPORT_DIR,
    "experiment2_rerouting.txt"
)

with open(
    report_path,
    "w",
    encoding="utf-8"
) as f:

    f.write("STAGE 8 - EXPERIMENT 2\n")
    f.write("BLOCKED ROAD & REROUTING ANALYSIS\n")
    f.write("=" * 60 + "\n\n")

    f.write("Objective:\n")
    f.write(
        "Evaluate whether the multi-agent navigation system "
        "can detect blocked pedestrian roads and successfully "
        "select alternative routes.\n\n"
    )

    f.write("Results:\n")
    f.write(
        f"Blocked-road scenarios : {blocked_count}\n"
    )

    f.write(
        f"Successful reroutes    : {rerouted_count}\n"
    )

    f.write(
        f"Rerouting success rate : "
        f"{reroute_success_rate:.2f}%\n\n"
    )

    f.write("Scenario Analysis:\n")

    for s in blocked_scenarios:
        f.write(
            f"{s['name']} | "
            f"Baseline={s['baseline_cost']} | "
            f"Rerouted={s['cost']} | "
            f"Additional={s['additional_cost']} | "
            f"Changed={s['route_changed']}\n"
        )

    f.write("\nConclusion:\n")
    f.write(
        "All blocked-road scenarios were successfully "
        "rerouted. The 100% rerouting success rate indicates "
        "that the navigation system can adapt when a pedestrian "
        "road becomes unavailable. The additional route cost "
        "quantifies the navigation penalty caused by road "
        "blockage.\n"
    )


# ------------------------------------------------------------
# Console output
# ------------------------------------------------------------

print()
print("=" * 60)
print("STAGE 8 - EXPERIMENT 2")
print("BLOCKED ROAD & REROUTING ANALYSIS")
print("=" * 60)

print()

print("Blocked-road scenarios :", blocked_count)
print("Successful reroutes    :", rerouted_count)
print(
    f"Rerouting success rate : "
    f"{reroute_success_rate:.2f}%"
)

print()
print("Additional Route Cost:")

for s in blocked_scenarios:
    print(
        f"{s['name']}: "
        f"+{s['additional_cost']:.2f} cost units"
    )

print()
print("Conclusion:")
print(
    "The system successfully rerouted all blocked-road "
    "scenarios, demonstrating adaptive navigation."
)

print()
print("Files generated:")
print(csv_path)
print(report_path)

print()
print("EXPERIMENT 2 COMPLETE")
print("=" * 60)