# Первый этап удаление символов кроме sid каналов

file_path = r'd:\Downloads\1.txt'
try:
    with open(file_path, 'w') as file:
        lines = file.readlines()
        for line in lines:
            # Find the index of '0B00&000000/' and extract the next 4 characters
            index = line.find('0B00&000000/')
            if index != -1:
                shortened_line = line[index + len('0B00&000000/'):index + len('0B00&000000/') + 4]
                file.write(shortened_line + '\n')
            else:
                # If '0B00&000000/' is not found, keep the original line
                file.write(line)

    print(f"Processed file '{file_path}' and saved the shortened lines.")
except FileNotFoundError:
    print(f"File '{file_path}' not found. Please make sure the file exists.")

# Второй этап удаление дубликатов sid
# Чтение файла и обработка строк
with open(file_path, 'r') as file:
    lines = file.readlines()

# Удаление дубликатов строк
unique_lines = set(lines)

# Запись уникальных строк обратно в файл
with open(file_path, 'w') as file:
    file.writelines(unique_lines)

print(f"Удалено {len(lines) - len(unique_lines)} дубликатов строк из файла {file_path}.")

# Третий этап замена шестьнадцатиричных чисел в десятичные
def hex_to_decimal(hex_str):
    try:
        return str(int(hex_str, 16))
    except ValueError:
        return hex_str  # If the input is not a valid hex number, keep it unchanged


try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            decimal_line = ' '.join(hex_to_decimal(hex_num) for hex_num in line.split())
            file.write(decimal_line + '\n')

    print(f"Converted hex numbers from '{file_path}' to decimals in the same file.")
except FileNotFoundError:
    print(f"File '{file_path}' not found. Please make sure the file exists.")