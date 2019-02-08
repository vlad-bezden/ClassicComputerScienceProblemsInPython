from __future__ import annotations
from enum import Enum
from typing import NamedTuple, List, Tuple, Optional, Union
from random import uniform
from queue import LifoQueue, Queue


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "#"
    START = "S"
    GOAL = "G"
    PATH = "."


Grid = List[List[Cell]]


class MazeLocation(NamedTuple):
    row: int
    column: int

    def add(self, coord: Tuple[int, int]) -> MazeLocation:
        new_cell = MazeLocation(self.row + coord[0], self.column + coord[1])
        return new_cell


class Node:
    def __init__(
        self,
        state: MazeLocation,
        parent: Optional[Node],
        cost: float = 0.0,
        heuristic: float = 0.0,
    ) -> None:
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


class Maze:
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(
        self,
        rows: int = 10,
        columns: int = 10,
        sparseness: float = 0.2,
        start: MazeLocation = MazeLocation(0, 0),
        goal: MazeLocation = MazeLocation(9, 9),
    ) -> None:
        # initialize basic instance variables
        self._rows = rows
        self._columns = columns
        self.start = start
        self.goal = goal
        # fill the grid with empty cells
        self._grid: Grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        # populate the grid with blocked cells
        self._randomly_fill(sparseness)
        # fill the start and goal locations in
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, sparseness: float) -> None:
        for row in range(self._rows):
            for column in range(self._columns):
                if uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def goal_test(self, ml: MazeLocation) -> bool:
        """Checks if goals is reached"""
        return ml == self.goal

    def _is_valid_point(self, ml: MazeLocation) -> bool:
        """Checks if point inside of the maze"""
        return (
            0 <= ml.row
            and ml.row < self._rows
            and ml.column < self._columns
            and 0 <= ml.column
            and self._grid[ml.row][ml.column] != Cell.BLOCKED
        )

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        """Finds the possible next locations from a given point."""
        return [ml.add(l) for l in self.moves if self._is_valid_point(ml.add(l))]

    def mark(self, path: List[MazeLocation], marker: Cell) -> None:
        for ml in path:
            if ml != self.start and ml != self.goal:
                self._grid[ml.row][ml.column] = marker

    def __repr__(self) -> str:
        output = []
        for row in self._grid:
            output.append("".join([c.value for c in row]))
        return "\n".join(output)

    def calculate(self, frontier: Union[LifoQueue, Queue]) -> Optional[Node]:
        """Uses BFS or DFS based on the storage type."""
        # frontier is where we've yet to go
        frontier.put(Node(self.start, None))
        # explored is where we've been
        explored = {self.start}

        while not frontier.empty():
            current_node = frontier.get()
            current_state = current_node.state
            if self.goal_test(current_state):
                return current_node
            for child in self.successors(current_state):
                # skip children we already explored
                if child in explored:
                    continue
                explored.add(child)
                frontier.put(Node(child, current_node))
        return None

    @staticmethod
    def node_to_path(node: Node) -> List[MazeLocation]:
        path = [node.state]
        while node.parent:
            node = node.parent
            path.append(node.state)
        path.reverse()
        return path


if __name__ == "__main__":
    maze = Maze()

    # DFS
    solution1 = maze.calculate(LifoQueue())
    if solution1 is None:
        print(maze)
        print("No solution found using DFS!")
    else:
        path1 = maze.node_to_path(solution1)
        maze.mark(path1, Cell.PATH)
        print(maze)
        maze.mark(path1, Cell.EMPTY)
    print("-" * maze._columns)

    # BFS
    solution2 = maze.calculate(Queue())
    if solution2 is None:
        print(maze)
        print("No solution found using BFS!")
    else:
        path2 = maze.node_to_path(solution2)
        maze.mark(path2, Cell.PATH)
        print(maze)
        maze.mark(path2, Cell.EMPTY)
    print("-" * maze._columns)
