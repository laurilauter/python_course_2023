"""Create table from the given string."""
import re


def create_table_string(text: str) -> str:
    """
    Create table string from the given logs.

    Example of logs:

    [10:50 UTC+8] nothing here
    [12:25 UTC-2] error 404

    There are a total of five categories you need to find the items for.
    Here are the rules for finding them:

    1. Time
    - Hour can be one or two characters long (1, 01, and 11)
    - Minute can be one or two characters long (2, 02, 22)
    - UTC offset ranges from -12 to 12
    - Times in the text are formatted in 24 hour time format (https://en.wikipedia.org/wiki/24-hour_clock)
    - Minimum time is 00:00 (0:00 and 0,00 and 00-0 are also valid)
    - Maximum time is 23:59
    - Hour and minute can be separated by any non-numeric character (01:11, 1.2, 6;5 and 1a4 are valid while 12345 is not)
    2. Username starts after "usr:" and contains letters, numbers and underscores ("_")
    3. Error code is a non-negative number up to 3 digits and comes after a case-insensitive form of "error "
    4. IPv4 address is good enough if it's a group of four 1- to 3-digit numbers separated by dots
    5. Endpoint starts with a slash ("/") and contains letters, numbers and "&/=?-_%"

    Each table row consists of a category name and items belonging to that category.
    Categories are named and ordered as follows: "time", "user", "error", "ipv4" and "endpoint".

    Table from the above input example:

    time  | 2.50 AM, 14.25 PM
    error | 404

    The category name and its items are separated by a vertical bar ("|").
    The length between the category name and separator is one whitespace (" ") for the longest category name in the table.
    The length between the separator and items is one whitespace.
    Items for each category are unique and are separated by a comma and a whitespace (", ") and must be sorted in ascending order.
    Times in the table are formatted in 12 hour time format (https://en.wikipedia.org/wiki/12-hour_clock), like "1:12 PM"
    and "12:00 AM".
    Times in the table should be displayed in UTC(https://et.wikipedia.org/wiki/UTC) time.
    If no items were found, return an empty string.
    """
    table_string = ""
    data_collection = {}

    times = get_times(text)
    if times:
        data_collection["time"] = set(calculate_times(times))
    users = get_usernames(text)
    if users:
        data_collection["user"] = set(users)
    errors = get_errors(text)
    if errors:
        data_collection["error"] = set(errors)
    ipv4s = get_addresses(text)
    if ipv4s:
        data_collection["ipv4"] = set(ipv4s)
    endpoints = get_endpoints(text)
    if endpoints:
        data_collection["endpoint"] = set(endpoints)

    # sort the dictionary
    sorted_data_collection = {}
    for key, value in data_collection.items():
        sorted_values = sorted(value)
        sorted_data_collection[key] = sorted_values

    # normalize times
    if "time" in sorted_data_collection:
        if sorted_data_collection["time"]:
            sorted_data_collection["time"] = normalize_times(sorted_data_collection["time"])

    longest_key_length = get_longest_key_length(sorted_data_collection)
    # build table
    for key in sorted_data_collection.keys():
        table_string += build_table_row(longest_key_length, key, sorted_data_collection[key])
    return table_string


def get_times(text: str) -> list[tuple[int, int, int]]:
    """
    Get times from text using the time pattern.

    The result should be a list of tuples containing the time that's not normalized and UTC offset.

    For example:

    [10:53 UTC+3] -> [(10, 53, 3)]
    [1:43 UTC+0] -> [(1, 43, 0)]
    [14A3 UTC-4] [14:3 UTC-4] -> [(14, 3, -4), (14, 3, -4)]

    :param text: text to search for the times
    :return: list of tuples containing the time and offset
    """
    # regex = r'\[(.+) (UTC[-+]\d{1,2})'
    regex = r'((?<=[\[])(.+)) (UTC[-+]\d{1,2})'
    times = []
    for match in re.finditer(regex, text):
        if match.group(0) is not None:
            time_fragments = match.group(0).strip("[]").split(" ")
            found_hour = re.search(r'((\d*)(?=[AaPp :.=-]))', time_fragments[0])
            found_minute = re.search(r'((?<=[AaPp :.=?-])(\d*))', time_fragments[0])
            # print(found_hour)
            # print(found_minute)
            if found_hour and found_minute:
                if found_hour.group(0) and found_minute.group(0):
                    hour = int(found_hour.group(0))
                    minute = int(found_minute.group(0))
                    offset = int(time_fragments[1].strip("UTC"))
                    if hour < 24 and minute < 60:
                        times.append((hour, minute, offset))
    return times


def get_usernames(text: str) -> list[str]:
    """Get usernames from text."""
    regex = r'(usr:(\w+))?'
    usernames = []
    for match in re.finditer(regex, text):
        if match.group(1) is not None:
            usernames.append(match.group(1).replace("usr:", ""))
    return usernames


def get_errors(text: str) -> list[int]:
    """Get errors from text."""
    regex = r'([eE][rR]{2}[oO][rR] \d{1,3})?'
    errors = []
    for match in re.finditer(regex, text):
        if match.group(1) is not None:
            error = int(match.group(1).split(" ")[1])
            errors.append(error)
    return errors


def get_addresses(text: str) -> list[str]:
    """Get IPv4 addresses from text."""
    regex = r'((?:[0-9]{1,3}\.){3}[0-9]{1,3})?'
    addresses = []
    for match in re.finditer(regex, text):
        if match.group(1) is not None:
            address = match.group(1)
            addresses.append(address)
    return addresses


def get_endpoints(text: str) -> list[str]:
    """Get endpoints from text."""
    regex = r'(\/[a-zA-Z0-9&/=?-_%-&/]*)?'
    endpoints = []
    for match in re.finditer(regex, text):
        if match.group(1) is not None:
            endpoint = match.group(1)
            endpoints.append(endpoint)
    return endpoints


def calculate_times(times: list[tuple[int, int, int]]) -> list[int]:
    """Calculate times."""
    calculated_times = []
    for time in times:
        hours = time[0] - time[2]
        if hours > 23:
            hours -= 24
        if hours < 0:
            hours += 24
        minutes = time[1]
        calculated_times.append(hours * 60 + minutes)
    return calculated_times


def normalize_times(minutes: list[int]) -> list[str]:
    """Convert minutes to 12 hour time."""
    normalized_times = []
    for minute in minutes:
        hour = minute // 60
        minute = minute % 60
        am_pm = "AM" if hour < 12 else "PM"
        hour = hour % 12
        normalized_time = f"{hour:1d}:{minute:02d} {am_pm}"
        normalized_times.append(normalized_time)
    return normalized_times


def build_table_row(longest_key_length: int, key: str, row_data: list) -> str:
    """Build a table row."""
    if isinstance(row_data, list):
        if isinstance(row_data[0], int):
            list_of_strings = []
            for integer in row_data:
                list_of_strings.append(str(integer))
            row_data = list_of_strings
        value_string = ", ".join(row_data)
    else:
        value_string = str(row_data)

    row_string = f"{key:<{longest_key_length + 1}}| {str(value_string):>1}\n"
    return row_string


def get_longest_key_length(sorted_data_collection: dict) -> int:
    """Get longest key length."""
    max_key_length = 0
    for key in sorted_data_collection.keys():
        if max_key_length < max(max_key_length, len(key)):
            max_key_length = max(max_key_length, len(key))
    return max_key_length


if __name__ == '__main__':

    logs = """
            [15=53 UTC+7] /NBYFaC0 468.793.214.681
            [23-7 UTC+12] /1slr8I
            [07.46 UTC+4] usr:B3HIyLm 119.892.677.533
            """

    logs1 = """
            [-1b35 UTC-4] errOR 741
            [24a48 UTC+0] 776.330.579.818
            [02:53 UTC+5] usr:96NC9yqb /aA?Y4pK
            [5b05 UTC+5] ERrOr 700 268.495.856.225
            [24-09 UTC+10] usr:uJV5sf82_ eRrOR 844 715.545.485.989
            [04=54 UTC+3] eRROR 452
            [11=57 UTC-6] 15.822.272.473 error 9
            [15=53 UTC+7] /NBYFaC0 468.793.214.681
            [23-7 UTC+12] /1slr8I
            [07.46 UTC+4] usr:B3HIyLm 119.892.677.533
            """

    logs2 = """
                [10:53 UTC+3]
                [1:43 UTC+0]
                [14A3 UTC-4]
                [-1b35 UTC-4]
                [5b05 UTC+5]
                [02:53 UTC+5]
                """
    logs3 = """
                [02:53 UTC+5
                [02:43 UTC-5
                [02:63 UTC+5
                [24:53 UTC-5
                """
    logs4 = """
            [11234 UTC+0
            [1112 UTC+0
            [123 UTC+0
            [10:25 UTC+8 15.822.272.473 error 9
            [1000 UTC+0
            """

    print(create_table_string(logs1))

    # print(get_times(logs3))
    # print(get_usernames(logs))
    # print(get_errors(logs))
    # print(get_addresses(logs))

    # time     | 5:36 AM, 2:48 PM
    # user     | kasutaja
    # error    | 418
    # ipv4     | 192.168.0.255
    # endpoint | /tere

    # [-1b35 UTC-4] errOR 741
    # [24a48 UTC+0] 776.330.579.818
    # [02:53 UTC+5] usr:96NC9yqb /aA?Y4pK
    # [5b05 UTC+5] ERrOr 700 268.495.856.225
    # [24-09 UTC+10] usr:uJV5sf82_ eRrOR 844 715.545.485.989
    # [04=54 UTC+3] eRROR 452
    # [11=57 UTC-6] 15.822.272.473 error 9
    # [15=53 UTC+7] /NBYFaC0 468.793.214.681
    # [23-7 UTC+12] /1slr8I
    # [07.46 UTC+4] usr:B3HIyLm 119.892.677.533
    #
    # [0:60 UTC+0] bad
    # [0?0 UTC+0] ok
    # [0.0 UTC+0] also ok
