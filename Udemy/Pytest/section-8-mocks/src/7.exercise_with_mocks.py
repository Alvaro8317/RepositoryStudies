import datetime
from unittest.mock import Mock

friday = datetime.datetime(year=2023, month=5, day=5)
saturday = datetime.datetime(year=2023, month=5, day=6)
datetime = Mock()


def is_weekend() -> bool:
    today = datetime.datetime.today()
    return not 0 <= today.weekday() < 5


datetime.datetime.today.return_value = friday
print(is_weekend())

datetime.datetime.today.return_value = saturday
print(is_weekend())
