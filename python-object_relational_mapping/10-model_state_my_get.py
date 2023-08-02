#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    # Create an instance of SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                            3306/{}'.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]))

    # Create a session to interact with the database
    session = Session(engine)
    # Query all State objects
    states = session.query(State).filter(State.name == sys.argv[4]).first()

    if states is None:
        print("Not found")
    else:
        print(states.id)
