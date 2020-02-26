import argparse


parser = argparse.ArgumentParser(description='BMO Trains Problem.  Solution created by Joshua Kraitberg.')
parser.add_argument('input', help='Input data to run on, can be text or file', )


def simple_cli(args):

    import os

    from trains_problem.route_planner import RoutePlanner
    
    # Turn file into data
    data = args.input
    if os.path.isfile(data):
        with open(data) as f:
            data = f.read()

    planner = RoutePlanner.build_simple_route_planner(data)

    return ( 
        '\n'.join(
            f'Output #{i}: {v}'
            for i, v in enumerate((
                planner.get_route_distance_from_stops('A', 'B', 'C'),
                planner.get_route_distance_from_stops('A', 'D'),
                planner.get_route_distance_from_stops('A', 'D', 'C'),
                planner.get_route_distance_from_stops('A', 'E', 'B', 'C', 'D'),
                planner.get_route_distance_from_stops('A', 'E', 'D'),
                planner.get_number_of_routes_with_maximum_n_stops('C', 'C', 3),
                planner.get_number_of_routes_with_exactly_n_stops('A', 'C', 4),
                planner.get_length_of_shortest_route('A', 'C'),
                planner.get_length_of_shortest_route('B', 'B'),
                planner.get_number_of_routes_with_distance_less_than_n('C', 'C', 30),
            ), 1)
        )
    )


def main(args=None):
    print(simple_cli(parser.parse_args(args)))

