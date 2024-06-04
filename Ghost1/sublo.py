import os
import subprocess

def run_python_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                print(f"Running {file_path}...")
                subprocess.Popen(["python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":
    directory = r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-Two\Ghost1"
    run_python_files(directory)
