from langchain_core.messages import HumanMessage

from models.ollama import llm


async def summary_agent(state):

    news = state["news"]

    news_text = ""

    for index, article in enumerate(news, start=1):

        news_text += f"""
NEWS {index}

Title:
{article.get("title", "")}

Source:
{article.get("source", "")}

Published:
{article.get("published", "")}

Description:
{article.get("summary", "")}

URL:
{article.get("url", "")}

-------------------------
"""

    prompt = f"""
You are a professional news summarization agent.

Below are the 5 latest news articles.

{news_text}

Your task:

1. Summarize each article.
2. Keep each summary to 2-3 sentences.
3. Mention the source.
4. Do not invent facts.
5. Preserve important numbers, names and dates.
6. Include the article URL.
7. Start each article with its number and title.

Use this format:

1. TITLE
Source: SOURCE

Summary: ...

URL: ...

2. TITLE
Source: SOURCE

Summary: ...

URL: ...
"""

    response = await llm.ainvoke(
        [HumanMessage(content=prompt)]
    )

    return {
        "summary": response.content
    }