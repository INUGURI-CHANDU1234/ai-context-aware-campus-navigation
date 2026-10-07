\# AI-BASED CONTEXT-AWARE CAMPUS NAVIGATION

\## USING SEARCH AND MULTI-AGENT SYSTEMS



\### Final Project Report



\---



\# ABSTRACT



Campus navigation becomes challenging when environmental conditions such as crowd density and blocked pedestrian paths change dynamically. Conventional navigation systems generally depend on static maps and shortest-path computation and may not adequately adapt to temporary campus conditions.



This project presents an AI-based context-aware campus navigation system that combines graph-based A\* search with a multi-agent architecture. The system uses specialized agents for campus context analysis, crowd analysis, obstacle detection, navigation, and explainable decision-making. A coordinator agent integrates the outputs of these agents and produces a context-aware routing decision.



The implemented system supports dynamic pedestrian route selection, crowd-sensitive route evaluation, blocked-road detection, automatic rerouting, and explainable routing decisions. A real-time WebSocket context layer allows changing campus conditions to influence routing decisions.



Experimental evaluation was conducted using predefined campus navigation scenarios. The system successfully generated routes for 8 out of 8 evaluated scenarios. All 4 evaluated blocked-road scenarios were successfully rerouted. The decision layer produced 7 correct decisions out of 7 evaluated decision scenarios. Route cost increased from 308.00 under low crowd conditions to 619.70 under high crowd conditions, representing a 101.20% increase.



The results demonstrate that the implemented architecture can adapt navigation decisions according to changing campus context while providing interpretable decision information.



\---



\# 1. INTRODUCTION



Campus environments contain multiple buildings, hostels, laboratories, academic blocks, roads, pedestrian paths, and other facilities. Students and visitors frequently need to navigate between these locations.



Traditional shortest-path algorithms can identify efficient routes on a predefined graph, but campus conditions are not always static. A pedestrian path may become temporarily unavailable, a particular area may become crowded, or an obstacle may require a route to be changed.



Therefore, an intelligent campus navigation system should consider both the underlying road network and the current environmental context.



This project proposes an AI-based context-aware navigation architecture that combines:



\- Graph-based route planning

\- A\* search

\- Multi-agent coordination

\- Crowd-context analysis

\- Obstacle detection

\- Dynamic rerouting

\- Explainable decision-making

\- Real-time context updates



The objective is not simply to calculate a shortest path but to select an appropriate route based on the current campus conditions.



\---



\# 2. PROBLEM STATEMENT



Existing campus navigation approaches generally operate using static maps and conventional shortest-path algorithms. Such approaches may not adequately handle temporary changes in campus conditions.



The major problems addressed by this project are:



1\. Static routing may become unsuitable when a pedestrian path is blocked.

2\. Increasing crowd density can affect the practical cost of a route.

3\. Different environmental conditions require different routing decisions.

4\. A navigation system should be able to explain why a route was retained or changed.

5\. Multiple context sources need to be coordinated before making a final routing decision.



The project therefore addresses the following problem:



> How can a campus navigation system dynamically adapt pedestrian routes according to changing campus context while coordinating multiple intelligent agents and providing an explainable routing decision?



\---



\# 3. OBJECTIVES



The main objectives are:



1\. Develop a campus navigation system based on a pedestrian road graph.

2\. Implement A\* search for route generation.

3\. Introduce context awareness into route selection.

4\. Model crowd density as a dynamic routing factor.

5\. Detect blocked pedestrian road segments.

6\. Automatically reroute when the selected path becomes unavailable.

7\. Use multiple specialized agents for context and navigation analysis.

8\. Coordinate agent outputs through a coordinator agent.

9\. Provide explainable routing decisions.

10\. Evaluate the system using controlled navigation scenarios.



\---



\# 4. EXISTING SYSTEM



Traditional campus navigation systems generally rely on:



\- Static maps

\- Fixed routes

\- GPS-based positioning

\- Conventional shortest-path algorithms

\- Manual route selection



A conventional shortest-path system may calculate the optimal path using distance or cost. However, if a road becomes blocked after route calculation, the original route may no longer be valid.



Similarly, a route that is shortest under low crowd conditions may not necessarily be the preferred route under high crowd conditions.



\### Limitations of the existing approach



\- Limited context awareness

\- Weak adaptation to temporary obstacles

\- Limited multi-source decision coordination

\- Lack of explainable routing decisions

\- Static or semi-static route assumptions



\---



\# 5. PROPOSED SYSTEM



The proposed system combines graph search with context-aware multi-agent coordination.



The major components are:



1\. Campus Road Graph

2\. Context Agent

3\. Crowd Agent

4\. Obstacle Agent

5\. Navigation Agent

6\. Decision Agent

7\. Coordinator Agent

8\. Real-Time Context Engine

9\. Frontend Visualization Layer



The system first receives a navigation request containing a starting location and destination.



The coordinator then invokes the specialized agents.



The navigation agent calculates a route using the campus pedestrian graph and A\* search.



The context, crowd, and obstacle agents provide environmental information.



The decision agent evaluates the navigation result together with the context information and determines whether the current route should be retained or changed.



\---



\# 6. SYSTEM ARCHITECTURE



The overall architecture can be represented as:



User

|

v

Campus Navigation Interface

|

v

Navigation Request

|

v

Coordinator Agent

|

+-------------------+

|                   |

v                   v

Context Agent      Crowd Agent

|                   |

+---------+---------+

&#x20;         |

&#x20;         v

&#x20;   Obstacle Agent

&#x20;         |

&#x20;         v

&#x20;   Navigation Agent

&#x20;         |

&#x20;         v

&#x20;      A\* Search

&#x20;         |

&#x20;         v

&#x20;   Candidate Route

&#x20;         |

&#x20;         v

&#x20;    Decision Agent

&#x20;         |

&#x20;         v

&#x20;Explainable Decision

&#x20;         |

&#x20;         v

&#x20;Final Route

&#x20;         |

&#x20;         v

&#x20;Campus Map / UI



A real-time context engine provides changing campus information to the system through a WebSocket connection.



\---



\# 7. MULTI-AGENT ARCHITECTURE



The system uses specialized agents rather than placing all responsibilities inside a single routing component.



\## 7.1 Context Agent



The Context Agent determines the current campus context.



It considers information such as:



\- Active campus area

\- Road status

\- Data quality

\- Context provider

\- Current environmental state



Its output contributes to the overall context snapshot.



\---



\## 7.2 Crowd Agent



The Crowd Agent evaluates the current crowd condition.



The implemented system supports:



\- LOW

\- MEDIUM

\- HIGH



Crowd information influences the route cost and therefore can affect route selection.



\---



\## 7.3 Obstacle Agent



The Obstacle Agent identifies blocked road segments.



When a pedestrian segment is blocked, the affected segment is removed from consideration during route evaluation.



This enables the system to search for an alternative path.



\---



\## 7.4 Navigation Agent



The Navigation Agent performs route calculation over the pedestrian road graph.



The implemented routing mechanism uses A\* search.



The navigation output includes:



\- Route path

\- Route cost

\- Route segments

\- Path coordinates

\- Network type

\- Route status



\---



\## 7.5 Decision Agent



The Decision Agent determines whether the existing route should be retained or whether a route change is justified.



It produces explainable information such as:



\- Decision summary

\- Selected action

\- Confidence

\- Risk score

\- Decision factors



This allows the system to communicate not only the selected route but also the reasoning associated with the routing decision.



\---



\## 7.6 Coordinator Agent



The Coordinator Agent integrates the outputs of the individual agents.



The implemented workflow is:



1\. Receive navigation state.

2\. Run Context Agent.

3\. Run Crowd Agent.

4\. Run Obstacle Agent.

5\. Run Navigation Agent.

6\. Run Decision Agent.

7\. Combine all outputs.

8\. Return the final navigation result.



This provides a structured multi-agent decision pipeline.



\---



\# 8. A\* ROUTE PLANNING



The Navigation Agent uses A\* search over the campus pedestrian road graph.



A\* evaluates nodes using:



f(n) = g(n) + h(n)



where:



\- `g(n)` represents the cost from the starting node to node `n`.

\- `h(n)` represents the estimated cost from node `n` to the destination.

\- `f(n)` represents the total estimated route cost.



The graph contains pedestrian routing nodes and connections between them.



The resulting path is converted into route segments and displayed on the campus map.



\---



\# 9. CONTEXT-AWARE ROUTING



A key feature of the system is that routing is not treated as a completely static operation.



The system considers environmental context including:



\- Crowd density

\- Blocked roads

\- Active campus area

\- Road availability



The route cost therefore represents more than simple geometric distance.



Experimental results demonstrate that route cost changes with crowd conditions.



Measured average route costs were:



| Crowd Condition | Average Route Cost |

|---|---:|

| LOW | 308.00 |

| MEDIUM | 455.64 |

| HIGH | 619.70 |



The increase from LOW to HIGH crowd conditions was:



\*\*101.20%\*\*



This demonstrates that changing context affects the routing evaluation.



\---



\# 10. REAL-TIME CONTEXT ENGINE



The frontend communicates with the backend through a WebSocket endpoint:



`/ws/context`



The real-time context mechanism allows the application to receive context updates without requiring a complete manual refresh.



The context update can contain information such as:



\- Crowd state

\- Blocked path

\- Context source

\- Event message



When live context changes, the frontend updates the displayed context and can recalculate the route.



This provides the foundation for dynamic context-aware navigation.



\---



\# 11. DYNAMIC REROUTING



Dynamic rerouting is triggered when a road segment used by the route becomes unavailable.



The system:



1\. Detects the blocked road.

2\. Updates the navigation state.

3\. Excludes the blocked segment.

4\. Executes route calculation again.

5\. Searches for an alternative pedestrian route.

6\. Updates the displayed route.

7\. Reports the routing decision.



The system was evaluated using four blocked-road scenarios.



Results:



| Metric | Result |

|---|---:|

| Blocked-road scenarios | 4 |

| Successful reroutes | 4 |

| Failed reroutes | 0 |

| Rerouting success rate | 100% |



The correct academic interpretation is:



> The system achieved a 100% rerouting success rate across the four evaluated blocked-road scenarios.



This result should not be interpreted as universal real-world success across every possible campus blockage.



\---



\# 12. EXPLAINABLE AI DECISION LAYER



The system includes an explainable decision layer that provides information associated with routing decisions.



The decision output contains:



\- Summary

\- Action

\- Confidence

\- Risk score

\- Factors



This allows the system to distinguish between situations such as:



\### Normal conditions



The current route remains available and no significant context constraint justifies rerouting.



\### Blocked-road conditions



The current route is no longer available, so an alternative route is selected.



The decision layer therefore makes the routing process more interpretable.



\---



\# 13. TECHNOLOGY STACK



\## Frontend



\- React

\- JavaScript

\- Vite

\- CSS

\- Interactive campus map visualization



\## Backend



\- Python

\- FastAPI

\- WebSocket communication



\## Artificial Intelligence / Algorithms



\- Multi-agent architecture

\- A\* search

\- Context-aware decision logic

\- Explainable decision layer



\## Data / Evaluation



\- CSV-based experimental datasets

\- Python-based evaluation scripts

\- Matplotlib-based visualization



\---



\# 14. EXPERIMENTAL METHODOLOGY



The evaluation was divided into multiple stages.



\## Stage 7 — System Evaluation



The navigation system was evaluated using eight predefined scenarios.



Measured metrics included:



\- Route success

\- Route cost

\- Confidence

\- Risk

\- Route changes

\- Blocked-road handling



Results:



\- Total scenarios: 8

\- Successful routes: 8

\- Route success rate: 100%



\---



\## Stage 8 — Controlled Experiments



Three major experiments were conducted.



\### Experiment 1 — Crowd Impact



Average route cost was measured under:



\- LOW crowd

\- MEDIUM crowd

\- HIGH crowd



Results:



\- LOW: 308.00

\- MEDIUM: 455.64

\- HIGH: 619.70



LOW to HIGH increase:



\*\*101.20%\*\*



\---



\### Experiment 2 — Blocked Road and Rerouting



Four blocked-road scenarios were evaluated.



Results:



\- Blocked scenarios: 4

\- Successful reroutes: 4

\- Success rate: 100%



The results demonstrate adaptive rerouting under the tested conditions.



\---



\### Experiment 3 — Decision Quality



Seven scenarios were evaluated for decision quality.



Results:



\- Evaluated scenarios: 7

\- Correct decisions: 7

\- Incorrect decisions: 0

\- Decision accuracy: 100%



Again, the result applies to the evaluated test scenarios.



\---



\# 15. RESULTS AND ANALYSIS



\## 15.1 Overall Navigation Performance



The system achieved:



\*\*8/8 successful routes\*\*



This corresponds to a route success rate of:



\*\*100%\*\*



\---



\## 15.2 Crowd Adaptation



Route cost increased with crowd density:



| Crowd | Cost |

|---|---:|

| LOW | 308.00 |

| MEDIUM | 455.64 |

| HIGH | 619.70 |



The LOW-to-HIGH increase was:



\*\*101.20%\*\*



This supports the context-adaptation capability of the system.



\---



\## 15.3 Rerouting Performance



The system successfully rerouted all four evaluated blocked-road scenarios.



\*\*4/4 = 100%\*\*



This demonstrates dynamic route adaptation when a route becomes unavailable.



\---



\## 15.4 Decision Accuracy



The decision layer produced correct decisions in all seven evaluated scenarios.



\*\*7/7 = 100%\*\*



This demonstrates consistency between the evaluated context and the generated routing decision.



\---



\## 15.5 Confidence and Risk



| Road Condition | Confidence | Risk |

|---|---:|---:|

| Open Road | 85.33% | 31.67 |

| Blocked Road | 94.00% | 91.25 |



Confidence and risk represent different dimensions.



Confidence indicates the system's confidence in its decision, whereas risk represents the severity or constraint associated with the navigation condition.



Therefore, a blocked-road condition can have both high risk and high decision confidence when the system has a clear reason to reroute.



\---



\# 16. RESEARCH GAP



Existing campus navigation approaches often focus primarily on shortest-path computation or static navigation.



The project addresses the following gaps:



\### Gap 1 — Limited environmental context



Traditional routing may not incorporate changing campus crowd conditions.



\### Gap 2 — Static route assumptions



A route may become invalid when a pedestrian segment is blocked.



\### Gap 3 — Limited multi-agent coordination



Different context sources may not be independently analyzed and then coordinated.



\### Gap 4 — Limited explainability



A navigation system may provide a route without explaining why the route was retained or changed.



\### Gap 5 — Limited experimental evaluation



Context-aware navigation requires evaluation under different environmental conditions rather than only testing normal routing.



\---



\# 17. PROJECT CONTRIBUTIONS



The main contributions of the project are:



1\. A campus-specific pedestrian routing graph.

2\. A\* based route generation.

3\. Multi-agent context processing.

4\. Crowd-aware route evaluation.

5\. Blocked-road detection and dynamic rerouting.

6\. Real-time context updates using WebSocket communication.

7\. Explainable navigation decisions.

8\. Experimental evaluation under different crowd and road conditions.

9\. Visualization of routing performance and decision behavior.



\---



\# 18. NOVELTY



The primary novelty of the project is the integration of multiple components into a unified campus navigation architecture.



Instead of treating navigation as only a shortest-path problem, the proposed system combines:



\*\*Context + Crowd + Obstacles + A\* Navigation + Multi-Agent Coordination + Explainable Decision-Making\*\*



This allows the route to be evaluated according to the current campus state.



The novelty is therefore primarily architectural and system-level rather than claiming a new A\* algorithm.



\---



\# 19. LIMITATIONS



The current implementation has several limitations.



\### 19.1 Limited evaluation size



The evaluation uses controlled scenarios rather than a large real-world campus deployment.



\### 19.2 Simulated context



Crowd and obstacle conditions are represented using controlled inputs rather than continuous physical sensor data.



\### 19.3 Limited geographic coverage



The current system focuses on the implemented campus map and pedestrian road network.



\### 19.4 No large-scale user study



The system has not yet been evaluated with a large population of actual campus users.



\### 19.5 Simplified crowd model



Crowd levels are represented using discrete states such as LOW, MEDIUM, and HIGH.



\### 19.6 Controlled experimental scenarios



The reported 100% results are based on the evaluated test scenarios and should not be generalized to all real-world conditions.



\---



\# 20. FUTURE ENHANCEMENTS



Future versions can extend the system with:



1\. Real-time CCTV-based crowd estimation.

2\. IoT-based pedestrian density sensors.

3\. GPS/mobile-based crowd estimation.

4\. Dynamic edge weights based on real-time density.

5\. Weather-aware routing.

6\. Emergency-event routing.

7\. Accessibility-aware routes for users with mobility constraints.

8\. Personalized route preferences.

9\. Larger campus-wide graph coverage.

10\. Historical traffic prediction.

11\. Machine-learning-based travel-time prediction.

12\. Federated or privacy-preserving crowd estimation.

13\. Mobile application deployment.

14\. Real-world user evaluation.

15\. Learning-based route optimization.



\---



\# 21. CONCLUSION



This project developed an AI-based context-aware campus navigation system that combines graph-based A\* search with multi-agent coordination and explainable decision-making.



The implemented system can process campus context, evaluate crowd conditions, identify blocked pedestrian paths, generate alternative routes, and provide an explainable routing decision.



The experimental evaluation produced the following results:



\- 8/8 successful routes

\- 4/4 successful blocked-road reroutes

\- 7/7 correct decision outcomes

\- 101.20% increase in route cost from LOW to HIGH crowd conditions

\- 85.33% open-road decision confidence

\- 94.00% blocked-road decision confidence



These results demonstrate the ability of the implemented architecture to adapt routing decisions according to changing campus conditions within the evaluated scenarios.



The project provides a foundation for developing a larger real-world intelligent campus navigation platform using live sensor data, machine learning, personalized navigation, and real-time campus infrastructure.



\---



\# 22. REFERENCES



The final reference list should contain the research papers and technical sources used during the development of the project.



Recommended categories include:



1\. A\* search and heuristic pathfinding.

2\. Multi-agent systems.

3\. Context-aware computing.

4\. Intelligent transportation/navigation systems.

5\. Explainable artificial intelligence.

6\. Dynamic route planning.

7\. Crowd-aware navigation.

8\. Real-time WebSocket/FastAPI systems.



Technical documentation may also be referenced for:



\- Python

\- FastAPI

\- React

\- Vite

\- WebSocket

\- Matplotlib



\---



\# APPENDIX A — FINAL EVALUATION METRICS



| Metric | Value |

|---|---:|

| Total evaluated route scenarios | 8 |

| Successful routes | 8 |

| Route success rate | 100% |

| Average route cost | 532.62 |

| Average confidence | 90.00% |

| Average risk score | 63.75 |

| Blocked-road scenarios | 4 |

| Successful blocked-road routes | 4 |

| Blocked-road success rate | 100% |

| Reroute decisions | 4 |

| LOW crowd average cost | 312.00 |

| MEDIUM crowd average cost | 463.69 |

| HIGH crowd average cost | 677.38 |



Note: The Stage 7 overall averages above are based on the eight-scenario evaluation dataset, while the controlled Stage 8 crowd experiment reports LOW/MEDIUM/HIGH values of 308.00, 455.64, and 619.70 respectively. These are different evaluation summaries and should not be treated as the same dataset.



\---



\# APPENDIX B — STAGE 8 EXPERIMENT RESULTS



\## Experiment 1



LOW → MEDIUM increase: 47.94%



MEDIUM → HIGH increase: 36.01%



LOW → HIGH increase: 101.20%



\## Experiment 2



Blocked-road scenarios: 4



Successful reroutes: 4



Rerouting success rate: 100%



\## Experiment 3



Evaluated scenarios: 7



Correct decisions: 7



Decision accuracy: 100%



\---



\# APPENDIX C — STAGE 9 VISUALIZATIONS



The following figures were generated from the experimental results:



1\. `crowd\_vs\_route\_cost.png`

2\. `crowd\_cost\_impact.png`

3\. `rerouting\_success.png`

4\. `decision\_accuracy.png`

5\. `confidence\_vs\_risk.png`



These figures are stored in:



`stage10/figures/`



\---



\# END OF REPORT

