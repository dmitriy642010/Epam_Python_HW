def read_magic_number(path: str) -> bool:
    try:
        with open(path) as f:
            file_read = f.readline()
        n = int(file_read)
        return 1 <= n < 3

    except FileNotFoundError:
        raise ("No file was found!")

    except ValueError:
        raise ("Should be number here!")
