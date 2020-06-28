# !/usr/bin/python3

import os

needs_renaming = []

for root, _dirs, files in os.walk("./assets/images/"):
    for name in files:
        if " " in name or not name == name.lower():
            needs_renaming.append((root, name))

for root, old_name in needs_renaming:
    parts = old_name.lower().split()
    fixed_name = "_".join(parts)

    original_path = os.path.join(root, old_name)
    fixed_path = os.path.join(root, fixed_name)

    print(f"{original_path} -> {fixed_path}")
    os.rename(original_path, fixed_path)
