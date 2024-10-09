# Zombie Dice Shell

Zombie Dice Shell is a command-line interface for configuring and running simulations of the Zombie Dice game. It is inspired by a practice project [Zombie Dice Bots](https://automatetheboringstuff.com/2e/chapter6/#calibre_link-236) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

Zombie Dice Shell is a command-line interface for managing settings and running simulations based on the [Zombie Dice game](https://www.sjgames.com/dice/zombiedice/). It provides options to configure the game with different types of zombies and run simulations to observe gameplay outcomes, featuring custom zombie bots alongside built-in ones.

### Custom Zombies

Custom zombie bots written by me:

`my_zombies.py`: This file contains two custom zombie classes:
1. **BrainHunterZombie**: This zombie strives to hunt as many brains as possible during a turn, continuing to roll the dice if the number of brains hunted is less than 3.
2. **RiskTakerZombie**: This zombie takes risks to hunt as many brains as possible during a turn, continuing to roll dice even if the number of shotguns exceeds the number of brains hunted, but stopping if it collects a certain number of shotguns.

## How to Run

1. Install the `zombiedice` module if it's not already installed. You can install it via pip: `pip install zombiedice`
2. Clone the repository or download the `zombie_dice_shell.py` file.
3. Navigate to the directory containing `zombie_dice_shell.py`.
4. Run the script: `python zombie_dice_shell.py`.

## Usage Example

**1. List available zombies**
```shell
Welcome to Zombie Dice Shell. Type help or ? to list commands.
(ZombieDiceShell) > setup list
Available zombies:
- BrainHunterZombie
- RiskTakerZombie
- AlwaysRollsTwiceZombie
- CrashZombie
- HumanPlayerZombie
- MinNumShotgunsThenStopsOneMoreZombie
- MinNumShotgunsThenStopsZombie
- MonteCarloZombie
- RandomCoinFlipZombie
- RollsUntilInTheLeadZombie
- SlowZombie
```
**2. Add zombie to setup**
```shell
(ZombieDiceShell) > setup add BrainHunterZombie
Zombie 'BrainHunterZombie' added successfully.
```

**3. List current zombies setup**
```shell
(ZombieDiceShell) > setup current
Current zombies:
1. RandomCoinFlipZombie
2. RollsUntilInTheLeadZombie
3. MinNumShotgunsThenStopsZombie
4. MinNumShotgunsThenStopsZombie
5. BrainHunterZombie
```
**4. Run simulation with 100 turns**
```shell
(ZombieDiceShell) > run 100
Tournament of 100 games started...
Tournament results:
Wins:
    Stop at 2 Shotguns  39
     BrainHunterZombie  22
         Until Leading  21
     Stop at 1 Shotgun  14
                Random   4
Ties:
                Random   0
         Until Leading   0
    Stop at 2 Shotguns   0
     Stop at 1 Shotgun   0
     BrainHunterZombie   0
```

# Contents

1. `my_zombies.py`: Classes for my custom zombie bots for the Zombie Dice game.
2. `zombie_dice_shell.py`: Command-line interface for managing settings and running simulations of the Zombie Dice game.

## Requirements

- [zombiedice](https://pypi.org/project/zombiedice/)

## *Notes*

- The **cmd** module provides an easy way to create CLI. Its built-in methods are used to process commands, validate input, and provide help information.
- **Classes and class methods** helped structure the project, making it more organized and easily extensible. Zombie classes allow you to abstract the logic and state of zombies, making their management more convenient and efficient.
- **argparse** module allows for flexibility and reliability in handling command line argument input from a user.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)