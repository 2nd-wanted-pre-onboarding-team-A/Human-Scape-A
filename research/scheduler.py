from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .updater import batch_task

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(batch_task, 'interval', seconds=10) # for test
    # scheduler.add_job(batch_task, 'interval', days=1)
    scheduler.start()