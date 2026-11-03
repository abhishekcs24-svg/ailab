import itertools

def calculate_cost(state):
    """
    Calculates the cost function: The number of pairs of queens 
    attacking each other, directly or indirectly.
    """
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Diagonal conflict: |row_i - row_j| == |col_i - col_j|
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def get_neighbors(state):
    """
    Generates all unique neighbors by swapping the row positions of two queens.
    Returns a list of tuples: (neighbor_state, swapped_pair_indices)
    """
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            neighbor = list(state)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append((tuple(neighbor), (i, j)))
    return neighbors

def print_board(state):
    """
    Prints a visual text-based grid representation of the n-queens board.
    """
    n = len(state)
    print("\nFinal Board Configuration:")
    for r in range(n):
        print("+" + "---+" * n)
        row_str = ""
        for c in range(n):
            if state[c] == r:
                row_str += "| Q "
            else:
                row_str += "|   "
        row_str += "|"
        print(row_str)
    print("+" + "---+" * n)

def hill_climbing_4_queens(initial_state):
    current_state = tuple(initial_state)
    current_cost = calculate_cost(current_state)
    
    step = 0
    print(f"=== Step {step} ===")
    print(f"Current State: {current_state} | Cost: {current_cost}\n")
    
    while True:
        neighbors = get_neighbors(current_state)
        best_neighbor = None
        best_cost = float('inf')
        chosen_swap = None
        
        print("Evaluating Neighbors (Swaps):")
        for neighbor, swap in neighbors:
            cost = calculate_cost(neighbor)
            print(f"  Swap {swap} -> State: {neighbor} | Cost: {cost}")
            
            # Steepest descent check
            if cost < best_cost:
                best_cost = cost
                best_neighbor = neighbor
                chosen_swap = swap
            # Tie-breaking rule rule from image
            elif cost == best_cost:
                if chosen_swap is None or swap < chosen_swap:
                    best_cost = cost
                    best_neighbor = neighbor
                    chosen_swap = swap
        
        print(f"\nBest Neighbor found: State: {best_neighbor} | Cost: {best_cost} via Swap {chosen_swap}")
        
        # Termination condition
        if best_cost >= current_cost:
            print("\nTermination: No neighbor has a lower cost than the current state.")
            print(f"Final local optimum state: {current_state} with Cost: {current_cost}")
            print_board(current_state)
            break
            
        # Move to the best neighbor
        current_state = best_neighbor
        current_cost = best_cost
        step += 1
        
        print(f"\n=== Step {step} ===")
        print(f"Current State: {current_state} | Cost: {current_cost}\n")
        
        if current_cost == 0:
            print("Goal configuration reached!")
            print_board(current_state)
            break

# Define the initial state from the image: x0=3, x1=1, x2=2, x3=0
initial_state = [3, 1, 2, 0]
hill_climbing_4_queens(initial_state)
