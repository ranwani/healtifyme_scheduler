from datetime import datetime

#  Constants with n = 10
DATE_1 = datetime(2017, 1, 1, 20, 30)  # Sunday
INPUT_1 = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
                {"start_time": "07:00", "end_time": "07:30"},
                {"start_time": "07:30", "end_time": "08:00"}
            ],
            [  # Tuesday
            ],
            [  # Wednesday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
                {"start_time": "07:00", "end_time": "07:30"},
                {"start_time": "07:30", "end_time": "08:00"}
            ],
            [  # Thursday
                {"start_time": "09:00", "end_time": "09:30"},
                {"start_time": "09:30", "end_time": "10:00"},
                {"start_time": "10:00", "end_time": "10:30"},
                {"start_time": "10:30", "end_time": "11:00"}
            ],
            [  # Friday
            ],
            [  # Saturday
            ],
            [  # Sunday
            ]
]
OUTPUT_1 = [
                {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
                {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
                {"start_time": "2017-01-02 07:00:00", "end_time": "2017-01-02 07:30:00"},
                {"start_time": "2017-01-02 07:30:00", "end_time": "2017-01-02 08:00:00"},
                {"start_time": "2017-01-04 06:00:00", "end_time": "2017-01-04 06:30:00"},
                {"start_time": "2017-01-04 06:30:00", "end_time": "2017-01-04 07:00:00"},
                {"start_time": "2017-01-04 07:00:00", "end_time": "2017-01-04 07:30:00"},
                {"start_time": "2017-01-04 07:30:00", "end_time": "2017-01-04 08:00:00"},
                {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 09:30:00"},
                {"start_time": "2017-01-05 09:30:00", "end_time": "2017-01-05 10:00:00"}
]

DATE_2 = datetime(2017, 1, 1, 20, 30)  # Sunday
INPUT_2 = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
]
OUTPUT_2 = []

DATE_3 = datetime(2017, 1, 1, 20, 30)  # Sunday
INPUT_3 = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
            ],
            [  # Tuesday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "07:00", "end_time": "07:30"},
                {"start_time": "07:30", "end_time": "07:45"}
            ],
            [  # Wednesday
            ],
            [  # Thursday
                {"start_time": "09:00", "end_time": "10:00"}
            ],
            [  # Friday
            ],
            [  # Saturday
            ],
            [  # Sunday
            ]
]
OUTPUT_3 = [
                {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
                {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
                {"start_time": "2017-01-03 06:00:00", "end_time": "2017-01-03 06:30:00"},
                {"start_time": "2017-01-03 07:00:00", "end_time": "2017-01-03 07:30:00"},
                {"start_time": "2017-01-03 07:30:00", "end_time": "2017-01-03 07:45:00"},
                {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 10:00:00"},
                {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},
                {"start_time": "2017-01-09 06:30:00", "end_time": "2017-01-09 07:00:00"},
                {"start_time": "2017-01-10 06:00:00", "end_time": "2017-01-10 06:30:00"},
                {"start_time": "2017-01-10 07:00:00", "end_time": "2017-01-10 07:30:00"}
]

#  Constants with n = 6
NUM_4 = 6
DATE_4 = datetime(2017, 1, 1, 20, 30)  # Sunday
INPUT_4 = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
            ],
            [  # Tuesday
                {"start_time": "06:00", "end_time": "06:30"},
                {"start_time": "07:00", "end_time": "07:30"},
                {"start_time": "07:30", "end_time": "07:45"}
            ],
            [  # Wednesday
            ],
            [  # Thursday
                {"start_time": "09:00", "end_time": "10:00"}
            ],
            [  # Friday
            ],
            [  # Saturday
            ],
            [  # Sunday
            ]
]
OUTPUT_4 = [
                {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
                {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
                {"start_time": "2017-01-03 06:00:00", "end_time": "2017-01-03 06:30:00"},
                {"start_time": "2017-01-03 07:00:00", "end_time": "2017-01-03 07:30:00"},
                {"start_time": "2017-01-03 07:30:00", "end_time": "2017-01-03 07:45:00"},
                {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 10:00:00"}
]

#  Constants with n = 4 and a different date
NUM_5 = 4
DATE_5 = datetime(2019, 5, 4, 20, 30)  # Saturday
INPUT_5 = [
            [  # Monday
                {"start_time": "06:00", "end_time": "06:30"},
            ],
            [  # Tuesday
            ],
            [  # Wednesday
            ],
            [  # Thursday
            ],
            [  # Friday
            ],
            [  # Saturday
                {"start_time": "09:00", "end_time": "10:00"}
            ],
            [  # Sunday
            ]
]
OUTPUT_5 = [
                {"start_time": "2019-05-06 06:00:00", "end_time": "2019-05-06 06:30:00"},
                {"start_time": "2019-05-11 09:00:00", "end_time": "2019-05-11 10:00:00"},
                {"start_time": "2019-05-13 06:00:00", "end_time": "2019-05-13 06:30:00"},
                {"start_time": "2019-05-18 09:00:00", "end_time": "2019-05-18 10:00:00"}
]

#  Failed Validation Constants

#  Case 2: Length of week_config is not 7
NUM_6 = 10
DATE_6 = datetime(2017, 1, 1, 20, 30)  # Sunday
INPUT_6 = [
            [],
            [],
            [],
            [],
            [],
            []
]
EXCEPTION_TYPE_6 = TypeError

#  Case 3: current_date is not a datetime.datetime object
NUM_7 = 10
DATE_7 = datetime.now().strftime('%Y')
INPUT_7 = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
]
EXCEPTION_TYPE_7 = TypeError

#  Case 4: n is not a int
NUM_8 = 'z'
DATE_8 = datetime.now()
INPUT_8 = [
            [],
            [],
            [],
            [],
            [],
            [],
            []
]
EXCEPTION_TYPE_8 = TypeError


#  Case 5: n is smaller than 0
NUM_9 = -2
DATE_9 = datetime.now()
INPUT_9 = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
]
EXCEPTION_TYPE_9 = ValueError

#  Case 6: start_time key missing from Monday's dict
NUM_10 = 10
DATE_10 = datetime(2017, 1, 1, 20, 30)
INPUT_10 = [
            [  # Monday
                {"": "06:00", "end_time": "06:30"},
                {"start_time": "06:30", "end_time": "07:00"},
            ],
            [  # Tuesday
            ],
            [  # Wednesday
            ],
            [  # Thursday
                {"start_time": "09:00", "end_time": "10:00"}
            ],
            [  # Friday
            ],
            [  # Saturday
            ],
            [  # Sunday
            ]
]
EXCEPTION_TYPE_10 = TypeError


SAMPLE_INPUT_OUTPUTS = [
    (DATE_1, INPUT_1, OUTPUT_1),
    (DATE_2, INPUT_2, OUTPUT_2),
    (DATE_3, INPUT_3, OUTPUT_3)
]

SAMPLE_INPUT_OUTPUTS_WITH_N = [
    (DATE_4, INPUT_4, NUM_4, OUTPUT_4),
    (DATE_5, INPUT_5, NUM_5, OUTPUT_5)
]

FAILED_VALIDATION_INPUT_OUTPUTS = [
    (DATE_6, INPUT_6, NUM_6, EXCEPTION_TYPE_6),
    (DATE_7, INPUT_7, NUM_7, EXCEPTION_TYPE_7),
    (DATE_8, INPUT_8, NUM_8, EXCEPTION_TYPE_8),
    (DATE_9, INPUT_9, NUM_9, EXCEPTION_TYPE_9),
    (DATE_10, INPUT_10, NUM_10, EXCEPTION_TYPE_10),
]