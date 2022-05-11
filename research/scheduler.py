from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .updater import batch_task

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(batch_task, 'date', run_date=datetime.now())
    # scheduler.add_job(batch_task, 'interval', days=1)
    scheduler.start()