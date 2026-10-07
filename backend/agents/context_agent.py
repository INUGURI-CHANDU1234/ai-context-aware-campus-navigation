def context_agent(state):
    crowd = state.get('crowd', 'LOW').upper()
    blocked = state.get('blocked_path', 'none')
    area = state.get('active_area', 'central')
    score = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3}.get(crowd, 1)
    return {
        'agent': 'Context Agent',
        'crowd': crowd,
        'blocked_path': blocked,
        'active_area': area,
        'context_score': score,
        'status': 'analyzed'
    }
