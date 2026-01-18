# Open Responses Python Samples

This repository contains Python code samples demonstrating the [Open Responses](https://openresponses.org/) specification.

## Overview

Open Responses is an open specification for AI model interactions that provides a unified interface for working with language models. These samples show how to use the Open Responses API with Python and the OpenAI client library.

## Quick Start with GitHub Codespaces

The quickest way to get started is using GitHub Codespaces, a hosted environment that is automatically set up for you. Click this button to create a Codespace (4-core machine recommended):

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=guygregory/open-responses-python-samples)

Wait for the Codespace to initialize. Python 3.12, Python extension, and dependencies will be automatically installed. For an even more streamlined experience, add the environment variables into your [Codespace user secrets](https://github.com/settings/codespaces).

## Samples

This repository includes the following examples:

### Basic Usage
- **`openresponses-basic.py`** - Simple text generation request

### Advanced Features
- **`openresponses-reasoning.py`** - Using reasoning capabilities with summary extraction
- **`openresponses-structured.py`** - Structured JSON output with schema validation
- **`openresponses-function-weather.py`** - Function calling with tool execution

### Streaming
- **`openresponses-stream-async.py`** - Asynchronous streaming with async/await
- **`openresponses-stream-sse.py`** - Server-Sent Events (SSE) streaming

## Prerequisites

- Python 3.7 or higher
- OpenAI Python client library
- A running inference server compatible with Open Responses (e.g., Ollama)

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Setup

These samples are configured to connect to a local Ollama server. Make sure you have:

1. Ollama installed and running on `http://localhost:11434`
2. The required models downloaded:
   - `gpt-oss:20b` - Used by most samples (basic, reasoning, structured, function calling)
   - `phi4-reasoning` - Used by streaming samples

To pull the models with Ollama:
```bash
ollama pull gpt-oss:20b
ollama pull phi4-reasoning
```

## Usage

Run any sample directly with Python:

```bash
python openresponses-basic.py
```

Each sample is self-contained and demonstrates a specific feature of the Open Responses specification.

## Configuration

All samples use the following default configuration:
- **Base URL**: `http://localhost:11434/v1/`
- **API Key**: `ollama` (required by the OpenAI client library but not used for authentication by Ollama - can be any string)

You can modify these settings in each sample file to connect to different Open Responses-compatible servers.

## Learn More

- [Open Responses Specification](https://openresponses.org/)
- [OpenAI Python Client](https://github.com/openai/openai-python)
- [Ollama](https://ollama.ai/)

## License

These samples are provided as examples for working with the Open Responses specification.
