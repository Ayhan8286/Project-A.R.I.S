# 🛠️ GTM Engine Troubleshooting Guide

This guide helps you resolve common issues when running the GTM Engine.

## 1. Docker Permission Errors

**Error:** `permission denied while trying to connect to the Docker daemon socket`

**Cause:** Your user is not in the `docker` group.

**Solution:**
Run the following command and then **log out and log back in**:
```bash
sudo usermod -aG docker $USER
newgrp docker
```

## 2. Port Conflicts

**Error:** `Bind for 0.0.0.0:5432 failed: port is already allocated`

**Cause:** Another service (like a local Postgres installation) is using the port.

**Solution:**
Stop the conflicting service or find what's using the port:
```bash
sudo lsof -i :5432
```
Kill the process (replace `<PID>` with the Process ID):
```bash
kill -9 <PID>
```

## 3. Ollama Connection Failed

**Error:** `Connection refused` when connecting to `http://gtm_ollama:11434` or `localhost:11434`.

**Cause:** The Ollama container might not be running or the model isn't pulled.

**Solution:**
1. Check if the container is running:
   ```bash
   docker ps | grep ollama
   ```
2. Pull the model manually if needed:
   ```bash
   docker exec -it gtm_ollama ollama pull llama3
   ```

## 4. Missing API Keys

**Error:** Agents fail with `ValueError: API Key not found`.

**Solution:**
Ensure you have edited your `.env` file in the root directory and added your `GROQ_API_KEY`.

## 5. Python Dependencies

**Error:** `ModuleNotFoundError: No module named 'redis'` (or similar).

**Solution:**
Re-run the setup script to ensure all requirements are installed:
```bash
./setup.sh
```
