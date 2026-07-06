import ChatBubble from "../chatBubble/chatBubble";
import "./convo.scss";

export function Convo({ input }: { input: Array<string> }) {
  const chatItems = input.map((message, index) => (
    <li key={`${message} - ${index}`}>
      <ChatBubble text={message} className="isme"></ChatBubble>
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
