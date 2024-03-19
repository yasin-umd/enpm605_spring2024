class Maze:
    """
    This class contains the maze and the robot's initial position, as well as functions to print the maze and move the robot.

    Attributes:
    - grid_size (int): the size of the maze
    - player_position (tuple): the player's initial position
    - obstacle_positions (list of tuples): the positions of the obstacles
    - goal_position (tuple): the position of the goal
    - empty (str): the string to represent an empty cell
    - obstacle (str): the string to represent an obstacle
    - goal (str): the string to represent the goal
    - skeleton (str): the string to represent a skeleton
    - zombie (str): the string to represent a zombie
    - player (str): the string to represent the player
    - horizontal_wall (str): the string to represent a horizontal wall
    - vertical_wall (str): the string to represent a vertical wall
    - corner (str): the string to represent a corner

    """

    _cls_grid_size = 10
    _cls_empty = "  "
    _cls_obstacle = "🟥"
    _cls_obstacle_positions = [
        (0, 6),
        (1, 1),
        (1, 3),
        (1, 4),
        (1, 6),
        (1, 8),
        (1, 9),
        (2, 1),
        (2, 4),
        (2, 6),
        (3, 2),
        (3, 4),
        (3, 7),
        (3, 8),
        (4, 0),
        (4, 2),
        (4, 4),
        (4, 5),
        (4, 8),
        (5, 2),
        (5, 6),
        (6, 1),
        (6, 2),
        (6, 3),
        (6, 4),
        (6, 6),
        (6, 7),
        (6, 8),
        (6, 9),
        (7, 4),
        (7, 6),
        (8, 0),
        (8, 1),
        (8, 2),
        (8, 4),
        (8, 6),
        (8, 8),
        (9, 4),
        (9, 8),
    ]
    _cls_goal = "🏆"
    _cls_goal_position = (9, 0)
    _cls_skeleton = "💀"
    _cls_skeleton_positions = [(1, 2), (2, 3), (3, 4)]
    _cls_zombie = "🧟"
    _cls_zombie_positions = [(5, 8)]
    _cls_player = "⏫"
    _cls_player_position = (9, 9)
    _cls_padlock = "🔒"
    _cls_padlock_positions = [(9, 6)]
    _cls_key = "🔑"
    _cls_key_positions = [(8, 9)]
    _cls_arrow = "🏹"
    _cls_arrow_positions = [(7, 7)]
    _cls_heart = "💖"
    _cls_heart_positions = [(1, 7), (2, 8), (3, 9)]
    _cls_horizontal_wall = "──"
    _cls_vertical_wall = "│"
    _cls_corner = "┼"

    def __init__(self):
        self._grid_size = self._cls_grid_size
        self._player_position = self._cls_player_position
        self._obstacle_positions = self._cls_obstacle_positions
        self._goal_position = self._cls_goal_position
        # Create the grid
        self._grid = [
            [self._cls_empty] * self._grid_size for _ in range(self._grid_size)
        ]
        self.spawn_player()
        self.spawn_obstacles()
        self.spawn_goal()
        # self.spawn_skeletons()
        self.spawn_zombies()
        self.spawn_padlocks()
        self.spawn_keys()
        self.spawn_arrows()
        # self.spawn_hearts()

    def spawn_player(self):
        """
        Spawn the player on the grid.
        """
        self._grid[self._player_position[0]][self._player_position[1]] = (
            self._cls_player
        )

    def spawn_obstacles(self):
        """
        Spawn the obstacles on the grid.
        """
        for position in self._obstacle_positions:
            self._grid[position[0]][position[1]] = self._cls_obstacle

    def spawn_goal(self):
        """
        Spawn the goal on the grid.
        """
        self._grid[self._goal_position[0]][self._goal_position[1]] = self._cls_goal

    def spawn_skeletons(self):
        """
        Spawn the skeletons on the grid.
        """
        for position in self._cls_skeleton_positions:
            self._grid[position[0]][position[1]] = self._cls_skeleton

    def spawn_zombies(self):
        """
        Spawn the zombies on the grid.
        """
        for position in self._cls_zombie_positions:
            self._grid[position[0]][position[1]] = self._cls_zombie

    def spawn_padlocks(self):
        """
        Spawn the padlocks on the grid.
        """
        for position in self._cls_padlock_positions:
            self._grid[position[0]][position[1]] = self._cls_padlock

    def spawn_keys(self):
        """
        Spawn the keys on the grid.
        """
        for position in self._cls_key_positions:
            self._grid[position[0]][position[1]] = self._cls_key

    def spawn_arrows(self):
        """
        Spawn the arrows on the grid.
        """
        for position in self._cls_arrow_positions:
            self._grid[position[0]][position[1]] = self._cls_arrow

    def spawn_hearts(self):
        """
        Spawn the hearts on the grid.
        """
        for position in self._cls_heart_positions:
            self._grid[position[0]][position[1]] = self._cls_heart

    def print_maze(self):
        """
        Print the maze.
        """

        print("  0  1  2  3  4  5  6  7  8  9")
        print("┌" + "─" * (self._cls_grid_size * 3 - 1) + "┐")

        for i, row in enumerate(self._grid):
            # Print left boundary
            print(self._cls_vertical_wall, end="")

            # Print cell contents
            for j, cell in enumerate(row):
                print(cell, end="")
                # Print vertical wall if not in the last column
                if j < self._cls_grid_size - 1:
                    print(self._cls_vertical_wall, end="")

            # Print right boundary
            print(self._cls_vertical_wall)

            # Print horizontal wall between rows (except for the last row)
            if i < self._cls_grid_size - 1:
                print("├" + "─" * (self._cls_grid_size * 3 - 1) + "┤")

        # Print bottom boundary
        print("└" + "─" * (self._cls_grid_size * 3 - 1) + "┘")


if __name__ == "__main__":
    maze = Maze()
    maze.print_maze()
