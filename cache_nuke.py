#run this in bash

"""



# pip caches
rm -rf ~/.cache/pip
rm -rf ~/.cache

# user-level python junk
rm -rf ~/.local/share/pip
rm -rf ~/.local/lib/python*

# build / temp leftovers
rm -rf /tmp/*
rm -rf /var/tmp/* 2>/dev/null

# compiled python files
find ~ -name "__pycache__" -type d -exec rm -rf {} +
find ~ -name "*.pyc" -delete

# wheels / archives
find ~ -name "*.whl" -delete
find ~ -name "*.tar.gz" -delete
find ~ -name "*.zip" -delete



"""