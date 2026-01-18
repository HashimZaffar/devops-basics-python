#!/usr/bin/env python3

import os

print("DevOps File Manager Script")

directory_name = "example_directory"

if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created")
else:
    print(f"Directory '{directory_name}' already exists")

file_name = "example.txt"

file_path = os.path.join(directory_name, file_name)

with open(file_path, "w") as file:
    file.write("This file was created using Python automation.\n")

print("File created successfully")

