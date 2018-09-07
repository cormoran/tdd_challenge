import re


def validate_addr(addr):
    index = addr.rfind("@")
    if index == -1:
        return False
    host = addr[:index]
    domain = addr[index + 1:]
    if not(validate_domain(domain)):
        return False
    return validate_domain(host) or validate_quated_string(host)


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
    # LQ5
    if len(quated_str) < 2:
        return False
    # LQ1,2
    if quated_str[0] != '"' or quated_str[-1] != '"':
        return False
    quated_str = quated_str[1:-1]
    if re.match(
            "^[a-zA-Z0-9!#$%&'*+\-/=?^_`{\|}~\(\),.:;<>@\[\]\"\\\\]*$",
            quated_str) is None:
        return False
    return True
