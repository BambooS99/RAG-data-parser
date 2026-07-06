import React from "react";
import "./chatInputForm.scss";

export default function ChatInputForm({
  input,
  setInput,
}: {
  input: string;
  setInput: React.Dispatch<React.SetStateAction<string>>;
}) {
  return (
    <>
      <div className="chatform-container">
        <textarea
          className="chat-form"
          value={input}
          id="input"
          onChange={(e) => setInput(e.target.value)}
        ></textarea>
        <button onClick={() => setInput("")}>send</button>
      </div>
    </>
  );
}
