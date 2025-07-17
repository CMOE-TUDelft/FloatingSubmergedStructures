import React, { useState, useRef, useEffect } from "react";

export default function Chatbot() {
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hi! Ask me anything." },
  ]);
  const [input, setInput] = useState("");
  const bottomRef = useRef(null);

  // Scroll to bottom when messages update
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // Handle sending message
  const sendMessage = () => {
    if (!input.trim()) return;
    // Add user message
    setMessages((msgs) => [...msgs, { from: "user", text: input.trim() }]);
    setInput("");

    fetch("http://127.0.0.1:8000/mybot_app/api/query/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: input.trim() }),
    })
      .then((res) => res.json())
      .then((data) => {
        setMessages((msgs) => [...msgs, { from: "bot", text: data.answer }]);
      })
      .catch(() => {
        setMessages((msgs) => [...msgs, { from: "bot", text: "Error fetching answer." }]);
      });
  };

  // Send message on Enter key
  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.chatWindow}>
        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              ...styles.message,
              alignSelf: msg.from === "user" ? "flex-end" : "flex-start",
              backgroundColor: msg.from === "user" ? "#007bff" : "#e5e5ea",
              color: msg.from === "user" ? "white" : "black",
            }}
          >
            {msg.text}
          </div>
        ))}
        <div ref={bottomRef} />
      </div>
      <div style={styles.inputArea}>
        <textarea
          rows={1}
          style={styles.textarea}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
        />
        <button style={styles.sendButton} onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    width: "100%",
    maxWidth: 600,
    height: "90vh",
    margin: "20px auto",
    display: "flex",
    flexDirection: "column",
    border: "1px solid #ccc",
    borderRadius: 8,
    fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
  },
  chatWindow: {
    flex: 1,
    padding: 16,
    overflowY: "auto",
    display: "flex",
    flexDirection: "column",
    gap: 12,
    backgroundColor: "#f6f6f8",
  },
  message: {
    maxWidth: "75%",
    padding: "10px 14px",
    borderRadius: 20,
    fontSize: 16,
    lineHeight: 1.4,
  },
  inputArea: {
    display: "flex",
    padding: 12,
    borderTop: "1px solid #ccc",
    backgroundColor: "white",
  },
  textarea: {
    flex: 1,
    resize: "none",
    padding: 10,
    fontSize: 16,
    borderRadius: 20,
    border: "1px solid #ccc",
    outline: "none",
    fontFamily: "inherit",
  },
  sendButton: {
    marginLeft: 12,
    backgroundColor: "#007bff",
    border: "none",
    borderRadius: 20,
    color: "white",
    padding: "10px 18px",
    fontSize: 16,
    cursor: "pointer",
  },
};
