import csv
import pandas as pd
from django.core.management import BaseCommand
from django.db.models import Q

from musical_works.models import MusicalWork, Contributor


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('tools/works_metadata.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i, (title, contributors, iswc) in enumerate(csv_reader):
                if i == 0:
                    continue
                contributors = contributors.split('|')

                requested_mus_works = MusicalWork.objects.filter(
                    Q(iswc=iswc) | Q(title=title) | Q(
                        contributor__name__in=contributors)
                )
                if not requested_mus_works.exists():
                    m_work = MusicalWork.objects.create(iswc=iswc, title=title)
                    for c_name in contributors:
                        c = Contributor.objects.get_or_create(name=c_name)[0]
                        c.musical_works.add(m_work)
                else:
                    for m_work in requested_mus_works:
                        if not m_work.iswc and iswc:
                            m_work.iswc = iswc
                            m_work.save()
                        for c_name in contributors:
                            if not m_work.contributor_set.filter(
                                name=c_name
                            ).exists():
                                c = Contributor.objects.get_or_create(
                                    name=c_name
                                )[0]
                                m_work.contributor_set.add(c)
