# agent_base.py

class AgentBase:
    def __init__(self, role, goal, attributes, llm, tools):
        self.role = role
        self.goal = goal
        self.attributes = attributes
        self.llm = llm
        self.tools = tools

    def execute_task(self, task):
        """Executes the given task."""
        # Implement the task execution logic here
        pass

    def get_info(self, query):
        """Use LLM to retrieve information related to the query."""
        # Implement logic for interacting with the language model here
        pass
