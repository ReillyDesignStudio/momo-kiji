# momo-kiji: CUDA for Apple Neural Engine

## The Vision

**Democratizing Apple Neural Engine development the way CUDA democratized GPU computing.**

momo-kiji is an open-source SDK and framework that brings clarity, control, and community to Apple Neural Engine (ANE) development. We're building the tools, documentation, and standards that have been missing since ANE launched in 2017.

---

## The Problem We Solve

### Apple Neural Engine is Powerful, But Inaccessible

**Current Reality:**
- Billions of devices have ANE (every Mac since M1, every modern iPhone/iPad)
- ANE is 10-100x more efficient than GPU for inference
- But developers have NO official SDK to use it

**The Result:**
- Developers fall back to CoreML (black box, limited control)
- Power users reverse-engineer private APIs (undocumented, risky)
- Researchers publish findings scattered across papers (fragmented)
- Performance is mysterious (20x variance, unexplained)

### This Changes With momo-kiji

We're creating:
- ✅ **Unified SDK** for ANE development (like CUDA is for GPUs)
- ✅ **Clear API** with comprehensive documentation
- ✅ **Compiler framework** for transparent optimization
- ✅ **Debugging tools** to understand performance
- ✅ **Community standards** for ANE development

---

## What's Inside

### Research & Knowledge Base
- Comprehensive ANE SDK landscape survey
- Reverse-engineered specs (from Orion paper + community)
- Official Apple API documentation review
- Competitive analysis (vs CUDA, OpenCL, Vulkan, MLX)

### Framework (In Development)
- High-level Python API (familiar to ML developers)
- Intermediate representation (ANDK IL standard)
- Compiler with optimization passes (inspired by Orion)
- Multiple backends (CoreML, custom, Metal)
- Debugging & profiling tools

### Community
- Open-source (MIT license)
- Contributor-friendly
- Meritocratic governance
- Built in public from day 1

---

## Why This Matters

### For Developers
- **Clarity:** Understand what's happening under the hood
- **Control:** Optimize for ANE explicitly
- **Debugging:** Tools to profile and understand performance
- **Community:** Share knowledge and best practices

### For the Industry
- **Efficiency:** Unlock ANE's 10-100x advantage for inference
- **Privacy:** Models run locally on billions of Apple devices
- **Accessibility:** Bring advanced ML to consumer hardware
- **Scale:** Democratize high-performance computing

### For Apple's Ecosystem
- **Adoption:** Easier ANE development → more ANE apps
- **Innovation:** Community contributions improve ecosystem
- **Standards:** Best practices emerge from open collaboration
- **Value:** Developers choose Apple silicon for ANE

---

## The Roadmap

### Phase 1: Research & Design (Q1-Q2 2026) 🔄 In Progress
- ANE landscape documented ✓
- Design proposal pending
- Community engagement starting

### Phase 2: Core Framework (Q3-Q4 2026)
- High-level API specification
- Reference compiler (learn from Orion)
- Multiple backends
- Basic debugging tools
- **Target:** v0.1.0 (research-ready)

### Phase 3: Production Ready (2027)
- Framework optimization
- Advanced tools (profiler, debugger, analyzer)
- Training support
- Framework integrations (MLX, Ollama, LangChain)
- **Target:** v1.0.0 (production-ready)

### Phase 4: Industry Standard (2028+)
- Widespread adoption
- M6+ hardware support
- Enterprise features & support
- Non-profit governance

---

## Inspiration: CUDA's Success

CUDA became the industry standard for GPU computing because:

1. **Clear abstraction:** "Kernels" made GPU programming understandable
2. **Unified API:** Single way to write GPU code across NVIDIA hardware
3. **Comprehensive docs:** Developers could learn and build
4. **Standard tools:** Profiler, debugger, compiler
5. **Community:** Developers built an ecosystem around CUDA

**momo-kiji applies this formula to ANE:**
- Clear API for ANE development
- Unified approach across Apple devices
- Comprehensive documentation of ANE
- Standard tools for profiling & debugging
- Open community contributions

---

## The Opportunity

Apple Neural Engine represents an untapped goldmine:
- **10x-100x more efficient** than GPU for inference
- **Billions of devices** with ANE capability
- **No official SDK** (huge gap)
- **Community ready** to contribute
- **Research support** (Orion paper just published)

**momo-kiji is the missing piece.**

---

## Getting Started

### For Researchers
Read the ANE landscape survey and Orion paper to understand:
- How ANE works internally
- What constraints exist
- Why performance varies
- Where optimization opportunities lie

### For Developers
Follow the roadmap and contribute:
- Documentation & tutorials
- Framework design & implementation
- Tools (profiler, debugger, analyzer)
- Test models & benchmarks
- Framework integrations

### For Everyone
Join the conversation:
- Ask questions
- Share findings
- Propose improvements
- Build together

---

## Technology Stack

### Current (Phase 1)
- Python (documentation, analysis)
- Markdown (knowledge base)
- Git & GitHub (collaboration)

### Planned (Phase 2-3)
- Python (high-level API)
- Rust/C++ (compiler, performance)
- Metal (GPU acceleration)
- CoreML (reference backend)

---

## License & Community

**License:** MIT (open-source, permissive)  
**Code of Conduct:** Respectful, inclusive, knowledge-sharing  
**Governance:** Meritocratic (early core team, community voting as grows)

---

## Key Questions

We're seeking input on:
1. **Scope:** ANE-only or broader Apple processors?
2. **Training:** Inference-first or support training?
3. **Devices:** M-series Macs only or include iPhone/iPad?
4. **Language:** Python first, C++, or both?
5. **Integration:** Standalone or work with MLX/Ollama?

---

## The Dream

In 5 years, when developers want to optimize for ANE:
1. They google "ANE framework"
2. They find momo-kiji
3. They follow a tutorial
4. They write an ANE kernel in Python
5. They profile with our tools
6. They see 10x speedup
7. They thank the community
8. They contribute back

**That's momo-kiji.**

---

## Related Projects

**momo-inu:** Local LLM research for OpenClaw on Apple Silicon  
→ https://github.com/rdreilly58/momo-inu

**MLX:** Array framework optimized for Apple Silicon  
→ https://github.com/ml-explore/mlx

**Orion:** ANE characterization & compiler research (https://arxiv.org/pdf/2603.06728)  
→ Latest academic work on ANE internals

**neural-engine:** Reverse-engineered ANE documentation  
→ https://github.com/hollance/neural-engine

---

## Contact & Contribution

We're building this in public. Come join us!

**GitHub Discussions:** Ask questions, share findings  
**Issues:** Report bugs, suggest features  
**Pull Requests:** Contribute code, docs, research  
**Email:** Reach out if you want to collaborate

---

## The Vision Statement

> **momo-kiji is the open-source SDK that enables developers to harness Apple Neural Engine the way CUDA enabled NVIDIA GPU development.**

We believe ANE should be as accessible and understandable as GPUs. We're building the tools, documentation, and community to make that happen.

---

_momo-kiji: "Machine learning made explicit on Apple silicon"_

**Let's build the future of ANE development together. 🍑**
