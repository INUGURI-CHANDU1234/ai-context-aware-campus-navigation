import csv
from collections import defaultdict

INPUT_FILE = "evaluation_results.csv"
OUTPUT_FILE = "evaluation_summary.csv"


def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


# ----------------------------------------
# Read evaluation results
# ----------------------------------------

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))


total = len(rows)

successful = sum(
    1 for row in rows
    if row["Route Found"].strip().lower() == "true"
)

blocked_rows = [
    row for row in rows
    if row["Blocked Path"].strip().lower() != "none"
]

blocked_success = sum(
    1 for row in blocked_rows
    if row["Route Found"].strip().lower() == "true"
)

costs = [
    to_float(row["Route Cost"])
    for row in rows
    if row["Route Cost"].strip()
]

confidences = [
    to_float(row["Confidence"])
    for row in rows
    if row["Confidence"].strip()
]

risks = [
    to_float(row["Risk Score"])
    for row in rows
    if row["Risk Score"].strip()
]


# ----------------------------------------
# Basic metrics
# ----------------------------------------

route_success_rate = (
    successful / total * 100
    if total else 0
)

blocked_success_rate = (
    blocked_success / len(blocked_rows) * 100
    if blocked_rows else 0
)

average_cost = (
    sum(costs) / len(costs)
    if costs else 0
)

average_confidence = (
    sum(confidences) / len(confidences)
    if confidences else 0
)

average_risk = (
    sum(risks) / len(risks)
    if risks else 0
)


# ----------------------------------------
# Crowd-wise analysis
# ----------------------------------------

crowd_data = defaultdict(list)

for row in rows:
    crowd = row["Crowd"].strip().upper()

    crowd_data[crowd].append(
        to_float(row["Route Cost"])
    )


crowd_average = {}

for crowd, values in crowd_data.items():
    if values:
        crowd_average[crowd] = sum(values) / len(values)


# ----------------------------------------
# Blocked-road decision analysis
# ----------------------------------------

blocked_recalculate = sum(
    1
    for row in blocked_rows
    if "lowest-cost available" in row["Decision"].lower()
    or "recalculate" in row["Decision"].lower()
)


blocked_reroute_rate = (
    blocked_recalculate / len(blocked_rows) * 100
    if blocked_rows else 0
)


# ----------------------------------------
# Save summary
# ----------------------------------------

summary = [
    ["Metric", "Value"],
    ["Total Scenarios", total],
    ["Successful Routes", successful],
    ["Route Success Rate (%)", round(route_success_rate, 2)],
    ["Average Route Cost", round(average_cost, 2)],
    ["Average Confidence (%)", round(average_confidence, 2)],
    ["Average Risk Score", round(average_risk, 2)],
    ["Blocked Road Scenarios", len(blocked_rows)],
    ["Blocked Road Successful Routes", blocked_success],
    ["Blocked Road Success Rate (%)", round(blocked_success_rate, 2)],
    ["Blocked Road Reroute Decisions (%)", round(blocked_reroute_rate, 2)],
    ["LOW Crowd Average Cost", round(crowd_average.get("LOW", 0), 2)],
    ["MEDIUM Crowd Average Cost", round(crowd_average.get("MEDIUM", 0), 2)],
    ["HIGH Crowd Average Cost", round(crowd_average.get("HIGH", 0), 2)],
]


with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)
    writer.writerows(summary)


# ----------------------------------------
# Display results
# ----------------------------------------

print()
print("=" * 55)
print("       STAGE 7B - EVALUATION ANALYSIS")
print("=" * 55)

print(f"\nTotal scenarios             : {total}")
print(f"Successful routes           : {successful}")
print(f"Route success rate          : {route_success_rate:.2f}%")
print(f"Average route cost          : {average_cost:.2f}")
print(f"Average confidence          : {average_confidence:.2f}%")
print(f"Average risk score          : {average_risk:.2f}")

print()
print("BLOCKED ROAD ANALYSIS")
print("-" * 55)
print(f"Blocked-road scenarios      : {len(blocked_rows)}")
print(f"Successful blocked routes   : {blocked_success}")
print(f"Blocked-road success rate   : {blocked_success_rate:.2f}%")
print(f"Reroute decisions           : {blocked_recalculate}")
print(f"Reroute decision rate       : {blocked_reroute_rate:.2f}%")

print()
print("CROWD ADAPTATION")
print("-" * 55)

for crowd in ["LOW", "MEDIUM", "HIGH"]:
    if crowd in crowd_average:
        print(
            f"{crowd:<10} average route cost : "
            f"{crowd_average[crowd]:.2f}"
        )

print()
print("=" * 55)
print(f"Summary saved to: {OUTPUT_FILE}")
print("=" * 55)
print()