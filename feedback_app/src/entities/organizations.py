class Organization:
    """Class representing an organization that recieves feedback."""
    def __init__(self, org_id: int, name: str):
        """Constructor for creating an organization.

        Args:
            org_id (int): Unique identifier for the organization.
            name (str): Name of the organization.
        """
        self.org_id = org_id
        self.name = name
