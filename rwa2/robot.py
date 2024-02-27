"""
This module contains the functions that control the robot's movement.
"""
from sys import exit
import maze as mz

ROBOT = {
    "up" : "⏫",
    "left" : "⏪",
    "right" : "⏩",
    "down" : "⏬"
}

def validate_path(current_position):    
    if mz.robot_position in mz.obstacle_positions:
        mz.maze[mz.robot_position[0]][mz.robot_position[1]] = "💥"
        mz.print_maze()
        print("💥 Oops! You have hit the an obstacle!!! 💥")
        return False
    
    if not (0 <= mz.robot_position[0], mz.robot_position[1] <mz.MAZE_SIZE) or not (0 <= mz.robot_position[0] < mz.MAZE_SIZE):
        mz.maze[current_position[0]][current_position[1]] = "💥"
        mz.print_maze()
        print("💥 Oops! You have hit the boundary of the maze!!! 💥")
        return False      
    return True

def move_forward():
    """
    TODO: Write documentation and implement this function
    """    
    # Keep current postion for boundary validation
    current_position = [mz.robot_position[0], mz.robot_position[1]]
    
    # Empty the current postion before moving the robot to next poition
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = "  "
    if mz.robot_orientation == "up":
        mz.robot_position[0] -= 1
    elif mz.robot_orientation == "down":
        mz.robot_position[0] += 1
    elif mz.robot_orientation == "left":
        mz.robot_position[1] -= 1
    elif mz.robot_orientation == "right":
        mz.robot_position[1] += 1
        
    if validate_path(current_position) is False:
        exit()
        
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = ROBOT[mz.robot_orientation]
    return

def move_backward():
    """
    TODO: Write documentation and implement this function
    """
    # Keep current postion for boundary validation
    current_position = [mz.robot_position[0], mz.robot_position[1]]
    
    # Empty the current postion before moving the robot to next poition
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = "  "
    if mz.robot_orientation == "up":
        mz.robot_position[0] += 1
    elif mz.robot_orientation == "down":
        mz.robot_position[0] -= 1
    elif mz.robot_orientation == "left":
        mz.robot_position[1] += 1
    elif mz.robot_orientation == "right":
        mz.robot_position[1] -= 1
        
    if validate_path(current_position) is False:
        exit()
            
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = ROBOT[mz.robot_orientation]
    if mz.robot_position == mz.goal_position:
        print("🎊 Congratulations! You have reached the goal!!! 🎊")
    return

def turn_left():
    """
    TODO: Write documentation and implement this function
    """    
    # This dictionary contains current orientation as key and next orientation as value
    orientations_left = {
        'up' : 'left',
        'left' : 'down',
        'down' : 'right',
        'right' : 'up'
        
    }
    mz.robot_orientation = orientations_left[mz.robot_orientation]
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = ROBOT[mz.robot_orientation]
    print(mz.robot_orientation)
    pass

def turn_right():
    """
    TODO: Write documentation and implement this function
    """
    # This dictionary contains current orientation as key and next orientation as value
    orientations_right = {
        'up' : 'right',
        'right' : 'down',
        'down' : 'left',
        'left' : 'up'
        
    }
    mz.robot_orientation = orientations_right[mz.robot_orientation]
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = ROBOT[mz.robot_orientation]
    print(mz.robot_orientation)
    pass


