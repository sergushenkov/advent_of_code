input_string = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
'''

# with open('input.txt', 'r') as file:
#     input_string = file.open()


def count_max_geode(timer, robots, costs, sources, builds):
    ore, clay, obs, geode = sources
    if timer <= 1:
        return geode + timer * robots['geode']
    timer -= 1
    sources = [ore + robots['ore'], clay + robots['clay'], obs + robots['obs'], geode + robots['geode']]

    if len(builds) > 1:
        if costs['geode'][0] <= robots['ore'] and costs['geode'][1] <= robots['clay'] and costs['geode'][2] <= robots['obs']:
            new_builds = {'geode'}
            next_time = []
        else:
            new_builds = builds.copy()
            if 'ore' in new_builds and robots['ore'] >= max(costs['ore'][0], costs['clay'][0], costs['obs'][0], costs['geode'][0]):
                new_builds.remove('ore')
            if 'clay' in new_builds and  robots['clay'] >= costs['obs'][1]:
                new_builds.remove('clay')
            if 'obs' in new_builds and  robots['obs'] >= costs['geode'][0]:
                new_builds.remove('obs')
            next_time = [count_max_geode(timer, robots, costs, sources, new_builds)]
    else:
        new_builds = builds.copy()
        next_time = []

    for robot in new_builds:
        if costs[robot][0] <= sources[0] and costs[robot][1] <= sources[1] and costs[robot][2] <= sources[2]:
            new_robots = robots.copy()
            new_robots[robot] += 1
            ore, clay, obs, geode = sources
            new_sources = [ore - costs[robot][0], clay - costs[robot][1], obs - costs[robot][2], geode]
            next_time.append(count_max_geode(timer, new_robots, costs, new_sources, new_builds))
    if next_time == []:     
        next_time = [count_max_geode(timer, robots, costs, sources, new_builds)]
    return max(next_time)
    
blueprint_count = 0
result = 0
for line in input_string.strip().split('\n'):
    _, ore_robot, clay_robot, obs_robot, geode_robot = line.split(' costs ')
    ore_robot_cost = (int(ore_robot.strip(' ore. Each clay robot')), 0, 0)
    clay_robot_cost = (int(clay_robot.strip(' ore. Each obsidian robot')), 0, 0)
    obs_robot_ore, obc_robot_clay = obs_robot.split(' ore and ')
    obs_robot_cost = (int(obs_robot_ore), int(obc_robot_clay.strip(' clay. Each geode robot')), 0)
    geode_robot_ore, geode_robot_obs = geode_robot.split(' ore and ')
    geode_robot_cost = (int(geode_robot_ore), 0, int(geode_robot_obs.strip(' obsidian.')))
    costs = {'ore': ore_robot_cost, 'clay': clay_robot_cost, 'obs': obs_robot_cost, 'geode': geode_robot_cost}
    print(costs)
    
    blueprint_count += 1
    robots = {'ore': 1, 'clay': 0, 'obs': 0, 'geode': 0}
    ore, clay, obs, geode = 0, 0, 0, 0
    sources = [ore, clay, obs, geode]
    builds = {'ore', 'clay', 'obs', 'geode'}
    timer = 10
    max_geode = count_max_geode(timer, robots, costs, sources, builds)
    result += max_geode * blueprint_count
    print(blueprint_count, max_geode)
print(result)
