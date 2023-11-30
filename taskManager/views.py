from django.shortcuts import render
from taskManager.constant import tabs, logo
from user.models import CustomUser, User
from task.models import Task
from comment.models import Comment
from taskManager.constant import searchTitles
from django.utils.safestring import mark_safe
import re


def highlight(query, text):
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    highlighted_text = pattern.sub(
        lambda match: f'<span class="highlight">{match.group()}</span>', text
    )
    has_results = len(re.findall(pattern, text)) > 0
    highlighted_text = f"<span>{highlighted_text}</span>"
    return mark_safe(highlighted_text), has_results


def searchPeople(query):
    result = []
    people = User.objects.all()

    for person in people:
        username = highlight(query, person.username)
        first_name = highlight(query, person.first_name)
        last_name = highlight(query, person.last_name)
        email = highlight(query, person.email)

        for field in [username, first_name, last_name, email]:
            if field[1]:
                person = {
                    "id": person.id,
                    "username": username[0],
                    "first_name": first_name[0],
                    "last_name": last_name[0],
                    "email": email[0],
                }
                result.append(person)
                break

    return result


def searchTasks(query):
    result = []
    tasks = Task.objects.all()

    for task in tasks:
        title = highlight(query, task.title)
        priority = highlight(query, str(task.priority))
        state = highlight(query, task.state)
        deadline_time = highlight(query, str(task.deadline_time))
        deadline_date = highlight(query, str(task.deadline_date))

        for field in [title, priority, state, deadline_time, deadline_date]:
            if field[1]:
                task = {
                    "id": task.id,
                    "title": title[0],
                    "priority": priority[0],
                    "user": User.objects.get(id=task.user.id),
                    "state": state[0],
                    "deadline_time": deadline_time[0],
                    "deadline_date": deadline_date[0],
                }
                result.append(task)
                break

    return result


def searchComments(query):
    result = []
    comments = Comment.objects.all()

    for comment in comments:
        text = highlight(query, comment.text)
        date = highlight(query, str(comment.date))
        time = highlight(query, str(comment.time))

        for field in [text, date, time]:
            if field[1]:
                comment = {
                    "id": comment.id,
                    "text": text[0],
                    "date": date[0],
                    "time": time[0],
                }
                result.append(comment)
                break

    return result


def search(request):
    query = request.GET.get("query", "")

    people = searchPeople(query)
    tasks = searchTasks(query)
    comments = searchComments(query)

    results = {"people": people, "tasks": tasks, "comments": comments}
    count = {
        "peopleCount": len(people),
        "tasksCount": len(tasks),
        "commentsCount": len(comments),
    }
    context = {"query": query}
    header = {
        "tabs": tabs,
        "logo": logo,
        "title": f"{searchTitles['search']} {query[0:10]}",
    }
    return render(
        request,
        "searchResult.html",
        {**context, **header, **results, **count, "search": True},
    )
