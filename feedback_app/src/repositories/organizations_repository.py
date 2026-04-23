from entities.organizations import Organization


class OganizationRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM organizations")

        rows = cursor.fetchall()

        return [Organization(row["org_id"], row["name"]) for row in rows]
