
from django.core.management.base import BaseCommand
from django.db.models import Count
from profiles.models import Profile, Note
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Commands displays all models and counts its instances'
  
    def handle(self, *args, **kwargs):
        for ct in ContentType.objects.all():
            m = ct.model_class()
            print('Model: ' + m.__name__ + '  ---- Obj qnty: ' +  str(m._default_manager.count()))