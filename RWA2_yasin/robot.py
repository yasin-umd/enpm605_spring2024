"""
This module contains the functions that control the robot's movement.
"""
from sys import exit
from random import randint
from random import choice as randomStr 
import maze as mz

# Robot emoji based on orientation
ROBOT = {
    "up" : "⏫",
    "left" : "⏪",
    "right" : "⏩",
    "down" : "⏬"
}


def move_forward():
    '''
    move_forward Move forward

    This method intends to move the robot one block forward according to current orientation (Left, Right, Up, Down)
    '''
    
    # Keep current postion for maze boundary validation
    current_position = [mz.robot_position[0], mz.robot_position[1]]
    
    # Empty the current postion before moving the robot to next position
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = "  "
    
    # Following if-elif block operates based on row-column concept. 
    # If robot orientation is up or down then the increament/decrement of 1 takes place for the row of robot position in the maze..
    # If robot orientation is left or right then the increament/decrement of 1 takes place for the column of robot position in the maze.
    if mz.robot_orientation == "up":
        mz.robot_position[0] -= 1
    elif mz.robot_orientation == "down":
        mz.robot_position[0] += 1
    elif mz.robot_orientation == "left":
        mz.robot_position[1] -= 1
    elif mz.robot_orientation == "right":
        mz.robot_position[1] += 1
    
    # Update robot to new position
    update_robot_position(current_position)
    
    return

def move_backward():
    '''
    move_backward Move Backward

    This method intends to move the robot one block backward according to current orientation (Left, Right, Up, Down)
    '''
    
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
    
    # Update robot to new position
    update_robot_position(current_position)
    
    pass

def turn_left():
    '''
    turn_left Turn left

    Process a left turn for the robot. Place a new emoji in robots current place based on previous and next orientation.
    '''
     
    # This dictionary contains current orientation as key and next orientation as value
    orientations_left = {
        'up' : 'left',
        'left' : 'down',
        'down' : 'right',
        'right' : 'up'
        
    }
    
    # Update robots new orientation and place the new emoji based on the new orientation 
    mz.robot_orientation = orientations_left[mz.robot_orientation]
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = ROBOT[mz.robot_orientation]
    
    pass

def turn_right():
    '''
    turn_right Turn Right

    Process a right turn for the robot. Place a new emoji in robots current place based on previous and next orientation.
    '''
    
    # This dictionary contains current orientation as key and next orientation as value
    orientations_right = {
        'up' : 'right',
        'right' : 'down',
        'down' : 'left',
        'left' : 'up'
        
    }
    
    # Update robots new orientation and place the new emoji based on the new orientation 
    mz.robot_orientation = orientations_right[mz.robot_orientation]
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = ROBOT[mz.robot_orientation]
    pass


def randomize_robot_position():
    '''
    randomize_robot_position Randomize Robot Position

    Call get_random_position() to get a randomly available block within the maze and place the robot accordingly.
    '''
    
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = "  "
    mz.robot_position = get_random_position()
    # Set orientation for the robot randomly
    mz.robot_orientation = randomStr(["up", "down", "left", "right"])
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = ROBOT[mz.robot_orientation]
    
    pass

def randomize_obstacles(number_of_obstacles: int = 3):
    '''
    randomize_obstacles Randomize Obstacles

    This method randomly allocates position of the obstacles for the robot.

    :param number_of_obstacles: Define how many obstacles to put within the maze. Default is 3 obstacles
    :type number_of_obstacles: int
    '''
 
    for i in range(number_of_obstacles):
        mz.obstacle_positions.append(get_random_position())
        mz.maze[mz.obstacle_positions[i][0]][mz.obstacle_positions[i][1]] = mz.OBSTACLE
    
    pass

def randomize_goal_position():
    '''
    randomize_goal_position Randomize Goal Position

    This function randomly selects the goal position for the Robot. When invoked, the robots's goal position will be shuffled withn the maze.
    '''
    
    mz.maze[mz.goal_position[0]][mz.goal_position[1]] = "  "
    mz.goal_position = get_random_position()
    mz.maze[mz.goal_position[0]][mz.goal_position[1]] = mz.GOAL
    
    pass

def get_random_position():
    '''
    get_random_position Get Random Position

    Get a randomly generated position for the robot within the maze. The function also validates whether the position is available or not. It only returns a position that is available. This funciton is used to randomize the goal position, robot position and obstacle positions.

    :return: Return the new random position
    :rtype: List
    '''
    while True: 
        # To-Do: Put the x, y values in a unique set so that the loop should not fall in infinite loop.
        x = randint(0, mz.MAZE_SIZE - 1)
        y = randint(0, mz.MAZE_SIZE - 1)
        if [x,y] not in mz.obstacle_positions and [x,y] != mz.robot_position and [x,y] != mz.goal_position:
            return [x, y]
    
    pass

def validate_path(current_position: list) -> bool:
    '''
    validate_path Validate Robot Path

    Validate robots next move. Check whether next moving block for robot is available or not. Validate for obstacles and maze boundary

    :param current_position: Robots existing position before movement. This is required to display the boom 💥 in current position if boundary validation fails.
    :type current_position: list
    :return: If next moving block is available then return true otherwise return false.
    :rtype: bool
    '''

    # Validate robots next move for obstacles. If robot hits a obstacle then place a boom "💥" in next position and print error message.
    if mz.robot_position in mz.obstacle_positions:
        mz.maze[mz.robot_position[0]][mz.robot_position[1]] = "💥"
        mz.print_maze()
        print("💥 Oops! You have hit an obstacle!!! 💥")
        return False
    
    # Validate robots next move for maze boundary. If robot hits maze boundary then place a boom "💥" in current position and print error message.
    if not (0 <= mz.robot_position[0] <mz.MAZE_SIZE) or not (0 <= mz.robot_position[1] < mz.MAZE_SIZE):
        mz.maze[current_position[0]][current_position[1]] = "💥"
        mz.print_maze()
        print("💥 Oops! You have hit the boundary of the maze!!! 💥")
        return False  
        
    return True

def update_robot_position(current_position: list):
    '''
    update_robot_position Update robot position

    Move Robot to it's new position after performing path validation

    :param current_position: Current position is required to show boom emoji if boundary validation fails.
    :type current_position: list
    '''

    # If validation fails then the validate_path prints a new maze with updated elements and terminates the program
    if validate_path(current_position) is False:
        exit()
    
    # Place the robot into it's new coordinates.
    mz.maze[mz.robot_position[0]][mz.robot_position[1]] = ROBOT[mz.robot_orientation]
    
    # If the robot has reached to goal position then print the new maze and terminate the program with a congratulation message.
    if mz.robot_position == mz.goal_position:
        mz.print_maze()
        print("🎉 Congratulations! You have reached the goal!!! 🎊")
        exit()
    
    pass