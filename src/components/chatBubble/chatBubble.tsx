import "./chatBubble.scss";

export default function ChatBubble({ text }: { text: string }) {
  return (
    <>
      <div className={'chat-bubble${isMe ? "me": "them"}'}>{text}</div>
    </>
  );
}
