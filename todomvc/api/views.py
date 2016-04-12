from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import TodoSerializer
from todo.models import Todo


@api_view(['GET', 'POST'])
def list_create_todo(request):

    if request.method == "GET":
        todos = Todo.objects.order_by('order')
        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUpdateDeleteTodo(APIView):

     def get(self, request, pk):
          try:
               todo = Todo.objects.get(pk=pk)
          except Todo.DoesNotExist as e:
               return Response(status=status.HTTP_404_NOT_FOUND)

          serializer = TodoSerializer(todo)
          return Response(serializer.data)

     def put(self, request, pk):
          try:
               todo = Todo.objects.get(pk=pk)
          except Todo.DoesNotExist as e:
               return Response(status=status.HTTP_404_NOT_FOUND)

          serializer = TodoSerializer(todo, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk):
         try:
             todo = Todo.objects.get(pk=pk)
         except Todo.DoesNotExist as e:
             return Response(status=status.HTTP_404_NOT_FOUND)

         todo.delete()

         return Response(status=status.HTTP_204_NO_CONTENT)