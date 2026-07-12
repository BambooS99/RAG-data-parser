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

  function handleButtonClick(input: string) {
    const message = input.trim();

    if (message.length > 0) {
      const nextMessage: ChatMessage = {
        id: crypto.randomUUID(), // later we will generate a user ID > store it in state > and then populate that in the chat.
        text: message,
        sender: "user",
        createdAt: new Date().toISOString(),
      };

      const nextValue = [...submittedValue, nextMessage];
      setSubmittedValue(nextValue);
      setInput("");
    }
  }
  return (
    <>
      <div className="chatform-container">
        <textarea
          className="chat-form"
          value={input}
          id="input"
          onChange={(e) => setInput(e.target.value)}
        ></textarea>
        <button onClick={() => handleButtonClick(input)}>send</button>
        {/* we want to make it so that the user input from text gets sent to the AI tool*/}
      </div>
    </>
  );
}
