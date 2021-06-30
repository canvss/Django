from django.test import TestCase

# Create your tests here.
from polls.models import Subject


subject1 = Subject(name='Python', intro='当下热门的学科',is_hot=True)
subject1.save()
