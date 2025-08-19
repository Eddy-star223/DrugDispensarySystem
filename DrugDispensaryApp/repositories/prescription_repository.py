class PrescriptionRepository:
    def __init__(self):
        self.db = {}

    def save(self, prescription):
        self.db[prescription.code] = prescription

    def find_by_code(self, code):
        return self.db.get(code)