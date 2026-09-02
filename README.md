# Codex AI

## Overview

Codex AI processes structured conversation transcripts and turns them into
useful follow-up actions. The first prototype focuses on transcripts and
documents such as PDF, Word, and Excel files.

## Roadmap

1. Accept a structured transcript as input.
2. Generate a conversation summary.
3. Analyze call productivity and participant tone.
4. Extract action items from the conversation.
5. Model participants as nodes in a graph.
6. Prioritize tasks with a max-heap.
7. Email each participant their prioritized tasks.

## Flow Diagram

```mermaid
flowchart TD
	A[Structured transcript] --> B[Transcript processing]
	B --> C[Conversation summary]
	B --> D[Productivity analysis]
	B --> E[Participant tone and emotion tracking]
	C --> F[Action-item extraction]
	D --> F
	E --> F
	F --> G[Participant graph]
	G --> H[Task prioritization with max-heap (priority queue)]
	H --> I[Email tasks to participants]
```

## Prototype Status

The prototype is complete.
