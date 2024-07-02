#!/usr/bin/env python3

import os
import yaml
import openpyxl

def find_yaml_files(directory):
    yaml_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml') or file.endswith('*.yml'):
                yaml_files.append(os.path.join(root, file))
    return yaml_files

def parse_yaml_file(yaml_files):
    yaml_data = []
    for file in yaml_files:
        with open(file, 'r') as f:
            try:
                data = yaml.safe_load(f)
                name = data.get('name', '')
                upstream = data.get('upstream', '')
                yaml_data.append({'name': name, 'upstream': upstream})
            except yaml.YAMLError as e:
                print(f"Error parsing YAML file {file}")
    return yaml_data

def write_to_xlsx(yaml_data, output_file):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = 'YAML Data'
    worksheet.append(['Name', 'Upstream', 'src-openEuler'])

    worksheet.freeze_panes = 'A2'
    worksheet.column_dimensions['A'].width = 30
    worksheet.column_dimensions['B'].width = 80
    worksheet.column_dimensions['C'].width = 80

    for data in yaml_data:
        name = data['name']
        upstream = data['upstream']
        worksheet.append([name, upstream, f'https://gitee.com/src-openeuler/{name}'])

    workbook.save(output_file)

def main():
    directory = os.getcwd()
    output_file = "yaml_data.xlsx"

    yaml_files = find_yaml_files(directory)

    yaml_data = parse_yaml_file(yaml_files)

    write_to_xlsx(yaml_data, output_file)
    print("Data written to", output_file)

if __name__ == "__main__":
    main()
