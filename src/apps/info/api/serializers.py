from rest_framework import serializers


from apps.info.models import InfoTodo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoTodo
        fields = (
            'title',
            'date_of_end',
            'created',
            'complete',
            'content',
        )