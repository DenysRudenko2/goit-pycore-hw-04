from fileHelper import get_valid_path_or_die
from fileHelper import write_dummy_data_workers

DUMMY_DATA = {
    'Alex Korp': 3000,
    'Nikita Borisenko': 2000,
    'Sitarama Raju': 1000
}

DATA_FILE_FULL_PATH = './data/salary.txt'


def total_salary(path):
    try:
        path = get_valid_path_or_die(path)
    except Exception as e:
        print(f"Error: {e}")
        exit()

    with open(file=path, mode='r', encoding='utf-8') as fh:
        total = 0
        workers_count = 0
        for row in fh:
            name, salary = row.strip().split(',')
            total += int(salary)
            workers_count += 1

    return total, int(total / workers_count)


# write_dummy_data_workers(DATA_FILE_FULL_PATH, DUMMY_DATA)  # Uncomment to write dummy data to file

total, average = total_salary(DATA_FILE_FULL_PATH)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
