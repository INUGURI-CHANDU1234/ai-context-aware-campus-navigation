import csv
import matplotlib.pyplot as plt

# Read evaluation results
with open("evaluation_results.csv", "r", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))


# -----------------------------------------
# 1. Route Cost vs Crowd Level
# -----------------------------------------

crowds = ["LOW", "MEDIUM", "HIGH"]

crowd_costs = []

for crowd in crowds:
    values = [
        float(row["Route Cost"])
        for row in rows
        if row["Crowd"].upper() == crowd
    ]

    crowd_costs.append(sum(values) / len(values))


plt.figure(figsize=(8, 5))
plt.bar(crowds, crowd_costs)

plt.title("Average Route Cost vs Crowd Level")
plt.xlabel("Crowd Level")
plt.ylabel("Average Route Cost")

plt.tight_layout()
plt.savefig("crowd_vs_route_cost.png", dpi=300)
plt.close()


# -----------------------------------------
# 2. Route Cost by Scenario
# -----------------------------------------

scenario_names = [
    row["Scenario"]
    for row in rows
]

scenario_costs = [
    float(row["Route Cost"])
    for row in rows
]


plt.figure(figsize=(10, 6))
plt.bar(range(len(rows)), scenario_costs)

plt.title("Route Cost Across Evaluation Scenarios")
plt.xlabel("Scenario")
plt.ylabel("Route Cost")

plt.xticks(
    range(len(rows)),
    [f"S{i+1}" for i in range(len(rows))]
)

plt.tight_layout()
plt.savefig("scenario_route_cost.png", dpi=300)
plt.close()


# -----------------------------------------
# 3. Confidence vs Risk
# -----------------------------------------

confidence = [
    float(row["Confidence"])
    for row in rows
]

risk = [
    float(row["Risk Score"])
    for row in rows
]


plt.figure(figsize=(8, 5))

plt.scatter(confidence, risk)

plt.title("Decision Confidence vs Risk Score")
plt.xlabel("Decision Confidence (%)")
plt.ylabel("Risk Score")

plt.tight_layout()
plt.savefig("confidence_vs_risk.png", dpi=300)
plt.close()


# -----------------------------------------
# 4. Route Success Rate
# -----------------------------------------

successful = sum(
    row["Route Found"].lower() == "true"
    for row in rows
)

failed = len(rows) - successful


plt.figure(figsize=(6, 6))

plt.pie(
    [successful, failed],
    labels=["Successful Routes", "Failed Routes"],
    autopct="%1.1f%%"
)

plt.title("Route Success Rate")

plt.tight_layout()
plt.savefig("route_success_rate.png", dpi=300)
plt.close()


print()
print("=" * 50)
print("STAGE 7C - VISUALIZATION COMPLETE")
print("=" * 50)

print()
print("Generated graphs:")

print("1. crowd_vs_route_cost.png")
print("2. scenario_route_cost.png")
print("3. confidence_vs_risk.png")
print("4. route_success_rate.png")

print()
print("All graphs saved in the project root.")
print()