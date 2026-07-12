import React, { useState } from "react";
import Header from "./components/header/header";
import "./App.css";
import { Convo } from "./components/convo/convo";
import ChatInputForm from "./components/chatInputForm/chatInputForm";
import type { ChatMessage } from "./types/chat";

export default function App() {
  const [submittedValue, setSubmittedValue] = useState<ChatMessage[]>([]);

  return (
    <>
      <Header className="welcome" />
      <Convo input={submittedValue} />
      <ChatInputForm
        submittedValue={submittedValue}
        setSubmittedValue={setSubmittedValue}
      />
    </>
  );
}
