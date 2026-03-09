def should_escalate(context, confidence_score, sentiment_score, intent):

    if confidence_score < 0.65:
        return True, "low_confidence"

    if sentiment_score < -0.6:
        return True, "angry_customer"

    if intent == "service_cancellation":
        return True, "service_cancellation"

    if context.tickets and context.tickets["complaints"].count(intent) >= 3:
        return True, "repeat_complaint"

    if context.crm.get("vip") and context.billing and context.billing.get("status") == "overdue":
        return True, "vip_overdue"

    if not context.data_complete and confidence_score < 0.80:
        return True, "incomplete_data"

    return False, "ai_can_handle"