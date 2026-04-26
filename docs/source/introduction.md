# Introduction to momo-kiji

## What is momo-kiji?

momo-kiji is an open-source framework that brings clarity, control, and community to **Apple Neural Engine (ANE)** development.

Think of it as **CUDA for Apple Neural Engine**—a unified SDK that makes ANE accessible to developers the way CUDA made GPU computing accessible.

## The Problem

Apple Neural Engine is:
- **In every modern Apple device** (Mac M1+, iPhone 15+, iPad Pro)
- **10-100x more efficient** than GPUs for inference
- **Completely private** (models run locally, never leave the device)

Yet there's **no official SDK** to use it.

Developers today resort to:

1. **CoreML** — Black box, limited control, often doesn't use ANE efficiently
2. **Reverse engineering** — Undocumented APIs, breaks with OS updates
3. **Hoping for the best** — Inconsistent results, performance is a mystery

## The Solution

momo-kiji provides:

```
Model (ONNX/PyTorch/TensorFlow)
        ↓
   momo-kiji compiler
        ↓
   ANE kernels + metadata
        ↓
   App uses native ANE (10x faster)
```

### Key Features

- **Direct ANE Access** — Compile models directly to ANE, not through CoreML
- **Transparent Compilation** — See how your model is compiled and optimized
- **Python API** — Familiar interface for ML developers
- **Multi-platform** — Target macOS and iOS with one toolchain
- **Open Source** — MIT license, built in public, community-driven

## Why Now?

Three things align:

1. **Research Available** — The Orion paper (https://arxiv.org/pdf/2603.06728) revealed detailed ANE internals 2 weeks ago
2. **Community Ready** — Developers are hungry for better ANE tools (high engagement on Reddit, HackerNews)
3. **Perfect Timing** — M5 just launched, M6 coming soon, ANE story is just beginning

## Current Phase

**Phase 1: Research & Design (Q1-Q2 2026)**

We're documenting ANE architecture, designing the framework, and engaging the community.

The framework is research-ready. Full production release comes in Phase 2 (Q3-Q4 2026).

## Get Started

1. [Installation](installation.md) — Set up momo-kiji
2. [Quickstart](quickstart.md) — Compile your first model
3. [API Reference](api_reference.md) — Detailed function documentation
4. [Examples](examples.md) — Real-world use cases

## Join the Community

- **GitHub** — https://github.com/ReillyDesignStudio/momo-kiji
- **Discord** — https://discord.gg/DHRbKbzr
- **Discussions** — Ask questions, share findings, propose ideas

## The Vision

> In five years, compiling models for ANE should be as straightforward as compiling for CUDA. Developers should understand their code, have standard tools, and contribute back to the community.

momo-kiji is the framework that makes this possible.
