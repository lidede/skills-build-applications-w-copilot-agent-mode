from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='marvel')
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='marvel')
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc')
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc')

        # Activities
        Activity.objects.create(user=tony.name, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve.name, type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce.name, type='swim', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark.name, type='yoga', duration=20, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='medium')
        Workout.objects.create(name='Burpees', description='Do 10 burpees', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
