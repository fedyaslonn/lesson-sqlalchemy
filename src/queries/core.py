from sqlalchemy import text
from src.database import sync_engine, session_factory
from src.models import metadata_obj, Event, Places, Ticket

def create_table():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

def add_event(new_name, new_date):
    with session_factory() as session:
        create_event = Event(name=new_name, date=new_date)
        session.add(create_event)
        session.commit()

def add_seat(num, new_event_id):
    with session_factory() as session:
        create_seat = Places(seat_num=num, event_location=new_event_id)
        session.add(create_seat)
        session.commit()

def add_ticket(new_place, new_price, new_event_name):
    with session_factory() as session:
        event = session.query(Event).filter(Event.name == new_event_name).first()
        if not event:
            print('Событие не найдено')
            return

        ticket = Ticket(price=new_price, event_name=new_event_name, seat_number=new_place)
        session.add(ticket)
        session.commit()

        print("Билет успешно забронирован")

def delete_seat(seat_to_del):
    with session_factory() as session:
        event_to_delete = session.query(Places).filter(Places.seat_num == seat_to_del).first()
        if event_to_delete:
            session.delete(event_to_delete)
            session.commit()
        else:
            print("Не найдено")

def edit_seat(num_to_replace, new_seat_num):
    with session_factory() as session:
        seat_to_edit = session.query(Places).filter(Places.seat_num == num_to_replace).first()
        if seat_to_edit:
            existing_seat = session.query(Places).filter(Places.seat_num == new_seat_num).first()
            if existing_seat:
                print("Место с таким номером уже существует")
            else:
                seat_to_edit.seat_num = new_seat_num
                session.commit()
                print(f"Место номер {num_to_replace} успешно изменено на {new_seat_num}")
        else:
            print("Не найдено")

def seat_info(seat_number):
    with session_factory() as session:
        seat_about = session.query(Places).filter(Places.seat_num == seat_number).first()
        if seat_about:
            ticket_about = session.query(Ticket).filter(Ticket.seat_number == seat_number).first()
            if ticket_about:
                print(f"Инфомарция о месте под номером {seat_about.seat_num}:"
                      f"Цена билета {ticket_about.price}")
            else:
                print(f"Место под номером {seat_about.seat_num} не имеет забронированного билета")
        else:
            print('Такого места нету')

def print_event_by_place(loc):
    with session_factory() as session:
        seat = session.query(Places).filter(Places.seat_num == loc).first()
        if seat:
            event = session.query(Event).filter(Event.ticket_id == seat.ticket).first()
            if event:
                print(f"Событие: {event.name}, Дата: {event.date}")
            else:
                print("Событие не найдено")
        else:
            print("Место не найдено")

def print_events(name):
    with session_factory() as session:
        event_to_find = session.query(Event).filter(Event.name.ilike(f'%{name}%')).all()
        if event_to_find:
            print('Совпадающие мероприятия: ')
            for event in event_to_find:
                print(f"Имя мероприятия: {event.name}")
                print(f"Дата мероприятия: {event.date}")
        else:
            print(f"Мероприятие не найдено")


def create_ticket(new_id, new_price, new_event_name):
    with session_factory() as session:
        event = session.query(Event).filter(Event.name == new_event_name).first()
        if not event:
            print('Событие не найдено')
            return

        ticket = Ticket(price=new_price, event_name=new_event_name, seat_number=new_id)
        session.add(ticket)
        session.commit()

        print("Билет успешно забронирован")


def cancel_ticket(ticket_num):
    with session_factory() as session:
        ticket = session.query(Ticket).filter(Ticket.seat_number == ticket_num).first()
        if not ticket:
            print("Билет не найден")
            return

        session.delete(ticket)
        session.commit()

        print("Бронирование успешно отменено")
