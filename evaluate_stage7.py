import json
import csv
import urllib.request

API_URL = "http://127.0.0.1:8000/api/route"

scenarios = [
    {
        "name": "Low Crowd - Open",
        "start": "engineering",
        "destination": "auditorium",
        "crowd": "LOW",
        "blocked_path": "none",
        "active_area": "central"
    },
    {
        "name": "Medium Crowd - Open",
        "start": "engineering",
        "destination": "auditorium",
        "crowd": "MEDIUM",
        "blocked_path": "none",
        "active_area": "central"
    },
    {
        "name": "High Crowd - Open",
        "start": "engineering",
        "destination": "auditorium",
        "crowd": "HIGH",
        "blocked_path": "none",
        "active_area": "central"
    },
    {
        "name": "Low Crowd - Engineering Road Blocked",
        "start": "engineering",
        "destination": "auditorium",
        "crowd": "LOW",
        "blocked_path": "engineering-east",
        "active_area": "central"
    },
    {
        "name": "Medium Crowd - Engineering Road Blocked",
        "start": "engineering",
        "destination": "auditorium",
        "crowd": "MEDIUM",
        "blocked_path": "engineering-east",
        "active_area": "central"
    },
    {
        "name": "High Crowd - Engineering Road Blocked",
        "start": "engineering",
        "destination": "auditorium",
        "crowd": "HIGH",
        "blocked_path": "engineering-east",
        "active_area": "central"
    },
    {
        "name": "High Crowd - Different Destination",
        "start": "engineering",
        "destination": "vidyalayam",
        "crowd": "HIGH",
        "blocked_path": "none",
        "active_area": "central"
    },
    {
        "name": "High Crowd - Central Road Blocked",
        "start": "engineering",
        "destination": "auditorium",
        "crowd": "HIGH",
        "blocked_path": "central-approach",
        "active_area": "central"
    }
]


def call_api(data):
    body = json.dumps(data).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def get_decision(data):
    decision = data.get("explanation", {})

    if not decision:
        decision = data.get("decision", {})

    return decision


results = []

baseline_route = None

print("\n==============================================")
print(" AI CAMPUS NAVIGATION - STAGE 7 EVALUATION")
print("==============================================\n")

for index, scenario in enumerate(scenarios, start=1):

    print(f"Running Scenario {index}: {scenario['name']}")

    try:
        response = call_api({
            "start": scenario["start"],
            "destination": scenario["destination"],
            "crowd": scenario["crowd"],
            "blocked_path": scenario["blocked_path"],
            "active_area": scenario["active_area"]
        })

        route = response.get("route", [])
        cost = response.get("cost")

        decision = get_decision(response)

        action = decision.get("action")
        confidence = decision.get("confidence")
        risk_score = decision.get("risk_score")

        route_found = response.get(
            "route_found",
            bool(route)
        )

        # First scenario becomes the baseline.
        if baseline_route is None:
            baseline_route = route

        route_changed = route != baseline_route

        results.append({
            "Scenario": scenario["name"],
            "Crowd": scenario["crowd"],
            "Blocked Path": scenario["blocked_path"],
            "Route Found": route_found,
            "Route Cost": cost,
            "Decision": action,
            "Confidence": confidence,
            "Risk Score": risk_score,
            "Route Changed": route_changed
        })

        print(f"  Route Found : {route_found}")
        print(f"  Cost        : {cost}")
        print(f"  Decision    : {action}")
        print(f"  Confidence  : {confidence}")
        print(f"  Risk Score  : {risk_score}")
        print(f"  Route Nodes : {len(route)}")
        print()

    except Exception as e:
        print(f"  ERROR: {e}\n")

        results.append({
            "Scenario": scenario["name"],
            "Crowd": scenario["crowd"],
            "Blocked Path": scenario["blocked_path"],
            "Route Found": False,
            "Route Cost": "",
            "Decision": "ERROR",
            "Confidence": "",
            "Risk Score": "",
            "Route Changed": ""
        })


output_file = "evaluation_results.csv"

fields = [
    "Scenario",
    "Crowd",
    "Blocked Path",
    "Route Found",
    "Route Cost",
    "Decision",
    "Confidence",
    "Risk Score",
    "Route Changed"
]

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(results)


print("==============================================")
print(" EVALUATION COMPLETE")
print("==============================================")
print(f"\nResults saved to: {output_file}\n")

successful = sum(
    1 for r in results
    if r["Route Found"] is True
)

print(f"Successful routes: {successful}/{len(results)}")