from routing.astar import astar
def navigation_agent(state):
 r=astar(state['start'],state['destination'],state.get('crowd','LOW'),state.get('blocked_path','none'))
 return {'agent':'Navigation Agent',**r,'status':'route_found' if r['path'] else 'no_route'}
