#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Date: 2020/05/09
# Author: huimingz
# Contact: huimingz12@outlook.com

from django.urls import path, include

from Foo import views


app_name = "api-foo"

urlpatterns = [
    path("course/", views.CourseListView.as_view(), name="course"),
    path("course/<int:id>/", views.CourseDetailView.as_view(), name="course_detail")
]
