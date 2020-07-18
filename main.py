import time
from plyer import notification

if __name__  == '__main__':
    while True:
        notification.notify(
            title = 'Please Drink Water Now',
            message = "Paani Nahi peyo ge to mar jao ge , aur mar gaye to kam kon karga is liye khata hu paani pe lo",
            app_icon = '',
            timeout = 5
        )
        time.sleep(60*60)