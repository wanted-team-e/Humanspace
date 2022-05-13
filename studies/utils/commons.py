from django.db.models import Q


class RequestHandler:
    def _request_param(self, request):
        """
            작성자 : 강정희
            파라미터 값 변수화
        """
        data = request.GET.get

        title = data('title', None)
        number = data('number', None)
        institute = data('institute', None)

        return title, number, institute

    def set_query(self, request):
        """
            작성자 : 강정희
            파라미터 기반 base query 작성
        """

        title, number, institute = self._request_param(request)

        query = Q()

        if title:
            query &= Q(title__icontains=title)
        if number:
            query &= Q(number__icontains=number)
        if institute:
            query &= Q(institute__name__icontains=institute)

        return query

    def has_weekly(self, request):
        """
            작성자 : 강정희
            파라미터 중 'weekly' 값 확인
        """
        weekly = request.GET.get('weekly', None)

        return weekly

    def offset_limit_paginator(self, request):
        """
            작성자 : 강정희
            pagination을 위한 offset, limit 변수화
        """
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 5))

        return offset, limit
