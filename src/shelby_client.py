import boto3
import io
import torch
from torch.utils.data import Dataset, DataLoader
from aptos_sdk.client import RestClient  # Aptos SDK for verification
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class ShelbyClient:
    def __init__(self, endpoint, access_key, secret_key, aptos_node_url="https://testnet.aptoslabs.com"):
        self.s3 = boto3.client(
            's3',
            endpoint_url=endpoint,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        self.aptos_client = RestClient(aptos_node_url)
        self.bucket = None

    def set_bucket(self, bucket):
        self.bucket = bucket

    def upload_file(self, file_path, object_key):
        with open(file_path, 'rb') as f:
            self.s3.upload_fileobj(f, self.bucket, object_key)
        print(f"Uploaded {file_path} to {self.bucket}/{object_key}")

    def stream_object(self, object_key):
        response = self.s3.get_object(Bucket=self.bucket, Key=object_key)
        return response['Body'].read()  # For streaming, can use .iter_lines() for large files

    def verify_proof(self, object_id):
        # Giả định Shelby có module on-chain để verify (thay bằng thực tế từ docs)
        # Query Aptos ledger for proof
        try:
            # Example: Query a hypothetical Shelby module
            module = "0x...::shelby::verify_object"  # Thay bằng address thực của Shelby module
            payload = {
                "function": module,
                "type_arguments": [],
                "arguments": [object_id]
            }
            result = self.aptos_client.view(payload)
            if result[0]:  # Assume returns bool
                print("Verification successful!")
                return True
            else:
                print("Verification failed.")
                return False
        except Exception as e:
            print(f"Error verifying: {e}")
            return False

class ShelbyDataset(Dataset):
    def __init__(self, client, object_key):
        self.client = client
        self.data = self.client.stream_object(object_key).decode('utf-8').splitlines()  # Example for CSV

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # Parse line to tensor (customize for your data)
        line = self.data[idx]
        # Example: simple float tensor
        return torch.tensor([float(x) for x in line.split(',')])
