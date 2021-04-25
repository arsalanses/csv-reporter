from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import RegisterReport
from .models import Member
import csv


def report(request):
    if request.method == "GET":
        form = RegisterReport()
        return render(request, 'register_report.html', context={'form': form})

    if request.method == "POST":
        form = RegisterReport(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            response = HttpResponse(content_type='text/csv')
            writer = csv.writer(response)
            writer.writerow(['_id', 'signup', 'points', 'name'])
            # members = Member.objects.filter(signup__gt=start_date.date(), signup__lt=end_date.date())
            members = Member.objects.filter(name='Nick')
            for member in members:
                writer.writerow(member)
            response['Content-Disposition'] = 'attachment; filename="members.csv"'
            return response

        return JsonResponse({"status": "error"})
