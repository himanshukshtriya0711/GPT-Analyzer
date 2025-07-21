from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constant import WORK_DIR,TIMEOUT
def getDockerCommandLineExecutor():
    docker  = DockerCommandLineCodeExecutor(
    work_dir=WORK_DIR,
    timeout=TIMEOUT
    
    )
    return docker


async def start_docker_container(docker):
    print("Startig the Docker Container")
    await docker.start()
    print("docker started")

async def stop_docker_container(docker):
    print("Stopping the Docker Container")
    await docker.stop()
    print("docker stopped")