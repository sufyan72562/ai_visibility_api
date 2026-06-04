from abc import ABC, abstractmethod


class BaseAgent(ABC):
    def __init__(self, llm_service):
        self.llm_service = llm_service

    @abstractmethod
    def run(self, *args, **kwargs):
        pass