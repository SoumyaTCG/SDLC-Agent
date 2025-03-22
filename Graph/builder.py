from langgraph.graph import StateGraph, START, END
from Common_Utility.state import SDLCState
from Nodes.User_Story.user_story import GenerateUserStory
from Nodes.Design.design import GenerateDesignSpecification
from Nodes.Development.development import GenerateCode
from Nodes.Security_Review.security import SecurityReview
from Nodes.Testing.testing import GenerateTestCases

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

    def user_story_graph(self):
        """
        Builds the Requirement Gathering phase graph.
        """
        user_story_node = GenerateUserStory(self.llm).generate
        self.graph_builder.add_node("user_story_generate", user_story_node)
        self.graph_builder.add_edge(START, "user_story_generate")

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
    
    def security_review_graph(self):
        """
        Builds the Security Review phase graph.
        """
        security_review_node = SecurityReview(self.llm).generate
        self.graph_builder.add_node("security_review", security_review_node)
        self.graph_builder.add_edge("development", "security_review")
    
    def test_cases_graph(self):
        """
        Builds the Testing phase graph.
        """
        test_cases_node = GenerateTestCases(self.llm).generate_test_cases
        self.graph_builder.add_node("test_cases_node", test_cases_node)
        self.graph_builder.add_edge("security_review", "test_cases_node")
        self.graph_builder.add_edge("test_cases_node", END)
    

    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected SDLC phase.

        Args:
            usecase (str): The SDLC phase to set up.
        """
        if usecase == "Requirement Gathering":
            self.requirement_gathering_graph()
        elif usecase == "Design":
            self.design_graph()
        elif usecase == "Development":
            self.development_graph()

        return self.graph_builder.compile()