import ChatBubble from "../chatBubble/chatBubble";
import "./convo.scss";

export function Convo({ input }: { input: Array<string> }) {
  const text = input;

  return (
    <>
      <div className="conversation-box">
        <ChatBubble text={text} />
      </div>
    </>
  );
}
