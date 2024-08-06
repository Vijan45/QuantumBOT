from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

# Define your SQLite database URL (update it if needed)
DATABASE_URL = "sqlite:///./chatbot.db"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define the metadata object
metadata = MetaData()

# Define the chat_logs table
chat_logs = Table(
    "chat_logs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_message", String),
    Column("bot_reply", String),
)

# Create the table in the database
metadata.create_all(engine)

print("Table 'chat_logs' created successfully.")
