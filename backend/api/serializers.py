"""Import."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Class."""

    class Meta:
        """Class."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
