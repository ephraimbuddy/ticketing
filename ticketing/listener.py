"""Airflow listeners for the External Tickets plugin."""

from __future__ import annotations

from airflow.listeners import hookimpl
from airflow.models import DagRun
from airflow.settings import Session
from ticketing.services import TicketService


@hookimpl
def on_dag_run_failed(dag_run: DagRun, msg: str) -> None:
    """Listener that triggers when a DagRun fails."""
    session = Session()  # you don't want to commit here
    service = TicketService(session=session)
    service.auto_create_for_failure(dag_run)
