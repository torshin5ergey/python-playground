'''
my_zombies.py - Simple zombie bots for zombiedice game
Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
'''

import zombiedice

class BrainHunterZombie:
    '''
    This zombie strives to hunt as many brains as possible during a turn. If the
    number of brains hunted on the current turn exceeds 3, he will keep rolling
    the dice in search of more brains.
    '''
    def __init__(self, name: str):
        self.name = name

    def turn(self, game_state: dict) -> None:
        # game_state (dict): Info about the current state of the game
        dice_roll_results = zombiedice.roll()
        brains = 0
        brains_to_continue = 3

        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            if brains < brains_to_continue:
                dice_roll_results = zombiedice.roll()
            else:
                break

class RiskTakerZombie:
    '''
    This zombie takes risks to hunt as many brains as possible during a turn. It
    continues rolling dice even if the number of shotguns exceeds the number of
    brains hunted, but stops if it collects a certain number of shotguns.
    '''
    def __init__(self, name: str):
        self.name = name

    def turn(self, game_state: dict) -> None:
        # game_state (dict): Info about the current state of the game
        dice_roll_results = zombiedice.roll()
        brains = 0
        shotguns = 0
        shotguns_to_stop = 2

        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            shotguns += dice_roll_results['shotgun']
            if shotguns < shotguns_to_stop:
                dice_roll_results = zombiedice.roll()
            else:
                break
