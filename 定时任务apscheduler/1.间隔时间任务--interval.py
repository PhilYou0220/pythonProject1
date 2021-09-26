from datetime import datetime
import os
# 导入调度器模块 BlockingScheduler，这是最简单的调度器，调用 start 方阻塞当前进程，如果你的程序只用于调度，除了调度进程外没有其他后台进程，
# 那么请用 BlockingScheduler 非常有用，此时调度进程相当于守护进程。
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()  # 实例化
    scheduler.add_job(tick, 'interval', seconds=3)  # 添加任务
    print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else '非windows系统'))
    try:
        # 直接开始进程
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
