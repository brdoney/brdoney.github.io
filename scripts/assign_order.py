# !/usr/bin/python3

import os
import re
import fileinput
from typing import Dict, List

start_dir = "./_docs/java/"
type_regex = re.compile(r"type: (\w+)")
order_regex = re.compile(r"order: (\w+)")


class ParsedFile:

    def __init__(self, path: str) -> None:
        self.path = path
        self._current_order = None
        self.doc_type = None

        with open(path, "r") as f:
            for line in f:
                if self._current_order is None:
                    match = order_regex.match(line)
                    if match is not None:
                        self._current_order = int(match.group(1))
                elif self.doc_type is None:
                    match = type_regex.match(line)
                    if match is not None:
                        self.doc_type = match.group(1)

    def get_order(self):
        return self._current_order

    def set_order(self, order: int):
        matched = False
        f = fileinput.input(self.path, inplace=True)
        for line in f:
            # Prints here are directed to the output file, not terminal stdout
            if not matched and order_regex.match(line) is not None:
                print(f"order: {order}")
                matched = True
            else:
                print(line, end="")

        self._current_order = order

    def __repr__(self) -> str:
        return f"'{self.path}' {self._current_order} - {self.doc_type}"


def get_type_map(parsed_files: List[ParsedFile]) -> Dict[str, List[ParsedFile]]:
    type_map = {"lesson": [], "exercise": []}
    for file in parsed_files:
        t = file.doc_type
        if t is not None:
            type_map[t].append(file)
    return type_map


def order_is_ascending(starting_order: int,
                       parsed_files: List[ParsedFile]) -> bool:
    orders = {file.get_order() for file in parsed_files}
    expected = set(range(starting_order, starting_order + len(parsed_files)))
    return orders == expected


def prompt_order_change(parsed_file: ParsedFile, suggested_order: int) -> int:
    try:
        new_order = input(f"{parsed_file.path} -> {suggested_order} ? ")
        if len(new_order) > 0:
            return int(new_order)
    except EOFError:
        pass

    return suggested_order


def fix_order(starting_order: int, parsed_files: List[ParsedFile]) -> int:
    properly_ordered = order_is_ascending(starting_order, parsed_files)
    suggested_order = starting_order

    for file in parsed_files:
        if not properly_ordered:
            new_order = prompt_order_change(file, suggested_order)
            file.set_order(new_order)
        else:
            print(f"{file.path} -> {suggested_order}")
        suggested_order += 1

    return suggested_order


def fix_order_by_category(starting_order: int,
                          parsed_files: List[ParsedFile]) -> int:
    """
    Fix the order of the parsed files, separating by category so that lessons are corrected before
    exercises.

    :param starting_order: the expected order of the first parsed file
    :type starting_order: int
    :param parsed_files: the files to correct the order of
    :type parsed_files: List[ParsedFile]
    :return: the suggested order of the last parsed file
    :rtype: int
    """

    type_map = get_type_map(parsed_files)
    suggested_order = starting_order

    lessons = type_map["lesson"]
    if len(lessons) > 0:
        print("Lessons:")
        suggested_order = fix_order(suggested_order, lessons)

    exercises = type_map["exercise"]
    if len(exercises) > 0:
        print("Exercises:")
        suggested_order = fix_order(suggested_order, exercises)

    print()

    return suggested_order


suggested_order = 1
sorted_dirs = False
for root, _dirs, files in os.walk(start_dir):
    if not sorted_dirs:
        # Runs only on the first iteration (when looking through start_dir) so no files are skipped
        _dirs.sort()
        sorted_dirs = True

    parsed_files = []
    for file in files:
        full_path = os.path.join(root, file)
        parsed_files.append(ParsedFile(full_path))

    suggested_order = fix_order_by_category(suggested_order, parsed_files)
