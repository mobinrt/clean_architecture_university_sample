from abc import ABC, abstractmethod

class ConvertEntity(ABC):
    
    @staticmethod
    @abstractmethod
    def to_entity(model_instance):
        raise NotImplementedError()
    
    @staticmethod
    @abstractmethod
    def to_dict(model_instance):
        raise NotImplementedError()
    
    @staticmethod
    @abstractmethod
    def to_read_model(model_instance):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def from_entity(entity):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def updated_model(update_entity, current_entity) :
        raise NotImplementedError()