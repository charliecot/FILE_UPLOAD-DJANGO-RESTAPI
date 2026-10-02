from rest_framework import serializers
from .models import User
from django.utils import timezone

class CVUploadSerializer(serializers.ModelSerializer):
    upload_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = User
        fields = ['cv','upload_at']

    def update(self,instance,validated_data):
        print("UPDATE METHOD CALLED")

        instance.cv=validated_data.get('cv',instance.cv)
        instance.upload_at = timezone.now()
        
        instance.save()
        print("SAVED:", instance.upload_at)

        return instance
