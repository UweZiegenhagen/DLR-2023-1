# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:56:10 2023

@author: Uwe

source ChatGPT 3.5

"Create me a Python script that gets all the files in a specific folder and 
the time these files were modified last, show the times  as difference in 
seconds to the current timestamp
"
"""

import os

def get_file_modification_times(folder_path):
    
    try:
        files = os.listdir(folder_path)
    except OSError as e:
        print(f"Error: {e}")
        return
    
    
    for file in files:
        if file[-3:] == 'tex':
            tex_path = os.path.join(folder_path, file)
            pdf_path = os.path.join(folder_path, file[:-3]+ 'pdf')
            
            if os.path.isfile(tex_path) and os.path.isfile(pdf_path): # both files exist
                tex_modification_time = os.path.getmtime(tex_path)
                pdf_modification_time = os.path.getmtime(pdf_path)
                
                time_difference = int(pdf_modification_time - tex_modification_time)
                print(f"{file}\t\t{time_difference} seconds")
                if time_difference < 60: # 60 Sekunden
                    print(f'must recompile {file}')
                    os.system(f"pdflatex {file}")
                else:
                    print(f'{time_difference} too small/big to recompile')

            
if __name__ == "__main__":
    folder_path =  '.' #input("Enter the folder path: ")
    get_file_modification_times(folder_path)