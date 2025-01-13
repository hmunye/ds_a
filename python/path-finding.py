# The maze is represented as a list of strings where each string contains
# characters such as walls (denoted by pound signs) and the starting and ending
# points of the maze. The goal is to navigate from the start to the end while
# avoiding walls

# Bases Cases:
# - If the spot is a wall
# - If the spot is off the maze
# - If the end was found
# - If the spot has already been traversed

from dataclasses import dataclass


# A `dataclass` in Python is a decorator that automatically generates special
# methods for classes used primarily to store data
@dataclass
class Point:
    x: int
    y: int


directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]


def walk(
    maze: list[str],
    wall: str,
    current: Point,
    end: Point,
    seen: list[list[bool]],
    path: list[Point],
) -> bool:
    # Base Case
    if (
        current.x < 0
        or current.x >= len(maze[0])
        or current.y < 0
        or current.y >= len(maze)
    ):
        return False

    # Base Case
    if maze[current.y][current.x] == "#":
        return False

    # Base Case
    if current.x == end.x and current.y == end.y:
        path.append(end)
        return True

    # Base Case
    if seen[current.y][current.x]:
        return False

    # Pre-condition
    seen[current.y][current.x] = True
    path.append(current)

    # Recurse-condition
    for i in range(len(directions)):
        [x, y] = directions[i]

        if walk(maze, wall, Point(current.x + x, current.y + y), end, seen, path):
            return True

    # Post-condition
    path.pop()

    return False


def maze_solver(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    seen: list[list[bool]] = [[]]
    path: list[Point] = []

    for _ in range(len(maze)):
        seen.append([False] * len(maze[0]))

    walk(maze, wall, start, end, seen, path)

    return path


maze = ["#######", "#S    #", "# # # #", "# # # #", "#     E", "#######"]

start = Point(1, 1)
end = Point(5, 4)

path = maze_solver(maze, "#", start, end)

print(path)

# The algorithm begins at a point (like x0) and attempts to move in different
# directions (up, right, down, left). If it hits a wall or revisits a position,
# it backtracks by removing the current position from the stack and tries another
# direction. This process continues recursively, marking each visited position as
# "true" in a seen array. When a dead-end is encountered, the algorithm pops
# the current position off the stack and returns to the previous position,
# checking other directions until it either finds the exit or exhausts all possible
# paths. The order in which the directions are explored doesn’t impact performance
# significantly, as the algorithm will eventually explore all paths. The time
# complexity is linear, O(N), because each square in the maze is checked up to
# four times, corresponding to the four possible directions, where N is the total
# number of squares
