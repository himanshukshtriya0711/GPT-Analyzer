from agents.Code_Executor_Agent import getCODEEXECUTORAGENT
from agents.Data_Analyzer_Agent import getDataAnalyzerAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat

def get_analyzer_gpt_team(docker,model_client):
    code_executor_agent = getCODEEXECUTORAGENT(docker)
    data_analyzer_agent = getDataAnalyzerAgent()

    team = RoundRobinGroupChat(
        participants=[data_analyzer_agent,code_executor_agent],
        max_turns=10,
        termination_condition=TextMentionTermination('STOP')
    )
    return team