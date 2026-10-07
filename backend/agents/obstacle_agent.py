def obstacle_agent(state):
    blocked=state.get('blocked_path','none')
    return {'agent':'Obstacle Agent','blocked_path':blocked,'status':'clear' if blocked=='none' else 'obstacle_detected','message':'No selected blockage.' if blocked=='none' else f'Blocked edge detected: {blocked}.'}
