import "./sidePanel.scss";

export default function SidePanel({ side }: { side: "left" | "right" }) {
  return <aside className={`side-panel side-panel--${side}`} />;
}
