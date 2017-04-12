import boto3

from st2actions.runners.pythonrunner import Action


# pylint: disable=too-few-public-methods
class Boto3ActionRunner(Action):
    def run(self, service, region, action_name, kwargs):
        client = boto3.client(service, region_name=region)
        if kwargs is not None:
            response = getattr(client, action_name)(**kwargs)
        else:
            response = getattr(client, action_name)()
        return (True, response)
