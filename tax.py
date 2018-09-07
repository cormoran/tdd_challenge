def calc_price(values):
    assert type(values) == list
    if len(values) > 0:
        assert 0 <= min(values) and max(values) <= 100 * 10000
    return int(sum(values) * 1.10 + 0.5)


if __name__ == '__main__':
    while True:
        try:
            values = list(map(int, input().split(',')))
            print(calc_price(values))
        except EOFError:
            break