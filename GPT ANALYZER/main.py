import asyncio
from team.analyzer_gpt import getDataAnalyzerTeam

from config.openai_model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor,start_docker_container,stop_docker_container

from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def main():
    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()


    team = getDataAnalyzerTeam(docker,openai_model_client)

    try:
        task = 'can you give me the graph of survived and died in my data titanic.csv' \
        ' and save it as ouput.png  '

        await start_docker_container(docker)

        async for message in team.run_stream(task=task):
            print("=======================")
            if isinstance(message,TextMessage):
                print(message.source, ":", message.content)
            elif isinstance(message,TaskResult):
                print("Stop reason : ",message.stop_reason)
            

    except Exception as e:
        print(e)
    finally:
        await stop_docker_container(docker)
    


if __name__=='__main__':
    asyncio.run(main())