from fileHelper import get_valid_path_or_die
from fileHelper import write_dummy_data_cats

DUMMY_DATA = [
    ['60b90c1c13067a15887e1ae1', 'Tayson', 3],
    ['60b90c2413067a15887e1ae2', 'Vika', 1],
    ['60b90c2e13067a15887e1ae3', 'Barsik', 2],
    ['60b90c3b13067a15887e1ae4', 'Simon', 12],
    ['60b90c4613067a15887e1ae5', 'Tessi', 5],
]

DATA_FILE_FULL_PATH = './data/cats.txt'


def get_cats_info(path) -> list[dict[str, int | str]]:
    try:
        path = get_valid_path_or_die(path)
    except Exception as e:
        print(f"Error: {e}")
        exit()

    dicts = []
    with open(file=path, mode='r', encoding='utf-8') as fh:
        for row in fh:
            id, name, age = row.strip().split(',')
            dicts.append({"id": id, "name": name, "age": int(age)})

    return dicts


# write_dummy_data_cats(DATA_FILE_FULL_PATH, DUMMY_DATA)  # Uncomment to write dummy data to file

cats_info = get_cats_info(DATA_FILE_FULL_PATH)
print(cats_info)
