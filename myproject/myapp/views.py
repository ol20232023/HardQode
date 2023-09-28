from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Lesson, UserLesson
from .serializers import LessonSerializer, UserLessonSerializer, ProductStatSerializer

@api_view(['GET'])
@login_required
def lesson_list(request):
    user = request.user
    products = Product.objects.filter(owner=user)
    lessons = Lesson.objects.filter(products__in=products)
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
def lesson_detail(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id, owner=user)
    lessons = Lesson.objects.filter(products=product)
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
def product_stats(request):
    products = Product.objects.all()
    serializer = ProductStatSerializer(products, many=True)
    return Response(serializer.data)

