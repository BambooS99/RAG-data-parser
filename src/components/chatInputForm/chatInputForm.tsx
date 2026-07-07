import React, { useState } from "react";
import "./chatInputForm.scss";

export default function ChatInputForm({
  submittedValue,
  setSubmittedValue,
}: {
  submittedValue: Array<string>;
  setSubmittedValue: React.Dispatch<React.SetStateAction<Array<string>>>;
}) {
  const [input, setInput] = useState("");

  function handleButtonClick(input: string) {
    const message = input.trim();
    if (message.length > 0) {
      const nextValue = [...submittedValue, message];
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
