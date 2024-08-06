from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from chatlogics import handle_user_message
from chatlogs.database import database, chat_logs

app = FastAPI()

# Serve static files (HTML, CSS, JavaScript, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create a FastAPI route to serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    return FileResponse("static/index.html")

# Create the chatbot route to handle user messages
@app.post("/chatbot/")
async def chat(user_message: dict):
    try:
        user_message_text = user_message["user_message"]
        bot_reply = handle_user_message(user_message_text)

        # Store the conversation in the database
        query = chat_logs.insert().values(user_message=user_message_text, bot_reply=bot_reply)
        await database.execute(query)

        return {"bot_reply": bot_reply}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

