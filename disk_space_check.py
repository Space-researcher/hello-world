
import shutil   
import os
from datetime import datetime


'''
python disk_space_check.py
Checks available free space on drive C: (Windows 10).
Saves the value to a file (free_space.txt).
On the next run, compares the current value with the previously saved value and prints the difference.
'''

data_file = 'free_space.txt'

def get_free_space_gb(drive='C:\\'):
    total, used, free = shutil.disk_usage(drive)  # documentation https://docs.python.org/3/library/shutil.html
    print("Total space = ", total, "bytes")
    print("Used space = ", used, "bytes")
    print("Free space = ", free, "bytes")
    return free / (1024 ** 3)  # recalculate to GB

def read_previous_data():
    if not os.path.exists(data_file):
        return None, None
    try:
        with open(data_file, 'r') as f:
            lines = f.readlines()
            if len(lines) != 2:
                return None, None
            previous_space = float(lines[0].strip())
            previous_timestamp = lines[1].strip()
            return previous_space, previous_timestamp
    except Exception:
        return None, None

def write_current_data(space):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')   # documentation https://ravesli.com/method-strftime-python/
    with open(data_file, 'w') as f:
        f.write(f"{space:.2f}\n{timestamp}")

def main():
    current_space = get_free_space_gb()
    previous_space, previous_timestamp = read_previous_data()

    print(f"Current free space on C: {current_space:.2f} GB")

    if previous_space is not None:
        difference = current_space - previous_space
        print()
        print(f"Previous check on {previous_timestamp}")
        print(f"Previous space was {previous_space} GB")
        print(f"Change since last check: {difference:.2f} GB")
    else:
        print("No previous record found. Saving current space and timestamp.")

    write_current_data(current_space)

if __name__ == '__main__':
    main()
	
	