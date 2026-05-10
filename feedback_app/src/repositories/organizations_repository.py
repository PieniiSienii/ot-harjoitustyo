from entities.organizations import Organization


class OrganizationRepository:
    """Repository class responsible for organization database operations."""

    def __init__(self, connection):
        """Constructor for the organization repository.

        Args:
            connection: SQLite database connection object
        """
        self._connection = connection

    def get_all(self):
        """Fetches all organizations from the database.

        Returns:
            List of Organization objects
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM organizations")

        rows = cursor.fetchall()

        return [Organization(row["id"], row["name"]) for row in rows]
