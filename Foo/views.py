# Create your views here.

from rest_framework import filters, generics
from rest_framework.response import Response

from Foo import models
from Foo.serializers import CourseDetailSerializer, CourseSerializer


class CourseListView(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = (
        "id",
        "is_active",
        "is_coding",
        "updated_at",
        "created_at",
    )
    search_fields = (
        "title",
        "first_price",
        "real_price",
    )


class CourseDetailView(generics.RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        rv_data = {
            "code": 200,
            "message": "SUCCESS",
            "data": serializer.data
        }
        return Response(rv_data)


from django.views import View
from django.shortcuts import HttpResponse, get_object_or_404


# 普通视图
class CouseView(View):

    def get(self, request, id):
        obj = get_object_or_404(models.Course, id=id)
        return HttpResponse(f"page for {obj.title} course", status=200)
