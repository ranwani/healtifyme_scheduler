from datetime import datetime, timedelta
import logging

from scheduler.constants import SAMPLE_INPUT_OUTPUTS


def validate_input(week_config, current_time, n):
    """
    :param week_config: list of list of dictionary
    :param current_time: datetime.datetime
    :param n: int
    :return: None
    """
    if not all(True if isinstance(slot, dict) and 'start_time' in slot and 'end_time' in slot else False for day_list in week_config for slot in day_list):
        raise TypeError("week_config should be of format: \
                        [ [{'start_time':'09:00','end_time':'09:30'}, {'start_time':'10:30','end_time':'11:00'}], [] ]")
    elif len(week_config) != 7:
        raise TypeError("week_config should have config for all 7 days")
    elif not isinstance(current_time, datetime):
        raise TypeError('current_time should be a datetime.datetime object')
    elif not isinstance(n, int):
        raise TypeError('n should be an int')
    elif n < 0:
        raise ValueError('n should be positive')


def is_week_config_empty(week_config):
    """
    :param week_config: List of list of dictionaries
    :return: Bool
    """
    for day in week_config:
        if day:
            return False
    return True


def get_next_n_slots(week_config, current_time, n=10):
    """
    :param week_config: List of list of dictionaries
    :param current_time: datetime.datetime
    :param n: int
    :return: int
    """
    next_n_slots = []

    # Input validation checks
    validate_input(week_config, current_time, n)
    if is_week_config_empty(week_config) or n == 0:
        logging.info('Week config is empty or n is 0. No upcoming slots could be found.')
        return next_n_slots

    while n > 0:
        day_config = week_config[current_time.weekday()]  # Returns list of dictionaries for a particular day
        for slot in day_config:
            if n > 0:
                hours, minutes = slot.get('start_time', '00:00').split(':')
                slot_start_time = current_time.replace(hour=int(hours), minute=int(minutes), second=0, microsecond=0)

                hours, minutes = slot.get('end_time', '00:00').split(':')
                slot_end_time = current_time.replace(hour=int(hours), minute=int(minutes), second=0, microsecond=0)

                if slot_start_time > current_time:
                    next_n_slots.append({'start_time': str(slot_start_time), 'end_time': str(slot_end_time)})
                    n -= 1

        current_time = current_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)

    return next_n_slots


if __name__ == '__main__':
    for time_of_run, ip, expected_output in SAMPLE_INPUT_OUTPUTS:
        output = get_next_n_slots(ip, time_of_run)
        assert output == expected_output
