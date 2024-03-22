try:
    # File Creation
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers: 54321\n")

    # File Reading and Display
    print("Contents of my_file.txt:")
    with open("my_file.txt", 'r') as file:
        for line in file:
            print(line.strip())

    # File Appending
    with open("my_file.txt", 'a') as file:
        file.write("Additional line 1\n")
        file.write("67890\n")
        file.write("Appending more text and numbers: 98765\n")

except FileNotFoundError:
    print("File not found error occurred.")
except PermissionError:
    print("Permission error occurred. Check file permissions.")
finally:
    print("File handling completed.")
