from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from UserApps.models  import *

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        print("hi")
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return redirect('user-home')
        

def edit_task_form(request, task_id):
        
        print("reached", task_id)
        task = get_object_or_404(Task, id=task_id)
        serializer = TaskSerializer(task)
        print(serializer.data,"data is here")
        return render(request, 'pages/EditTask.html', {'task_data': serializer.data})



@api_view(['POST'])
def createView(request):
    print("coming to this")
    email = request.session.get('user_email')
    
    try:
        user = AppUsers.objects.get(email=email)
    except AppUsers.DoesNotExist:
        # Handle the case when the user does not exist
        return Response({"error": "User does not exist."})

    print(user.id, "gottt")
    print("create")
   
    title = request.data.get('title')
    description = request.data.get('description')
    due_date = request.data.get('due_date')
    print(title, description, due_date, "hhhhhhhhhhhhhhhhhhhhh")

    serializer = TaskSerializer(data={
        'user': user.id,
        'description': description,
        'title': title,
        'due_date': due_date,
    })

    if serializer.is_valid():
        serializer.save()
        return redirect('user-home')

    return Response(serializer.errors)








def CreateTask(request):
    return render(request,'pages/CreateTask.html')