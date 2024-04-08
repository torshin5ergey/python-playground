'''
zombie_dice_shell.py - CLI for zombie dice games.
Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
'''

import cmd
import sys
import argparse
import zombiedice
from my_zombies import *

# Create interactive shell interface
class ZombieDiceShell(cmd.Cmd):
# class ZombieDiceShell:

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Zombie Dice Shell. Type help or ? to list commands.'
        self.prompt = '(ZombieDiceShell) > '
        # Default zombies setup
        self.zombies = [
            zombiedice.examples.RandomCoinFlipZombie(name='Random'),
            zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
            zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
            zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
        ]
        # Available zombies
        # Add my zombies
        self.available_zombies = [
            BrainHunterZombie.__name__,
            RiskTakerZombie.__name__
        ]
        # Add example zombies
        # Get all attributes of the module
        example_zombies = dir(zombiedice.examples)
        for zombie in example_zombies:
            # Get class by name
            obj = getattr(zombiedice.examples, zombie)
            if isinstance(obj, type):
                self.available_zombies.append(zombie)         
    
    def show_current_zombies(self):
        print("Current zombies:")
        for i, zombie in enumerate(self.zombies):
            print(f'{i+1}.', zombie.__class__.__name__)
        
    def show_available_zombies(self):
        print("Available zombies:")
        for i, zombie in enumerate(self.available_zombies):
            print(f'- {zombie}')
    
    def add_zombie(self, name: str):
        try:
            # Get all globals
            zombie_class = globals()[name]
            self.zombies.append(zombie_class(name))
            print(f"Zombie '{name}' added successfully.")
        except KeyError:
            print(f"Error: Zombie '{name}' is not available.")
        except Exception as e:
            print(f"Error {e}: Failed to create zombie '{name}'.")

    def remove_zombie(self, name: str):
        try:
            for zombie in self.zombies:
                if zombie.__class__.__name__ == name:
                    self.zombies.remove(zombie)
                    print(f"Zombie '{name}' removed successfully.")
                    break
            else:
                print(f"Zombie '{name}' not found in the current zombies.")
        except Exception as e:
            print(f"Error {e}: Failed to remove zombie '{name}'.")  

    # ----- Commands -----
    def do_run(self, arg: str) -> None:
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('num_games', nargs='?', type=int, default=1000)
        args = parser.parse_args(arg.split())
        zombiedice.runTournament(zombies = self.zombies, numGames = args.num_games)
    def help_run(self):
        print("""Run the Zombie Dice simulation.
syntax: run [num_games]
Parameters:
\tnum_games (optional): Number of games to simulate (default: 1000)""")
    
    def do_setup(self, arg: str):
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('command', nargs='?', type=str, default='current',
                            choices=['current', 'list', 'add', 'remove'])
        parser.add_argument('zombie_name', nargs='?', type=str)
        args = parser.parse_args(arg.split())
        if args.command == 'current':
            self.show_current_zombies()
        elif args.command == 'list':
            self.show_available_zombies()
        elif args.command == 'add':
            if args.zombie_name:
                self.add_zombie(args.zombie_name)
            else:
                print("Error: Zombie name cannot be empty.")
        elif args.command == 'remove':
            if args.zombie_name:
                self.remove_zombie(args.zombie_name)
            else:
                print("Error: Zombie name cannot be empty.")
    def help_setup(self):
        print("""Setup the simulation.
syntax: setup [command]
Command options:
\t- current: display current setup
\t- list: list available zombies
\t- add <zombie_name>: add zombie with name <zombie_name> to current setup
\t- remove <zombie_name>: remove zombie with name <zombie_name> from current setup""")

    def do_quit(self, arg):
        sys.exit()
    def help_quit(self):
        print("Quit the program.")

def main():
    ZombieDiceShell().cmdloop()
    
if __name__ == "__main__":
    main()