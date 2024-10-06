
class CreateTeacherCommand:
    def __init__(self, id: int, name: str, password: str):
        self.id = id
        self.name = name
        self.password = password
        
class UpdateTeacherCommand:
    def __init__(self, name: str | None = None, password: str | None = None):
        self.name = name
        self.password = password
        
class DeleteTeacherCommand:
    def __init__(self, id: int):
        self.id = id
