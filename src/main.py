import click
from shelby_client import ShelbyClient, ShelbyDataset
from utils import get_dataloader

@click.group()
def cli():
    pass

@cli.command()
@click.option('--file', required=True, help='Path to file to upload')
@click.option('--bucket', required=True, help='Shelby bucket name')
@click.option('--object-key', default=None, help='Object key (default: filename)')
@click.option('--endpoint', required=True, help='Shelby S3 endpoint')
@click.option('--access-key', required=True, help='Access key')
@click.option('--secret-key', required=True, help='Secret key')
def upload(file, bucket, object_key, endpoint, access_key, secret_key):
    client = ShelbyClient(endpoint, access_key, secret_key)
    client.set_bucket(bucket)
    object_key = object_key or file.split('/')[-1]
    client.upload_file(file, object_key)

@cli.command()
@click.option('--bucket', required=True, help='Shelby bucket name')
@click.option('--object-key', required=True, help='Object key to stream')
@click.option('--endpoint', required=True, help='Shelby S3 endpoint')
@click.option('--access-key', required=True, help='Access key')
@click.option('--secret-key', required=True, help='Secret key')
@click.option('--batch-size', default=32, help='Batch size for DataLoader')
def stream(bucket, object_key, endpoint, access_key, secret_key, batch_size):
    client = ShelbyClient(endpoint, access_key, secret_key)
    client.set_bucket(bucket)
    dataset = ShelbyDataset(client, object_key)
    dataloader = get_dataloader(dataset, batch_size)
    print("DataLoader ready! Example batch:")
    for batch in dataloader:
        print(batch)
        break  # Just print first batch for demo

@cli.command()
@click.option('--object-id', required=True, help='Object ID/hash to verify')
@click.option('--aptos-node', default='https://testnet.aptoslabs.com', help='Aptos node URL')
def verify(object_id, aptos_node):
    client = ShelbyClient(None, None, None, aptos_node)  # No S3 needed for verify
    client.verify_proof(object_id)

if __name__ == '__main__':
    cli()
