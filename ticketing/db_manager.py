from airflow.utils.db_manager import BaseDBManager
from ticketing.models import Base
from pathlib import Path

PACKAGE_DIR = Path(__file__).parent

_REVISION_HEADS_MAP: dict[str, str] = {
    "0.1.0": "d759c6d30f5a",
}


class DRTDBManager(BaseDBManager):
    """Database manager for DagRunTicket model."""

    metadata = Base.metadata
    version_table_name = "alembic_version_drt"
    migration_dir = (PACKAGE_DIR / "migrations").as_posix()
    alembic_file = (PACKAGE_DIR / "alembic.ini").as_posix()
    supports_table_dropping = True
    revision_heads_map = _REVISION_HEADS_MAP

    def downgrade(self, to_revision, from_revision=None, show_sql_only=False):
        """Downgrade the database to a specific version."""
        # alembic adds significant import time, so we import it lazily
        from alembic import command

        self.log.info(
            "Attempting downgrade of DagRunTicket migration to revision %s", to_revision
        )
        config = self.get_alembic_config()
        # show_sql_only not supported here but could be added if needed
        self.log.info("Applying DagRunTicket downgrade migrations.")
        command.downgrade(config, revision=to_revision, sql=show_sql_only)
