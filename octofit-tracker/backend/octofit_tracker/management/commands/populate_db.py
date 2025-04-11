from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Replace the truncate_table function with MongoDB-specific logic
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        def clear_collections():
            db['octofit_tracker_user'].drop()
            db['octofit_tracker_team'].drop()
            db['octofit_tracker_activity'].drop()
            db['octofit_tracker_leaderboard'].drop()
            db['octofit_tracker_workout'].drop()

        # Call clear_collections() at the start of the handle method
        clear_collections()

        # Create users
        users = [
            User.objects.create(email='thundergod@mhigh.edu', name='Thor'),
            User.objects.create(email='metalgeek@mhigh.edu', name='Tony Stark'),
            User.objects.create(email='zerocool@mhigh.edu', name='Steve Rogers'),
            User.objects.create(email='crashoverride@mhigh.edu', name='Natasha Romanoff'),
            User.objects.create(email='sleeptoken@mhigh.edu', name='Bruce Banner'),
        ]

        # Create teams
        team_blue = Team(name='Blue Team')
        team_blue.members = [user.id for user in users]
        team_blue.save()

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60),
            Activity(user=users[1], activity_type='Crossfit', duration=120),
            Activity(user=users[2], activity_type='Running', duration=90),
            Activity(user=users[3], activity_type='Strength', duration=30),
            Activity(user=users[4], activity_type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100),
            Leaderboard(user=users[1], score=90),
            Leaderboard(user=users[2], score=95),
            Leaderboard(user=users[3], score=85),
            Leaderboard(user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))