# !/usr/bin/python3

import os
import re
import fileinput

start_dir = "./_docs/java/"

type_regex = re.compile(r"type: (\w+)")
order_regex = re.compile(r"order: \w+")
suggested_order = 1


def get_type_map(root, files):
    type_map = {"lesson": [], "exercise": []}
    for file in files:
        path = os.path.join(root, file)

        with open(path, "r") as f:
            for line in f:
                match = type_regex.match(line)
                if match is not None:
                    file_type = match.group(1)
                    if file_type in type_map:
                        type_map[file_type].append(path)
                        break
    return type_map


def change_order(documents):
    global suggested_order

    if len(documents) > 1:
        for path in documents:
            order = prompt_order_change(path, suggested_order)
            write_order_change(path, order)
            suggested_order += 1
    elif len(documents) == 1:
        path = documents[0]
        print(f"{path} order -> {suggested_order}")
        write_order_change(path, suggested_order)
        suggested_order += 1


def prompt_order_change(path, suggested_order):
    try:
        new_order = input(f"{path} -> {suggested_order} ? ")
        if len(new_order) > 0:
            return int(new_order)
    except EOFError:
        pass

    return suggested_order


def write_order_change(path, order):
    matched = False
    f = fileinput.input(path, inplace=True)
    for line in f:
        # Prints here are directed to the output file, not terminal stdout
        if not matched and order_regex.match(line) is not None:
            print(f"order: {order}")
            matched = True
        else:
            print(line, end="")


sorted_dirs = False
for root, _dirs, files in os.walk(start_dir):
    if not sorted_dirs:
        # Runs only on the first iteration, which is when looking through start_dir
        _dirs.sort()
        sorted_dirs = True

    type_map = get_type_map(root, files)

    lessons = type_map["lesson"]
    if len(lessons) > 0:
        print("Lessons:")
        change_order(lessons)

    exercises = type_map["exercise"]
    if len(exercises) > 0:
        print("Exercises:")
        change_order(exercises)

    print()
