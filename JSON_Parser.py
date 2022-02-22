# importing required libraries
import pandas as pd
import os

# assigning directory paths for file I/O
input_file_path = 'E:\\dummy_json\\'
output_file_path = 'E:\\dummy_json\\'

# creates a list of file names to be iterated through will and also only target json files
file_list = [file.replace(".json", "") for file in os.listdir(input_file_path) if file.endswith(".json")]
# output list of files
print(file_list)

# checks that I/O directories exist then iterates through files coverting them to csv files
if os.path.exists(input_file_path) and os.path.exists(output_file_path):
    try:
        for json in file_list:
            with open(input_file_path + json + '.json', encoding='utf-8') as file:
                df = pd.read_json(file)
                df.to_csv(output_file_path + json + '.csv', encoding='utf-8', index=False)
                print(json + ' converted to csv')
    # throws an exception if files do no exist within set directory
    except FileNotFoundError as e:
        print(e)
else:
    print('one or more diretory variables is incorrectly assinged')
