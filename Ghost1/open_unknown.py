import os
import subprocess

def open_all_files_in_vscode(directories):
    for directory in directories:
        # Walk through the directory and subdirectories
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check if the file is a Python file
                if file.endswith('.py'):
                    # Construct the full path to the file
                    file_path = os.path.join(root, file)
                    
                    # Open the file in VS Code using subprocess
                    subprocess.Popen(['code', file_path])

if __name__ == "__main__":
    directories = [
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\badserver,",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\bash..;;[['']]\console",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\bash..;;[['']]\loghead",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\bash..;;[['']]\password",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\dawgserver,",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\doublelane~~",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\doublemain!",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\icosik~space",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\main#ly",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\closed\MirrorDAWg\open_unknown",
        r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-One\Mirror\plant tree_v"
    ]
    
    open_all_files_in_vscode(directories)
