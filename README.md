# NexusAI Intern Challenge

This repository contains my implementation of the **NexusAI AI Engineering Internship Challenge**.

The project demonstrates skills in:
- Async Python programming
- AI API integration
- PostgreSQL database design
- Concurrent data fetching
- Decision engine logic
- Automated testing with pytest

The implementation follows the structure requested in the assignment.

---

# Repository Structure

nexusai-intern-challenge/

task1/  
- AI Message Handler implementation

task2/  
- PostgreSQL schema and database access layer

task3/  
- Async parallel data fetching system

task4/  
- Escalation decision engine and pytest tests

ANSWERS.md  
- Written answers for system design questions

requirements.txt  
- Python dependencies

README.md  
- Project documentation

---

# Task 1 — AI Message Handler

This task implements an async function that processes customer messages and returns a structured AI response.

### Function

handle_message(customer_message, customer_id, channel)

### Output

Returns a `MessageResponse` dataclass containing:

- response_text
- confidence
- suggested_action
- channel_formatted_response
- error

### Features

- Async API call handling
- System prompt designed for telecom support
- Error handling for:
  - Empty input
  - API timeout
  - API rate limiting

Voice responses are restricted to short responses while chat responses may contain longer troubleshooting instructions.

---

# Task 2 — Database Schema

A PostgreSQL table `call_records` is designed to store every customer interaction.

### Columns

- customer_phone
- channel
- transcript
- ai_response
- outcome
- confidence_score
- csat_score
- timestamp
- duration

### Constraints

- Confidence score must be between **0 and 1**
- CSAT score must be between **1 and 5**

### Indexes

Indexes were added to improve query performance:

1. customer_phone index  
   → speeds up customer history lookups

2. timestamp index  
   → speeds up recent interaction queries

3. outcome index  
   → improves analytics queries

A Python repository class is implemented to:

- Save new call records
- Retrieve recent call history

Parameterized queries are used to prevent SQL injection.

---

# Task 3 — Parallel Data Fetcher

When a customer calls, the system must fetch data from multiple services simultaneously.

Mock services simulate real systems:

- CRM system
- Billing system
- Ticket history service

Each service includes simulated network latency.

Two approaches are implemented:

### Sequential Fetch

Requests are executed one after another.

Total execution time ≈ sum of all requests.

### Parallel Fetch

Requests run concurrently using:

asyncio.gather()

Total execution time ≈ slowest request.

The parallel approach demonstrates significant performance improvement.

A `CustomerContext` dataclass merges all results and includes:

- CRM data
- Billing data
- Ticket history
- data_complete flag
- fetch_time_ms

The billing service includes a **10% simulated timeout error**, which is handled gracefully.

---

# Task 4 — Escalation Decision Engine

This module determines whether a customer issue should be handled by the AI or escalated to a human agent.

### Function

should_escalate(context, confidence_score, sentiment_score, intent)

### Returns

(bool, reason)

### Escalation Rules

1. Confidence < 0.65 → escalate
2. Sentiment < -0.6 → escalate
3. Same complaint repeated 3+ times → escalate
4. Intent = service_cancellation → always escalate
5. VIP customer + overdue billing → escalate
6. Missing data and confidence < 0.80 → escalate

Unit tests are implemented using pytest.

Run tests using:

pytest task4 -v

---

# Task 5 — Design Questions

Detailed answers for system design questions are provided in:

ANSWERS.md

Topics covered include:

- Streaming speech transcript handling
- Knowledge base quality risks
- Escalation flow for angry customers
- System improvement proposal

---

# Requirements

Install dependencies:

pip install -r requirements.txt

Dependencies include:

- openai
- asyncpg
- pytest
- python-dotenv

---

# Author

Durga Dhanush
