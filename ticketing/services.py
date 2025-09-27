"""Domain logic for managing DagRun ticket records."""

from __future__ import annotations

from typing import Optional

from sqlalchemy.orm import Session

from ticketing.models import DagRunTicket


class TicketService:
    """Encapsulate ticket persistence and integration logic."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def auto_create_for_failure(self, dag_run) -> Optional[DagRunTicket]:

        # title = f"DagRun failed: {dag_run.dag_id}/{dag_run.run_id}"
        # body = f"DagRun {dag_run.run_id} for {dag_run.dag_id} failed."
        # In a real implementation, you'd create the ticket in github or any other system
        # here and return metadata. For this example, we'll just simulate it.
        metadata = {"key": "5454", "url": "https://example.com/tickets/5454"}

        ticket = DagRunTicket(
            dag_id=dag_run.dag_id,
            run_id=dag_run.run_id,
            system="GITHUB",  # github, jira, etc
            key=metadata.get("key", ""),
            status="OPEN",
            url=metadata.get("url"),
        )
        self._session.add(ticket)
        return ticket
