def get_todos(filepath="files/data.txt"):
    """
    Read a file and get the todos list
    :param filepath:
    :return:todos list kept in the file
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/data.txt"):
    """
    Write a todos list in the file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())