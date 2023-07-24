
#open the "pelican.txt" file in read mode
#with open("pelican.txt", "r") as file_handle:
    # Read the entire contents of the file and store it in the variable "content"
#    content = file_handle.read()

# Print the contents of the file
#print(content)

# text or string data

# Open the "pelican.txt" file in read mode "r"
with open("pelican.txt", "r") as file_handle:
    # Read the file and store it in the variable "content"
    content = file_handle.read()

# Print the contents of the file
print("Content of pelican.txt:")
print(content)

# Open the "pelican.txt" file again in read mode "r"
with open("pelican.txt", "r") as file_handle:
    # Read the lines of the file and store them in a list named "lines"
    lines = file_handle.readlines()

# Output the number of items (lines) in the list
num_items = len(lines)
print("Number of items in the list:", num_items)


# Iterate over the lines using a loop and print each line
# Used the strip() function to remove the newline character at the end of each line
print("\nContents of pelican.txt (using a loop):")
for line in lines:
    print(line.strip())




