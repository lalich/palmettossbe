from .models import (School, SSS)
from rest_framework import serializers

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'school_photo', 'state', 'zip_code', 'security_description')

class SSSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SSS
        fields = ('id', 'first_name', 'last_name', 'sss_photo', 'years_experience', 'description', 'specialty', 'state', 'zip_code')
