def exchange_money(budget, exchange_rate):
    amount = budget * (1 / exchange_rate)
    return amount


def get_change(budget, exchanging_value):
    if exchanging_value == 1:
        return budget
    amount = budget - exchanging_value
    return abs(amount)


def get_value_of_bills(denomination, number_of_bills):
    value = denomination * number_of_bills
    return int(value)


def get_number_of_bills(budget, denomination):
    if denomination == 1:
        return budget
    number = budget // denomination
    return int(number)


def get_leftover_of_bills(budget, denomination):
    number_of_bills = get_number_of_bills(budget, denomination)
    value_of_bills = get_value_of_bills(denomination, number_of_bills)
    change = get_change(budget, value_of_bills)
    return change


def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_percent = spread / 100
    new_exchange_rate = exchange_rate + (exchange_rate * spread_percent)
    amount = exchange_money(budget, new_exchange_rate)
    change = get_leftover_of_bills(amount, denomination)
    new_amount = int(abs(amount - change))
    return new_amount

print(exchange_money(127.5, 1.2))
print(get_change(127.5, 120))
print(get_value_of_bills(5, 128))
print(get_number_of_bills(127.5, 5))
print(get_leftover_of_bills(127.5, 20))
print(exchangeable_value(127.25, 1.20, 10, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))
print(exchangeable_value(100000, 10.61, 10, 1))
