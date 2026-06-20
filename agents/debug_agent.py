from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def debug_agent(state):

    prompt = f"""
    You are a Senior Debugging Engineer.

    Review the following code:

    {state["code"]}

    Find:
    - Syntax Errors
    - Runtime Issues
    - Logic Bugs
    - Security Problems

    Suggest fixes and improvements.
    """

    response = llm.invoke(prompt)

    state["debug"] = response.content

    return state
