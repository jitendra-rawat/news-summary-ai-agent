import feedparser

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("News Server")


@mcp.tool()
def search_news(topic: str = "technology", limit: int = 5) -> list[dict]:
    """
    Get the latest news articles for a topic.

    Args:
        topic: News topic such as technology, sports, business, India, AI.
        limit: Number of articles to return.
    """

    url = (
        "https://news.google.com/rss/search"
        f"?q={topic}&hl=en-IN&gl=IN&ceid=IN:en"
    )

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries[:limit]:

        article = {
            "title": entry.get("title", ""),
            "url": entry.get("link", ""),
            "published": entry.get("published", ""),
            "source": entry.get("source", {}).get("title", ""),
            "summary": entry.get("summary", ""),
        }

        articles.append(article)

    return articles


if __name__ == "__main__":
    mcp.run()