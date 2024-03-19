
import rpg.player 
"""
This file contains the Enemy class.
"""

class Enemy():
    """
    A class representing an enemy in the game.

    Attributes:
        name (str): The name of the enemy.
        health (int): The health of the enemy.
    """

    def __init__(self, name="Enemy", health=50):
        self._name = name
        self._health = health
        
    @property
    def name(self):
        """
        str: The name of the enemy.
        """
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("The name must be a string.")

    def __str__(self):
        """
        Returns the string representation of the enemy.

        Returns:
            str: The string representation of the enemy.
        """
        return f"{self._name} has {self._health} health."
    
    def __repr__(self):
        """
        Returns the string representation of the enemy.

        Returns:
            str: The string representation of the enemy.
        """
        return f"{self._name} has {self._health} health."

    def attack(self, player: rpg.player.Player, damage):
        """
        Attack the player.

        Args:
            player (Player): The player to attack.
            damage (int): The amount of damage to deal.
        """
        print(f"🧟🗡️ {self._name} attacks {player.name}!")
        player.take_damage(damage)

    def take_damage(self, damage):
        """
        Take damage from the player.

        Args:
            damage (int): The amount of damage to take.
        """
        self._health -= damage
        if self._health <= 0:
            print(f"🧟💀 {self._name} has been defeated!")
        else:
            print(f"🧟💜 {self._name} has {self._health} health left.")


class Skeleton(Enemy):
    """
    A class representing a skeleton enemy in the game. All skeletons have a shield power. The health of a skeleton is 50.
    
    Attributes:
        shield_power (int): The power of the skeleton's shield.
    """

    def __init__(self, shield_power, name="Skeleton"):
        super().__init__(name=name, health=50)
        self._shield_power = shield_power
        
    def take_damage(self, damage):
        """
        Take damage from the player.

        Args:
            damage (int): The amount of damage to take.
        """
        super().take_damage(damage - self._shield_power)
        
class Dragon(Enemy):
    """
    A class representing a dragon enemy in the game. All dragons have a fire breath power. The health of a dragon is 200.
    
    Attributes:
        fire_breath_power (int): The power of the dragon's fire breath.
    """

    def __init__(self, fire_breath_power, name="Dragon"):
        super().__init__(name=name, health=80)
        self._fire_breath_power = fire_breath_power

    def attack(self, player: rpg.player.Player, damage):
        """
        Attack the player.

        Args:
            player (Player): The player to attack.
            damage (int): The amount of damage to deal.
        """
        super().attack(player, damage + self._fire_breath_power)
 
        
if __name__ == "__main__":
    print("Creating an enemy:")
    enemy = Enemy()
    enemy.attack(rpg.player.Player(), 10)