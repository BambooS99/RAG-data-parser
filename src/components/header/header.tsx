import React from "react";
import "./header.scss";

export default function Header({ className }: { className: string }) {
  return (
    <div className="container">
      <div className={className}>Welcome!</div>
    </div>
  );
}
