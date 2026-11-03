# 8-Puzzle using A* Search
# Heuristic: Number of Misplaced Tiles

def display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    # Up
    if row > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 3] = \
            new_state[blank - 3], new_state[blank]
        neighbors.append(tuple(new_state))

    # Down
    if row < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]
        neighbors.append(tuple(new_state))

    # Left
    if col > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]
        neighbors.append(tuple(new_state))

    # Right
    if col < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]
        neighbors.append(tuple(new_state))

    return neighbors


def misplaced_tiles(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


def a_star(start, goal):

    # OPEN = [state, path, g, f]
    open_list = [
        (start, [start], 0, misplaced_tiles(start, goal))
    ]

    visited = set()

    while open_list:

        # Select state with smallest f value
        open_list.sort(key=lambda x: x[3])

        state, path, g, f = open_list.pop(0)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_neighbors(state):

            if next_state not in visited:

                new_g = g + 1
                h = misplaced_tiles(next_state, goal)
                new_f = new_g + h

                new_path = path + [next_state]

                open_list.append(
                    (next_state, new_path, new_g, new_f)
                )

    return None


# Main program

start = tuple(map(int, input(
    "Enter initial state (use 0 for blank): "
).split()))

goal = tuple(map(int, input(
    "Enter goal state: "
).split()))

print("\nInitial State:")
display(start)

print("Goal State:")
display(goal)

solution = a_star(start, goal)

if solution:

    print("Solution Found!")
    print("Number of moves:", len(solution) - 1)

    print("\nSolution Path:")

    for i, state in enumerate(solution):
        print("Step", i)
        display(state)

else:
    print("Solution Not Found!")