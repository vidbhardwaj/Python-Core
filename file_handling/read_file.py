# Read data from a file
file = open("data.txt", "r")   # "r" mode opens file for reading
content = file.read()
print("File content:\n", content)
file.close()
# Example: reading line by line
with open("data.txt", "r") as f:
    print("Reading line by line:")
    for line in f:
        print(line.strip())