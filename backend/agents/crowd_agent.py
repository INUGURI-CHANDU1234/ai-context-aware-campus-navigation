def crowd_agent(state):
    crowd=state.get('crowd','LOW').upper(); return {'agent':'Crowd Agent','crowd':crowd,'penalty':{'LOW':0,'MEDIUM':70,'HIGH':180}.get(crowd,0),'status':'evaluated'}
