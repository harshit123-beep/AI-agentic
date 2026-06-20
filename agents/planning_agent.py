from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)


def planning_agent(state):

    prompt = f"""
    You are a Senior Software Architect.

    Based on the following requirements:

    {state["requirements"]}

    Generate:

    1. Project Architecture
    2. Development Roadmap
    3. Database Design Suggestions
    4. Module Breakdown
    5. Folder Structure
    """

    response = llm.invoke(prompt)

    state["plan"] = response.content

    return state
