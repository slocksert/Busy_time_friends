from timerange import TimeRange
from friend import Friend
from custom_list import CustomList
import helpers as h

def main():
    avaialable_minutes = CustomList(range(1440))
    f1 = Friend('Jim')
    f1.add_busy_range(TimeRange(start_time='08:00', end_time='10:00'))
    f2 = Friend('Chris')
    f2.add_busy_range(TimeRange(start_time='08:00', end_time='14:00'))
    f2.add_busy_range(TimeRange(start_time='18:00', end_time='23:30'))
    f3 = Friend('Michael')
    f3.add_busy_range(TimeRange(start_time='17:00', end_time='23:00'))
    for m in avaialable_minutes[:]:
        for r in Friend.all_busy_minutes_range:
            if m in r:
                avaialable_minutes.remove_if_exist(m)
    
    for tr in h.prettify_available_minutes(avaialable_minutes):
        print(f'You can meet in {tr}')

if __name__ == '__main__':
    main()
