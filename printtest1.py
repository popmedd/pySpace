
"""
Created on Fri Jul 24 16:16:56 2020

@author: Administrator
"""
import datetime 

from apscheduler.schedulers.blocking import BlockingScheduler
scheduler = BlockingScheduler()
def printtest1(text):
    print(text)
def job1():
    print('test',datetime.datetime.now())
scheduler.add_job(job1,'interval',seconds=3,id='job1')
scheduler.add_job(printtest1,'date',run_date = datetime.datetime(2020,7,24,19,27,55), args=['测试'])
scheduler.start()