
import subprocess
import os

repo_dir = os.path.dirname(os.path.abspath(__file__))

commands = [
    ["git", "fetch", "origin"],
    ["git", "reset", "--hard", "origin/main"],  # Replace 'main' if your branch is different
    ["git", "clean", "-fd"],                    # Remove untracked files/directories
]

for cmd in commands:
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, cwd=repo_dir, check=True)

print("Repository is now identical to origin/main.")
input("Press Enter to continue...")
