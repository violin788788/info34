file_path = "fed.txt"  # Replace with your actual file name or path
target_string = "Digitized for FRASER http://fraser.stlouisfed.org/ Federal Reserve Bank of St. Louis"

# Read the file content
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace all instances of the target string with an empty string
updated_content = content.replace(target_string, "")


new_file = file_path.replace(".txt","_fixed.txt")
# Write the cleaned content back to the file (use a new filename if you want to keep the original)
with open(new_file, "w", encoding="utf-8") as file:
    file.write(updated_content)

print("Replacement complete!")