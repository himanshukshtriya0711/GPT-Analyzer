from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.conditions import TextMentionTermination
import os
from agents.prompts.DataAnalyzerAgentPrompt import Data_Analyzer_Msg

def getDataAnalyzerAgent(model_client):
    data_analyzer_agent  =AssistantAgent(
        name = "data_analyzer_agent",
        description="An agent which helps with solving Data Analysis task abd gives the code as well",
        system_message=Data_Analyzer_Msg

    )
    return data_analyzer_agent

