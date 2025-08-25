def modify_content(text):
    # Example modification: convert to uppercase
    return text.upper()

try:
    # 🧪 Ask user for input filename
    filename = input("Enter the name of the file to read: ")

    # 🖋️ Try to open and read the file
    with open(filename, "r") as infile:
        original_content = infile.read()

    # Modify the content
    modified_content = modify_content(original_content)

    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ Modified content written to '{new_filename}'")

except FileNotFoundError:
    print("❌ Error: File not found. Please check the filename and try again.")
except IOError:
    print("❌ Error: Could not read or write to the file.")
