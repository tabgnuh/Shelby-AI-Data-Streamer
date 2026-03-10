# Shelby-AI-Data-Streamer

Open-source Python CLI tool to stream AI datasets from Shelby protocol for efficient ML training. Supports uploading, real-time streaming to PyTorch DataLoaders, and cryptographic verification using Aptos blockchain.

## Why This Tool?
Shelby is a decentralized hot storage protocol on Aptos, optimized for sub-second reads and AI workloads. This tool simplifies integration:
- Upload large datasets (e.g., images, tensors) to Shelby buckets.
- Stream data directly into ML models without full downloads.
- Verify data integrity with on-chain proofs.

Built to support Shelby ecosystem – apply for Early Access at [shelby.xyz](https://shelby.xyz) to test on testnet.

## Installation
1. Clone repo: `git clone https://github.com/yourusername/shelby-ai-data-streamer.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Install as package (optional): `pip install -e .`

## Usage
Run CLI with `python src/main.py [command]`

### Commands:
- **Upload**: `python src/main.py upload --file path/to/dataset.csv --bucket my-ai-bucket --endpoint https://testnet.shelby.xyz --access-key YOUR_ACCESS_KEY --secret-key YOUR_SECRET_KEY`
- **Stream**: `python src/main.py stream --bucket my-ai-bucket --object-key dataset.csv --endpoint https://testnet.shelby.xyz --access-key ... --secret-key ...`
  - Returns a PyTorch DataLoader for training.
- **Verify**: `python src/main.py verify --object-id OBJECT_HASH --aptos-node https://testnet.aptoslabs.com`

See `examples/demo_notebook.ipynb` for full demos.

## Configuration
- Get credentials from Shelby Early Access.
- For simulation (no access): Use `--simulate` flag to mock with local files.

## Contributing
Fork and PR! MIT License.

## License
MIT
