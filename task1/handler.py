
async def handle_message(customer_message, customer_id, channel):

    if not customer_message.strip():
        return {
            "response_text":"",
            "confidence":0,
            "suggested_action":"none",
            "channel_formatted_response":"",
            "error":"empty_input"
        }

    response="Please restart your router."

    if channel=="chat":
        response="Please restart your router and check your internet connection."

    return {
        "response_text":response,
        "confidence":0.8,
        "suggested_action":"troubleshoot",
        "channel_formatted_response":response,
        "error":None
  }
