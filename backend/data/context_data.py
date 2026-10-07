"""Structured campus context data layer.

The demo uses deterministic snapshots so the system is reproducible. In a real
deployment, this module can be replaced by database, sensor, event, or API
adapters without changing the routing agents.
"""

from datetime import datetime, timezone

AREA_BASE = {
    "engineering": {"crowd": "LOW", "occupancy": 32},
    "central": {"crowd": "MEDIUM", "occupancy": 58},
    "vidyalayam": {"crowd": "LOW", "occupancy": 24},
    "auditorium": {"crowd": "LOW", "occupancy": 20},
    "main": {"crowd": "MEDIUM", "occupancy": 55},
}

SCENARIOS = [
    {"name": "normal", "crowd": "LOW", "blocked_path": "none",
     "event": "Campus conditions normal.", "event_type": "routine",
     "area": "engineering", "source": "Campus Context Engine"},
    {"name": "central_crowd", "crowd": "MEDIUM", "blocked_path": "none",
     "event": "Crowd increasing near the central corridor.", "event_type": "crowd",
     "area": "central", "source": "Campus Context Engine"},
    {"name": "peak_crowd", "crowd": "HIGH", "blocked_path": "none",
     "event": "High crowd detected near the central corridor. Road costs are being updated.", "event_type": "crowd",
     "area": "central", "source": "Campus Context Engine"},
    {"name": "road_blockage", "crowd": "HIGH", "blocked_path": "vidyalayam-approach",
     "event": "Temporary blockage detected on the Vidyalayam approach road.", "event_type": "road_blockage",
     "area": "vidyalayam", "source": "Campus Context Engine"},
    {"name": "event_cleared", "crowd": "MEDIUM", "blocked_path": "none",
     "event": "Blockage cleared. Campus conditions improving.", "event_type": "recovery",
     "area": "vidyalayam", "source": "Campus Context Engine"},
    {"name": "normal_return", "crowd": "LOW", "blocked_path": "none",
     "event": "Campus conditions returned to normal.", "event_type": "recovery",
     "area": "engineering", "source": "Campus Context Engine"},
]


def build_snapshot(index: int = 0):
    scenario = SCENARIOS[index % len(SCENARIOS)]
    areas = {k: dict(v) for k, v in AREA_BASE.items()}
    area = scenario["area"]
    if scenario["crowd"] == "HIGH":
        areas[area]["crowd"] = "HIGH"
        areas[area]["occupancy"] = 86
    elif scenario["crowd"] == "MEDIUM":
        areas[area]["crowd"] = "MEDIUM"
        areas[area]["occupancy"] = 62
    else:
        areas[area]["crowd"] = "LOW"
        areas[area]["occupancy"] = 28

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": scenario["source"],
        "scenario": scenario["name"],
        "event_type": scenario["event_type"],
        "message": scenario["event"],
        "crowd": scenario["crowd"],
        "blocked_path": scenario["blocked_path"],
        "active_area": area,
        "areas": areas,
        "road_status": "BLOCKED" if scenario["blocked_path"] != "none" else "OPEN",
        "data_quality": 0.98,
        "provider": "demo-context-adapter",
    }
