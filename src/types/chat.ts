export type Sender = "user" | "assistant";

export type ChatMessage = {
  id: string;
  text: string;
  sender: Sender;
  createdAt: string;
};
