import os
import sys
from datetime import time
sys.path.insert(1, os.path.join(sys.path[0], '..'))


from queries.core import create_table, add_seat, delete_seat, edit_seat, seat_info, print_event_by_place, print_events, create_ticket, cancel_booking

if __name__ == "__main__":
    create_table()
    add_seat('1', time(13, 0))
    delete_seat('1')



