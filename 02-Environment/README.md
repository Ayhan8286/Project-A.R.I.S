# Milestone 2: Environment Setup

This directory contains scripts to set up the environment on the infrastructure provisioned in Milestone 1.

**Prerequisite: Complete Milestone 01**

## Instructions

### 1. Copy the Install Script to the Server

You can copy the `install_docker.sh` script to your server using `scp` (Secure Copy Protocol) or by copy-pasting the content.

**Option A: Using SCP**

Run the following command from your local machine, replacing `[EXTERNAL_IP]` with the external IP address of your VM instance (from Milestone 1 output):

```bash
scp -i /path/to/your/ssh/key 02-Environment/install_docker.sh USERNAME@[EXTERNAL_IP]:~/install_docker.sh
```

**Option B: Copy-Paste**

1.  SSH into your server:
    ```bash
    ssh -i /path/to/your/ssh/key USERNAME@[EXTERNAL_IP]
    ```
2.  Create a new file:
    ```bash
    nano install_docker.sh
    ```
3.  Copy the content of `install_docker.sh` from this repository and paste it into the editor.
4.  Save and exit (Ctrl+O, Enter, Ctrl+X).

### 2. Run the Install Script

Once the script is on your server, make it executable and run it:

```bash
chmod +x install_docker.sh
./install_docker.sh
```

## Common Errors

### Docker Daemon Permission Error

**Error Message:**
`Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?` or `permission denied while trying to connect to the Docker daemon socket`

**Cause:**
The current user has not been added to the `docker` group, or the group membership changes haven't taken effect in the current session.

**Solution:**
The install script attempts to add the user to the group, but you must refresh your group membership.

Run the following command:

```bash
newgrp docker
```

Alternatively, you can **logout and login** again to your SSH session.
