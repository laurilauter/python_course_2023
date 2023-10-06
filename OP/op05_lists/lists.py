"""Phone inventory."""


def phone_brand_and_models(all_phones: str):
    """
    Create a list of structured information about brands and models.

    For each different phone brand in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the brand (string),
    the second element is a list of models for the given brand (list of strings).

    No duplicate brands or models should be in the output.

    The order of the brands and models should be the same as in the input list (first appearance).

    "Honor Magic5,IPhone 11,IPhone 12,Google Pixel,Samsung Galaxy S22,IPhone 13,IPhone 13,Google Pixel2" =>
    [['Honor', ['Magic5']], ['IPhone', ['11', '12', '13']], ['Google', ['Pixel', 'Pixel2']], ['Samsung', ['Galaxy S22']]]
    """
    phones = all_phones.split(",")
    phone_collection = []
    if all_phones:
        for phone in phones:
            brand, *model = phone.split(" ")  # unpacking phone[0] to brand and the rest to model
            if not any(brand == i[0] for i in phone_collection):  # check if brand in phone_collection
                phone_collection.append([brand, []])
            if model:
                for j in phone_collection:
                    model_string = " ".join(model)
                    if j[0] == brand and model_string not in j[1]:  # prevent duplicate models
                        j[1].append(model_string)
                        break  # no point to look further
    return phone_collection


def add_phones(phone_list, all_phones) -> list:
    """
    Add phones from the list into the existing phone list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated phones (as in all the previous functions).
    The task is to add phones from the string into the list.

    Hint: This and phone_brand_and_models are very similar functions. Try to use one inside another.

    [['IPhone', ['11']], ['Google', ['Pixel']]] and "IPhone 12,Samsung Galaxy S22,IPhone 11"

        =>

    [['IPhone', ['11', '12']], ['Google', ['Pixel']], ['Samsung', ['Galaxy S22']]]
    """
    result = {}
    merged_list = []
    new_phones = phone_brand_and_models(all_phones)
    if new_phones:
        for key, value in phone_list + new_phones:  # looping over bot lists
            if key not in result:
                result[key] = []
            result[key].extend(value)
        # merged_list = [[key, list(set(value))] for key, value in result.items()]  # using set to get rid of duplicates
        merged_list = [[key, value] for key, value in result.items()]
    return merged_list


def number_of_phones(all_phones: str) -> list:
    """
    Create a list of tuples with brand quantities.

    The result is a list of tuples.
    Each tuple is in the form: (brand_name: str, quantity: int).
    The order of the tuples (brands) is the same as the first appearance in the list.
    """
    phone_count = []
    if all_phones:
        phones_to_count = phone_brand_and_models(all_phones)
        for phone in phones_to_count:
            brand = phone[0]
            count = len(phone[1])
            phone_count.append((brand, count))
    return phone_count


def phone_list_as_string(phone_list: list) -> str:
    """
    Create a list of phones.

    The input list is in the same format as the result of phone_brand_and_models function.
    The order of the elements in the string is the same as in the list.
    [['IPhone', ['11']], ['Google', ['Pixel']]] =>
    "IPhone 11,Google Pixel"
    """
    phones_string = ""
    if phone_list:
        for phone in phone_list:
            phones_string += str(phone[0]) + " "
            for model in phone[1]:
                phones_string += str(model) + ","
        phones_string = phones_string.rstrip(phones_string[-1])  # remove trailing ,
    return phones_string


if __name__ == '__main__':
    # print(phone_brand_and_models("Google GM1,Google GM1,Google GM2,IPhone IM1,IPhone IM2,IPhone IM3"))
    # print(
    #     phone_brand_and_models("Honor Magic5,Google Pixel2,Google Pixel6,IPhone 7,Google Pixel,Google Pixel,IPhone 14"))
    # # [['Honor', ['Magic5']], ['Google', ['Pixel2', 'Pixel6', 'Pixel']], ['IPhone', ['7', '14']]]
    #
    # print(phone_brand_and_models("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  # [['Google', ['Pixel']]]
    # print(phone_brand_and_models(""))  # []
    #
    print(add_phones([['IPhone', ['11']], ['Google', ['Pixel']]], "IPhone 12,Samsung Galaxy S22,IPhone 11"))
    # [['IPhone', ['11', '12']], ['Google', ['Pixel']], ['Samsung', ['Galaxy S22']]]
    #
    # print(number_of_phones(
    #     "IPhone 11,Google Pixel,Honor Magic5,IPhone 12"))  # [('IPhone', 2), ('Google', 1), ('Honor', 1)]
    #
    # print(number_of_phones("HTC one,HTC one,HTC one,HTC one"))  # [('HTC', 4)]
    #
    # print(number_of_phones(""))  # []
    #
    # print(phone_list_as_string([['IPhone', ['11']], ['Google', ['Pixel']]]))  # "IPhone 11,Google Pixel"
