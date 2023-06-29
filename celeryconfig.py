from datetime import timedelta

beat_schedule = {
    'monitor-user-activity': {
        'task': 'tasks.monitor_user_activity',
        'schedule': timedelta(minutes=1),  # Check user activity
    },
}
