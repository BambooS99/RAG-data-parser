type Sender = "user" | "assistant";

type ChatMessage = {
  id: string;
  text: string;
  sender: Sender;
  CreatedAt: String;
};
