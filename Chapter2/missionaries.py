"""
Missionaries and cannibals task solution

Three missionaries and three cannibals are on the west bank of a river.
They have a canoe that can hold two people, and they all must cross
to the east bank of the river.
There may never be more cannibals than missionaries on either side of the river
or the cannibals will eat the missionaries.
Further, the canoe must have at least one person on board to cross the river.

What sequence of crossings will successfully take the entire party across the river?
"""

from __future__ import annotations
from typing import List, Optional
from queue import Queue

MAX_NUM: int = 3


class Node:
    def __init__(self, state: MCState, parent: Optional[Node]):
        self.state = state
        self.parent = parent


class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries  # west bank missionaries
        self.wc: int = cannibals  # west bank cannibals
        self.em: int = MAX_NUM - self.wm  # east bank missionaries
        self.ec: int = MAX_NUM - self.wc  # east bank cannibals
        self.boat: bool = boat

    def __hash__(self):
        return hash((self.wm, self.wc, self.em, self.ec, self.boat))

    def __eq__(self, other):
        return (
            self.wm == other.wm
            and self.wc == other.wc
            and self.em == other.em
            and self.ec == other.ec
            and self.boat == other.boat
        )

    def __str__(self) -> str:
        return (
            f"On the west bank there are {self.wm} missionaries and "
            f"{self.wc} cannibals.\n"
            f"On the east bank there are {self.em} missionaries and "
            f"{self.ec} cannibals.\n"
            f"The boat is on the {'west' if self.boat else 'east'} bank."
        )

    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and 0 < self.wm:
            return False
        if self.em < self.ec and 0 < self.em:
            return False
        return True

    @staticmethod
    def goal_test(state: MCState) -> bool:
        """If goal is reached."""
        return state.is_legal and state.em == MAX_NUM and state.ec == MAX_NUM

    @staticmethod
    def successors(state) -> List[MCState]:
        sucs: List[MCState] = []

        # if boat on west bank
        if state.boat:
            if 1 < state.wm:
                sucs.append(MCState(state.wm - 2, state.wc, not state.boat))
            if 0 < state.wm:
                sucs.append(MCState(state.wm - 1, state.wc, not state.boat))
            if 1 < state.wc:
                sucs.append(MCState(state.wm, state.wc - 2, not state.boat))
            if 0 < state.wc:
                sucs.append(MCState(state.wm, state.wc - 1, not state.boat))
            if 0 < state.wc and 0 < state.wm:
                sucs.append(MCState(state.wm - 1, state.wc - 1, not state.boat))
        else:  # boat on east bank
            if 1 < state.em:
                sucs.append(MCState(state.wm + 2, state.wc, not state.boat))
            if 0 < state.em:
                sucs.append(MCState(state.wm + 1, state.wc, not state.boat))
            if 1 < state.ec:
                sucs.append(MCState(state.wm, state.wc + 2, not state.boat))
            if 0 < state.ec:
                sucs.append(MCState(state.wm, state.wc + 1, not state.boat))
            if 0 < state.ec and 0 < state.em:
                sucs.append(MCState(state.wm + 1, state.wc + 1, not state.boat))
        return [x for x in sucs if x.is_legal]

    def bfs(self) -> Optional[Node]:
        """Uses BFS to find solution"""
        frontier: Queue = Queue()
        frontier.put(Node(self, None))
        explored = {self}

        while not frontier.empty():
            current_node = frontier.get()
            current_state = current_node.state
            if MCState.goal_test(current_state):
                return current_node
            for child in MCState.successors(current_state):
                if child in explored:
                    continue
                explored.add(child)
                frontier.put(Node(child, current_node))
        return None

    @staticmethod
    def display_solution(solution) -> None:
        path = MCState.node_to_path(solution)
        print_separator = lambda: print("-" * 50, "\n")
        if len(path) == 0:
            return
        old_state = path[0]
        print("\n", old_state)
        print_separator()
        for current_state in path[1:]:
            if current_state.boat:
                print(
                    f"{old_state.em - current_state.em} missionaries and "
                    f"{old_state.ec - current_state.ec} cannibals moved from "
                    "the east bank to the west bank."
                )
            else:
                print(
                    f"{old_state.wm - current_state.wm} missionaries and "
                    f"{old_state.wc - current_state.wc} cannibals moved from "
                    "the west bank to the east bank"
                )
            print(current_state)
            print_separator()
            old_state = current_state

    @staticmethod
    def node_to_path(node: Node) -> List[MCState]:
        path = [node.state]
        while node.parent:
            node = node.parent
            path.append(node.state)
        path.reverse()
        return path


if __name__ == "__main__":
    mc = MCState(MAX_NUM, MAX_NUM, True)
    solution = mc.bfs()
    if solution is None:
        print("No solution found")
    else:
        MCState.display_solution(solution)
