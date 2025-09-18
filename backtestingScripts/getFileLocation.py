import os
from pathlib import Path

def getFileLocation(target_name):
    print(f"Running file locator for: {target_name}")

    # Define the starting points for the search
    script_dir = Path(__file__).parent.resolve()
    parent_dir = script_dir.parent
    
    # List of top-level directories to begin searching from
    dirs_to_search = [script_dir, parent_dir]

    for start_dir in dirs_to_search:
        # os.walk recursively explores all directories starting from start_dir
        for dirpath, dirnames, filenames in os.walk(start_dir):
            # Check if the target is a file or a directory in the current location
            if target_name in filenames or target_name in dirnames:
                # If found, join the path and name, then return it
                found_path = os.path.join(dirpath, target_name)
                print(f"Found at: {found_path}")
                return found_path
    
    print(f"'{target_name}' not found.")
    return None
