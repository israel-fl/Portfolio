from multiprocessing import cpu_count

def max_workers():
    return (cpu_count() * 2) + 1


bind = "0.0.0.0:5000"
x_forwarded_for_header = "X-Real-IP"
pidfile = "pid"
loglevel = 'error'
workers = max_workers()
access_log_format = '[%({X-Real-IP}i)s] %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_fork(server, worker):
    pass


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")
