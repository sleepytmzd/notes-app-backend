from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def getNotes(request, id):
    notes = Note.objects.filter(user_id=id)
    serializedNotes = NoteSerializer(notes, many=True)
    return Response(serializedNotes.data)

@api_view(['POST'])
def createNote(request):
    note = NoteSerializer(data=request.data)
    if note.is_valid():
        note.save()
        return Response(note.data, status=status.HTTP_201_CREATED)
    return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getSpecificNote(request, user_id, note_id):
    note = Note.objects.get(id=note_id, user_id=user_id)
    serializedNote = NoteSerializer(note)
    return Response(serializedNote.data)

@api_view(['DELETE'])
def deleteNote(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return Response("Note deleted successfully")

from django.http import JsonResponse

@api_view(['GET'])
def health_check(request):
    return JsonResponse({"status": "ok"})

