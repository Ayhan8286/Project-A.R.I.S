# Milestone 6: Senses (Vision, Voice, Local Intelligence)

This directory contains the "Senses" configuration for the project, focusing on local intelligence and multimedia capabilities.

## System Requirements

To ensure the voice engine functions correctly, the following packages must be installed on your Linux system:

*   `ffmpeg`
*   `espeak-ng`

You can install them using:

```bash
sudo apt-get install -y ffmpeg espeak-ng
```

## "Hybrid" Approach

We have adopted a hybrid approach for this milestone. Instead of running dedicated Docker containers for TTS (Text-to-Speech) and OCR (Optical Character Recognition) due to registry instability, we are handling these tasks directly in Python using the `coqui-tts` library and `torchcodec`.

## Local Brain (Ollama)

The infrastructure now includes an `ollama` service running on port `11434`. This acts as the "Local Brain" for our AI agents.

### Running the Local Brain Script

1.  Ensure the Docker containers are running (specifically `ollama`).
2.  Pull the required model in Ollama:
    ```bash
    docker compose exec ollama ollama pull llama3
    ```
3.  Run the python script:
    ```bash
    python3 06-Senses/local_brain.py
    ```

This script demonstrates how to connect a CrewAI agent to the local Ollama instance using the "Imposter" strategy (mimicking the OpenAI API).
