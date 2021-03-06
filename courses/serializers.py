from rest_framework.serializers import ModelSerializer
from courses.models import Course


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseNameSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', )

