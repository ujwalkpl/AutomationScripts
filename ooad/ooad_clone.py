import os
import pandas as pd
import subprocess

#File with mappings of student names with their github username
ROSTER_FILE = "name_handle_mapping.csv"

#Students Names
students = [
    "LastName, FirstName,
    "LastName1, FirstName1",
    "LastName2, FirstName12",
]

students = [" ".join(name.split(", ")[::-1]) for name in students]

# Destination directory
CLONE_DIR = "homework1"


GITHUB_ORG = "University-of-Colorado-Boulder-S2025"
ASSIGNMENT_PREFIX = "csci-4448-5448-spring-2025-homework-1"

roster = pd.read_csv(ROSTER_FILE)


os.makedirs(CLONE_DIR, exist_ok=True)


for student in students:
    row = roster[roster['roster_identifier'] == student]
    if not row.empty:
        github_username = row.iloc[0]['github_username']
        repo_name = f"{ASSIGNMENT_PREFIX}-{github_username}"  # Replace with the repo naming pattern

        # Construct the repository URL
        repo_url = f"git@github.com:{GITHUB_ORG}/{repo_name}.git"

        # Clone the repository
        print(f"Cloning {repo_name} for {student}...")
        subprocess.run(["git", "clone", repo_url, os.path.join(CLONE_DIR, repo_name)])
    else:
        print(f"Student {student} not found in the roster!")
