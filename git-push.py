

import os

# Define the Git commands
commands = [
    "git add -A",
    'git commit -m "Remove unwanted files and directories, and add/modify other changes"',
    "git push origin main --force"
]

# Execute the commands in the shell using os.system()
for command in commands:
    os.system(command)

    """
create git
git init

create main branch
git checkout -b main

add remote
git remote add origin https://github.com/violin788788/info34.git

stage all changes
git add -A

commit changes
git commit -m "Remove unwanted files and directories, and add/modify other changes"

force?
git push origin main --force

username
violin788788
token


remove tracking
git rm --cached .lesshst


"""