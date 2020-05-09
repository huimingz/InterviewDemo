#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Date: 2020/05/09
# Author: huimingz
# Contact: huimingz12@outlook.com

from rest_framework import serializers

from Foo import models


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = "__all__"
        extra_kwargs = {
            "type": {"source": "type_name", "read_only": True}
        }


class UnitDetailSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(source="chapter_set", many=True, read_only=True)

    class Meta:
        model = models.Unit
        fields = (
            "id",
            "name",
            "planning_des",
            "course",
            "chapters",
            "is_active",
            "create_at",
            "update_at",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class GiftCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GiftCategory
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = models.Course
        fields = "__all__"
        read_only_fields = ("id",)
        extra_kwargs = {
            "url": {"source": "mobile_url", "read_only": True},
            "type": {"source": "type_name", "read_only": True}
        }


class CourseDetailSerializer(serializers.ModelSerializer):
    units = UnitDetailSerializer(source="unit_set", many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    gift_category = CategorySerializer(read_only=True)

    class Meta:
        model = models.Course
        fields = (
            "id",
            "title",
            "type",
            "basic_introduce",
            "detail",
            "first_price",
            "real_price",
            "units",
            "pic",
            "thumbnail",
            "fake_people",
            "has_free_chapter",
            "share",
            "url",
            "recomment_times",
            "recomment_look_times",
            "course_index",
            "is_coding",
            "is_active",
            "create_at",
            "update_at",
            "category",
            "parent_course",
            "gift_category",

        )
        read_only_fields = ("id",)
        extra_kwargs = {
            "url": {"source": "mobile_url", "read_only": True},
            "type": {"source": "type_name", "read_only": True}
        }
