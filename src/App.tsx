import React, { useState } from "react";
import Header from "./components/header/header";
import "./App.css";
import { Convo } from "./components/convo/convo";
import ChatInputForm from "./components/chatInputForm/chatInputForm";

export default function App() {
  const [input, setInput] = useState("");

  return (
    <>
      <Header className="welcome" />
      <Convo />
      <ChatInputForm input={input} setInput={setInput} />
    </>
  );
}
