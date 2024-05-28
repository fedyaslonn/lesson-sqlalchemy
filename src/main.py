import os
import sys
from datetime import time
sys.path.insert(1, os.path.join(sys.path[0], '..'))


from queries.core import create_table,add_event, add_seat, delete_seat, edit_seat, seat_info, print_event_by_place, print_events, create_ticket, cancel_ticket

if __name__ == "__main__":
    create_table()
    add_event('Concert', time(15,0,22))
    add_event('Concerttt', time(13,0,1))
    add_seat(1,1)
    add_seat(2, 3)
    create_ticket(2,300, 'Concert')
    add_seat(39, 4)
    add_seat(10, 5)
    delete_seat(39)
    edit_seat(10,11)
    seat_info(2)
    print_event_by_place(11)
    print_events('Conce')
    create_ticket(45, 20, 'Concert')
    cancel_ticket(45)


