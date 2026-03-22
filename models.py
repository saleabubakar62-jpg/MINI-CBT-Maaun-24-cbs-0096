class Business:
    def __init__(self, name, category, location):
        self.name = name
        self.category = category
        self.location = location

    def get_info(self):
        return f"{self.name} - {self.category} ({self.location})"