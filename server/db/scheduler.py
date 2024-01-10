import sys
sys.path.append("update-chat-server/server")

import atexit
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from db.model_session  import *

scheduler_cycle_time = 180 # seconds

# 만료된 세션을 삭제하는 함수
def cleanup_expired_sessions():
    now = datetime.now()
    db= next(get_db())
    expired_sessions = db.query(Session).filter(Session.expired_at <= now).all()
    
    count = 0
    for deleted in expired_sessions:
        count += 1
        db.delete(deleted)
    
    db.commit()
    print("OK SCHEDULER, delete ", count ," record")

# APScheduler를 설정합니다.
scheduler = BackgroundScheduler()
scheduler.add_job(cleanup_expired_sessions, 'interval', seconds=scheduler_cycle_time)  # 15분마다 실행하도록 설정
scheduler.start()
print("START SCHEDULER")
# 프로그램 종료 시 스케줄러를 정리합니다.
atexit.register(lambda: scheduler.shutdown())

