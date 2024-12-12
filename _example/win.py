排除列表=[
    '任务栏',
    'NVIDIA GeForce Overlay DT',
    'NVIDIA GeForce Overlay'
]
服务器地址='http://192.168.2.123:9010/set'
secret="MySecret"

from pywinauto import Desktop
import requests
import time
while True:
    windows = Desktop(backend="uia").windows()
    o=[]
    for w in windows:
        t=w.window_text().split('-')[-1].strip()
        if t not in 排除列表 and t not in o and t:
            o.append(t)
    print(o)
    if len(o)>0:
        requests.get(服务器地址,params={'pc_status':0,'pc_app_name':' | '.join(o)+' || '+time.strftime('%Y-%m-%d %H:%M:%S'),'secret':secret})
    else:
        requests.get(服务器地址,params={'pc_status':1,'pc_app_name':'','secret':secret})
    time.sleep(10)