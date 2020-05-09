#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Date: 2020/05/09
# Author: huimingz
# Contact: huimingz12@outlook.com

from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class FooPageNumberPagination(PageNumberPagination):
    """自定义参数信息格式"""

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('code', 200),
            ('message', 'SUCCESS'),
            ('data', data)
        ]))
