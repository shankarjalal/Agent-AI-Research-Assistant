# Import Libraries
import sys
sys.stdout.reconfigure(encoding='utf-8')
from langchain.tools import tool  # it is use for create tools of agent & it is use for make agent to do work
import requests  # it is use for make requests to the web
from bs4 import BeautifulSoup  # it is use for parse the html content
from tavily import TavilyClient  # it is use for search the web
import os  # it is use for access the environment variables
from dotenv import load_dotenv  # it is use for load the environment variables
from rich import print  # it is use for print the output
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query : str) -> str:
    """ Search the web for recent and reliable information on a topic.
        Returns Titles, URLs and Snippets."""
    results = tavily.search(query=query, max_results=5)

    out = []
    for r in results['results']:
        out.append(f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n")
    return "\n-----\n".join(out)

print(web_search.invoke('What is the recent news of war'))


print("__________________________________________________")
print("__________________________________________________")
@tool 
def scrape_url(url : str) -> str:
    """ Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers= {"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, "html.parser")
        for tag in soup(['script', 'style', 'nav', 'footer']):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:4000]
    except Exception as e:
        return f"Error scraping URL: {str(e)}"  

print(scrape_url.invoke("https://timesofindia.indiatimes.com/sports/cricket/ipl-live-rcb-vs-lsg-live-score-update-royal-challengers-bengaluru-vs-lucknow-super-giants-cricket-match-ipl-scorecard-ball-to-ball-commentary-playing-11-cricket-news-virat-kohli/liveblog/130281762.cms"))


