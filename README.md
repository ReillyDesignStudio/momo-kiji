# momo-kiji: Open-Source Apple Neural Engine Framework

**Status:** Research & Planning Phase  
**Version:** 0.1.0  
**Date:** March 18, 2026

## Vision

Create an open-source framework for Apple Neural Engine (ANE) development — equivalent to **CUDA for GPUs**.

Currently, developers have:
- ❌ No unified SDK for ANE programming
- ❌ Limited official Apple documentation
- ❌ Scattered reverse-engineered implementations
- ❌ No standard abstractions (like CUDA's kernel model)

**momo-kiji** aims to:
- ✅ Provide a clean, unified API for ANE development
- ✅ Offer comprehensive documentation & examples
- ✅ Support multiple backends (CoreML, Metal, custom)
- ✅ Build a community of ANE developers
- ✅ Enable production-grade ANE applications

---

## Project Goals

### Phase 1: Research & Documentation (Q1 2026)
- [x] Survey existing ANE implementations
- [x] Document Apple's official SDKs & APIs
- [x] Identify gaps & opportunities
- [ ] Create architecture proposal
- [ ] Engage community feedback

### Phase 2: Core Framework (Q2 2026)
- [ ] Design high-level abstractions
- [ ] Implement reference backends
- [ ] Write comprehensive documentation
- [ ] Create example applications
- [ ] Release v0.1.0

### Phase 3: Ecosystem (Q3-Q4 2026)
- [ ] Integrate with popular frameworks (MLX, Ollama, LangChain)
- [ ] Build tooling (profiler, debugger, benchmarker)
- [ ] Optimize for M4/M5 hardware
- [ ] Launch community initiatives

### Phase 4: Production (2027+)
- [ ] Stabilize APIs
- [ ] Release v1.0.0
- [ ] Build enterprise support

---

## Key Questions (Research Focus)

### 1. Apple SDK Landscape
- **Is there an official Apple Neural Engine SDK?**
  - Current status: No unified SDK (only CoreML)
  - Documentation: Fragmented across frameworks
  
- **What APIs exist for ANE access?**
  - CoreML (high-level, inference only)
  - Metal Performance Shaders (GPU, not ANE)
  - Private _ANECompiler APIs (reverse-engineered)
  - ANE ONNX conversion tools (undocumented)

- **Documentation availability:**
  - Official: CoreML docs (500+ pages, ANE not mentioned)
  - Academic: Orion paper (20 pages, comprehensive)
  - Community: reverse-engineered specs (4+ projects)
  - Missing: Official ANE SDK documentation

### 2. Technical Architecture
- **What's the ANE execution model?**
  - Compile-once, run-many (like CUDA kernels)
  - MIL (Model Intermediate Language) IR
  - 20 constraints on operations/memory/layout
  - Sequential execution (no kernel pipelining)

- **Memory model:**
  - Direct unified memory access (no explicit copy)
  - SRAM caching & alignment requirements
  - Zero-copy tensor I/O via IOSurface
  - Constraints on tensor layout (4D format)

- **Compiler pipeline:**
  - HuggingFace → ONNX → CoreML → MIL IR → ANE binary
  - 5-pass compiler (DCE, fusion, constraint validation)
  - No public compiler source code

### 3. SDK Design (The "CUDA for ANE" Challenge)
- **What abstractions would developers expect?**
  - Model definition (like torch.nn)
  - Kernel compilation (like CUDA's nvcc)
  - Memory management (like cudaMalloc)
  - Profiling & debugging (like NVIDIA's tools)

- **What makes ANE different from CUDA?**
  - Inference-focused (no training APIs from Apple)
  - Unified memory (no explicit GPU↔CPU copy)
  - Hardware constraints (20 documented limits)
  - Model-first (compile once, run many)

- **Framework architecture:**
  - High-level API (Python-like, familiar)
  - Intermediate representation (standardized IR)
  - Multiple backends (CoreML, Metal, custom)
  - Runtime & scheduler

---

## Research Deliverables

### Documents in This Repository

1. **ANE_SDK_LANDSCAPE_2026.md** (In Progress)
   - Comprehensive survey of ANE access methods
   - Official Apple documentation review
   - Reverse-engineered API documentation
   - Comparative analysis (CoreML vs private APIs vs ONNX)

2. **ANE_ARCHITECTURE_DEEP_DIVE.md** (Planned)
   - ANE execution model detailed
   - MIL IR specification
   - 20 constraints fully documented
   - Compiler pipeline walkthrough
   - Memory management strategies

3. **FRAMEWORK_DESIGN_PROPOSAL.md** (Planned)
   - High-level API design
   - Abstract syntax for ANE kernels
   - Memory model specification
   - Backend plugin architecture
   - Example code & use cases

4. **COMPETITIVE_ANALYSIS.md** (Planned)
   - Comparison with CUDA, OpenCL, Vulkan
   - What momo-kiji does differently
   - Lessons from GPU framework history
   - Market positioning & adoption strategy

5. **IMPLEMENTATION_ROADMAP.md** (Planned)
   - Phase-by-phase breakdown
   - Milestone definitions
   - Resource requirements
   - Risk assessment

---

## Current Findings (From momo-inu Research)

### SDK Status: **Fragmented (No Official Unified SDK)**

**Official Apple Offerings:**
| Framework | Level | ANE Support | Documentation |
|-----------|-------|-------------|----------------|
| CoreML | High | Yes (inference) | Extensive (no ANE details) |
| Metal | Low | Indirect | Extensive (GPU focus) |
| ONNX Runtime | Medium | Via CoreML | Limited |
| Xcode | Tools | ANE compiler | Minimal (trial-and-error) |

**Community/Reverse-Engineered:**
| Project | Type | ANE Access | Status |
|---------|------|-----------|--------|
| Orion | Research | MIL IR + compiler | ArXiv paper (latest) |
| NeuralForge | Production | Private APIs | Working |
| Anemll | Tools | CoreML bridge | Active |
| neural-engine | Docs | Specs | Maintained |

### SDK Gap Analysis

**What Exists:**
- ✅ CoreML for model inference (high-level)
- ✅ Metal for GPU compute (not ANE)
- ✅ Some reverse-engineered private APIs (risky, undocumented)
- ✅ Academic research (Orion compiler)

**What's Missing:**
- ❌ Official ANE SDK (like CUDA toolkit)
- ❌ Unified API (like OpenCL)
- ❌ Training support (Apple restricts to inference)
- ❌ Debugging tools (profiler, debugger)
- ❌ Standard compiler toolchain
- ❌ Memory management abstractions
- ❌ Kernel definition language
- ❌ Community standard (like CUDA is for GPUs)

### Why This Matters

**Current Developer Experience:**
1. Write model in PyTorch/TensorFlow
2. Convert to ONNX (manual, error-prone)
3. Convert to CoreML (Xcode tools, limited control)
4. Hope it compiles to ANE (trial-and-error, black box)
5. Get 5-20x performance variation (no way to debug)

**With momo-kiji (Proposed):**
1. Write in momo-kiji's kernel language
2. Compile via momo-kiji (deterministic)
3. Target multiple backends (CoreML, Metal, custom)
4. Profile & debug with standard tools
5. Achieve predictable performance

---

## Technical Challenges

### Challenge 1: Apple Doesn't Want You to Know Everything
- ANE APIs are partially private
- Training APIs are officially forbidden
- Reverse-engineering violates TOS
- **Solution:** Focus on inference; use documented APIs; contribute findings back to Apple

### Challenge 2: ANE is Fixed-Function Hardware
- Unlike CUDA's flexible kernel model
- Only 27 supported operations (not infinite)
- Memory layout constraints (4D tensor format only)
- **Solution:** Embrace the constraints; optimize for them; provide good error messages

### Challenge 3: M-series Evolution
- M4 ANE ≠ M5 ANE ≠ M6 ANE (spec changes)
- Feature detection required
- **Solution:** Abstract over versions; similar to CUDA's "compute capability"

### Challenge 4: Fragmented Hardware Landscape
- M1, M1 Pro, M1 Max, M1 Ultra
- M2, M3, M4 (2 years of chips)
- M5, M5 Pro, M5 Max (brand new)
- iPhone/iPad A17 Pro, A18, A19 variants
- **Solution:** Comprehensive device database; runtime feature detection

---

## Inspiration & Precedents

### What CUDA Did Right
1. **Clear abstraction:** Kernel = function on GPU
2. **Unified memory model:** Handles CPU↔GPU copies
3. **Standard compiler:** nvcc; error messages are helpful
4. **Ecosystem:** cuBLAS, cuDNN, Thrust, etc.
5. **Community:** CUDA developers are a tribe

### What CUDA Did Wrong (Lessons)
1. NVIDIA-only (vendor lock-in)
2. Expensive licensing historically
3. High learning curve (memory management hard)
4. Compute capability fragmentation
5. **Solution for momo-kiji:** Open-source, free, simpler, multi-backend

### Alternative Models
- **OpenCL:** Portable but less optimized
- **Vulkan Compute:** Verbose but powerful
- **SYCL:** Standards-based, emerging
- **oneAPI:** Intel's unified framework

**momo-kiji approach:** Take CUDA's simplicity, OpenCL's portability, SYCL's standardization

---

## Research Areas for Community

### 1. ANE Hardware Reverse Engineering
- [ ] Complete MIL IR specification
- [ ] Characterize memory bandwidth limits
- [ ] Measure operation latencies
- [ ] Test constraint boundaries

### 2. Compiler Optimization
- [ ] Learn from Orion's 5-pass compiler
- [ ] Implement custom passes for specific models
- [ ] Auto-tune layout & quantization
- [ ] Generate optimal schedules

### 3. Framework Design
- [ ] API design workshops
- [ ] Language/syntax for kernels
- [ ] Backend abstraction patterns
- [ ] Error handling & debugging

### 4. Ecosystem Integration
- [ ] MLX backend plugin
- [ ] Ollama integration
- [ ] LangChain support
- [ ] HuggingFace model export

### 5. Community Contributions
- [ ] Benchmark suite
- [ ] Device database (specs for M1-M5)
- [ ] Model zoo (optimized for ANE)
- [ ] Documentation & tutorials

---

## Getting Started (For Contributors)

### 1. Read the Research
- Start: `ANE_SDK_LANDSCAPE_2026.md` (when ready)
- Then: Orion paper (ArXiv 2603.06728)
- Dive: neural-engine GitHub documentation

### 2. Understand the Hardware
- M4 Max: 38 TFLOPS ANE, 16-core, 400 GB/s bandwidth
- M5 Max: Distributed accelerators, 460 GB/s, 4x faster TTFT
- Constraints: 20 documented, 14 previously unknown (Orion)

### 3. Explore Existing Solutions
- CoreML: How does compilation work?
- MLX: How does GPU acceleration compare?
- NeuralForge: How are private APIs being used?
- Orion: What's the compiler doing?

### 4. Contribute
- **Documentation:** Fill in gaps in ANE knowledge
- **Reverse Engineering:** Discover new constraints/operations
- **Prototypes:** Build example frameworks
- **Community:** Share findings, build support

---

## License & Community

**License:** MIT (open-source, permissive)  
**Code of Conduct:** Be respectful, share knowledge, no gatekeeping  
**Governance:** Meritocratic (early decisions by core team, voting as grows)

---

## Comparison: CUDA vs momo-kiji Goals

| Aspect | CUDA | momo-kiji Vision |
|--------|------|------------------|
| **Vendor** | NVIDIA only | Apple ANE (+ future?) |
| **Hardware** | GPUs | Neural Engines |
| **Model** | Kernel-based | Model + compiler |
| **Memory** | Explicit copy | Unified memory |
| **Training** | Full support | Inference focus (for now) |
| **Open Source** | No | Yes |
| **Learning Curve** | Steep | Gentle |
| **Ecosystem** | Mature | TBD |
| **Goal** | Dominate ML | Empower developers |

---

## Next Steps

### Immediate (This Week)
- [ ] Complete ANE_SDK_LANDSCAPE_2026.md
- [ ] Engage with Orion authors (via ArXiv)
- [ ] Survey community interest (Reddit, HN, Twitter)
- [ ] Create preliminary API design sketch

### This Month
- [ ] Write ANE_ARCHITECTURE_DEEP_DIVE.md
- [ ] Create FRAMEWORK_DESIGN_PROPOSAL.md
- [ ] Prototype simple compiler pass
- [ ] Launch discussion forum/Discord

### This Quarter
- [ ] Release 0.1.0 research package
- [ ] Identify core team members
- [ ] Build reference implementation
- [ ] Write comprehensive documentation

---

## Questions for Bob

1. **Scope:** Focus on ANE only, or plan for broader Apple silicon (GPU, Neural Engine, CPU)?
2. **Language:** Python first? C++ for performance? Support both?
3. **Target Users:** ML researchers? Application developers? Both?
4. **Timeline:** 6 months to MVP? 2 years to production? No deadline?
5. **Community:** Build in private first, then open-source? Open from day 1?
6. **Licensing:** MIT? Apache 2.0? Dual licensing?

---

## Resources

### Official Apple
- [CoreML Documentation](https://developer.apple.com/coreml/)
- [Metal Performance Shaders](https://developer.apple.com/metal/neural-engine/)
- [WWDC Videos (MLX, Metal 4)](https://developer.apple.com/videos/)

### Academic Research
- [Orion: ArXiv 2603.06728](https://arxiv.org/abs/2603.06728) ⭐ Latest
- [Apple Intelligence Foundation LLMs](https://arxiv.org/abs/2407.21075)
- [Native LLM Inference at Scale](https://arxiv.org/abs/2601.19139)

### Community
- [neural-engine GitHub](https://github.com/hollance/neural-engine)
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)
- [MLX Discussion](https://github.com/ml-explore/mlx/discussions)

### Related Projects
- [MLX](https://github.com/ml-explore/mlx) - Array framework
- [vLLM-MLX](https://github.com/waybarrios/vllm-mlx) - Inference server
- [NeuralForge](https://github.com/Khaeldur/NeuralForge) - Fine-tuning
- [Anemll](https://github.com/Anemll/Anemll) - Model conversion

---

## Contributors

- **Initiation:** Bob Reilly (Vision for "CUDA for ANE")
- **Research:** Momotaro 🍑 (momo-kiji framework designer)
- **Community:** You? (Help build this!)

---

**Last Updated:** March 18, 2026  
**Status:** Research Phase 1 (Documentation gathering)  
**Next Review:** March 25, 2026

---

_Building the open-source framework for Apple Neural Engine development._
