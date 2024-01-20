from tastypie.resources import ModelResource
from shop.models import Category, Course
from shop.models import Category, Course

# Create your models here.


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()  # Use `queryset` instead of `query`
        resource_name = 'categories'
        allowed_methods = ['get']

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()  # Use `queryset` instead of `query`
        resource_name = 'course'
        allowed_methods = ['get', 'delete', 'post']


