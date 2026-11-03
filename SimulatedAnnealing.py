import math
import random


def get_cost(state):
    """Calculates the number of attacking pairs of queens (cost).

    A cost of 0 means a valid solution is found.
    """
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if they are in the same row or same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks


def get_random_neighbour(state):
    """Generates a neighbour by moving one random queen to a different row in its column."""
    neighbour = list(state)
    col = random.randint(0, 7)
    current_row = state[col]

    # Choose a new row that is different from the current row
    new_row = random.choice([r for r in range(8) if r != current_row])
    neighbour[col] = new_row
    return neighbour


def simulated_annealing():
    # 1: current <- initial state (random row for each of the 8 columns)
    current = [random.randint(0, 7) for _ in range(8)]
    current_cost = get_cost(current)

    # 2: T <- a large positive value
    T = 100.0
    cooling_rate = 0.995
    absolute_temperature = 0.00001

    # 3: while T > 0 do (using a tiny positive threshold to avoid infinite precision limits)
    while T > absolute_temperature:
        # If we found a solution with 0 attacking pairs, we can stop early
        if current_cost == 0:
            break

        # 4: next <- a random neighbour of current
        nxt = get_random_neighbour(current)
        nxt_cost = get_cost(nxt)

        # 5: ΔE <- current.cost - next.cost
        delta_E = current_cost - nxt_cost

        # 6: if ΔE > 0 then
        if delta_E > 0:
            # 7: current <- next
            current = nxt
            current_cost = nxt_cost
        # 8: else
        else:
            # 9: current <- next with probability p = e^(ΔE / T)
            p = math.exp(delta_E / T)
            if random.random() < p:
                current = nxt
                current_cost = nxt_cost

        # 11: decrease T
        T *= cooling_rate

    # 13: return current
    return current, current_cost


def print_board(state):
    """Helper to visualize the 8x8 chessboard layout."""
    for row in range(8):
        line = ""
        for col in range(8):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)


# --- Execution ---
if __name__ == "__main__":
    # Simulated Annealing can occasionally get stuck if T drops too fast,
    # so we run it until a perfect solution (cost = 0) is found.
    attempts = 0
    while True:
        attempts += 1
        solution, final_cost = simulated_annealing()
        if final_cost == 0:
            print(f" Solution found after {attempts} attempt(s)!")
            print(f"Final State (Row indices per column): {solution}")
            print("\nVisual Board Layout:")
            print_board(solution)
            break
