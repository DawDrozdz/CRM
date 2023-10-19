from django.db import models


class QuerysetCategory(models.QuerySet):
    def query_state(self):
        return self.filter(choose='STATES').order_by('name')

    def query_motorcycle(self):
        return self.filter(choose='MOTORCYCLE').order_by('name')

    def query_show_aparment(self):
        return self.filter(meeting_type='SHOWING THE APARTMENT')

    def query_valuation(self):
        return self.filter(meeting_type='VALUATION OF RENOVATION')

    def query_inspect(self):
        return self.filter(meeting_type='CONSTRUCTION INSPECTION')

    def query_pick_up(self):
        return self.filter(meeting_type='PICKING UP THE MOTORCYCLE')


class ManagerCategory(models.Manager):
    def get_queryset(self):
        return QuerysetCategory(self.model, using=self._db)

    def motorcycle(self):
        return self.get_queryset().query_motorcycle()

    def state(self):
        return self.get_queryset().query_state()

    def show_apartment(self):
        return self.get_queryset().query_show_aparment()

    def valuation(self):
        return self.get_queryset().query_valuation()

    def inspect(self):
        return self.get_queryset().query_inspect()

    def pick_up(self):
        return self.get_queryset().query_pick_up()
