from langchain_core.messages import HumanMessage

from models.ollama import llm


async def news_agent(state, tools):

    topic = state["topic"]

    tool = next(
        tool
        for tool in tools
        if tool.name == "search_news"
    )

    prompt = f"""
You are a News Research Agent.

The user wants the latest news about:

{topic}

Your task:

1. Use the search_news tool.
2. Retrieve exactly 5 news articles.
3. Do not summarize the news yourself.
4. Return the raw news articles.

Call the tool now.
"""

    response = await llm.ainvoke(
        [HumanMessage(content=prompt)]
    )

    # The model should tell us to use the tool,
    # we directly call the MCP tool.

    news = await tool.ainvoke(
        {
            "topic": topic,
            "limit": 5,
        }
    )

    return {
        "news": news
    }