from sqlalchemy import text
from src.database import sync_engine, session_factory
from src.models import metadata_obj, Event, Places, Ticket

def create_table():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

def add_seat(name, date):
    with session_factory() as session:
        create_event = Event(name=name, date=date)
        session.add(create_event)
        session.commit()

def delete_seat(seat_to_del):
    with session_factory() as session:
        event_to_delete = session.query(Places).filter(Places.id == seat_to_del).first()
        if event_to_delete:
            session.delete(seat_to_del)
            session.commit()
        else:
            print("Не найдено")

def edit_seat(seat_id, num_to_replace):
    with session_factory() as session:
        seat_to_edit = session.query(Places).filter(Places.id == seat_id)
        if seat_to_edit:
            seat_to_edit.name= num_to_replace
            session.commit()
        else:
            print("Не найдено")

def seat_info(seat_id):
    with session_factory() as session:
        seat_about = session.query(Places).filter(Places.id == seat_id)
        if seat_about:
            print(f"Инфомарция о месте под номером {Places.seat_number}:"
                  f"Номер билета {Places.ticket_id}")
        else:
            print('Такого места нету')

def print_event_by_place(seat_id):
    with session_factory() as session:
        seat = session.query(Places).filter(Places.id == seat_id).first()
        if seat:
            event = session.query(Event).filter(Event.id == seat.event_id).first()
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


def create_ticket(event_id, seat_id, price):
    with session_factory() as session:
        ticket_insert = session.query(Event).filter(Event.id == event_id).first()
        if not ticket_insert:
            print('Событие не найдено')
            return
        seat = session.query(Places).filter(Places.id == seat_id).first()
        if not seat:
            print("Место не найдено")
            return
        if seat_id is not None:
            return(f"Место уже загято")

        ticket = Ticket(price=price, event_id=event_id)
        session.add(ticket)
        session.commit()

        seat.event_id = event_id
        session.commit()

        print("Билет успешно забронирован")


def cancel_booking(ticket_id):
    with session_factory() as session:
        ticket = session.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not ticket:
            print("Билет не найден")
            return



        seat = session.query(Places).filter(Places.event_id == ticket.event_id).first()
        seat.event_id = None
        session.commit()

        session.delete(ticket)
        session.commit()

        print("Бронирование успешно отменено")
