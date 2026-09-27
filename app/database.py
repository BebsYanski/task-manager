from sqlmodel import SQLModel, create_engine,Session

database_name = "task.db"
sqlilte_url = f"sqlite:///{database_name}"

connect_args = {"check_same_thread":False}
engine = create_engine(sqlilte_url,echo = True, connect_args = connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session