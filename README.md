# SWE-Bridge 🔄

🔄 SWE-Bridge – Bridge agent outputs into [SWE-Bench](https://github.com/SWE-bench/SWE-bench) submission-ready formats for standardized benchmarking across different agents

A lightweight Python utility that converts various AI agent outputs into standardized SWE-Bench submission formats, enabling consistent evaluation and comparison across different agent implementations.

> **Note**: This project is a fork of [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent), enhanced with additional submission bridging capabilities for SWE-Bench evaluation.

## ✨ Key Features

- **🔄 Format Conversion**: Automatically convert agent outputs to SWE-Bench submission format
- **🎯 Multi-Environment Support**: Works with local and Docker environments
- **📊 Standardized Output**: Generate consistent submission data for benchmarking
- **🔧 Easy Integration**: Simple interface for integrating with existing agent systems
- **📝 Flexible Configuration**: Support for various model configurations and environments
- **⚡ Lightweight**: Minimal dependencies, focused on core bridging functionality

## 🚀 Quick Start

### Installation

#### From Source
```bash
# Clone the repository
git clone https://github.com/yourusername/SWE-bridge.git
cd SWE-bridge

# Install dependencies
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

**Dependencies:**
- Python 3.10+
- minisweagent
- python-dotenv
- rich
- typer
- litellm
- tenacity

### Basic Usage

```python
from bridge import SWEBenchSubmissionBridger
import yaml
import datasets

# Load configuration
with open('./minisweagent/config/default.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Set default values if not present
if not 'model_name' in config.get('model', {}):
    config['model']['model_name'] = 'gpt-4o'
if not 'cwd' in config.get('environment', {}):
    config['environment']['cwd'] = '/testbed'

# Load dataset
dataset_name_or_path = 'princeton-nlp/SWE-bench_Verified'
split = 'test[:1]'
dataset = datasets.load_dataset(dataset_name_or_path, split=split)

# Create bridger and format submission
instance = dataset[0]
formatter = SWEBenchSubmissionBridger()
submission_data = formatter.format_submission(instance, config)

# Display results
for key, value in submission_data.items():
    print(f'{key:<50}: {value}')
```

## 📖 Configuration

The bridge supports various configuration options through the [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) config system:

```yaml
model:
  model_name: "gpt-4o"
  # Other model-specific configurations

environment:
  cwd: "/testbed"
  # Environment-specific settings
```

## 🧪 Testing

```bash
# Run the bridge directly
python src/bridge.py

# This will process a sample instance and display the formatted output
```

## 📚 API Reference

### SWEBenchSubmissionBridger Class

```python
class SWEBenchSubmissionBridger:
    def format_submission(
        self,
        instance: dict,
        config: dict,
    ) -> dict
```

**Parameters:**
- `instance`: SWE-Bench instance data containing problem information
- `config`: Configuration dictionary for model and environment settings

**Returns:**
- Dictionary containing formatted submission data with keys:
  - `instance_id`: The unique identifier for the instance
  - `model_name_or_path`: The name or path of the model used
  - `model_patch`: The git patch representing the model's solution

### Environment Support

The bridge automatically handles:
- Local environment execution
- Docker container execution
- Environment-specific configuration
- Automatic environment detection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔮 Future Work

Our vision is to create a **universal wrapper** that can seamlessly integrate with various AI agents, providing a complete end-to-end pipeline for [SWE-Bench](https://github.com/SWE-bench/SWE-bench) submissions:

- **🔄 Universal Agent Integration**: Develop a standardized interface that can wrap around any agent implementation
- **📥 Pre-processing Pipeline**: Automatically handle input formatting, environment setup, and configuration management
- **📤 Post-processing Pipeline**: Standardize outputs, generate git patches, and format submissions for SWE-Bench

This would make SWE-Bench evaluation accessible to the entire AI agent ecosystem, enabling standardized benchmarking across different frameworks and implementations.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built on top of the excellent [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) project
- Designed for standardized AI agent benchmarking
- Thanks to the SWE-Bench team for creating the evaluation framework

---

Made with ❤️ for the AI agent benchmarking community
