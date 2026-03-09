from escalation import should_escalate


class DummyContext:

    def __init__(self):
        self.crm = {"vip": False}
        self.billing = {"status": "paid"}
        self.tickets = {"complaints": []}
        self.data_complete = True


def test_low_confidence():
    """AI confidence below threshold should escalate."""
    ctx = DummyContext()
    assert should_escalate(ctx,0.5,0,"billing")[0] == True


def test_angry_customer():
    """Highly negative sentiment should escalate."""
    ctx = DummyContext()
    assert should_escalate(ctx,0.9,-0.8,"billing")[0] == True


def test_service_cancellation():
    """Cancellation intent must always escalate."""
    ctx = DummyContext()
    assert should_escalate(ctx,0.9,0,"service_cancellation")[0] == True


def test_repeat_complaint():
    """Repeated complaint should escalate."""
    ctx = DummyContext()
    ctx.tickets={"complaints":["billing","billing","billing"]}
    assert should_escalate(ctx,0.9,0,"billing")[0] == True


def test_vip_overdue():
    """VIP customer with overdue billing escalates."""
    ctx = DummyContext()
    ctx.crm={"vip":True}
    ctx.billing={"status":"overdue"}
    assert should_escalate(ctx,0.9,0,"billing")[0] == True


def test_incomplete_data():
    """Incomplete context + low confidence escalates."""
    ctx = DummyContext()
    ctx.data_complete=False
    assert should_escalate(ctx,0.7,0,"billing")[0] == True


def test_ai_handles_normal():
    """Normal case handled by AI."""
    ctx = DummyContext()
    assert should_escalate(ctx,0.9,0,"billing")[0] == False


def test_edge_case_high_confidence():
    """Edge case: high confidence, neutral sentiment."""
    ctx = DummyContext()
    assert should_escalate(ctx,0.95,0.1,"billing")[0] == False