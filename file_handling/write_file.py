# Create and write data into a file
file = open("data.txt", "w")   # "w" mode creates/overwrites file
file.write("Hello, this is my first file.\n")
file.write("Writing multiple lines is easy!\n")
file.close()
print("Data written successfully.")