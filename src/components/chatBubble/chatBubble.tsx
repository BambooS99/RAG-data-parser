import type { ChatMessage } from "../../types/chat";
import "./chatBubble.scss";

export default function ChatBubble({ message }: { message: ChatMessage }) {
  const isMe = message.sender === "user";

  return (
    <>
      <div className={`chat-bubble ${isMe ? "me" : "them"}`}>
        {message.text}
      </div>
    </>
  );
}
