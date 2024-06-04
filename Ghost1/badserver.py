import os
import subprocess
import time

def run_python_files(directory):
    processes = []
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                print(f"Starting {file_path}...")

                try:
                    proc = subprocess.Popen(
                        ["python", file_path],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        creationflags=subprocess.CREATE_NEW_CONSOLE
                    )
                    processes.append((file_path, proc))
                except Exception as e:
                    print(f"Failed to start {file_path}: {e}")

    # Monitor the processes
    while True:
        for file_path, proc in processes:
            retcode = proc.poll()
            if retcode is not None:  # Process finished.
                print(f"{file_path} terminated with return code {retcode}")
                try:
                    # Restart the process if it terminates
                    print(f"Restarting {file_path}...")
                    proc = subprocess.Popen(
                        ["python", file_path],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        creationflags=subprocess.CREATE_NEW_CONSOLE
                    )
                    processes.append((file_path, proc))
                except Exception as e:
                    print(f"Failed to restart {file_path}: {e}")
            time.sleep(1)  # Avoid busy waiting

if __name__ == "__main__":
    directory = r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-Two\Ghost1"
    run_python_files(directory)
