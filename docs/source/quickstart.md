# Quickstart

Get your first momo-kiji compilation working in 5 minutes.

## Before You Start

Make sure you've [installed momo-kiji](installation.md).

## 1. Create a Simple Model

First, create a basic neural network and export it to ONNX format.

```python
import torch
import torch.nn as nn

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 4)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Create and export model
model = SimpleModel()
dummy_input = torch.randn(1, 10)
torch.onnx.export(model, dummy_input, "simple_model.onnx")
print("✓ Model exported to simple_model.onnx")
```

## 2. Compile to ANE

```python
import momo_kiji as mk

# Compile the model for ANE
mk.compile(
    input_path="simple_model.onnx",
    target="ane",
    output_path="simple_model_ane.mlmodel",
    optimization_level="high"
)
print("✓ Model compiled to ANE format")
```

## 3. Use in Your App

### Python

```python
import momo_kiji as mk

# Load the compiled model
model = mk.load("simple_model_ane.mlmodel")

# Prepare input (must match training shape)
import numpy as np
input_data = np.random.randn(1, 10).astype(np.float32)

# Run inference
output = model.predict(input_data)
print(f"Output shape: {output.shape}")
print(f"Output: {output}")
```

### Swift

```swift
import CoreML

// Load the model
let model = try simple_model_ane(configuration: MLModelConfiguration())

// Prepare input
let input = simple_model_aneInput(fc1_input: /* your input */)

// Run inference
let output = try model.prediction(input: input)
print("Prediction: \(output)")
```

## 4. Check Performance

```python
import momo_kiji as mk

# Profile the model
profile = mk.profile("simple_model_ane.mlmodel")

print(f"Model size: {profile.model_size_mb} MB")
print(f"Latency: {profile.latency_ms} ms")
print(f"Peak memory: {profile.peak_memory_mb} MB")
print(f"ANE utilization: {profile.ane_utilization}%")
```

## 5. What Happened?

momo-kiji:

1. **Analyzed** your ONNX model
2. **Decomposed** operations into ANE-compatible kernels
3. **Optimized** for the Neural Engine
4. **Generated** an MLModel bundle
5. **Profiled** performance on your hardware

The result: Your model runs **10-100x faster** on ANE compared to CPU.

## Next Steps

- **Learn more** about [how it works](how_it_works.md)
- **Explore examples** for your use case in [Examples](examples.md)
- **Deep dive** into the [API Reference](api_reference.md)
- **Join Discord** to ask questions: https://discord.gg/DHRbKbzr

## Troubleshooting

### Model Won't Compile

Check that your ONNX model is valid:

```bash
momo-kiji validate simple_model.onnx
```

### Compilation is Slow

Large models take time to compile. For faster iteration:

```python
# Enable incremental compilation
mk.compile(
    input_path="model.onnx",
    target="ane",
    output_path="model_ane.mlmodel",
    use_cache=True  # Reuse compilation results
)
```

### Inference is Slower Than Expected

Check if the model is actually using ANE:

```python
profile = mk.profile("model_ane.mlmodel")
print(f"ANE utilization: {profile.ane_utilization}%")
```

If low (<80%), some operations may fall back to CPU. Check the detailed report.

## Getting Help

- **GitHub Issues** — Report bugs: https://github.com/ReillyDesignStudio/momo-kiji/issues
- **Discord** — Ask questions: https://discord.gg/DHRbKbzr
- **Documentation** — Browse guides and examples
