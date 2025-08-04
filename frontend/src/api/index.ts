import type { paths } from "./openapi-types";
import { api } from "./api";

// Derive types for request and response bodies
type CreateItemReq  = paths["/items/"]["post"]["requestBody"]["content"]["application/json"];
type CreateItemResp = paths["/items/"]["post"]["responses"]["200"]["content"]["application/json"];

export async function createItem(payload: CreateItemReq): Promise<CreateItemResp> {
  console.log("Creating item with payload:", payload);
  const { data } = await api.post<CreateItemResp>("/items/", payload);
  return data;
}
