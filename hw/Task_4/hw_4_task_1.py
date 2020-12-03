def read_magic_number(path: str) -> bool:
    try:
        with open(path) as f:
            file_read = f.readline()
        n = int(file_read)
        return 1 <= n < 3

    except ValueError:
        raise ValueError("it's not a number!")
    except FileNotFoundError:
        raise FileNotFoundError("No file here!")
