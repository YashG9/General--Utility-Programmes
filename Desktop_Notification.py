from plyer import notification
import time

if __name__=='__main__':
    while True:
        notification.notify(
            title="*** Hey !! Take Some Rest ***",
            message="Its been a long since you are working ....so please do rest for sometime relax your mind body drink some water then start again after sometime !!!",
            timeout =10
            )
        time.sleep(7200)
