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
    ticket_id = Column(Integer)

class Places(Base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    seat_num = Column(Integer)
    event_location = Column(Integer, ForeignKey('Event.ticket_id', ondelete="CASCADE"))
    ticket = relationship("Ticket", uselist=False, backref="places")

class Ticket(Base):
    __tablename__ = "Ticket"
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    event_name = Column(String, ForeignKey('Event.name', ondelete="CASCADE"))
    seat_number = Column(Integer, ForeignKey('Places.seat_num', ondelete="CASCADE"))