from .models import *
from rest_framework import serializers
#from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Users
       fields = ['fam', 'name', 'otc', 'email', 'phone']