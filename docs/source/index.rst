momo-kiji Documentation
=======================

CUDA for Apple Neural Engine

.. toctree::
   :maxdepth: 3
   :caption: Getting Started

   introduction
   installation
   quickstart

.. toctree::
   :maxdepth: 3
   :caption: User Guide

   how_it_works
   api_reference
   examples
   troubleshooting

.. toctree::
   :maxdepth: 3
   :caption: Contributing

   contributing
   development
   roadmap

.. toctree::
   :maxdepth: 2
   :caption: Community

   community
   code_of_conduct
   security

Welcome to momo-kiji!
=====================

momo-kiji is an open-source framework that brings clarity, control, and community to Apple Neural Engine (ANE) development.

Instead of struggling with CoreML's black box or reverse-engineering private APIs, momo-kiji gives you:

- **Direct ANE access** with a unified SDK
- **10-100x efficiency** for on-device inference
- **Simple Python API** familiar to ML developers
- **Multi-platform support** for macOS and iOS
- **Transparent compilation** that you can understand and optimize

Why momo-kiji?
==============

Apple Neural Engine is incredible—it's in every modern Apple device, 10-100x more efficient than GPUs for inference, and runs models completely locally for privacy.

But there's no official SDK.

Developers fall back to:

1. **CoreML** (black box, limited control)
2. **Reverse engineering** (undocumented, risky)
3. **Hoping it works** (inconsistent results)

momo-kiji fixes this. We're building what Apple hasn't: a unified, open-source SDK for ANE development, inspired by how CUDA revolutionized GPU computing.

Quick Links
===========

- **GitHub:** https://github.com/ReillyDesignStudio/momo-kiji
- **Discord:** https://discord.gg/DHRbKbzr
- **Website:** https://momo-kiji.dev
- **Research:** https://github.com/rdreilly58/momo-inu

Current Status
==============

**Phase 1: Research & Design (Q1-Q2 2026)**

We're here. Building the foundation:

- ANE architecture documented ✓
- Design proposal in progress
- Community engagement starting
- This documentation is evolving

The framework is research-ready. Full production release in Phase 2 (Q3-Q4 2026).

Get Started
===========

1. **Read the introduction** to understand the vision
2. **Install momo-kiji** (once released)
3. **Try the quickstart** with a simple example
4. **Explore the API reference** for detailed usage
5. **Join the community** on Discord to ask questions

Contributing
============

momo-kiji is open-source and built in public. We welcome contributions of all kinds:

- Code (compiler, tools, examples)
- Documentation (guides, tutorials, API docs)
- Research (ANE analysis, optimization findings)
- Community (helping others, organizing discussions)

See :doc:`contributing` for details.

License
=======

momo-kiji is licensed under the MIT License. See LICENSE file for details.
