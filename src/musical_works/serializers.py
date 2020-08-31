from rest_framework import serializers

from musical_works.models import MusicalWork

from musical_works.models import Contributor


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ('name', )


class MusicalWorkSerializer(serializers.ModelSerializer):
    contributors = serializers.SerializerMethodField()

    def get_contributors(self, obj):
        return ContributorSerializer(
            obj.contributor_set.all(), many=True
        ).data

    class Meta:
        model = MusicalWork
        fields = (
            'iswc', 'title', 'lyrics', 'duration_in_seconds', 'contributors',
        )
