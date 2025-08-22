from DrugDispensaryApp.services.login_service import register_user

class PrescriptionController:
    def __init__(self):
        self.service = register_user()

    def create_prescription(self, request):
        return self.service.create_prescription(request)

    def get_prescription(self, code):
        return self.service.get_prescription_by_code(code)