
class CreateClassroomCommand:
    def __init__(self, id: int, number: int):
        self.id = id
        self.number = number
        
class UpdateClassroomCommand:
    def __init__(self, number: int):
        self.number =number
        
class DeleteClassroomCommand:
    def __init__(self, id: int):
        self.id = id
