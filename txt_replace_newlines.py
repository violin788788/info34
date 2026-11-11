

with open('new.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Replace all newlines with a single space
modified_content = content.replace('\n', ' ')

# Write the modified content back to the same file (or a new one)
with open('out.txt', 'w', encoding='utf-8') as file:
    file.write(modified_content)