from langgraph.func import entrypoint, task

@task
def task1():
    print("task1")
    return "task 1 executed"

@task
def task2():
    print("task2")
    return "task 2 executed"

@entrypoint()
def run_flow(input:str):
    print("Running simple flow",input)

    task1_output=task1().result()
    task2_output=task2().result()

    return f"workflow executed with {task1_output} and {task2_output}"

def run_chain():
    run_flow.invoke(input="Simple Input")