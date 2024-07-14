from pathlib import Path


def get_valid_path_or_die(file_path) -> Path:
    path = Path(file_path)
    if not path.exists():
        raise Exception(f"Data file with path:{file_path} does not exist.")

    if not path.is_file():
        raise Exception(f"File with path:{file_path} is broken or not a file.")

    # process case when file is broken or empty
    if path.stat().st_size == 0:
        raise Exception(f"Data file with path:{file_path} is empty.")

    return path


def write_dummy_data_workers(file_path: str, data: dict[str, int]):
    path = Path(file_path)
    folder = path.parent
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)

    with open(path, 'w', encoding='utf-8') as fh:
        for name, salary in data.items():
            fh.write(f'{name},{salary}\n')


def write_dummy_data_cats(file_path: str, data: list[list]):
    path = Path(file_path)
    folder = path.parent
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)

    with open(path, 'w', encoding='utf-8') as fh:
        for cat in data:
            fh.write(f'{cat[0]},{cat[1]},{cat[2]}\n')

