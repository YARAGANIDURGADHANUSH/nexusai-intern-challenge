def should_escalate(context, confidence_score, sentiment_score, intent):

    if confidence_score < 0.65:
        return True,"low_confidence"

    if sentiment_score < -0.6:
        return True,"angry_customer"

    if intent == "service_cancellation":
        return True,"service_cancellation"

    return False,"ai_can_handle"
