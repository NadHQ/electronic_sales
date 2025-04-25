from celery.schedules import crontab

CELERY_SCHEDULE = {
    "reduce_debt_task_everyday_6_30": {
        "task": "network.tasks.reduce_debt_task",
        "schedule": crontab(minute=30, hour=6),  # everyday in 6.30 am
        # "schedule": 60, # uncomment for testing
        "args": (),
    },
    "add_debt_task_every_3_hours": {
        "task": "network.tasks.add_debt_task",
        "schedule": crontab(minute=0, hour="*/3"),  # every 3 hour
        # "schedule": 10, # uncomment for testing
        "args": (),
    },
}
