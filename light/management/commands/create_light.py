from django.core.management.base import BaseCommand, CommandError
from light.models import Light
import random


class Command(BaseCommand):


    def handle(self, *args, **options):
        Light.objects.all().delete()
        for x in range(0, 10):

            r = lambda: random.randint(0,255)
            randColor = '#%02X%02X%02X' % (r(),r(),r())

            randState = random.choice([True, False])

            Light.objects.create(

                color = randColor,
                state =  randState

            )
      
