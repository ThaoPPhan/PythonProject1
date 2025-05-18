input_file_path = r'c:\users\phan0\pycharmmiscproject\textfile1.txt'
output_file_path = r'c:\users\phan0\pycharmmiscproject\textfile2.txt'

try:
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for index, line in enumerate(infile, start=1):
            if index % 2 != 0:  # Write only odd-numbered lines
                outfile.write(line)
    print(f"Odd lines written to: {output_file_path}")
except FileNotFoundError:
    print(f"File not found: {input_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

#read textfile2
try:
    with open(output_file_path, 'r') as file:
        for line in file:
            print(line.strip())  # .strip() removes leading/trailing whitespace including newlines
except FileNotFoundError:
    print(f"File not found: {output_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")