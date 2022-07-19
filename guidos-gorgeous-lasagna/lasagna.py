# CONSTANTS
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
    Calculates the bake time remaining in minutes, based on the EXPECTED_BAKE_TIME
    
    :param elapsed_bake_time: int the amount of time that has elapsed since the lasagna started baking
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_layers):
    """
    Calculates the amount of time in minutes it will take to prepare the lasagna
    
    :param num_layers: int number of layers in the lasagna
    :return: int the amount of total time to prepare each layer of the lasagna, derived from 'PREPARATION_TIME'
    """
    return num_layers * PREPARATION_TIME

def elapsed_time_in_minutes(num_layers, elapsed_bake_time):
    """
    Calculates the time in minutes that has elapsed from both preparing and baking the lasagna
   
    :param num_layers: int number of layers in the lasagna
    :param elapsed_bake_time: int the amount of time that has elapsed since the lasagna started baking
    :return: int the total time that has elapsed including prepration time
    """
    return preparation_time_in_minutes(num_layers) + elapsed_bake_time
