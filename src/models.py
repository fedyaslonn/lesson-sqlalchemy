from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

metadata_obj = MetaData()
Base = declarative_base(metadata=metadata_obj)


class Event(Base):
    __tablename__ = "Event"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Time)


class Places(Base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    seat_number = Column(Integer)
    event_id = Column(Integer, ForeignKey('Event.id'))
    ticket_id = Column(Integer, ForeignKey('Ticket.id'))

class Ticket(Base):
    __tablename__ = "Ticket"
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    event_name = Column(String, ForeignKey('Event.name'))
    place = relationship('Places', backref=backref('ticket', uselist=False))