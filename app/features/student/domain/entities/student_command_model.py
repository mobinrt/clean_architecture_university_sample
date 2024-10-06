from app.core.enum.major import Major

class CreateStudentCommand:
    def __init__(self, id: int, name: str, password: str, major: Major):
        self.id = id
        self.name = name
        self.password = password
        self.major = major

class UpdateStudentCommand:
    def __init__(self, name: str | None = None, password: str | None = None):
        self.name = name
        self.password = password
        
class DeleteStudentCommand:
    def __init__(self, id: int):
        self.id = id
