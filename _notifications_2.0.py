from plyer import notification
import time


if __name__ == '__main__':
    while True:
        notification.notify(
            title = " Rest time",
            message ="Rest lele Bhai",
            app_icon ="/Users/akshat/Desktop/Dragon.jpg",
            timeout = 5)
        time.sleep(10)
