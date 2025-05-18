file_path = r'c:\users\phan0\pycharmmiscproject\textfile1.txt'

try:
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())  # .strip() removes leading/trailing whitespace including newlines
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
