"""
This is the main file which contains the entry point of your program.
"""

from maze import print_maze
import robot as rbt

def main():
    print("Initial Maze:")
    print_maze()
    while True:
        action = input("Enter action (w: forward, s: backward, a: left, d: right, q: quit): ")
        # TODO write the main function
        # Ctrl-c to stop the program
        if action == "a":
            rbt.turn_left()
        elif action == "d":
            rbt.turn_right() 
        elif action == "w":
            rbt.move_forward()
        elif action =="s":
            rbt.move_backward()
        print_maze()


# Run the main function
if __name__ == "__main__":
    main()
