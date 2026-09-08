{
  "name": "library_search",
  "description": "Search local BotShelf library snippets",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {"type": "string", "minLength": 1, "maxLength": 200}
    },
    "required": ["query"]
  }
}
