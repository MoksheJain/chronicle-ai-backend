from apscheduler.schedulers.blocking import BlockingScheduler
from run_agent import news_run_agent

scheduler = BlockingScheduler()
scheduler.add_job(news_run_agent, 'cron', hour=9)
scheduler.start()