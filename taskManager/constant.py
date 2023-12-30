tabs = [
    {"text": "Back", "staticLink": True, "link": "/", "class": "text-warning"},
    {"text": "Add Task +", "staticLink": False, "link": "addTaskPage", "class": ""},
    {"text": "Home", "staticLink": False, "link": "homePage", "class": ""},
    {"text": "My Tasks", "staticLink": False, "link": "myTasksPage", "class": ""},
    {"text": "My Comments", "staticLink": False, "link": "myCommentsPage", "class": ""},
    {"text": "Profile", "staticLink": False, "link": "profilePage", "class": ""},
]


def dynamicTabs(pageName, user):
    dynTabs = None
    if user.is_authenticated:
        dynTabs = tabs.copy()
    else:
        dynTabs = [
            {"text": "Back", "staticLink": True, "link": "/", "class": "text-warning"},
            {"text": "Home", "staticLink": False, "link": "homePage", "class": ""},
            {
                "text": "Profile",
                "staticLink": False,
                "link": "profilePage",
                "class": "",
            },
        ]

    for dic in dynTabs[1:]:
        if dic["link"] == pageName:
            dic["class"] = "text-dark active"
        else:
            dic["class"] = "text-white"

    backNotList = [
        "homePage",
    ]
    if pageName in backNotList:
        return dynTabs[1:]
    return dynTabs


logo = "HERISI Task Manager"

taskTitles = {
    "add": "Add Task",
    "myTasks": "My Task",
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

reservedWords = [
    "add",
    "delete",
    "edit",
    "myTasks",
    "register",
    "logout",
    "login",
    "profile",
    "admin",
    "account",
]
