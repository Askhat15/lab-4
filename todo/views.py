from django.views.generic import ListView
from .models import ToDoItem


class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/index.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date=date.today())