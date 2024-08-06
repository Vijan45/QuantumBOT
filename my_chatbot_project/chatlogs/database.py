import databases
import sqlalchemy

database = databases.Database("sqlite:///./chatbot.db")
metadata = sqlalchemy.MetaData()

chat_logs = sqlalchemy.Table(
    "chat_logs",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_message", sqlalchemy.String),
    sqlalchemy.Column("bot_reply", sqlalchemy.String),
)

