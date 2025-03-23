from langgraph.graph import StateGraph, START, END
from Common_Utility.state import SDLCState
from Nodes.User_Story.user_story import UserStoryGenerator
from Nodes.Design.design import DesignSpecificationGenerator
from Nodes.Development.development import CodeGenerator

from Nodes.Testing.testing import GenerateTestCases

class GraphBuilder:
    """
    Builds the complete SDLC process graph using LangGraph.
    """

    def __init__(self, model, user_input):
        """
        Initializes the GraphBuilder with the LLM model and user input.

        Args:
            model (LLM): The language model used for processing.
            user_input (str): The requirement text provided by the user.
        """
        self.llm = model
        self.user_input = user_input  # Capture user input dynamically
        self.graph_builder = StateGraph(SDLCState)

    def build_sdlc_graph(self):
        """
        Constructs the full SDLC workflow graph.
        """
        # Requirement Gathering Phase (Pass user input dynamically)
        def user_story_node(state: SDLCState):
            generator = UserStoryGenerator(self.llm)
            # Only pass the 'state' object to generate_user_stories
            state = generator.generate_user_stories(state)  
            return state

        self.graph_builder.add_node("user_story_generate", user_story_node)
        self.graph_builder.add_edge(START, "user_story_generate")

        # Design Phase
        def design_node(state: SDLCState):
            designer = DesignSpecificationGenerator(self.llm)
            # Call the correct method 'generate_design_specification'
            state = designer.generate_design_specification(state)  
            return state

        self.graph_builder.add_node("design", design_node)
        self.graph_builder.add_edge("user_story_generate", "design")

        # Development Phase
        def development_node(state: SDLCState):
            developer = CodeGenerator(self.llm)
            # Call the correct method 'generate_code'
            state = developer.generate_code(state)  
            return state

        self.graph_builder.add_node("development", development_node)
        self.graph_builder.add_edge("design", "development")

        # Test Phase
        def test_node(state: SDLCState):
            tester = GenerateTestCases(self.llm)
            state = tester.generate_test_cases(state)  # Call generate_test_cases 
            return state
        
        self.graph_builder.add_node("test",test_node)
        self.graph_builder.add_edge("development","test")
        self.graph_builder.add_edge("test", END)

        return self.graph_builder.compile()
  

