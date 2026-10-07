import heapq
from math import hypot

# Hand-mapped pedestrian/path network aligned to the supplied Amrita campus image.
# These are internal routing nodes; users never select them.
NODES = {
    # User-facing locations
    'engineering': (431, 418), 'itcanteen': (416, 330), 'girls': (482, 166),
    'vidyalayam': (571, 376), 'auditorium': (712, 367), 'children': (592, 396),
    'hanger': (820, 470), 'kashyapa': (904, 463), 'sriVyasa': (907, 571),
    'main': (726, 602), 'gym': (193, 557), 'asb': (343, 477), 'cafe': (300, 788),

    # Hidden road/intersection nodes
    'r_e1': (448, 418), 'r_e2': (478, 417), 'r_e3': (515, 405),
    'r_e4': (545, 391), 'r_i1': (424, 372), 'r_i2': (418, 348),
    'r_i3': (455, 300), 'r_i4': (482, 250), 'r_g1': (500, 205),
    'r_v1': (602, 374), 'r_v2': (635, 372), 'r_v3': (668, 369),
    'r_a1': (690, 368), 'r_c1': (610, 415), 'r_c2': (650, 425),
    'r_a2': (750, 385), 'r_a3': (790, 430), 'r_h1': (800, 470),
    'r_h2': (850, 468), 'r_m1': (780, 510), 'r_m2': (755, 555),
    'r_m3': (726, 580), 'r_s1': (800, 555), 'r_s2': (860, 565),
    'r_e5': (405, 435), 'r_e6': (370, 450), 'r_a4': (335, 475),
    'r_gym1': (310, 500), 'r_gym2': (265, 525), 'r_gym3': (225, 545),
    'r_cafe1': (250, 620), 'r_cafe2': (275, 700), 'r_cafe3': (290, 755),
    'r_main1': (470, 470), 'r_main2': (520, 505), 'r_main3': (575, 535),
    'r_main4': (635, 565), 'r_main5': (685, 585), 'r_main6': (760, 615),
}

# (a, b, base cost, segment id, crowd sensitivity)
EDGES = [
    ('engineering','r_e1',20,'engineering-east',0.8),
    ('r_e1','r_e2',30,'engineering-east',0.8),
    ('r_e2','r_e3',40,'central-approach',1.0),
    ('r_e3','r_e4',35,'central-approach',1.0),
    ('r_e4','vidyalayam',35,'vidyalayam-approach',1.2),

    ('engineering','r_i1',50,'engineering-north',1.0),
    ('r_i1','r_i2',28,'it-canteen-road',1.1),
    ('r_i2','itcanteen',24,'it-canteen-road',1.1),
    ('itcanteen','r_i3',65,'girls-road',0.8),
    ('r_i3','r_i4',55,'girls-road',0.8),
    ('r_i4','r_g1',50,'girls-road',0.8),
    ('r_g1','girls',48,'girls-road',0.8),

    ('vidyalayam','r_v1',30,'vidyalayam-east',1.1),
    ('r_v1','r_v2',35,'vidyalayam-east',1.1),
    ('r_v2','r_v3',34,'auditorium-approach',1.2),
    ('r_v3','r_a1',25,'auditorium-approach',1.2),
    ('r_a1','auditorium',24,'auditorium-approach',1.2),

    ('vidyalayam','r_c1',45,'children-hostel-road',0.9),
    ('r_c1','children',25,'children-hostel-road',0.9),
    ('children','r_c2',45,'children-east',1.0),
    ('r_c2','r_a2',55,'children-east',1.0),
    ('r_a2','auditorium',50,'auditorium-south',1.0),

    ('auditorium','r_a3',55,'auditorium-hanger-road',0.8),
    ('r_a3','r_h1',45,'auditorium-hanger-road',0.8),
    ('r_h1','hanger',25,'hanger-road',0.7),
    ('hanger','r_h2',38,'hanger-east',0.7),
    ('r_h2','kashyapa',45,'kashyapa-road',0.7),
    ('hanger','r_m1',60,'hanger-main-road',0.8),
    ('r_m1','r_m2',55,'main-south-road',0.9),
    ('r_m2','r_m3',35,'main-south-road',0.9),
    ('r_m3','main',25,'main-campus-road',0.8),

    ('main','r_s1',75,'sri-vyasa-road',0.7),
    ('r_s1','r_s2',55,'sri-vyasa-road',0.7),
    ('r_s2','sriVyasa',48,'sri-vyasa-road',0.7),

    ('engineering','r_e5',42,'engineering-west',0.9),
    ('r_e5','r_e6',38,'asb-road',0.9),
    ('r_e6','r_a4',34,'asb-road',0.8),
    ('r_a4','asb',18,'asb-road',0.8),
    ('r_e6','r_gym1',55,'gym-road',0.7),
    ('r_gym1','r_gym2',50,'gym-road',0.7),
    ('r_gym2','r_gym3',48,'gym-road',0.7),
    ('r_gym3','gym',35,'gym-road',0.7),

    ('gym','r_cafe1',80,'south-west-road',0.5),
    ('r_cafe1','r_cafe2',80,'south-west-road',0.5),
    ('r_cafe2','r_cafe3',65,'cafe-road',0.5),
    ('r_cafe3','cafe',50,'cafe-road',0.5),

    ('engineering','r_main1',75,'engineering-south',0.7),
    ('r_main1','r_main2',70,'engineering-south',0.7),
    ('r_main2','r_main3',70,'staff-quarter-road',0.8),
    ('r_main3','r_main4',70,'staff-quarter-road',0.8),
    ('r_main4','r_main5',55,'main-campus-road',0.8),
    ('r_main5','main',50,'main-campus-road',0.8),
    ('r_main3','r_cafe2',115,'south-road',0.5),

    # Cross-links that make the network realistic and provide alternate routes.
    ('r_e3','r_i1',48,'central-north-link',1.0),
    ('r_v2','r_c1',55,'vidyalayam-children-link',1.0),
    ('r_a1','r_a2',45,'auditorium-link',1.0),
    ('r_a2','r_a3',60,'auditorium-south-link',0.9),
    ('r_m2','r_c2',85,'south-east-link',0.8),
]

LOCATION_IDS = set(k for k in NODES if not k.startswith('r_'))


def build_graph(crowd='LOW', blocked='none'):
    graph = {k: [] for k in NODES}
    crowd = crowd.upper()
    multiplier = {'LOW': 0.0, 'MEDIUM': 0.45, 'HIGH': 0.95}.get(crowd, 0.0)
    for a, b, base, segment, sensitivity in EDGES:
        if blocked == segment:
            continue
        weight = base * (1.0 + multiplier * sensitivity)
        graph[a].append((b, weight, segment))
        graph[b].append((a, weight, segment))
    return graph


def heuristic(a, b):
    ax, ay = NODES[a]
    bx, by = NODES[b]
    return hypot(ax - bx, ay - by) * 0.55


def astar(start, goal, crowd='LOW', blocked='none'):
    if start not in LOCATION_IDS or goal not in LOCATION_IDS:
        return {'path': [], 'cost': None, 'segments': []}
    if start == goal:
        return {'path': [start], 'cost': 0, 'segments': []}

    graph = build_graph(crowd, blocked)
    open_heap = [(heuristic(start, goal), start)]
    came_from = {}
    came_segment = {}
    g_score = {start: 0.0}

    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            path = [current]
            segments = []
            while current in came_from:
                segments.append(came_segment[current])
                current = came_from[current]
                path.append(current)
            path.reverse()
            segments.reverse()
            return {
                'path': path,
                'cost': round(g_score[goal], 2),
                'segments': segments,
                'network_type': 'pedestrian_road_segments',
                'path_coords': [NODES[node] for node in path],
            }

        for neighbor, weight, segment in graph[current]:
            tentative = g_score[current] + weight
            if tentative < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                came_segment[neighbor] = segment
                g_score[neighbor] = tentative
                f = tentative + heuristic(neighbor, goal)
                heapq.heappush(open_heap, (f, neighbor))

    return {'path': [], 'cost': None, 'segments': [], 'path_coords': [], 'network_type': 'pedestrian_road_segments'}
