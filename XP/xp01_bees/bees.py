"""Whether bees meet."""


def do_bees_meet(honeycomb_width: int, honeyhopper_data: str, pollenpaddle_data: str) -> bool:
    """Return whether bees meet."""
    def convert_to_int(string):
        list_of_letters = string.split(",")
        list_of_numbers = []
        for i in list_of_letters:
            list_of_numbers.append(int(i))
        return list_of_numbers

    p1 = convert_to_int(honeyhopper_data)
    p2 = convert_to_int(pollenpaddle_data)

    if ((len(p1) or len(p2)) < 4 or
            (honeyhopper_data.isalpha() or pollenpaddle_data.isalpha())):
        raise ValueError("Insufficient data for sequence identification")

    if (p1[0] <= p2[-1] and p2[0] <= p1[-1]) or (p2[0] <= p1[-1] and p1[0] <= p2[-1]):
        return True
    return False


if __name__ == '__main__':
    print(do_bees_meet(50, "1,2,3,4,5", "1,2,4,8,16"))  # True


