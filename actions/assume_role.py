import boto3

from st2actions.runners.pythonrunner import Action


# pylint: disable=too-few-public-methods
class Boto3AssumeRoleRunner(Action):
    def run(self, role_arn, role_session_name, policy, duration, external_id, serial_number, token_code):
        client = boto3.client('sts')
        response = client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=role_session_name,
            Policy=policy,
            DurationSeconds=duration,
            ExternalId=external_id,
            SerialNumber=serial_number,
            TokenCode=token_code)
            
        print 'sts response', response
        return (True, response)
