# AWS Tagger

AWS Tagger is a serverless application tool designed to automatically tag AWS resources that are missing the `Name` tag. By ensuring that all resources are properly tagged, this project helps improve cost visibility, resource organization, and cost optimization.

## Overview

In AWS, tagging resources is a best practice for managing and organizing your cloud infrastructure. Tags allow you to:
- Track costs by resource.
- Identify unused or underutilized resources for cost optimization.
- Improve resource discoverability and management.

AWS Tagger automates the process of tagging some resources, ensuring that every resource has a `Name` tag on it. This is particularly useful for maintaining consistent tagging across your AWS environment.

## Use Cases

- **Cost Management**: Gain better insights into how costs are distributed across your AWS resources.
- **Resource Organization**: Ensure all resources are consistently tagged for easier management.
- **Cost Optimization**: Identify resources that may be underutilized or unnecessary.

## Resources Supported
- AWS Lambda Functions
- AWS S3 Buckets

## Getting Started

### Prerequisites

- AWS account
- Python 3.12 (you can change the version in the template.yaml file)
- AWS SAM CLI installed and configured.

### Deployment
1. Edit the `samconfig.toml` file to set your AWS region and other configurations.
2. Edit the `scripts` folder to set the correct profile for your AWS account.
3. run `./scripts/sync.sh` to sync your local serverless application changes to the AWS Cloud **OR** `./scripts/deploy.sh` to deploy it.

## Contributing
Contributions are welcome!
I did this project to address a personal need, but I believe it can be useful to others as well. If you find this project helpful, please consider contributing to its development by adding support to new resources or improving existing ones. Feel free to open an issue or submit a PR =)