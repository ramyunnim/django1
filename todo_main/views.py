from django.shortcuts import render

from django.views import View, generic

class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_main/index.html'
        return render(request, template_name)


# Create your views here.