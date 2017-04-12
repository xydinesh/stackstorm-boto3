import boto3

from st2actions.runners.pythonrunner import Action


# pylint: disable=too-few-public-methods
class Boto3ActionRunner(Action):
    def run(self, service, action, kwargs):
        print service, action, kwargs
        return (True, "")
