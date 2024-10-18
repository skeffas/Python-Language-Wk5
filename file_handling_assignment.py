# File Creation: Write Mode ('w')
# Step 1: Create a new text file and write some text to it
with open("my_file.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line with a number: 42\n")
    file.write("Here's the third line, and we are done!\n")

# File Reading: Read Mode ('r')
# Step 2: Read the contents of the file and display them on the console
with open("my_file.txt", "r") as file:
    print("Contents of 'my_file.txt' after writing:")
    print(file.read())

# File Appending: Append Mode ('a')
# Step 3: Append additional lines to the file
with open("my_file.txt", "a") as file:
    file.write("This is an appended fourth line.\n")
    file.write("Adding a fifth line with a number: 100\n")
    file.write("Finally, this is the sixth line added to the file.\n")

# Step 4: Read the updated contents of the file and display them on the console
with open("my_file.txt", "r") as file:
    print("\nContents of 'my_file.txt' after appending:")
    print(file.read())