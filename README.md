# NexusAI Intern Challenge

## Overview

This repository contains my implementation of the **NexusAI Intern Challenge**, which simulates a backend system for an **AI-powered telecom customer support assistant**.

The system processes customer messages, retrieves relevant service data, analyzes interactions, and determines whether the issue should be handled automatically by AI or escalated to a human agent.

The project demonstrates key backend engineering concepts including:

* Asynchronous AI request handling
* PostgreSQL database schema design
* Analytics queries
* Parallel API data fetching
* Escalation decision logic
* Automated unit testing

---

# System Architecture

The system follows a modular architecture where customer messages flow through multiple components.

Customer Message
→ AI Message Handler (Task 1)
→ Intent + Sentiment Detection
→ Escalation Decision Engine (Task 4)

If the AI can resolve the issue:

AI Response → Customer

If escalation is required:

Context + Transcript → Human Support Agent

Supporting services are fetched in parallel:

* CRM Service
* Billing Service
* Ticket History Service

These services are retrieved using **async parallel fetching** (Task 3).

All interactions are stored in a PostgreSQL database for analytics and reporting (Task 2).

---

# Project Structure

```
nexusai-intern-challenge
│
├── task1
│   ├── handler.py
│   └── models.py
│
├── task2
│   ├── analytics.py
│   ├── repository.py
│   └── schema.sql
│
├── task3
│   └── fetcher.py
│
├── task4
│   ├── escalation.py
│   └── test_escalation.py
│
├── ANSWERS.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Task 1 – AI Message Handler

The system includes an asynchronous function:

```
handle_message(customer_message, customer_id, channel)
```

The handler processes a customer support message using an AI model and returns a structured response.

Key features:

* OpenAI API integration
* Async request handling
* Dataclass response model
* Input validation
* Timeout handling
* Rate-limit retry handling
* Channel-specific response formatting

Voice responses are kept shorter for clarity, while chat responses can provide slightly more detailed instructions.

The response format:

```
MessageResponse(
    response_text,
    confidence,
    suggested_action,
    channel_formatted_response,
    error
)
```

---

# Task 2 – Database Schema & Analytics

A PostgreSQL table `call_records` stores support interaction data.

Stored fields include:

* Customer phone number
* Communication channel
* Transcript
* AI response
* Call outcome
* Confidence score
* CSAT score
* Timestamp
* Call duration

Indexes were created to optimize common queries:

* Customer history lookup
* Recent call retrieval
* Analytics queries grouped by outcome

Repository functions:

```
save(call_data)
get_recent(phone, limit=5)
```

Analytics query:

Returns the **top 5 intents with the lowest resolution rate in the last 7 days** along with their average CSAT score.

This helps identify problem areas in the support system.

---

# Task 3 – Parallel Data Fetching

When a customer contacts support, the system retrieves data from multiple services:

* CRM system
* Billing service
* Ticket history service

Two approaches are demonstrated.

### Sequential Fetch

Requests are executed one after another.

CRM → Billing → Tickets

Total latency equals the sum of all request times.

### Parallel Fetch

Using:

```
asyncio.gather()
```

All services are executed simultaneously.

Total latency becomes roughly the duration of the slowest request instead of the sum.

Example timing:

Sequential: ~700–900 ms
Parallel: ~300–400 ms

This demonstrates the performance benefit of asynchronous concurrency in backend systems.

The billing service also simulates a **10% timeout scenario**, where the system gracefully handles failures instead of crashing.

---

# Task 4 – Escalation Decision Engine

The escalation engine determines whether the AI can resolve a case or if it should be escalated to a human support agent.

Function:

```
should_escalate(context, confidence_score, sentiment_score, intent)
```

Escalation rules include:

* AI confidence < 0.65
* Sentiment score < -0.6
* Repeated complaints (3+ times)
* Service cancellation intent
* VIP customer with overdue billing
* Missing system data combined with low confidence

The function returns:

```
(True, "reason")
```

or

```
(False, "ai_can_handle")
```

Example:

```
(True, "angry_customer")
```

Unit tests were implemented using **pytest** to validate escalation rules and edge cases.

---

# Example AI Interaction

Customer message:

```
"My internet has been down for 2 days and I already called support."
```

Channel:

```
chat
```

AI Response:

```
{
  "response_text": "I'm sorry you're experiencing connectivity issues. Please restart your router and check your connection. If the problem continues, I can escalate this to a technician.",
  "confidence": 0.82,
  "suggested_action": "troubleshoot",
  "channel_formatted_response": "Please restart your router and check your internet connection.",
  "error": null
}
```

---

# Running Tests

To run escalation logic tests:

```
pytest task4 -v
```

Example output:

```
test_low_confidence ........ PASSED
test_angry_customer ........ PASSED
test_cancellation .......... PASSED
```

---

# Technologies Used

Python
Asyncio
PostgreSQL
asyncpg
pytest
OpenAI API

---

# Future Improvements

Potential improvements include:

* Vector search for similar historical support cases
* Improved intent classification models
* Knowledge base learning with human review
* Real-time monitoring dashboards
* Automated ticket creation workflows

These enhancements could further reduce escalation rates and improve AI response accuracy.

---

# Author

Durga Dhanush Yaragani
AI / ML Engineer (Learning Path)