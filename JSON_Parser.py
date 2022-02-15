import pandas as pd

input_file_path = 'path_to_input/'
output_file_path = 'path_to_output/'
file_list = ['json1', 'json2']

for json in file_list:
    with open(input_file_path + json + '.json', encoding='utf-8') as file:
        df = pd.read_json(file)
        df.to_csv(output_file_path + json + '.csv', encoding='utf-8', index=False)
        print(json + ' converted to csv')
