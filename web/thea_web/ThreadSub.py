import logging, time, queue
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def sleepsub(s, q):
    logging.debug("Sub thread sleeps for {} seconds".format(s))
    time.sleep(int(s))
    logging.debug("Sub thread woke up")
    rtnval = "Sub thread is awake now after sleeping for {} seconds".format(s)
    q.put(rtnval)