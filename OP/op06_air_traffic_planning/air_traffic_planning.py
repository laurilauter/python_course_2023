"""Air traffic planning."""


def to_minutes(time: str) -> int:
    """Convert time string to minutes."""
    time_fragments = time.split(":")
    hours = int(time_fragments[0])
    minutes = int(time_fragments[1])
    minutes += hours * 60
    return minutes


def update_delayed_flight(schedule: dict[str, tuple[str, str]], delayed_flight_number: str, new_departure_time: str) -> dict[str, tuple[str, str]]:
    """
    Update the departure time of a delayed flight in the flight schedule.

    Return a dictionary where the time of the specified flight is modified.
    This means that the result dictionary should not contain the old time,
    instead a new departure time points to the specified flight.
    The input schedule cannot be changed.

    :param schedule: Dictionary of flights ({time string: (destination, flight number)})
    :param delayed_flight_number: Flight number of the delayed flight
    :param new_departure_time: New departure time for the delayed flight
    :return: Updated flight schedule with the delayed flight's departure time changed
    """
    updated_schedule = schedule.copy()
    for key, value in schedule.items():
        flight_number = value[1]
        departure_time = key
        if flight_number == delayed_flight_number:
            updated_schedule[new_departure_time] = updated_schedule.pop(departure_time)  # return old value for new key
    return dict(sorted(updated_schedule.items()))  # sorting the dict after the update above


def cancel_flight(schedule: dict[str, tuple[str, str]], cancelled_flight_number: str) -> dict[str, tuple[str, str]]:
    """
    Create a new schedule where the specified flight is cancelled.

    The function cannot modify the existing schedule parameter.
    Instead, create a new dictionary where the cancelled flight is not added.

    :param schedule: Dictionary of flights ({time: (destination, flight number)})
    :param cancelled_flight_number: Flight number of the cancelled flight
    :return: New flight schedule with the cancelled flight removed
    """
    updated_schedule = schedule.copy()
    for key, value in schedule.items():
        flight_number = value[1]
        departure_time = key
        if flight_number == cancelled_flight_number:
            updated_schedule.pop(departure_time)  # remove canceled flight
    return dict(sorted(updated_schedule.items()))  # sort the dict after the above update


def busiest_time(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour(s) at the airport based on the flight schedule.

    Finds the busiest hour(s) at the airport based on the flight schedule. The busiest hour(s)
    is/are determined by counting the number of flights departing in each hour of the day.
    All flights departing with the same hour in their departure time, are counted into the same hour.

    The function returns a list of strings of the busiest hours, sorted in ascending order, such as ["08", "21"].

    :param schedule: Dictionary containing the flight schedule, where keys are departure times
                     in the format "HH:mm" and values are tuples containing destination and flight number.
    :return: List of strings representing the busiest hour(s) in 24-hour format, such as ["08", "21"].
    """
    busiest_hours = []
    hours_counter = {}
    for time in schedule.keys():
        hour = time[:2]
        if hour not in hours_counter:
            hours_counter[hour] = 1
        else:
            hours_counter[hour] = hours_counter[hour] + 1

    # # prepare list for display
    max_value = 0
    for key, value in hours_counter.items():
        if value > max_value:
            max_value = value
    for key, value in hours_counter.items():
        if value == max_value:
            busiest_hours.append(key)
    return busiest_hours


def connecting_flights(schedule: dict[str, tuple[str, str]], arrival: tuple[str, str]) -> list[tuple[str, str]]:
    """
    Find connecting flights based on the provided arrival information and flight schedule.

    The function takes a flight schedule and the arrival time and location of a flight,
    and returns a list of available connecting flights. A connecting flight is considered
    available if its departure time is at least 45 minutes after the arrival time, but less
    than 4 hours after the arrival time. Additionally, a connecting flight must not go back
    to the same place the arriving flight came from.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :param arrival: Tuple containing the arrival time and the location the flight is
                    arriving from. For example:
                    ("11:05", "Tallinn")

    :return: A list of tuples containing the departure time and destination of the
             available connecting flights, sorted by departure time. For example:
             [
                 ("14:00", "Paris"),
                 ("15:00", "Berlin")
             ]
             If no connecting flights are available, the function returns an empty list.
    """
    available_connecting_flights = []
    arrival_time = to_minutes(arrival[0])

    for key, value in schedule.items():
        if 45 <= to_minutes(key) - arrival_time < 240 and value[0] != arrival[1]:
            available_connecting_flights.append((key, value[0]))
    return available_connecting_flights


def busiest_hour(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour-long slot(s) in the schedule.

    One hour slot duration is 60 minutes (or the diff of two times is less than 60).
    So, 15:00 and 16:00 are not in the same slot.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :return: A list of strings representing the starting time(s) of the busiest hour-long
             slot(s) in ascending order. For example:
             ["08:00", "15:20"]
             If the schedule is empty, returns an empty list.
    """
    busiest_hour_slots = []
    hour_counts = {}

    # populate hour_counts
    for hour_start_time in schedule.keys():
        if hour_start_time not in hour_counts:
            hour_counts[hour_start_time] = 0
        hour_counts[hour_start_time] += 1

    # calculate hour_counts
    for key, value in hour_counts.items():
        for time in hour_counts.keys():
            if 0 < to_minutes(time) - to_minutes(key) < 60:
                hour_counts[key] += 1

    # Find the busiest slot
    max_count = 0
    if hour_counts.values():
        max_count = max(hour_counts.values())
    for hour_start_time, count in hour_counts.items():
        if count == max_count:
            busiest_hour_slots.append(hour_start_time)
    # Sort the busiest hours in ascending order.
    busiest_hour_slots.sort()
    return busiest_hour_slots


def most_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the most passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the most popular destination.
    """
    # create initial passengers_to_destination dict
    passengers_to_destination = {}
    for value in schedule.values():
        if value[0] not in passengers_to_destination:
            passengers_to_destination[value[0]] = 0

    # populate dict with counts
    for key, value in schedule.items():
        for flight, count in passenger_count.items():
            if flight == value[1]:
                passengers_to_destination[value[0]] += count
    destination = max(passengers_to_destination, key=passengers_to_destination.get)  # return the corresponding key
    return destination


def least_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the fewest passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the least popular destination.
    """
    # create initial passengers_to_destination dict
    passengers_to_destination = {}
    for value in schedule.values():
        if value[0] not in passengers_to_destination:
            passengers_to_destination[value[0]] = 0

    # populate dict with counts
    for key, value in schedule.items():
        for flight, count in passenger_count.items():
            if flight == value[1]:
                passengers_to_destination[value[0]] += count
    destination = min(passengers_to_destination, key=passengers_to_destination.get)  # return the corresponding key
    return destination


if __name__ == '__main__':
    # schedule = {
    #     "06:15": ("Tallinn", "OWL6754"),
    #     "11:35": ("Helsinki", "BHM2345")
    # }
    # new_schedule = update_delayed_flight(schedule, "OWL6754", "09:00")
    # print(schedule)
    # # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    # print(new_schedule)
    # # {'09:00': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}

    # new_schedule = cancel_flight(schedule, "OWL6754")
    # print(schedule)
    # # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    # print(new_schedule)
    # # {'11:35': ('Helsinki', 'BHM2345')}
    #
    # schedule = {
    #     "04:35": ("Maardu", "MWL6754"),
    #     "06:15": ("Tallinn", "OWL6754"),
    #     "06:30": ("Paris", "OWL6751"),
    #     "07:29": ("London", "OWL6756"),
    #     "08:00": ("New York", "OWL6759"),
    #     "11:30": ("Tokyo", "OWL6752"),
    #     "11:35": ("Helsinki", "BHM2345"),
    #     "19:35": ("Paris", "BHM2346"),
    #     "20:35": ("Helsinki", "BHM2347"),
    #     "22:35": ("Tallinn", "TLN1001"),
    # }

    schedule = {}
    # print(busiest_time(schedule))
    # # ['06', '11']

    # print(connecting_flights(schedule, ("04:00", "Tallinn")))
    # # [('06:30', 'Paris'), ('07:29', 'London')]

    print(busiest_hour(schedule))
    # ['06:15', '06:30', '07:29', '11:30']
    # 19:35 does not match because 20:35 is not in the same slot
    # #
    # # flight number: number of passengers
    # passengers = {
    #     "MWL6754": 100,
    #     "OWL6754": 85,
    #     "OWL6751": 103,
    #     "OWL6756": 87,
    #     "OWL6759": 118,
    #     "OWL6752": 90,
    #     "BHM2345": 111,
    #     "BHM2346": 102,
    #     "BHM2347": 94,
    #     "TLN1001": 1
    # }
    #
    # print(most_popular_destination(schedule, passengers))
    # # Paris
    # #
    # print(least_popular_destination(schedule, passengers))
    # # Tallinn
