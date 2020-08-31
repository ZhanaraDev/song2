import pandas as pd
from django.core.management import BaseCommand
from musical_works.models import MusicalWork, Contributor

CSV_FILE_PATH = 'tools/works_metadata.csv'


def reconcile_musical_works():
    df = pd.read_csv(CSV_FILE_PATH, sep=',')
    group_by_iswc = df.groupby(['iswc', 'title'])['contributors'].apply(
        lambda x: '|'.join(x)
    ).reset_index()
    for i, title in enumerate(group_by_iswc['title']):
        songs_with_same_title = df[df['title'] == title]
        if songs_with_same_title['title'].count() <= 1:
            continue

        for contributors in songs_with_same_title['contributors']:
            contributors_by_iswc = set(
                group_by_iswc['contributors'][i].split('|')
            )
            contributors_by_title = set(contributors.split('|'))

            if contributors_by_iswc & contributors_by_title:
                group_by_iswc['contributors'][i] = '|'.join(
                    contributors_by_iswc | contributors_by_title
                )

    return group_by_iswc.to_dict('records')


class Command(BaseCommand):

    def handle(self, *args, **options):
        reconciled_data = reconcile_musical_works()

        for document in reconciled_data:
            m_work = MusicalWork.objects.get_or_create(
                iswc=document['iswc'], title=document['title']
            )[0]
            for c_name in document['contributors'].split('|'):
                c = Contributor.objects.get_or_create(name=c_name)[0]
                if not c.musical_works.filter(id=m_work.id).exists():
                    c.musical_works.add(m_work)
