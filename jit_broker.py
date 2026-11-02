import boto3
import json

def issue_temporary_access(role_arn: str, engineer_name: str, duration_minutes: int):
    # AWS STS minimum duration is 15 minutes (900 seconds)
    duration_seconds = max(900, duration_minutes * 60)
    
    sts_client = boto3.client('sts')
    
    print(f"[*] Requesting temporary credentials for {engineer_name}...")
    
    # This call creates the temporary keycard
    response = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName=f"JIT-{engineer_name}",
        DurationSeconds=duration_seconds
    )
    
    credentials = response['Credentials']
    
    print("\n--- TEMPORARY ACCESS GRANTED ---")
    print(f"Expires at: {credentials['Expiration']}")
    print("\n--- RUN THESE 3 COMMANDS IN POWERSHELL ---")
    print(f'$env:AWS_ACCESS_KEY_ID="{credentials["AccessKeyId"]}"')
    print(f'$env:AWS_SECRET_ACCESS_KEY="{credentials["SecretAccessKey"]}"')
    print(f'$env:AWS_SESSION_TOKEN="{credentials["SessionToken"]}"')
    print("-------------------------------------------\n")
    return credentials

if __name__ == "__main__":
    # Put your Role ARN here
    ROLE_ARN = "arn:aws:iam::1234567891011:role/Target-S3Reader-Role"
    
    # Simulate a request: Alice needs 15 minutes to inspect S3 buckets
    issue_temporary_access(
        role_arn=ROLE_ARN,
        engineer_name="Alice",
        duration_minutes=15
    )