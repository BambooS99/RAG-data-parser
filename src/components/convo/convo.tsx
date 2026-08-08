import type { ChatMessage } from "../../types/chat";
import ChatBubble from "../chatBubble/chatBubble";
import "./convo.scss";

export function Convo({ input }: { input: ChatMessage[] }) {
  const chatItems = input.map((message) => (
    <li key={message.id}>
      <ChatBubble message={message}></ChatBubble>
    </li>
  ));
  return (
    <>
      <div className="conversation-box">
        <ul className="chat-list">{chatItems}</ul>
      </div>
    </>
  );
}
