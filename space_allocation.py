

import subprocess
commands=[
"du -sh ~/.local/lib/python*/site-packages/* | sort -h",
"du -sh ~/* | sort -h",
"du -ah ~ 2>/dev/null | sort -hr | head -50"
]
for command in commands:
    print("\nRUNNING:",command)
    result=subprocess.run(command,shell=True,capture_output=True,text=True)
    print(result.stdout)


"""
import subprocess
commands=[
"du -sh ~/.local/lib/python*/site-packages/* | sort -h",
"du -sh ~/* | sort -h",
"du -ah ~ 2>/dev/null | sort -h | head -50"
]
for command in commands:
    print("\nRUNNING:",command)
    result=subprocess.run(command,shell=True,capture_output=True,text=True)
    print(result.stdout)

    """