from django.db import models
import json
from django.core import serializers


# Create your managers here.
class SlackCredManager(models.Manager):

    def get_token_for_team(self, team_id):
        creds = self.filter(team_id=team_id).all()

        if creds:
            cred = json.loads(serializers.serialize('json', [cred for cred in creds]))
            return cred[0]["fields"]["bot_communication_token"]
        else:
            return None

    def create_token_for_team(self,team_id,workspace_name,bot_communication_token):
        try:
            self.create(team_id=team_id,workspace_name=workspace_name,bot_communication_token=bot_communication_token)
            return True
        except Exception as e:
            print("error creating token for team %s", e)
            return False

    def delete_token_for_team(self,team_id):
        try:
            return self.filter(team_id=team_id).delete()
        except Exception as e:
            print("error deleting token for team ", e)
            return False


# Create your models here.
class SlackCred(models.Model):

    class Meta:
        db_table = "log_slack_team"

    log_slack_team_id = models.AutoField(primary_key=True)
    team_id = models.CharField(max_length=100, blank=False, null=False, unique=True)
    workspace_name = models.CharField(max_length=1000, blank=False, null=False)
    bot_communication_token = models.CharField(max_length=1000, blank=False, null=False)
    objects = SlackCredManager()