from task.signals import getTaskCount


tabs = [
    # fmt: off
    {"show":False, "text": "Back", "staticLink": True, "link": "/", "class": "text-warning"},
    {"show":False, "text": "Add Task", "staticLink": False, "link": "addTaskPage", "class": ""},
    {"show":False, "text": "Home", "staticLink": False, "link": "homePage", "class": ""},
    {"show":False, "text": "My Tasks", "staticLink": False, "link": "myTasksPage", "class": ""},
    {"show":False, "text": "My Comments", "staticLink": False, "link": "myCommentsPage", "class": ""},
    {"show":False, "text": "Admin Console", "staticLink": False, "link": "adminPage", "class": ""},
    {"show":False, "text": "Profile", "staticLink": False, "link": "profilePage", "class": ""},
]


def dynamicTabs(pageName, user):
    dynTabs = tabs.copy()

    # give text list to enable the headers
    def triggerHeader(textList, show=True):
        for text in textList:
            # fmt: off
            index=next((index for index, item in enumerate(dynTabs) if item["text"] == text), None)
            dynTabs[index]["show"] = show # type: ignore

    # default headers for all users
    triggerHeader(["Home", "Profile"])

    # customize tabs accoarding to user authentication
    if user.is_authenticated:
        triggerHeader(["Add Task", "My Tasks", "My Comments"])
    else:
        triggerHeader(["Add Task", "My Tasks", "My Comments"], False)

    if user.is_superuser:
        triggerHeader(["Admin Console"])
        triggerHeader(["Profile"], False)
    else:
        triggerHeader(["Profile"])
        triggerHeader(["Admin Console"], False)

    # exception pages for Back button
    exception = ["homePage"]
    triggerHeader(["Back"], False) if pageName in exception else triggerHeader(["Back"])

    # stylize the tabs
    for dic in dynTabs[1:]:
        dic["class"] = "text-dark active" if dic["link"] == pageName else "text-white"

    return dynTabs


logo = "HERISI Task Manager"

taskTitles = {
    "admin": "Admin Console",
    "add": "Add Task",
    "myTasks": "My Tasks",
    "home": "Home",
    "task": "Task",
    "edit": "Edit",
}

profileTitles = {
    "profile": "User Account",
    "register": "Register",
    "login": "Login",
}

commentTitles = {
    "add": "Add Comment",
    "edit": "Edit Comment",
    "my": "My Comments",
}

searchTitles = {"search": "Search results for"}

titles = {**taskTitles, **profileTitles, **commentTitles, **searchTitles}


def generateBasicData(request, tabName, titleName):
    try:
        temp = {"title": titles[titleName]}
    except Exception:
        temp = {"title": titleName}

    return {
        **temp,
        "tabs": dynamicTabs(tabName, request.user),
        "logo": logo,
        "taskCount": getTaskCount(),
    }
