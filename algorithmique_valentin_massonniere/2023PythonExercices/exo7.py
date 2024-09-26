from datetime import datetime, timedelta
import codecs
import xlsxwriter

def get_data(file_url):
    try:
        with codecs.open(file_url, mode='r', encoding='utf-8') as inputFile:
            data = inputFile.readlines() 
            return data
    except FileNotFoundError:
        print("FileNotFoundError: No such file or directory")
    except UnicodeError:
        print("UnicodeError: UTF-16 stream does not start with BOM")
    return []

def parse_line(line):
    date_string, float_value, int_value = line.strip().split(';')
    date_object = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
    return date_object, float(float_value), int(int_value)

def check_and_fill_dates(data):
    filled_data = []
    previous_date = None
    previous_float = None
    previous_int = None
    
    for line in data:
        date_object, float_value, int_value = parse_line(line)
        
        if previous_date is not None:
            diff = (date_object - previous_date).total_seconds()
            if diff > 30:
                num_intervals = int(diff // 30)
                for j in range(1, num_intervals + 1):
                    new_date = previous_date + timedelta(seconds=j * 30)
                    filled_data.append(f"{new_date.strftime('%d/%m/%Y %H:%M:%S')};{previous_float};{previous_int}\n")
        
        filled_data.append(f"{date_object.strftime('%d/%m/%Y %H:%M:%S')};{float_value};{int_value}\n")
        
        previous_date = date_object
        previous_float = float_value
        previous_int = int_value

    return filled_data

def replace_date_file(file_url, filled_data):
    try:
        workbook = xlsxwriter.Workbook(file_url)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({"bold": True})
    except Exception as e:
        print(e)


data = get_data("algorithmique_valentin_massonniere/2023PythonExercices/DataExo5.txt")
if data:
    filled_data = check_and_fill_dates(data)
    replace_date_file("algorithmique_valentin_massonniere/2023PythonExercices/DataExo7Out.xlsx", filled_data)
