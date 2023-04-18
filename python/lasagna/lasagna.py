EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(minutes):
    """ Calculate the time to bake a lasagna

    :param minutes: int number of minutes to remaining
    :return: int number of minutes to take done the lasagna
    """
    time = EXPECTED_BAKE_TIME - minutes
    return abs(time)

def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the time in minutes take to prepare a lasagna
    :param number_of_layers: int number of layers
    :return: the number of layers elevated two
    """
    return number_of_layers*PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the time to elapsed in minutes
    :param number_of_layers: int number of layers
    :param elapsed_bake_time: int number of elapsed time
    :return: int minutes elapsed
    """
    result = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return result


print(bake_time_remaining(30))
print(preparation_time_in_minutes(2))
print(elapsed_time_in_minutes(3,20))