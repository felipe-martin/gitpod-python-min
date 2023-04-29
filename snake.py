import random
import time 

def game():
    # Set up initial board and food on the board.
    board = [" "] * 100
    x_position = random.randint(1, 9)
    o_position = random.randint(1, 9)
    board[x_position-1] = "#"
    board[o_position-1] = "#"
    print("Your position is: ", (x_position))
    time.sleep(2)

    # Game loop continues until one of them wins or draw occurs.
    while True:
        board = input()
        
        # Find direction from user's current position to its next move.
        new_position = get_direction((board),(x_position), 8)
    
        if new_position != -1:
            # Move snake head towards new position.
            board = add_snnake_head(board,new_position)
            
            # Check if the snake has eaten any food available.
            check_food(board, (x_position))
    
            # Update score and show it after every successful moves.
            score += 1
            score_display(score)

def main():
    """This function initializes the game with instructions."""
    print("Welcome to SnakeGame")
    print("\nInstructions: Type 'exit' to quit or type anything else to start playing.")
    choice = input("What would you like to do? ")
    if choice == 'exit':
        exit()
    elif choice != 'play':
        print("Invalid instruction.")
        return False
    else:
        return game()

main()
input("Presione cualquier tecla para salir...")
