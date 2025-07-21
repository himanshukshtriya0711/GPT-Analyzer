from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor



def getCODEEXECUTORAGENT(code_executor):
    code_executor_agent = CodeExecutorAgent(
        name="CodeExecutorAgent",
        code_executor=code_executor,

    )

    return code_executor_agent


import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
async def main():
    docker = DockerCommandLineCodeExecutor(
    work_dir='temp',
    timeout=120,
)
    

    code_executor_agent = getCODEEXECUTORAGENT(docker)

    task = TextMessage(
        content=''' Here is the python code which you have to run
```python
print('Hello World!')
```

''',
    source='user'
    )

    try:
        await docker.start()
        res = await code_executor_agent.on_messages(
            messages=[task],
            cancellation_token=CancellationToken()
        )
        print(res)
        
    except Exception as e:
        print(e)
    finally:
        await docker.stop()


if __name__=='__main__':
    asyncio.run(main())
