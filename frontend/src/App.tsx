import React, { useState } from "react";
import { createItem } from "./api/index";

export function App() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState(0);
  const [created, setCreated] = useState<string | null>(null);

  const onSubmit = async () => {
    const result = await createItem({ id: Math.floor(Math.random() * 1_000_000), name, price, tags: [] });
    setCreated(`Created item ${result.id}: ${result.name}`);
  };

  return (
    <div style={{ padding: 20, backgroundColor: "#f0f0f0" }}>
      <h1>Create an Item</h1>
      <input
        placeholder="Name"
        value={name}
        onChange={e => setName(e.target.value)}
      />
      <input
        type="number"
        placeholder="Price"
        value={price}
        onChange={e => setPrice(parseFloat(e.target.value))}
      />
      <button onClick={onSubmit}>Create</button>
      {created && <p>{created}</p>}
    </div>
  );
}
