from apscheduler.schedulers.background import BackgroundScheduler
from .updater import BatchTask

batch = BatchTask()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(batch.batch_task, 'interval', seconds=10)
    # scheduler.add_job(batch.batch_task, 'interval', days=1)
    scheduler.start()