from langgraph.graph import StateGraph, START, END
from langchain_core.prompts import ChatPromptTemplate
from Common_Utility.state import SDLCState
from Nodes.User_Story.user_story import GenerateUserStory
from Nodes.Design.design import GenerateDesignSpecification
from Nodes.Development.development import GenerateCode
# from Nodes.Testing import RunTests
# from Nodes.Deployment import DeployCode
# from Nodes.Maintenance import MonitorAndMaintain

class GraphBuilder:
    """
    Builds the SDLC process graph using LangGraph.
    """

    def __init__(self, model):
        """
        Initializes the GraphBuilder with the LLM model.
        
        Args:
            model (LLM): The language model used for processing.
        """
        self.llm = model
        self.graph_builder = StateGraph(SDLCState)

    def requirement_gathering_graph(self):
        """
        Builds the Requirement Gathering phase graph.
        """
        requirement_node = GenerateUserStory(self.llm).generate
        self.graph_builder.add_node("requirement_gathering", requirement_node)
        self.graph_builder.add_edge(START, "requirement_gathering")

    def design_graph(self):
        """
        Builds the Design phase graph.
        """
        design_node = GenerateDesignSpecification(self.llm).generate
        self.graph_builder.add_node("design", design_node)
        self.graph_builder.add_edge("requirement_gathering", "design")

    def development_graph(self):
        """
        Builds the Development phase graph.
        """
        development_node = GenerateCode(self.llm).generate
        self.graph_builder.add_node("development", development_node)
        self.graph_builder.add_edge("design", "development")

    # def testing_graph(self):
    #     """
    #     Builds the Testing phase graph.
    #     """
    #     testing_node = RunTests(self.llm).generate
    #     self.graph_builder.add_node("testing", testing_node)
    #     self.graph_builder.add_edge("development", "testing")

    # def deployment_graph(self):
    #     """
    #     Builds the Deployment phase graph.
    #     """
    #     deployment_node = DeployCode(self.llm).generate
    #     self.graph_builder.add_node("deployment", deployment_node)
    #     self.graph_builder.add_edge("testing", "deployment")

    # def maintenance_graph(self):
    #     """
    #     Builds the Maintenance phase graph.
    #     """
    #     maintenance_node = MonitorAndMaintain(self.llm).generate
    #     self.graph_builder.add_node("maintenance", maintenance_node)
    #     self.graph_builder.add_edge("deployment", "maintenance")
    #     self.graph_builder.add_edge("maintenance", END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected SDLC phase.

        Args:
            usecase (str): The SDLC phase to set up.
        """
        if usecase == "Requirement Gathering":
            self.requirement_gathering_graph()
        if usecase == "Design":
            self.design_graph()
        if usecase == "Development":
            self.development_graph()
        # if usecase == "Testing":
        #     self.testing_graph()
        # if usecase == "Deployment":
        #     self.deployment_graph()
        # if usecase == "Maintenance":
        #     self.maintenance_graph()

        return self.graph_builder.compile()
