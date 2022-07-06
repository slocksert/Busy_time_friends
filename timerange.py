from dataclasses import dataclass, field
import helpers as h

@dataclass
class TimeRange:
    start_time : str # 00:30
    end_time : str # 05:00

    start_minutes : int = field(init=False, repr=False)
    end_minutes : int = field(init=False, repr=False)

    minutes_range : range = field(init=False, repr=False)

    def __post_init__(self):
        self.start_minutes = h.timerange_to_minutes(self.start_time)
        self.end_minutes = h.timerange_to_minutes(self.end_time)
        self.minutes_range = range(self.start_minutes, self.end_minutes)

t1 = TimeRange(start_time='02:00', end_time='12:00')
