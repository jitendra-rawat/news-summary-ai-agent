import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient

from graph.workflow import build_graph


async def main():

    print("\n==============================")
    print("     NEWS AI AGENT")
    print("==============================\n")

    topic = input(
        "Enter news topic: "
    ).strip()

    if not topic:

        topic = "technology"

    print("\nConnecting to MCP server...\n")

    client = MultiServerMCPClient(
        {
            "news": {
                "command": "python",
                "args": [
                    "mcp_servers/news_server.py"
                ],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()

   

    graph = build_graph(tools)

    

    result = await graph.ainvoke(
        {
            "topic": topic,
            "news": [],
            "summary": "",
        }
    )

    print("\n")
    print("=" * 70)
    print("TOP 5 NEWS")
    print("=" * 70)

    for index, article in enumerate(
        result["news"],
        start=1
    ):

        print(f"\n{index}. {article['title']}")

        print(
            f"Source: "
            f"{article.get('source', 'Unknown')}"
        )

        print(
            f"Published: "
            f"{article.get('published', '')}"
        )

        print(
            f"URL: "
            f"{article.get('url', '')}"
        )

    print("\n")
    print("=" * 70)
    print("AI SUMMARY")
    print("=" * 70)

    print(
        result["summary"]
    )


if __name__ == "__main__":

    asyncio.run(main())