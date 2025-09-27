"""Airflow plugin definition for External Tickets."""

from __future__ import annotations

from airflow.plugins_manager import AirflowPlugin
from ticketing import listener


class TicketingPlugin(AirflowPlugin):
    name = "dag_run_ticketing"
    listeners = [listener]


__all__ = ["TicketingPlugin"]
