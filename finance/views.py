from django.shortcuts import render
from django.http import HttpResponse
def feeCollection(Request):
    return HttpResponse("I will collect fee")


def feeDuesReport(Request):
    return HttpResponse("I will get fee dues report")

def collectionReport(request):
    return HttpResponse("This is collection report page.")

