import time
from plyer import notification
from topstories import topStories

ICON = "C:/Users/user/PycharmProjects/DesktopNotifier/ic.png"

newsitems = topStories()
# print(newsitems[0]['title'])
# print(newsitems[0]['description'])
# notification.notify(title = "Amit",message = "IIT kanpur",app_icon = None,timeout=10,toast = False)
notification.notify(title = str(newsitems[0]['title'])[1:60],message = str(newsitems[0]['description'])[1:255],app_icon = ICON,timeout=10)

