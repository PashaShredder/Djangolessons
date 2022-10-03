from rest_framework import serializers
from .models import Medicines


class MedicinesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicines
        fields = ('title', 'id', 'content')
