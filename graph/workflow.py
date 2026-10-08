from langgraph.graph import StateGraph, START, END

from graph.state import NewsState

from agents.news_agent import news_agent
from agents.summary_agent import summary_agent


def build_graph(tools):

    async def news_node(state):

        return await news_agent(
            state,
            tools,
        )

    async def summary_node(state):

        return await summary_agent(
            state
        )

    graph = StateGraph(NewsState)

    graph.add_node(
        "news_agent",
        news_node,
    )

    graph.add_node(
        "summary_agent",
        summary_node,
    )

    graph.add_edge(
        START,
        "news_agent",
    )

    graph.add_edge(
        "news_agent",
        "summary_agent",
    )

    graph.add_edge(
        "summary_agent",
        END,
    )

    return graph.compile()