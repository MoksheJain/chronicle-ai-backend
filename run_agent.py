from agent.planner import plan_categories
from agent.summariser import summarise_english, summarise_hindi
from tools.news_fetcher import fetch_news
from tools.email_sender import send_newsletter
from agent.planner import plan_categories
from agent.summariser import summarise_english, summarise_hindi
from tools.news_fetcher import fetch_news
from tools.email_sender import send_newsletter


def news_run_agent():

    categories = plan_categories()

    # Separate HTML bodies
    full_html_english = "<h1>📰 ChronicleAI - Daily News Roundup</h1>"
    full_html_hindi = "<h1>📰 ChronicleAI - आज की प्रमुख खबरें</h1>"

    for category in categories:

        articles = fetch_news(category)

        # Generate summaries
        summary_html_english = summarise_english(category, articles)
        summary_html_hindi = summarise_hindi(category, articles)

        # Add category headings
        full_html_english += f"<h2>{category.title()}</h2>"
        full_html_english += summary_html_english

        full_html_hindi += f"<h2>{category.title()}</h2>"
        full_html_hindi += summary_html_hindi

    # Send both versions
    send_newsletter(
        subject_en="📰 Your Daily ChronicleAI Brief",
        subject_hi="📰 ChronicleAI - आज की संक्षिप्त खबरें",
        html_en=full_html_english,
        html_hi=full_html_hindi
    )

if __name__ == "__main__":
    news_run_agent()
