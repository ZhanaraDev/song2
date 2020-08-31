from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action

from musical_works.serializers import MusicalWorkSerializer

from musical_works.models import MusicalWork
from rest_framework.response import Response


class MusicalWorksViewSet(viewsets.ModelViewSet):
    serializer_class = MusicalWorkSerializer
    queryset = MusicalWork.objects.all()

    @action(detail=True, methods=('get',))
    def music_by_iswc(self, request, pk):
        data = self.serializer_class(instance=self.queryset.get(iswc=pk)).data
        return Response(data=data, status=200)
