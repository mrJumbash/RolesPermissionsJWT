from django.shortcuts import render, redirect
from django.views import View
from service.utils import ProductReviewsStatistic
import json
from django.core.serializers.json import DjangoJSONEncoder


class ReviewBarChartView(View):
    def get(self, request):
        if request.user.is_staff == True:
            labels = ProductReviewsStatistic.get_labels()
            data = ProductReviewsStatistic.get_data()
            context = {
                "labels": json.dumps(labels, cls=DjangoJSONEncoder),
                "data": json.dumps(data, cls=DjangoJSONEncoder),
            }
            return render(request, "admin/review_line_chart.html", context=context)

        else:
            return redirect("/")
