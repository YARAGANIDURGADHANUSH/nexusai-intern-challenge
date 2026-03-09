import asyncio
from openai import AsyncOpenAI
from models import MessageResponse

client = AsyncOpenAI()

SYSTEM_PROMPT = """
You are an AI telecom support assistant.

Rules:
- Help customers troubleshoot telecom issues.
- Be polite, calm, and solution-oriented.
- If the channel is voice, keep responses under 2 sentences.
- If the channel is chat or whatsapp, responses may be slightly longer.
- Always suggest a clear troubleshooting step or action.
"""


async def handle_message(customer_message: str, customer_id: str, channel: str) -> MessageResponse:

    # Case 1 — Empty input
    if not customer_message.strip():
        return MessageResponse(
            response_text="",
            confidence=0.0,
            suggested_action="none",
            channel_formatted_response="",
            error="empty_input"
        )

    try:

        # Case 2 — Timeout after 10 seconds
        response = await asyncio.wait_for(
            client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": customer_message}
                ]
            ),
            timeout=10
        )

    except asyncio.TimeoutError:
        return MessageResponse(
            response_text="",
            confidence=0.0,
            suggested_action="retry",
            channel_formatted_response="",
            error="api_timeout"
        )

    except Exception as e:

        # Case 3 — Rate limit retry once after 2 seconds
        if "rate_limit" in str(e).lower():

            await asyncio.sleep(2)

            response = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": customer_message}
                ]
            )

        else:
            return MessageResponse(
                response_text="",
                confidence=0.0,
                suggested_action="error",
                channel_formatted_response="",
                error=str(e)
            )

    ai_text = response.choices[0].message.content.strip()

    # Channel-specific formatting
    if channel == "voice":
        formatted_response = ai_text.split(".")[0] + "."
    else:
        formatted_response = ai_text

    return MessageResponse(
        response_text=ai_text,
        confidence=0.85,
        suggested_action="troubleshoot",
        channel_formatted_response=formatted_response,
        error=None
    )