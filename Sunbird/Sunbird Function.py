#DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
import os
import subprocess
import time

def run_python_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                print(f"Running {file_path}...")
                subprocess.Popen(["python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
                time.sleep(5)  # Adjust the delay to 5 seconds for extra caution

if __name__ == "__main__":
    directory = r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-Two\Ghost1"
    run_python_files(directory)
