# NexusAI Intern Challenge

## Overview

This repository contains my implementation of the **NexusAI Intern Challenge**, which simulates a backend system for an AI-powered telecom support assistant.

The project demonstrates core backend and AI system concepts including:

* asynchronous AI message handling
* database schema design and analytics
* parallel service fetching
* escalation decision logic
* automated testing

The goal is to design a system that can automatically assist customers while safely escalating complex cases to human agents.

---

# Project Structure

```id="3xp1p2"
nexusai-intern-challenge
│
├── task1
│   ├── handler.py
│   └── models.py
│
├── task2
│   ├── repository.py
│   ├── analytics.py
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
└── requirements.txt
```

---

# Task 1 – AI Message Handler

The system includes an asynchronous function:

```
handle_message(customer_message, customer_id, channel)
```

It processes customer messages and returns a structured response using a `MessageResponse` dataclass.

Key features:

* OpenAI API integration
* telecom-specific system prompt
* timeout handling (10 seconds)
* rate limit retry handling
* empty input validation
* channel-specific formatting

Voice responses are restricted to short replies, while chat responses may be slightly longer.

---

# Task 2 – Database Schema

A PostgreSQL table `call_records` stores every support interaction.

Stored data includes:

* customer phone
* communication channel
* transcript
* AI response
* call outcome
* confidence score
* CSAT score
* timestamp
* call duration

Indexes were added to optimize:

1. **Customer history lookups**
2. **Recent interaction queries**
3. **Analytics queries grouped by outcome**

A repository class provides asynchronous methods:

```
save(call_data)
get_recent(phone, limit=5)
```

An analytics query returns the **top 5 intent types with the lowest resolution rate in the last 7 days** along with their average CSAT.

---

# Task 3 – Parallel Data Fetching

When a customer contacts support, the system must fetch data from multiple services:

* CRM system
* Billing service
* Ticket history service

Each service has simulated latency.

Two approaches were implemented:

### Sequential fetch

Requests are executed one after another.

```
CRM → Billing → Tickets
```

Total time ≈ sum of all delays.

### Parallel fetch

Using:

```
asyncio.gather()
```

All services are fetched concurrently.

Total time ≈ slowest request instead of sum.

Example timing:

```
Sequential: ~700–900 ms
Parallel:   ~300–400 ms
```

This demonstrates a **2x+ performance improvement**, which is important for real-time customer support systems.

The system also includes a **10% simulated timeout for the billing service**. If this occurs, the system continues running and marks the data as incomplete instead of crashing.

---

# Task 4 – Escalation Decision Engine

The escalation engine decides whether a case should be handled by AI or escalated to a human agent.

Function:

```
should_escalate(context, confidence_score, sentiment_score, intent)
```

It evaluates six rules:

1. AI confidence < 0.65
2. Sentiment score < -0.6
3. Same complaint appears 3+ times
4. Intent = service cancellation
5. VIP customer with overdue billing
6. Missing system data with low confidence

The function returns:

```
(bool, reason)
```

Example:

```
(True, "angry_customer")
```

Unit tests were written using **pytest** to validate all rules and edge cases.

---

# Rule Conflict Handling

If multiple escalation rules trigger simultaneously, the system prioritizes **customer safety and business risk**.

For example:

* confidence = 0.90
* intent = service_cancellation

Even though the confidence is high, the cancellation intent rule takes priority because losing a customer is a high-impact event.

In general, **explicit business-critical intents override AI confidence scores**, ensuring sensitive situations are handled by human agents.

---

# Running Tests

Tests can be executed using:

```id="gx7g1h"
pytest task4 -v
```

All escalation logic tests should pass without additional setup.

---

# Technologies Used

* Python
* Asyncio
* PostgreSQL
* asyncpg
* pytest
* OpenAI API

---

# Future Improvements

Potential enhancements include:

* vector search over historical support cases
* improved intent classification
* real-time monitoring dashboards
* knowledge base auto-learning with human validation

These improvements would help the AI system provide more accurate responses and reduce escalation rates.

---

# Author

Durga Dhanush Yaragani
AI / ML Engineer (Learning Path)