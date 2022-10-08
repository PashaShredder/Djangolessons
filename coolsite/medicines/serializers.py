import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

import medicines
from .models import Medicines


# class MedicinesModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class MedicinesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    content = serializers.CharField()
    photo = serializers.ImageField()
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_published = serializers.BooleanField(default=True)
    cat = serializers.PrimaryKeyRelatedField(read_only=True)


    # # преобразование(кодирование) объектов MedicinesModel в json (JSONRenderer преобразовывает в байтовую строку для дальнейшего парсинга)
    # def encode():
    #     model = MedicinesModel('Tavegil', 'Content:  Tavegil')
    #     model_serializer = MedicinesSerializer(model)
    #     print(model_serializer.data, type(model_serializer.data), sep='\n')
    #     json = JSONRenderer().render(model_serializer.data)
    #     print(json)
    #
    # # декодирование поступающего потока (запроса) и чтение json
    # def decode():
    #     stream = io.BytesIO(b'{"title":"Tavegil", "content":"Content :Tavegil "}')
    #     data = JSONParser().parse(stream)
    #     serializer = MedicinesSerializer(data=data)
    #     serializer.is_valid()
    #     print(serializer.validated_data)
    class Meta:
        model = Medicines
        # fields = "__all__"
        fields = ['title',
                  'slug',
                  'content',
                  'photo',
                  'time_create',
                  'time_update',
                  'is_published',
                  'cat'
                  ]
