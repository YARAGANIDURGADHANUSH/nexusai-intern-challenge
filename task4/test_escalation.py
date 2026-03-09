from escalation import should_escalate


def test_low_confidence():
    result = should_escalate({}, 0.5, 0.1, "general_query")
    assert result == (True, "low_confidence")


def test_angry_customer():
    result = should_escalate({}, 0.9, -0.8, "billing_issue")
    assert result == (True, "angry_customer")


def test_service_cancellation():
    result = should_escalate({}, 0.9, 0.1, "service_cancellation")
    assert result == (True, "service_cancellation")


def test_ai_can_handle():
    result = should_escalate({}, 0.9, 0.2, "general_query")
    assert result == (False, "ai_can_handle")