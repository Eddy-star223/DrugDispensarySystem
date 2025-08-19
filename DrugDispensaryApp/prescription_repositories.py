class PrescriptionRepository:
    def __init__(self):
        self.db = {}

    def save(self, prescription):
        self.db[prescription.code] = prescription

    def find_by_code(self, code):
        return self.db.get(code)

    def find_by_name(self, name):
        return self.db.get(name)
