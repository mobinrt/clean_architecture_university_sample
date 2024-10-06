from abc import ABC, abstractmethod

class ConvertEntity(ABC):
    
    @staticmethod
    @abstractmethod
    def to_entity(model_instance):
        pass
    
    @staticmethod
    @abstractmethod
    def to_dict(model_instance):
        pass
    
    @staticmethod
    @abstractmethod
    def to_read_model(model_instance):
        pass

    @staticmethod
    @abstractmethod
    def from_entity(entity):
        pass
