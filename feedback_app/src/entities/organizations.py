class Organization:
    def __init__(self, org_id: int, name: str):
        self.org_id = org_id
        self.name = name


ORGANIZATIONS = [Organization(1, "Apple"), Organization(
    2, "Power"), Organization(3, "Zara"), Organization(4, "Prisma")]
