import re


def validate_addr(addr):
    return True


def validate_domain(domain):
    # D5
    if len(domain) == 0:
        return False
    # D2, D3
    if domain[0] == '.' or domain[-1] == '.':
        return False
    # D 4
    if domain.find('..') >= 0:
        return False
    return re.match("^[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~.]*$", domain) is not None


def validate_quated_string(quated_str):
    return True