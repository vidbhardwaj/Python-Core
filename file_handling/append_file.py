# Append new data without deleting old content
file = open("data.txt", "a")   # "a" mode adds to file
file.write("This is an appended line.\n")
file.close()
print("New line appended successfully.")