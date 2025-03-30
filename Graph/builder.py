import streamlit as st
from langgraph.graph import StateGraph, START, END
from Common_Utility.state import SDLCState
from Nodes.User_Story.user_story import UserStoryGenerator
from Nodes.Design.design import DesignSpecificationGenerator
from Nodes.Development.development import CodeGenerator
from Nodes.Testing.testing import GenerateTestCases
from Common_Utility.Evaluator import FeedbackEvaluator
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()



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
        self.evaluator = FeedbackEvaluator(self.llm)
        
    def route_based_on_feedback(self, state: SDLCState, current_phase: str) -> str:
        """
        Determines the next phase based on feedback by evaluating the current state.
    
        Args:
            state (SDLCState): The current state of the SDLC process.
            current_phase (str): The current phase (e.g., "user_story_generate", "design").
    
        Returns:
            str: The evaluation result ("Good" or "Bad") for the current phase.
        """
        # Get the feedback for the current phase from the state
        feedback_data = state.feedback.get(current_phase, {})
    
        # Extract relevant feedback components
        quick_feedback = feedback_data.get("quick_feedback", "Good")  # Default to "Good"
        detailed_feedback = feedback_data.get("detailed_feedback", "")
        rating = feedback_data.get("rating", 5)  # Default to 5
        missing_requirements = feedback_data.get("missing_requirements", False)
        inaccurate_info = feedback_data.get("inaccurate_info", False)
        poor_formatting = feedback_data.get("poor_formatting", False)

        # Combine feedback components into a single string for evaluation
        combined_feedback = f"""
        Quick Feedback: {quick_feedback}
        Detailed Feedback: {detailed_feedback}
        Rating: {rating}
        Missing Requirements: {missing_requirements}
        Inaccurate Info: {inaccurate_info}
        Poor Formatting: {poor_formatting}
        """

        # Evaluate the combined feedback using FeedbackEvaluator
        evaluation_result = self.evaluator.evaluate(state, current_phase, combined_feedback)

        # Update the evaluation in the state
        state.evaluation[current_phase] = evaluation_result

        # Return the evaluation result
        return evaluation_result
    
    def build_sdlc_graph(self):
        """
        Constructs the full SDLC workflow graph.
        """
        # Requirement Gathering Phase
        def user_story_node(state: SDLCState):
            generator = UserStoryGenerator(self.llm)
            state = generator.generate_user_stories(state)
            return state

        self.graph_builder.add_node("user_story_generate", user_story_node)

        def refine_user_story_node(state: SDLCState):
            generator = UserStoryGenerator(self.llm)
            state = generator.refine_user_story(state)
            return state

        self.graph_builder.add_node("refine_user_stories", refine_user_story_node)

        # Design Phase
        def design_node(state: SDLCState):
            designer = DesignSpecificationGenerator(self.llm)
            state = designer.generate_design_specification(state)
            return state

        self.graph_builder.add_node("design", design_node)

        def refine_design_specification_node(state: SDLCState):
            designer = DesignSpecificationGenerator(self.llm)
            state = designer.refine_design_specification(state)
            return state

        self.graph_builder.add_node("refine_design_specification", refine_design_specification_node)

        # Development Phase
        def generate_node(state: SDLCState):
            developer = CodeGenerator(self.llm)
            state = developer.generate_code(state)
            return state

        self.graph_builder.add_node("generate_code", generate_node)

        def refine_code_node(state: SDLCState):
            developer = CodeGenerator(self.llm)
            state = developer.refine_code(state)
            return state

        self.graph_builder.add_node("refine_code", refine_code_node)

        # Test Phase
        def test_node(state: SDLCState):
            tester = GenerateTestCases(self.llm)
            state = tester.generate_test_cases(state)
            return state

        self.graph_builder.add_node("test_case_generate", test_node)

        def refine_test_cases_node(state: SDLCState):
            tester = GenerateTestCases(self.llm)
            state = tester.refine_test_cases(state)
            return state

        self.graph_builder.add_node("refine_test_cases", refine_test_cases_node)

        # Define edges
        self.graph_builder.add_edge(START, "user_story_generate")

        self.graph_builder.add_conditional_edges(
            "user_story_generate",
            lambda state: self.route_based_on_feedback(state, "user_story_generate"),
            {
                "Good": "design",
                "Bad": "refine_user_stories"
            }
        )

        self.graph_builder.add_conditional_edges(
            "refine_user_stories",
            lambda state: self.route_based_on_feedback(state, "refine_user_stories"),
            {
                "Good": "design",
                "Bad": "refine_user_stories"
            }
        )

        self.graph_builder.add_conditional_edges(
            "design",
            lambda state: self.route_based_on_feedback(state, "design"),
            {
                "Good": "generate_code",
                "Bad": "refine_design_specification"
            }
        )

        self.graph_builder.add_conditional_edges(
            "refine_design_specification",
            lambda state: self.route_based_on_feedback(state, "refine_design_specification"),
            {
                "Good": "generate_code",
                "Bad": "refine_design_specification"
            }
        )

        self.graph_builder.add_conditional_edges(
            "generate_code",
            lambda state: self.route_based_on_feedback(state, "generate_code"),
            {
                "Good": "test_case_generate",
                "Bad": "refine_code"
            }
        )

        self.graph_builder.add_conditional_edges(
            "refine_code",
            lambda state: self.route_based_on_feedback(state, "refine_code"),
            {
                "Good": "test_case_generate",
                "Bad": "refine_code"
            }
        )

        self.graph_builder.add_conditional_edges(
            "test_case_generate",
            lambda state: self.route_based_on_feedback(state, "test_case_generate"),
            {
                "Good": END,
                "Bad": "refine_test_cases"
            }
        )

        self.graph_builder.add_conditional_edges(
            "refine_test_cases",
            lambda state: self.route_based_on_feedback(state, "refine_test_cases"),
            {
                "Good": END,
                "Bad": "refine_test_cases"
            }
        )

        return self.graph_builder.compile(interrupt_after=["user_story_generate","refine_user_stories","design","refine_design_specification", "generate_code","refine_code", "test_case_generate","refine_test_cases"], checkpointer=memory)