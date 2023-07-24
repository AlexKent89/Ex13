
# Creates a text file called pelican.txt
file_handle = open("pelican.txt", "w")

# This appends the line to the file
line_to_append = "A wonderful bird is the Pelican,"

# \n stands for new line.
with open("pelican.txt", "a") as file_handle:
    file_handle.write(line_to_append + "\n")

line_to_append = "His bill holds more than his belican."

with open("pelican.txt", "a") as file_handle:
    file_handle.write(line_to_append + "\n")

# List created
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

# Write lines method prints the items in the list and \n will put each one on a new line
with open("pelican.txt", "a") as file_handle:
    file_handle.writelines(lines)