from django.core.management.base import BaseCommand

from claimspy.models import Tier

class Command(BaseCommand):
    help = "Create tiers in the database if they do not exist."

    def handle(self, *args, **options):
        Tier.objects.get_or_create(name="Free", max_request=100)
        Tier.objects.get_or_create(name="Pro", max_request=1000)
        Tier.objects.get_or_create(name="Enterprise", max_request=10000)