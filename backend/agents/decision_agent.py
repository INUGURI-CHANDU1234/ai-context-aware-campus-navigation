from routing.astar import astar


def _label(path):
    return ' → '.join(path) if path else 'No route'


def decision_agent(state, navigation):
    crowd = state.get('crowd', 'LOW').upper()
    blocked = state.get('blocked_path', 'none')
    start = state['start']
    destination = state['destination']

    baseline = astar(start, destination, 'LOW', 'none')
    current = navigation
    baseline_path = baseline.get('path', [])
    current_path = current.get('path', [])
    changed = baseline_path != current_path

    crowd_impact = {'LOW': 0, 'MEDIUM': 25, 'HIGH': 40}.get(crowd, 0)
    obstacle_impact = 45 if blocked != 'none' else 0
    route_impact = 15 if changed else 0
    risk = min(100, 10 + crowd_impact + obstacle_impact + route_impact)

    if blocked != 'none':
        summary = f'Blocked road segment detected: {blocked}. The route engine removed that segment from the graph.'
        action = 'A* selected the lowest-cost available pedestrian path around the blocked road segment.'
    elif crowd == 'HIGH' and changed:
        summary = 'High crowd density increased the cost of sensitive pedestrian road segments.'
        action = 'A* selected a lower-exposure pedestrian route using dynamic segment costs.'
    elif crowd == 'MEDIUM' and changed:
        summary = 'Moderate crowd density changed the relative cost of pedestrian road segments.'
        action = 'A* selected the best context-aware road path.'
    else:
        summary = 'The pedestrian road network is open and the current path remains the lowest-cost option.'
        action = 'Keep the current road route; no context constraint justifies a reroute.'

    confidence = min(98, 84 + (8 if blocked != 'none' else 0) + (4 if crowd == 'HIGH' else 0))

    return {
        'agent': 'Explainable Decision Agent',
        'decision': 'recalculate' if changed else 'keep_route',
        'summary': summary,
        'action': action,
        'confidence': confidence,
        'risk_score': risk,
        'factors': [
            {'name': 'Blocked segment', 'impact': obstacle_impact, 'level': 'HIGH' if obstacle_impact else 'LOW'},
            {'name': 'Crowd density', 'impact': crowd_impact, 'level': crowd},
            {'name': 'Route change', 'impact': route_impact, 'level': 'HIGH' if route_impact else 'LOW'},
            {'name': 'Road availability', 'impact': 20 if blocked != 'none' else 0, 'level': 'HIGH' if blocked != 'none' else 'LOW'},
        ],
        'baseline': {'path': baseline_path, 'cost': baseline.get('cost')},
        'selected': {'path': current_path, 'cost': current.get('cost')},
        'alternatives_rejected': [_label(baseline_path)] if changed else [],
        'status': 'explanation_ready',
    }
