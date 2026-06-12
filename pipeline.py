import time
from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

def run_with_retry(func, *args, **kwargs):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Encountered Google API Rate Limit. Waiting 65 seconds before retry...")
                time.sleep(65)
            else:
                raise e

def run_research_pipeline(topic : str) -> dict:

    state = {}

    print("\n"+ "=" * 50)
    print("step 1 - search agent is working...")
    
    search_agent = build_search_agent()
    search_result = run_with_retry(search_agent.invoke, {
        "messages" : [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    state['search_results'] = search_result['messages'][-1].content

    print("\n search result ", state['search_results'])


    print("\n" + "=" * 50)
    print("Step 2 - Reader agent is scraping top resources...")
    print("="*50)

    time.sleep(5)
    reader_agent = build_reader_agent()
    reader_result = run_with_retry(reader_agent.invoke, {
        "messages" : [("user",
            f"Based on the following search results about '{topic}',\n"
            f"Pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search results:\n{state['search_results'][:800]}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content

    print("\nscraped content ", state['scraped_content'])


    print("\n" + " ="* 50)
    print("step 3 - Writer is drafting the report...")
    print("="*50)

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTANT : \n {state['scraped_content']}"
    )

    time.sleep(5)
    state['report'] = run_with_retry(writer_chain.invoke, {
            "topic":topic,
            "research":research_combined
    })

    print("\nFinal Report\n", state['report'])


    print("\n" + "=" * 50)
    print("Step 4 - Critic is reviewing the report...")
    print("=" * 50)

    time.sleep(5)
    state['Feedback'] = run_with_retry(critic_chain.invoke, {
        "report": state['report']
    })

    print("\nCritic Review\n", state['Feedback'])

    return state


if __name__ == "__main__":
    topic = input("Enter topic to research: ")
    run_research_pipeline(topic)