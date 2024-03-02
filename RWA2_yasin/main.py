"""
This is the main file which contains the entry point of your program.
"""
from maze import print_maze
from sys import exit
import robot as rbt


#This color dictionary is used to set the color for terminal texts.
TEXT_COLOR = {"danger" : "\033[91m", "reset" : "\033[0m"}


def main():
    
    # Randomize robot postion, goal position and obstacle positions. Default number of obstacle is 3. 
    rbt.randomize_goal_position()
    rbt.randomize_obstacles() # Call with number of obstacles to get a specific number of obstacles. Eg. rbt.randomize_obstacles(5)
    rbt.randomize_robot_position()
    
    print("Initial Maze:")
    print_maze()
    while True:
        update_action()            
        print_maze()

def update_action():
    '''
    update_action Update Action

    Perform movement operation within the maze according to user inputs. Possible operations are - w: forward, s: backward, a: left, d: right, q: quit
    '''
    
    action = input("Enter action (w: forward, s: backward, a: left, d: right, q: quit): ")
    if action == "a":
        rbt.turn_left()
    elif action == "d":
        rbt.turn_right() 
    elif action == "w":
        rbt.move_forward()
    elif action == "s":
        rbt.move_backward()
    elif action =="q":
        print("Quitting the maze game!!!")
        exit()
    else:
        print(f"{TEXT_COLOR['danger']}Invalid action.! Please enter a valid action!{TEXT_COLOR['reset']}")
    
    pass  
    
# Run the main function
if __name__ == "__main__":
    main()
