from solverCommand import SolverCommand
from EightPuzzle import EightPuzzle as ep
import Node


class BFSSolver(SolverCommand):
    initial_node = None
    with_parents = False
    depth = 0

    def __init__(self, node, with_parents):
        self.initial_node = Node.Node(node, 0)
        self.with_parents = with_parents
        self.depth = 0

    def execute(self):
        # Implement BFS algorithm for solving the puzzle
        # Initialize the frontier queue, the explored set, and
        # the frontier hashtable for faster neighbour existence checking
        frontier = []
        explored = set()
        frontier_hash = {}
        frontier.append(self.initial_node)
        frontier_hash[self.initial_node.data] = True

        # Initialize the parents dictionary for printing the path to the goal
        parents = {self.initial_node.data: self.initial_node.data}
        while frontier:
            state = frontier.pop(0)
            explored.add(state.data)
            if ep.is_goal(state.data):  # Reached 012345678

                return "success", (ep.path_cost(state), ep.nodes_expanded(explored), self.depth,
                                   ep.path_to_goal(state, parents))

            # Get the possible actions for the current state
            possible_actions = ep.actions(state)
            for action in possible_actions:
                if action.data not in explored and action.data not in frontier_hash:
                    frontier.append(action)
                    frontier_hash[action.data] = True
                    parents[action.data] = state.data
                    self.depth = max(self.depth, action.depth)
        return "fail", (0, 0, 0, [])
