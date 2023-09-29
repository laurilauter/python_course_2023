"""Email validation."""


# Write your functions here
def has_at_symbol(email: str):
    """
    Check if email has at symbol
    """
    if "@" in email:
        return True
    return False


def is_valid_username(email):
    """
    Check if email has valid username
    """
    fragments = email.split("@")[:-1]  # remove tha last element
    username = "@".join(fragments)  # if there is anything to join, add @ back in
    symbols = ' ?+-,;:%¤#"&/@[_'
    for character in username:
        if character in symbols:
            return False
    return True


def find_domain(email):
    """
    Extract domain from email
    """
    fragments = email.split(".")[-2:]
    domain = fragments[0].split("@")[-1] + "." + fragments[-1]
    return domain


def is_valid_domain(email):
    """
    Check if email has valid domain
    """
    domain = find_domain(email)
    fragments = domain.split(".")
    if "." in domain:
        if domain.replace(".", "").isalpha() is True:
            if 3 <= len(fragments[0]) <= 10:
                if 2 <= len(fragments[1]) <= 5:
                    return True
    return False


def is_valid_email_address(email):
    """
    Check if email address is valid
    """
    def check_conditions(email_to_validate):
        list_of_conditions = [has_at_symbol(email_to_validate),
                              is_valid_username(email_to_validate),
                              is_valid_domain(email_to_validate)]
        print(list_of_conditions)
        return all(list_of_conditions)

    return check_conditions(email)


def create_email_address(domain, username):
    """
    Create email address
    """
    email = username + "@" + domain
    if is_valid_email_address(email):
        return email
    return "Cannot create a valid email address using the given parameters!"


if __name__ == '__main__':
    print("Email has the @ symbol:")
    print(has_at_symbol("joonas.kivi@gmail.com"))  # -> True
    print(has_at_symbol("joonas.kivigmail.com"))  # -> False

    print("\nUsername has no special symbols:")
    print(is_valid_username("martalumi@taltech.ee"))  # -> True
    print(is_valid_username("marta.lumi@taltech.ee"))  # -> True
    print(is_valid_username("marta lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta&lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta@lumi@taltech.ee"))  # -> False
    print(is_valid_username("karu.[m6mm@mesi.ee"))  # -> False

    print("\nFind the email domain name:")
    print(find_domain("karla.karu@saku.ee"))  # -> saku.ee
    print(find_domain("karla.karu@taltech.ee"))  # -> taltech.ee
    print(find_domain("karla.karu@yahoo.com"))  # -> yahoo.com
    print(find_domain("karla@karu@yahoo.com"))  # -> yahoo.com

    print("\nCheck if the domain is correct:")
    print(is_valid_domain("pihkva.pihvid@ttu.ee"))  # -> True
    print(is_valid_domain("metsatoll@&gmail.com"))  # -> False
    print(is_valid_domain("ewewewew@i.u.i.u.ewww"))  # -> False
    print(is_valid_domain("pannkook@m.oos"))  # -> False

    print("\nIs the email valid:")
    print(is_valid_email_address("DARJA.darja@gmail.com"))  # -> True
    print(is_valid_email_address("DARJA=darjamail.com"))  # -> False

    print("\nCreate your own email address:")
    print(create_email_address("hot.ee", "vana.ema"))  # -> vana.ema@hot.ee
    print(create_email_address("jaani.org", "lennakuurma"))  # -> lennakuurma@jaani.org
    print(create_email_address("koobas.com",
                               "karu&pojad"))  # -> Cannot create a valid email address using the given parameters!

    print(create_email_address("taltech.ee", "uni_id"))  # -> Cannot create a valid email address using the given parameters!