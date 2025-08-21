"""Test async_notify and async_notify_on_failure for import and basic invocation."""
import asyncio
from gcp_notifier import async_notify, async_notify_on_failure

def test_async_notify_runs():
    async def runner():
        # This should not raise, even if secrets are missing (should print error)
        await async_notify(subject="Test", body="Async test", channels=["email", "gchat"])
    asyncio.run(runner())

def test_async_notify_on_failure_runs():
    class DummyRetryState:
        def __init__(self):
            self.fn = lambda: None
            self.outcome = type("Outcome", (), {"exception": lambda self: Exception("fail")})()
    async def runner():
        await async_notify_on_failure(DummyRetryState())
    asyncio.run(runner())
