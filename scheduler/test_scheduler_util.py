import unittest

from scheduler.constants import SAMPLE_INPUT_OUTPUTS, SAMPLE_INPUT_OUTPUTS_WITH_N, FAILED_VALIDATION_INPUT_OUTPUTS
from scheduler.scheduler_util import get_next_n_slots, validate_input


class SchedulerUtilTests(unittest.TestCase):

    def test_scheduler(self):
        for time_of_run, week_config, expected_output in SAMPLE_INPUT_OUTPUTS:
            output = get_next_n_slots(week_config, time_of_run)
            self.assertEqual(output, expected_output)

    def test_scheduler_with_n(self):
        for time_of_run, week_config, n, expected_output in SAMPLE_INPUT_OUTPUTS_WITH_N:
            output = get_next_n_slots(week_config, time_of_run, n)
            self.assertEqual(output, expected_output)

    def test_validate_input(self):
        for time_of_run, week_config, n, expected_exception in FAILED_VALIDATION_INPUT_OUTPUTS:
            with self.assertRaises(expected_exception):
                validate_input(week_config, time_of_run, n)
