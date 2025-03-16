# SDLC-Agent
An AI-powered Software Development Life Cycle (SDLC) agent built using Langraph and Streamlit to automate and streamline the software development process. The agent assists with all key SDLC phases — from requirement gathering to deployment and maintenance — while incorporating human feedback at every stage.

## 🚀 **Features**
✅ Modular architecture for each SDLC phase.  
✅ Uses Langraph to manage state and transitions.  
✅ Human feedback loop to refine outputs.  
✅ Clean UI with Streamlit.  
✅ Conda environment for easy setup.  


## 🏗️ **Project Structure**

sdlc_agent/
├── requirement_gathering/         # Requirement Gathering Phase
│   ├── __init__.py
│   ├── state.py
│   ├── transitions.py
│   └── agent.py
├── design/                        # Design Phase
│   ├── __init__.py
│   ├── state.py
│   ├── transitions.py
│   └── agent.py
├── development/                   # Development Phase
│   ├── __init__.py
│   ├── state.py
│   ├── transitions.py
│   └── agent.py
├── testing/                       # Testing Phase
│   ├── __init__.py
│   ├── state.py
│   ├── transitions.py
│   └── agent.py
├── deployment/                    # Deployment Phase
│   ├── __init__.py
│   ├── state.py
│   ├── transitions.py
│   └── agent.py
├── maintenance/                   # Maintenance Phase
│   ├── __init__.py
│   ├── state.py
│   ├── transitions.py
│   └── agent.py
├── ui/                            # UI Components (New)
│   ├── __init__.py
│   ├── requirement_ui.py          # UI for Requirement Gathering
│   ├── design_ui.py               # UI for Design
│   ├── development_ui.py          # UI for Development
│   ├── testing_ui.py              # UI for Testing
│   ├── deployment_ui.py           # UI for Deployment
│   └── maintenance_ui.py          # UI for Maintenance
├── utils/                         # Shared utility functions
│   ├── __init__.py
│   └── logger.py
├
├── requirements.txt               # Dependencies
└── README.md                      # Project documentation
