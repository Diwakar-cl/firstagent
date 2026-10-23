# firstagent

My first chatbot, written before I understood what an agent was. It matches keywords in
your input and prints a canned reply — no model, no API, no dependencies.

**This repo is a milestone, not a tool.** `coin-agent` is what came after it, and is the
one worth reading.

## Run it

```
python3 firstagent.py
```

## What it does

- Asks how you'd like to be addressed, and remembers it
- Matches `hello`, `name`, `age`, `price`, `history`
- Keeps the conversation in a list of `{"role", "content"}` dicts
- `history` prints the whole transcript back
