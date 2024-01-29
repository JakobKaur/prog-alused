import csv

def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename, 'r') as file:
        return file.read()


def read_file_contents_to_list(filename: str) -> list:
    """
    Read file contents into list of lines.

    :param filename: File to read.
    :return: List of lines.
    """
    with open(filename, 'r') as file:
        return file.readlines()


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    :param filename: File to read.
    :return: List of lists.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader]


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, 'w') as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    dates_data = read_csv_file(dates_filename)
    towns_data = read_csv_file(towns_filename)

    merged_data = []

    for date_row in dates_data:
        name = date_row[0]
        date = date_row[1]

        town_row = next((town_row for town_row in towns_data if town_row[0] == name), None)

        if town_row:
            town = town_row[1]
            merged_data.append([name, town, date])
        else:
            merged_data.append([name, '-', date])

    write_csv_file(csv_output_filename, merged_data)