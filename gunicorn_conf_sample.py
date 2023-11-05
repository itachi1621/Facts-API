from multiprocessing import cpu_count



# Socket Path

bind = 'unix:'#Your socket path



# Worker Options

workers = cpu_count() + 1

worker_class = 'uvicorn.workers.UvicornWorker'



# Logging Options

loglevel = 'debug'

accesslog = ''#Your access log path

errorlog =  ''#Your error log path
