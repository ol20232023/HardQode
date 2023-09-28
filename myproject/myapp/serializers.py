from rest_framework import serializers
from .models import Lesson, Product, UserLesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'video_link', 'duration']


class UserLessonSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = UserLesson
        fields = ['lesson', 'viewed_time', 'status']


class ProductStatSerializer(serializers.ModelSerializer):
    num_viewed_lessons = serializers.SerializerMethodField()
    total_viewing_time = serializers.SerializerMethodField()
    num_users = serializers.SerializerMethodField()
    percent_purchased = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'num_viewed_lessons', 'total_viewing_time', 'num_users', 'percent_purchased']

    def get_num_viewed_lessons(self, obj):
        return UserLesson.objects.filter(lesson__products=obj, status='Viewed').count()

    def get_total_viewing_time(self, obj):
        viewed_lessons = UserLesson.objects.filter(lesson__products=obj, status='Viewed')
        total_time = sum(lesson.viewed_time for lesson in viewed_lessons)
        return total_time

    def get_num_users(self, obj):
        return obj.owner.count()

    def get_percent_purchased(self, obj):
        total_users = User.objects.count()
        num_purchased = obj.owner.count()
        return (num_purchased / total_users) * 100 if total_users > 0 else 0
