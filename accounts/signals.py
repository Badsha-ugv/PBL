from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.contrib.auth.models import User, Group
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        # if instance.is_staff:
        # # Get or create the "contributor" group
        #     contributor_group, created = Group.objects.get_or_create(name='Contributors')

        #     # Add the user to the "contributor" group
        #     instance.groups.add(contributor_group)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

