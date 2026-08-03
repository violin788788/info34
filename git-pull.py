import os
from git import Repo

cwd = os.getcwd()
directory_name = os.path.basename(cwd)

# Use cwd directly since you are already inside the repo, or fix the path string
repo_path = os.path.abspath(cwd)
repo = Repo(repo_path)

print("Fetching latest updates from remote...")
for remote in repo.remotes:
    remote.fetch()

print("Hard resetting local files to match remote main...")
# Replace 'main' with 'master' if your branch name differs
repo.git.reset('--hard', 'origin/main')

print("Cleaning untracked local files...")
# -f forces removal, -d removes untracked directories
repo.git.clean('-f', '-d')

print("Your local files are now identical to the Git repository!")
