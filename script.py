import os

def fix_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".tas"):  # Adjust the file extension as needed
            filepath = os.path.join(directory, filename)
            with open(filepath, "r+") as file:
                lines = file.readlines()
                file.seek(0)  # Move the file pointer to the beginning
                file.truncate()  # Clear the file contents
                
                for line in lines:
                    if "(2X)" in line:
                        line = line.replace("(2X)", "")  # Remove (1X)
                    elif line.startswith("#2x"):
                        line = "#" + line.capitalize()  # Capitalize and prepend #
                    elif line.startswith("#2X"):
                        line = "#" + line  # Prepend #
                    file.write(line)

directory = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Celeste\\TAS Files\\SC2020 Dashless\\1_Beginner_Dashless"  # Replace with your target directory path
fix_files(directory)
