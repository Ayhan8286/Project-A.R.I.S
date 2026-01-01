# Milestone 1: Infrastructure

This directory contains the Terraform code to provision the infrastructure for Milestone 1.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed.
- A Google Cloud Platform (GCP) project.
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed and configured with your project.

## Instructions

1.  **Navigate to the infrastructure directory:**

    ```bash
    cd 01-Infrastructure
    ```

2.  **Initialize Terraform:**

    This command initializes the working directory containing Terraform configuration files.

    ```bash
    terraform init
    ```

3.  **Update the Project ID:**

    Open `main.tf` and replace `your-project-id` with your actual Google Cloud Project ID.

    ```hcl
    provider "google" {
      project = "your-actual-project-id"
      ...
    }
    ```

4.  **Plan the infrastructure:**

    This command creates an execution plan, which lets you preview the changes that Terraform will make to your infrastructure.

    ```bash
    terraform plan
    ```

5.  **Apply the changes:**

    This command executes the actions proposed in a Terraform plan.

    ```bash
    terraform apply
    ```

    Type `yes` when prompted to confirm.

## Resources Provisioned

-   **Google Compute Instance:**
    -   Name: `milestone1-vm`
    -   Machine Type: `e2-standard-8` (8 vCPUs, 32 GB memory)
    -   Image: `debian-cloud/debian-11`
    -   Region: `us-central1`
    -   Zone: `us-central1-a`

## Clean Up

To destroy the infrastructure created by Terraform:

```bash
terraform destroy
```
