from django.db import models

# Create your models here.
# In our research software we have task objects that a user has to complete, each task has a title, an order field,
# a description and a type (such as survey, discussion, diary).
# We group tasks together in a container which we call a tile. Each tile has a launch date and a status.
# The status can be either live, pending or archived. A tile can be made up of one or many tasks.
# A task can only belong to a single tile.

# Task
# - title
# - order field
# - type (survey, discussion, diary)
# - tile.id

# Tile
# - launch date
# - status (live, pending, archived)


class Tile(models.Model):
    CHOICES = {
        0: 'live',
        1: 'pending',
        2: 'archived'
    }
    launch_date = models.DateField()
    status = models.PositiveSmallIntegerField(choices=CHOICES.items())

    def __str__(self):
        return f'Tile created at {self.launch_date.strftime("%Y-%m-%d")} - {self.CHOICES[self.status]}'


class Task(models.Model):
    CHOICES = {
        0: 'survey',
        1: 'discussion',
        2: 'diary'
    }

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    type = models.PositiveSmallIntegerField(choices=CHOICES.items())
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.CHOICES[self.type]}]:{self.title}'
