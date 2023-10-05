"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    """
    phones = []
    if all_phones:
        phones = all_phones.split(",")
    return phones


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google", "Honor"]
    """
    phones = all_phones.split(",")
    brands = []
    if all_phones:
        for phone in phones:
            brand = phone.split(" ")[0]
            if brand not in brands:
                brands.append(brand)
    return brands


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).

    "Honor Magic5,Google Pixel,Honor Magic4" => ['Magic5', 'Pixel', 'Magic4']
    """
    phones = all_phones.split(",")
    models = []
    if all_phones:
        for phone in phones:
            phone_fragments = phone.split(" ")
            model = phone_fragments
            if len(phone_fragments) > 1:
                model = phone_fragments[1:]
            if model[0] not in models:
                models.append(" ".join(model))
    return models


def search_by_brand(all_phones: str, search_term: str) -> list:
    """Return phone by brand."""
    phones = all_phones.split(",")
    search_results = []
    for phone in phones:
        phone_fragments = phone.split(" ")
        phone_fragments = phone_fragments[:1]
        for i in phone_fragments:
            if search_term.lower() in i.lower() and len(search_term) == len(i):
                search_results.append(phone)
    return search_results


def search_by_model(all_phones: str, search_term: str) -> list:
    """Return phone by model."""
    phones = all_phones.split(",")
    search_results = []
    for phone in phones:
        phone_fragments = phone.split(" ")
        phone_fragments = phone_fragments[1:]
        for i in phone_fragments:
            if search_term.lower() in i.lower() and len(search_term) == len(i):
                search_results.append(phone)
    return search_results


if __name__ == '__main__':

    print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))  # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    print(list_of_phones(""))  # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    print(phone_brands(
        "Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11"))  # ['Google', 'Honor', 'IPhone', 'Samsung']
    print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  # ['Google']
    print(phone_brands(""))  # []
    print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14"))  # ['14', 'Pixel', 'Magic5']
    print(phone_models("Samsung Galaxy S23,IPhone 14 Pro Max"))  # ['14', 'Pixel', 'Magic5']
    print(phone_models(""))  # ['14', 'Pixel', 'Magic5']
    print(phone_models("one,one,one,one"))  # ['14', 'Pixel', 'Magic5']

    print(search_by_brand("IPhone 14,iphone 7,IPHONE 11 Pro, Something", "IPhone"))  # ['14', 'Pixel', 'Magic5']
    print(search_by_brand("IPhone 14,iphone 7,IPHONE 11 Pro, Something", "Pro"))  # ['14', 'Pixel', 'Magic5']

    print(search_by_model("IPhone X,IPhone 12 Pro,IPhone 14 pro Max,Something", "Pro"))  # ['14', 'Pixel', 'Magic5']
    print(search_by_model("IPhone X,IPhone 12 Pro,IPhone 14 pro Max", "14"))  # ['14', 'Pixel', 'Magic5']
    print(search_by_model("IPhone X,IPhone 12 Pro,IPhone 14 pro Max", "12 Pro"))  # ['14', 'Pixel', 'Magic5']
    print(search_by_model("IPhone X,IPhone 12 Pro,IPhone 14 pro Max", "iphone"))  # ['14', 'Pixel', 'Magic5']
