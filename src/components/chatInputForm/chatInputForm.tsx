import React, { useState } from "react";
import "./chatInputForm.scss";
import type { ChatMessage } from "../../types/chat";

export default function ChatInputForm({
  submittedValue,
  setSubmittedValue,
}: {
  submittedValue: ChatMessage[];
  setSubmittedValue: React.Dispatch<React.SetStateAction<ChatMessage[]>>;
}) {
  const [input, setInput] = useState("");

  async function sendPrompt(message: string) {
    const url = "http://127.0.0.1:8000/chat";
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await response.json();
    console.log(data);
  }

  function handleSend() {
    const message = input.trim();
    if (message.length === 0) return;

    const nextMessage: ChatMessage = {
      id: crypto.randomUUID(),
      text: message,
      sender: "user",
      createdAt: new Date().toISOString(),
    };

    setSubmittedValue([...submittedValue, nextMessage]);
    setInput("");
    sendPrompt(message);
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }

  return (
    <div className="chatform-container">
      <div className="chatform-bar">
        <textarea
          className="chatform-bar__input"
          placeholder="Message Math GPT..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          rows={1}
        />
        <button
          className="chatform-bar__send"
          onClick={handleSend}
          disabled={input.trim().length === 0}
          aria-label="Send message"
        >
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.75"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M12 19V5" />
            <path d="M5 12l7-7 7 7" />
          </svg>
        </button>
      </div>
    </div>
  );
}
