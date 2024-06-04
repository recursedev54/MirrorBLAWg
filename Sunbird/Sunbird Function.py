#DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
import os
#DEV TOOL
import subprocess
#DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
import time
#DEV TOOL
def run_python_files(directory):
#DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
    for root, dirs, files in os.walk(directory):
        #DEV TOOL       
        for filename in files:
        #DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                #DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
                print(f"Running {file_path}...")
                subprocess.Popen(["python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
                #DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
                time.sleep(5)  # Adjust the delay to 5 seconds for extra caution
                #DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
if __name__ == "__main__":
    #DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
    directory = r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-Two\Ghost1"
    #DO NOT RUN THIS CODE IT WILL RECURSE AND KILL YOUR COMPUTER
    run_python_files(directory)
    #deadlained
