# Architecture - AIO Chess Training Assistant

## Flow

```text
User Question
   ↓
RAG Engine
   ↓
Local Chess Knowledge Base
   ↓
Relevant Chess Context
   ↓
Coach Prompt
   ↓
LLM / Demo Response Generator
   ↓
Structured Chess Coaching Answer
```

## Components

### 1. Knowledge Base
Stores chess notes, PGNs, opening ideas, endgame explanations, and tournament checklists.

### 2. Retriever
Searches the local files and finds the most relevant content.

### 3. Coach Agent
Combines the user question with retrieved context and produces a coaching answer.

### 4. Future LLM Integration
The demo currently works without an external API. For production, the generated prompt can be sent to OpenAI or Claude.

## Why RAG?

RAG is useful because chess coaching answers should be grounded in specific notes, player games, and tournament preparation material instead of generic advice.
