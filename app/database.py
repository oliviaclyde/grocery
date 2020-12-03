from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 


def choose_engine(mode='live'):
    if mode == 'test':
        engine = create_engine('sqlite:///mock_items.db', connect_args={'check_same_thread': False}, echo=True)
    elif mode == 'live':
        engine = create_engine('sqlite:///items.db', connect_args={'check_same_thread': False}, echo=True)

    return engine


def SessionLocal(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)()
