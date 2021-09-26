from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import dingshi2


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(dingshi2.go_home(), 'cron', hour=17, minute=00)
    # # 定时 cron 任务也非常简单，直接给触发器 trigger 传入 ‘cron’ 即可。hour =19 ,minute =23 这里表示每天的19：23 分执行任务。这里可以填写数字，也可以填写字符串
    # # hour =19 , minute =23
    # # hour ='19', minute ='23'
    # # minute = '*/3' 表示每 5 分钟执行一次
    # # hour ='19-21', minute= '23' 表示 19:23、 20:23、 21:23 各执行一次任务
    print('Press Ctrl+{0} to exit'.format('Z' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
