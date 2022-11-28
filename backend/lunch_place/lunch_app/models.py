from django.db import models
import uuid as uuid
import json


class LunchBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True  # Set this model as Abstract


class Restaurant(LunchBaseModel):

    name = models.CharField(null=False, max_length=200)
    address = models.CharField(null=False, blank=False, max_length=200)
    phone_number = models.CharField(null=False, blank=False, max_length=15)

    @property
    def description(self):
        return f"The {self.name} restaurant address is {self.address}, phone {self.phone_number}"

    def __str__(self):
        return self.description


class Employe(LunchBaseModel):

    first_name = models.CharField(null=False, max_length=200)
    last_name = models.CharField(null=False, max_length=200)
    email = models.EmailField(null=False, max_length=100, unique=True, db_index=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name


class Menu(LunchBaseModel):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.JSONField(default=dict, blank=False, null=False)

    @property
    def vote_count(self):
        return self.votes.count()

    @property
    def preferences(self):
        return self.menu and json.loads(self.menu)

    @preferences.setter
    def preferences(self, preferences_dict):
        self.menu = json.dumps(preferences_dict) if preferences_dict else None


class Vote(LunchBaseModel):
    menu = models.ForeignKey(Menu, related_name="votes", on_delete=models.CASCADE)
    voted_by = models.ForeignKey(Employe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("menu", "voted_by")
