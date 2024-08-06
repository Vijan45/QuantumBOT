document.getElementById("send-button").addEventListener("click", function () {
    const userMessage = document.getElementById("user-message").value;
    // Make a POST request to the chatbot backend
    fetch("/chatbot/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_message: userMessage }),
    })
        .then(response => response.json())
        .then(data => {
            const chatHistory = document.getElementById("chat-history");
            const userMessageElement = document.createElement("div");
            userMessageElement.className = "user-message";
            userMessageElement.innerHTML = `<span class="message-icon">You:</span> ${userMessage}`;
            chatHistory.appendChild(userMessageElement);

            const botMessageElement = document.createElement("div");
            botMessageElement.className = "bot-message";
            botMessageElement.innerHTML = `<span class="message-icon">Bot:</span> ${data.bot_reply}`;
            chatHistory.appendChild(botMessageElement);

            // Clear the input field
            document.getElementById("user-message").value = "";

            // Scroll to the bottom of the chat history
            chatHistory.scrollTop = chatHistory.scrollHeight;
        });
});
