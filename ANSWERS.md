# NexusAI Challenge Answers

## Q1
Partial transcripts can reduce latency but may cause unnecessary queries if the intent changes mid sentence. A hybrid approach is best where lightweight intent detection runs early but heavier database queries wait until the final transcript.

## Q2
One issue is incorrect solutions entering the knowledge base if CSAT scores are misleading. Another problem is outdated solutions remaining after system updates. This can be prevented using review processes and periodic validation.

## Q3
The AI detects strong negative sentiment and cancellation intent. It apologizes for the issue and immediately escalates to a human agent while passing the transcript and context.

## Q4
A useful improvement would be adding vector search to retrieve similar previous support cases so the AI can suggest better solutions.
