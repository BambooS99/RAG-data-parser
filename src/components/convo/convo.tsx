import { useEffect, useRef } from "react";
import type { ChatMessage } from "../../types/chat";
import ChatBubble from "../chatBubble/chatBubble";
import "./convo.scss";

export function Convo({ input }: { input: ChatMessage[] }) {
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [input]);

  return (
    <div className="conversation-box" ref={scrollRef}>
      <div className="conversation-box__inner">
        {input.length === 0 ? (
          <div className="conversation-box__empty">
            <div className="conversation-box__empty-title">Ask anything about your data</div>
            <div className="conversation-box__empty-subtitle">
              Your documents have been indexed and are ready to query.
            </div>
          </div>
        ) : (
          <ul className="chat-list">
            {input.map((message) => (
              <li key={message.id}>
                <ChatBubble message={message} />
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
