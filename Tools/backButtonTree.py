import os
import re

rootFolder = 'DesignPatterns'

def button(pagePath: str):
    return f'[<kbd><br><- Return<br></kbd>]({pagePath})\n'

# Step 1: Collect all links in each file
links = {}  # Dictionary to store links found in each file

for (dirpath, dirnames, filenames) in os.walk(rootFolder):
    for name in filenames:
        if name.endswith('.md'):
            with open(os.path.join(dirpath, name), 'r') as f:
                content = f.read()
                matches = re.findall(r'\((.*?\.md)\)', content)
                if matches:
                    print(f'found links in {os.path.join(dirpath, name)}')
                    full_path = os.path.join(dirpath, name)
                    links[full_path] = matches

# Step 2: For each link found, navigate to the linked file and append the back button
for file_path, linked_files in links.items():
    for linked_file in linked_files:
        linked_file_path = os.path.join(os.path.dirname(file_path), linked_file)
        if os.path.exists(linked_file_path):
            relative_path = os.path.relpath(file_path, os.path.dirname(linked_file_path))
            # Calculate the relative path for the image from the linked file to Notes/img
            back_button = button(relative_path)
            with open(linked_file_path, 'r') as f:
                content = f.read()
                # Check if the button is already there
                if back_button not in content:
                    with open(linked_file_path, 'a') as f_append:
                        f_append.write(back_button)
