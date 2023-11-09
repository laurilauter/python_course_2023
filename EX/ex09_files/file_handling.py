"""File handling."""

import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into a string.

    In this exercise, assume that the file exists.

    :param filename: The name of the file to read.
    :return: The contents of the file as a string.
    """
    with open(filename, "r") as f:
        content = f.read()
        f.close()
    return content


def read_file_contents_to_list(filename: str) -> list[str]:
    r"""
    Read file contents into a list of lines.

    In this exercise, assume that the file exists.

    Each line from the file is a separate element in the list,
    and the order of the list matches the order in the file.
    Newline characters ('\n') are removed from each line.

    :param filename: The name of the file to read.
    :return: A list of lines without newline characters.
    """
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        f.close()
    return lines


def read_csv_file(filename: str) -> list[list[str]]:
    """
    Read CSV file contents into a list of rows.

    Each row is represented as a list of "columns" or fields.

    Example CSV (Comma-separated values) data:
    name,age
    john,12
    mary,14

    Will return as:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Note: The "csv" module should be used.

    :param filename: The name of the file to read.
    :return: A list of lists, where each inner list represents a row of CSV data.
    """
    data = []
    with open(filename, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=':')  # : is needed for the final func
        for row in reader:
            data.append(row)
    return data


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to a file.

    If the file does not exist, it will be created.
    If the file already exists, its contents will be overwritten.

    :param filename: The name of the file to write to.
    :param contents: The content to write to the file.
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(contents)
        f.close()


def write_lines_to_file(filename: str, lines: list[str]) -> None:
    """
    Write lines to a file.

    Each string in the 'lines' list represents a separate line in the file.
    The function ensures that there is no extra newline added at the end of the file,
    unless the last element in the 'lines' list itself ends with a newline.

    :param filename: The name of the file to write to.
    :param lines: A list of strings, each representing a line to write to the file.
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as f:
        first_line_done = False
        for line in lines:
            if first_line_done:
                f.write('\n')
            first_line_done = True
            f.write(line)


def write_csv_file(filename: str, data: list[list[str]]) -> None:
    """
    Write data into a CSV file.

    The data is a list of lists, where each inner list represents a row,
    and the elements within each inner list represent the columns.

    Example data:
    [["name", "age"], ["john", "11"], ["mary", "15"]]

    Will be written in the .csv file as:
    name,age
    john,11
    mary,15

    Note: The "csv" module should be used.

    :param filename: The name of the file to write to.
    :param data: A list of lists to write to the file, where each list represents a row.
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        # writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two input CSV files into one output CSV file.

    The dates file contains names and dates separated by a colon, and the towns file contains
    names and towns separated by a colon. Both files have no headers.

    Example format of the dates file:
    john:01.01.2001
    mary:06.03.2016

    Example format of the towns file:
    john:london
    mary:new york

    The merging is performed based on the names found in input files.
    The order of the lines in the output file follows the order in the dates input file.
    Names that are missing in the dates input file will follow the order in the towns input file.
    The order of the fields is: name, town, date.

    The resulting CSV file should have the following format:
    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be represented as "-" in the output file.

    Example:
    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Reuse CSV reading and writing functions.
    Note: When reading CSV files, specify the delimiter (improve existing method).

    :param dates_filename: The name of the CSV file with names and dates (name:date).
    :param towns_filename: The name of the CSV file with names and towns (name:town).
    :param csv_output_filename: The name of the CSV file to write to names, towns, and dates.
    :return: None
    """
    dates = read_csv_file(dates_filename)
    towns = read_csv_file(towns_filename)
    print(dates)
    print(towns)
    merged_data = [["name", "town", "date"]]
    for date in dates:
        merged_data.append([date[0], "-", date[1]])

    for town in towns:
        for row in merged_data:
            if town[0] in row[0]:
                row[1] = town[1]
            elif len(merged_data) <= len(towns):
                merged_data.append([town[0], town[1], "-"])

    write_csv_file(csv_output_filename, merged_data)


if __name__ == '__main__':
    # print(read_csv_file("data.csv"))
    # print(read_csv_file("data2.csv"))
    # filename = "multi.txt"
    # lines = ["hello\nWorld\nstop", "hello\nWorld\nstop"]
    # filename2 = "single.txt"
    # lines2 = ["hello\nWorld\nstop"]
    # print(write_lines_to_file(filename2, lines2))
    #
    dates_filename = "dates.txt"
    towns_filename = "towns.txt"
    csv_output_filename = "data.csv"
    print(merge_dates_and_towns_into_csv(dates_filename, towns_filename, csv_output_filename))
