from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine=create_engine("postgresql://postgres:postgres@localhost:5432/fastapi", 
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)

