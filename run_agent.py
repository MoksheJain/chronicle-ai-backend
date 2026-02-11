from agent.planner import plan_categories
from agent.summariser import summarise
from tools.news_fetcher import fetch_news
from tools.email_sender import send_newsletter

def news_run_agent():
    categories = plan_categories()
    full_html = "<h1> ChronicleAI - Daily news roundup </h1>"
    for category in categories:
        articles = fetch_news(category)
        # print(articles)
        summary_html = summarise(category, articles)
        full_html += f"<h2>{category.title()}</h2>"
        full_html += summary_html
    send_newsletter("Your daily ChronicleAI brief", full_html)

if __name__ == "__main__":
    news_run_agent()
