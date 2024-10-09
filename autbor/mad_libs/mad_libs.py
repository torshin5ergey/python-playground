"""
mad_libs.py - Mad Libs CLI word game

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

import os
import sys
from pathlib import Path
import re
from typing import List, Dict
import pyinputplus as pyip


def parse_stories_files() -> List[str]:
    """List all stories files from designated directory.
    
    Returns:
        List[str]: A list of filenames with .txt extension.
    """
    stories_path = os.path.dirname(sys.argv[0]) / Path("./stories")
    files = os.listdir(stories_path)
    # Filter only txt
    files = [file for file in files if file.endswith(".txt")]
    return files


def list_stories(files: List[str]) -> Dict[str, List[str]]:
    """Organize story files by their base names.

    Args:
        files (List[str]): A list of filenames.

    Returns:
        Dict[str, List[str]]: A dictionary with story base names as keys and
        lists of corresponding filenames as values.
    """
    stories = {}
    story_regex = re.compile(r'(.+)-[a-zA-Z]{2}\.txt$')
    for file in files:
        story = re.search(story_regex, file).group(1)
        if story not in stories:
            stories[story] = [file]
        else:
            stories[story].append(file)
    return stories


def choose_story(stories: Dict[str, List[str]]):
    """Prompt the user to choose a story to play.

    Args:
        stories (Dict[str, List[str]]): A dictionary of stories.

    Returns:
        str: The chosen story base name.
    """
    if len(stories) < 2:
        print(f"There is only one story: {list(stories.keys())[0]}.")
        # Get the only one dict element
        story_to_play = list(stories.keys())[0]
    else:
        story_to_play = pyip.inputMenu(list(stories.keys()),
                                       numbered=True,
                                       prompt="Select the story you want to play:\n")
    return story_to_play

def choose_story_version(filenames: List[str]) -> str:
    """Prompt the user to choose a version of the selected story.

    Args:
        story (str): The base name of the story.
        filenames (List[str]): A list of filenames for the story.

    Returns:
        Path: The path to the chosen story version file.
    """
    versions = [f.rstrip(".txt") for f in filenames]
    version = pyip.inputMenu(list(versions),
                             numbered=True,
                             prompt=(f"This story has {len(filenames)} versions."
                                     " Choose the one you want to play:\n"))
    filename =  version + ".txt"
    path = os.path.dirname(sys.argv[0]) / Path("./stories") / filename
    return path


def find_story_file(story: str, files: List[str]) -> Path:
    """Find the file path for a given story.

    Args:
        story (str): The base name of the story.
        files (List[str]): A list of filenames.

    Returns:
        Path: The path to the story file.
    """
    for f in files:
        if story in f:
            return os.path.dirname(sys.argv[0]) / Path("./stories") / f
    raise FileNotFoundError(f"Story file for '{story}' not found.")

def find_placeholders(text: str) -> Dict[str, List[str]]:
    """Find all placeholders in the text.

    Args:
        text (str): The story text.

    Returns:
        List[str]: A list of placeholders found in the text.
    """
    placeholders = re.findall(r'\b(NOUN|VERB|ADJECTIVE)\b', text)
    return placeholders


def replace_placeholders(text: str, placeholders: List[str], answers: List[str]):
    """Replace placeholders in the text with user-provided answers.

    Args:
        text (str): The story text.
        placeholders (List[str]): A list of placeholders.
        answers (List[str]): A list of user-provided words.

    Returns:
        str: The text with placeholders replaced by user-provided words.
    """
    for i, v in enumerate(placeholders):
        text = text.replace(v, answers[i], 1)
    return text


def main():
    """Main."""
    # Menu
    print("--Mad Libs Game--\n")
    stories_files = parse_stories_files()
    stories = list_stories(stories_files)
    story_to_play = choose_story(stories)
    if len(stories[story_to_play]) > 1:  # One story version
        text_file = choose_story_version(stories[story_to_play])
    else:
        text_file = find_story_file(story_to_play, stories_files)

    # Game
    print(f"\nLet's play the {story_to_play.title()} story!")
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    pls = find_placeholders(text)
    user = [input(f"Enter {pls[i].lower()}: ") for i in range(len(pls))]
    new_text = replace_placeholders(text, pls, user)
    print('\n--Your text--\n')
    print(new_text)


if __name__ == "__main__":
    main()
