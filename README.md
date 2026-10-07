# AI-Based Context-Aware Campus Navigation Using Intelligent Agents

## Stage 6 — Campus Context Engine

Stage 6 introduces a structured context-data layer between the campus environment and the routing agents.

### Context dimensions
- Crowd level and occupancy by campus area
- Road/path status
- Context event type
- Active campus area
- Data-quality indicator
- Provider/adapter identity
- Timestamped context snapshots

The demo currently uses a deterministic `demo-context-adapter` so experiments are repeatable. In a real deployment, the adapter can be replaced by sensors, a campus database, event feeds, Wi-Fi/IoT telemetry, or an external API without changing the routing graph or A* implementation.

### API
- `GET /api/health` — service and context-engine status
- `GET /api/campus/context` — current structured campus context snapshot
- `POST /api/route` — context-aware route calculation
- `WS /ws/context` — streaming context snapshots

### Run backend
```powershell
cd E:\campus-navigation-ai-stage6\campus-navigation-ai-stage3\backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload --port 8000
```

### Run frontend in another terminal
```powershell
cd E:\campus-navigation-ai-stage6\campus-navigation-ai-stage3
npm install
npm run dev
```

Open http://localhost:5173/
