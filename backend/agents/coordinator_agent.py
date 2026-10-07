from agents.context_agent import context_agent
from agents.crowd_agent import crowd_agent
from agents.obstacle_agent import obstacle_agent
from agents.navigation_agent import navigation_agent
from agents.decision_agent import decision_agent


def coordinator(state):
    context = context_agent(state)
    crowd = crowd_agent(state)
    obstacle = obstacle_agent(state)
    navigation = navigation_agent(state)
    decision = decision_agent(state, navigation)

    return {
        'request': {
            'start': state['start'],
            'destination': state['destination'],
        },
        'context': context,
        'crowd': crowd,
        'obstacle': obstacle,
        'navigation': navigation,
        'decision': decision,
        'coordinator': {
            'agent': 'Coordinator Agent',
            'decision': decision['decision'],
            'status': 'complete'
        }
    }
