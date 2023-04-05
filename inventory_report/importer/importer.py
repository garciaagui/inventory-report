from abc import ABC, abstractclassmethod


class Importer(ABC):
    @classmethod
    @abstractclassmethod
    def import_data(cls, path: str, report_type: str):
        raise NotImplementedError
