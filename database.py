from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = 'postgresql://manith:7crFlAONKonjFvCAhnWTySsdnfIM2yYY@dpg-cs9kgdo8fa8c73cbn0t0-a.oregon-postgres.render.com/fluttermusicapp'
DATABASE_URL = 'postgresql://postgres:root@localhost/fluttermusicapp'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()