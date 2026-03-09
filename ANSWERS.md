# NexusAI Intern Challenge – Design Answers

## Q1: Should we query the database using partial transcripts?

Using partial transcripts can significantly reduce system latency because the AI can start processing the request before the user finishes speaking. However, there is a tradeoff. Early transcripts are often incomplete and the user’s intent may change mid-sentence. For example, a customer might initially say “I want to cancel…” but finish with “…my appointment for tomorrow.” Triggering database queries too early could result in unnecessary work or incorrect actions.

A practical approach is a hybrid strategy. The system should perform lightweight tasks on partial transcripts, such as intent classification or sentiment detection, which are fast and inexpensive. These early signals can help prepare the system by prefetching likely data sources or prioritizing certain workflows. However, expensive operations such as database queries, billing lookups, or CRM updates should wait until the final transcript is received or until the intent confidence crosses a threshold.

In this system, partial transcripts could be used to detect potential escalation scenarios (for example, negative sentiment or cancellation intent) while the full transcript is used to trigger definitive actions. This approach balances responsiveness with correctness and avoids unnecessary system load while still delivering fast AI responses.

---

## Q2: Risks of auto-learning from CSAT ≥ 4

Automatically adding solutions to the knowledge base based on CSAT scores can improve system learning, but it introduces several risks over time.

One risk is incorrect solutions being reinforced. A customer may give a high CSAT score simply because the human agent was polite or because the issue resolved later for unrelated reasons. If the system assumes the AI’s response was correct, it may store inaccurate solutions that later mislead the AI. Over several months, this could gradually degrade the quality of responses.

A second risk is outdated information remaining in the knowledge base. Telecom systems frequently change billing policies, network configurations, and troubleshooting procedures. A solution that worked months ago may become invalid after system updates. If outdated answers continue to be reused, the AI could repeatedly give incorrect guidance to customers.

To mitigate these issues, the system should introduce validation mechanisms. Newly learned solutions should be reviewed periodically or flagged when used repeatedly with low CSAT results. Confidence thresholds and versioning of knowledge entries can also help track when solutions become obsolete. Combining automated learning with periodic human oversight ensures the knowledge base remains accurate and reliable.

---

## Q3: Handling an angry cancellation request

When a customer says something like “I’ve been without internet for 4 days, I called 3 times already, your company is useless and I want to cancel right now,” the system should follow a clear escalation workflow.

First, the AI analyzes the transcript using sentiment analysis and intent classification. In this example, the sentiment would likely be strongly negative and the detected intent would be service cancellation. Both of these signals trigger escalation rules in the system’s decision engine.

Second, the AI should respond empathetically to the customer before escalation. The response might acknowledge the frustration and reassure the user that the issue will be handled quickly. For example, the AI could say: “I’m really sorry you’ve experienced repeated outages. Let me connect you with a specialist who can resolve this immediately.”

Finally, the system escalates the conversation to a human support agent. When escalation occurs, the system should pass relevant context to the agent, including the full transcript, detected intent, sentiment score, account status, and recent ticket history. Providing this context allows the agent to understand the situation immediately and avoid asking the customer to repeat information. This improves both response time and customer satisfaction.

---

## Q4: Most important improvement to this system

The most valuable improvement to this system would be adding semantic search using vector embeddings of past support interactions.

Currently, the AI generates responses based only on the immediate conversation. However, many customer issues repeat across thousands of interactions. By embedding transcripts and solutions into vector representations and storing them in a vector database, the system could retrieve similar past cases whenever a new support request arrives.

When the AI receives a new message, the system would generate an embedding for the transcript and search for the most similar previous cases. The retrieved examples could then be used to guide the AI’s response generation or recommend troubleshooting steps that previously worked for similar problems.

To evaluate whether this improvement works, we would track metrics such as resolution rate, CSAT score, and escalation frequency. If the AI consistently resolves issues faster and requires fewer human escalations, it would indicate that the retrieval system is improving the accuracy of responses.

This approach effectively transforms the system into a retrieval-augmented support assistant that learns from historical customer interactions while still allowing the AI to generate flexible responses.
