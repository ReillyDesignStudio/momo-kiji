# Apple Neural Engine SDK Landscape 2026
## Comprehensive Survey of Available APIs, Documentation, & Tools

**Date:** March 18, 2026  
**Status:** Research Complete  
**Sources:** 30+ (Apple docs, GitHub, ArXiv, community)

---

## Executive Summary

### The Problem: No Unified ANE SDK

Unlike GPUs with CUDA/OpenCL, Apple Neural Engine (ANE) has:
- ✅ **High-level API:** CoreML (inference only, limited control)
- ✅ **Reverse-engineered access:** Private _ANECompiler APIs (undocumented, risky)
- ✅ **Academic research:** Orion paper (latest, 2 weeks old)
- ❌ **Unified SDK:** Like CUDA or OpenCL (DOES NOT EXIST)
- ❌ **Training support:** Apple forbids via TOS
- ❌ **Debugging tools:** Profiler, debugger, memory analyzer (not available)

### Current Landscape

```
Developer Journey (Current State):
  PyTorch/TF → ONNX (manual) → CoreML (Xcode) → ANE (black box)
                                                ↑
                                        20x performance variance
                                        No visibility into why
```

### What This Means for momo-kiji

**Opportunity:** Create the missing SDK layer  
**Challenge:** Apple hasn't published full ANE specs  
**Solution:** Reverse-engineer + document + standardize

---

## Part 1: Official Apple APIs

### 1.1 CoreML Framework

**What:** High-level machine learning inference framework (iOS, macOS, tvOS)  
**When:** Introduced iOS 11 (2017), evolved continuously  
**Purpose:** Deploy ML models on Apple devices  
**ANE Support:** Yes (automatic, but limited control)

#### CoreML API Layers

```
Application Code (Swift/Obj-C)
        ↓
CoreML High-Level API (MLModel, MLPredictionOptions)
        ↓
CoreML Compute Backend Selection
        ├─ Neural Engine (if available)
        ├─ GPU (Metal)
        ├─ CPU (fallback)
        └─ Distributed (multi-core CPU)
        ↓
Hardware Execution
```

#### What You Can Control in CoreML

**Model Properties:**
```swift
let model = try MLModel(contentsOf: modelURL)

// Get model description
print(model.modelDescription.inputDescriptionsByName)
print(model.modelDescription.outputDescriptionsByName)

// Control compute options
var options = MLPredictionOptions()
options.usesCPUOnly = false  // Allow ANE/GPU
options.usesMultipleThreads = true

let prediction = try model.prediction(from: input, options: options)
```

**What You Cannot Control:**
- ❌ Where exactly it runs (ANE? GPU? CPU?)
- ❌ Memory layout or allocation
- ❌ Quantization method (CoreML decides)
- ❌ Compilation details
- ❌ Kernel scheduling

#### ANE In CoreML

**Automatic ANE Usage:**
- CoreML automatically routes to ANE if available
- Typical case: 80%+ of ops route to ANE (if compatible)
- No explicit "enable ANE" flag
- Black box: You can't see why some ops don't route

**ANE Compatibility:**
- Supported operations: ~100 (CoreML public ops)
- ANE-supported subset: ~27 operations
- Unsupported ops fall back to GPU/CPU

**Example: What Happens Inside CoreML**

```python
# You write PyTorch
model = MyTransformer()

# Convert to ONNX (manual, error-prone)
torch.onnx.export(model, dummy_input, "model.onnx")

# Apple's CoreMLTools converts ONNX → CoreML → ANE IR
coreml_model = ct.converters.convert("model.onnx")
coreml_model.save("model.mlmodel")

# At runtime:
# CoreML reads .mlmodel
# → Analyzes ops
# → Tries to compile to ANE
# → Falls back to GPU/CPU if needed
# → You have NO visibility into this process
```

#### CoreML Documentation

**Official Apple Resources:**
- Developer.apple.com/coreml (100+ pages)
- "Core ML" programming guide (PDF)
- WWDC videos (2017-2025)
- Xcode help & sample code

**What's Documented:**
- ✅ How to use CoreML (high-level)
- ✅ Supported operations (extensive list)
- ✅ Model conversion process (MLModelFormats)
- ✅ Performance tips (general)

**What's NOT Documented:**
- ❌ How ANE works internally
- ❌ Why specific ops don't route to ANE
- ❌ Memory layout for ANE
- ❌ ANE compiler details
- ❌ ANE constraints (Apple doesn't mention them publicly)

---

### 1.2 Metal Performance Shaders (MPS)

**What:** Low-level GPU compute framework  
**When:** Introduced iOS 8 (2014), evolving  
**Purpose:** Custom GPU kernels and optimization  
**ANE Support:** No direct access (GPU only)

#### Metal vs ANE

```
Metal Performance Shaders:
  - Purpose: GPU compute (not ANE)
  - Level: Low-level kernel code
  - Control: Full (you write the shaders)
  - Performance: Good for GPU-resident code
  - ANE: Not applicable

Metal 4 (New in 2025):
  - New tensor operations (linear algebra)
  - Better GPU integration
  - Still NOT ANE-specific
```

#### Metal + ANE Relationship

While MPS doesn't directly access ANE, Apple's newer "Metal Neural Engine" work suggests:
- Metal could eventually abstract over CPU/GPU/ANE
- Not ready for developers yet (research phase)
- WWDC 2025 hints at future Metal+Neural Engine integration

**Current Status:** Metal is for GPU; ANE requires CoreML or reverse engineering

---

### 1.3 ONNX Runtime for Apple

**What:** Cross-platform inference engine with Apple support  
**When:** Latest versions (2024-2026)  
**Purpose:** Run ONNX models on Apple hardware  
**ANE Support:** Indirect (via CoreML backend)

#### How ONNX Uses ANE

```
ONNX Model (.onnx file)
        ↓
ONNX Runtime (Apple build)
        ├─ CoreML Execution Provider (uses CoreML → ANE)
        ├─ MPS Execution Provider (GPU only)
        ├─ CPU Execution Provider (fallback)
        └─ Neural Engine Provider (not available)
        ↓
Execution
```

#### ONNX Documentation

**What's Available:**
- ✅ ONNX format specification
- ✅ How to use ONNX Runtime
- ✅ Execution provider documentation
- ❌ Anything ANE-specific

**Gap:** ONNX Runtime has CoreML backend, but ONNX docs don't explain ANE

---

### 1.4 Xcode Tools

**What:** IDE & build tools for Apple development  
**When:** Integrated over years (especially Xcode 13+)  
**Purpose:** Compile CoreML models, analyze performance  
**ANE Support:** Limited tools for model compilation

#### Xcode Model Compilation

**Features:**
- Model preview (shows architecture)
- MLModel file validation
- Automatic op routing analysis (NEW in Xcode 15)
- Performance metrics (CPU time, estimated memory)

**Limitations:**
- ❌ No ANE-specific metrics
- ❌ No per-operation breakdown
- ❌ No memory layout visualization
- ❌ No debugging inside ANE compilation
- ❌ Trial-and-error to optimize

#### Xcode.app Analysis

```
File → model.mlmodel → Open In
                     → Core ML Model Viewer
                        ├─ Model description
                        ├─ Layer visualization
                        ├─ Inference timing (CPU baseline)
                        └─ ??? (ANE routing opaque)
```

**What Would Help:**
- Breakdown: which ops route to ANE?
- Compiler logs: why did this op fail to route?
- Memory profiler: ANE SRAM usage
- Hardware metrics: ANE utilization

---

## Part 2: Community/Reverse-Engineered Access

### 2.1 Orion: Latest Research (https://arxiv.org/pdf/2603.06728)

**What:** Academic paper detailing ANE architecture and compiler  
**When:** Published March 5, 2026 (2 weeks old) ⭐ LATEST  
**Authors:** Apple AI research team (implied, not confirmed)  
**Impact:** Most comprehensive public ANE documentation ever

#### What Orion Reveals

**ANE Architecture:**
```
MIL Intermediate Representation (IR)
        ↓
5-Pass Compiler:
  1. Dead Code Elimination (DCE)
  2. Identity Elimination (remove no-ops)
  3. Cast Fusion (combine type conversions)
  4. SRAM Annotation (mark for on-chip memory)
  5. Constraint Validation (20 limits enforced)
        ↓
ANE Machine Code
```

**20 ANE Constraints (Now Documented):**
- Layout constraints (4D tensor format required)
- Operation constraints (only 27 supported ops)
- Memory constraints (SRAM limits, cache alignment)
- Numerical constraints (special value handling)
- Compilation constraints (14 previously unknown)

**Contributions:**
- Delta compilation (efficient weight updates)
- Zero-copy tensor I/O (IOSurface-backed)
- Program caching (avoid recompilation)

#### Orion Impact on momo-kiji

**This is Gold for SDK Development:**
- ✅ Explains why certain ops fail
- ✅ Documents memory constraints precisely
- ✅ Provides compiler pass examples
- ✅ Enables better error messages
- ✅ Foundation for custom compiler

**Note:** Orion paper may be from Apple (unconfirmed) but published openly

---

### 2.2 NeuralForge

**What:** Production-grade ANE fine-tuning framework  
**Where:** GitHub: Khaeldur/NeuralForge  
**Status:** Active development, well-tested (568 tests)  
**Documentation:** Minimal (code-focused)

#### What NeuralForge Shows

**ANE Access Method:**
- Uses reverse-engineered _ANECompiler APIs
- Calls private Apple frameworks directly
- Undocumented, against TOS, but works
- Risk: Apple could remove in OS update

**What It Can Do:**
- Train small models on ANE (sub-1B)
- Fine-tune models with custom data
- Optimize for specific hardware

**What It Teaches momo-kiji:**
- ANE APIs ARE accessible (if you dig)
- Training IS possible (not just inference)
- Private APIs are risky but viable
- Better solution: Standardize & make official

---

### 2.3 neural-engine (Documentation)

**What:** Reverse-engineered ANE documentation  
**Where:** GitHub: hollance/neural-engine  
**Status:** Maintained, 4K+ stars  
**Documentation:** Comprehensive (150+ pages of reverse engineering)

#### What neural-engine Documents

**ANE Hardware:**
```
16-core ANE (per M-series chip)
  - 38 TFLOPS @ FP16 (M4)
  - Matrix multiply unit
  - Activation functions
  - Memory subsystem (SRAM, cache)
  - Constraints on all operations
```

**ANE Compiler:**
- MIL IR format (partially reverse-engineered)
- Operation set (27 ops supported)
- Memory layout rules
- Compilation constraints
- Device-specific capabilities

**Supported Operations (27 total):**
```
Compute:
  - matmul, add, mul, dot_product
  - relu, sigmoid, tanh, softmax
  - conv1d, conv2d, conv3d
  - reshape, transpose, gather
  - split, concat

Memory:
  - load, store, rank_preserve_reshape
  - reverse_along_axis, scatter

Special:
  - noop, const, variable
  - custom_layer (limited)
```

**Devices Supported:**
- M1, M1 Pro, M1 Max, M1 Ultra
- M2, M2 Pro, M2 Max, M2 Ultra
- M3, M3 Pro, M3 Max
- M4, M4 Pro, M4 Max
- M5, M5 Pro, M5 Max (spec changes)
- A14-A19 (iPhone/iPad)

#### neural-engine Impact on momo-kiji

**Provides:**
- ✅ Comprehensive operation reference
- ✅ Device capability matrix
- ✅ Memory layout specification
- ✅ Clear constraint documentation
- ✅ Reverse-engineered compiler insights

**Gaps (Still Unknown):**
- Exact MIL IR grammar (inferred, not official)
- Compiler optimization strategies
- Performance scheduling algorithms
- Advanced features (grouped convolutions, etc.)

---

### 2.4 Other Reverse-Engineered Projects

**more-ane-transformers** (smpanaro)
- Focus: Transformer optimization for ANE
- Key finding: 4D tensor layout optimization
- Teaches: Memory access patterns matter

**Anemll** (Anemll/Anemll)
- Focus: HuggingFace → ANE conversion
- Key finding: Model compatibility varies
- Teaches: Quantization strategy is critical

**geohot/tinygrad ANE accelerator** (partial)
- Focus: Inference framework with ANE support
- Key finding: Can bypass CoreML
- Teaches: Alternative execution paths exist

---

## Part 3: What's Missing (SDK Gaps)

### Gap 1: No Official ANE SDK

**What Exists:**
- CoreML (high-level, black box)
- Private APIs (undocumented, risky)
- Reverse-engineered specs (community knowledge)

**What's Missing:**
- Unified, official ANE SDK
- Like CUDA but for ANE
- Published by Apple
- With documentation & support

### Gap 2: No Unified IR (Intermediate Representation)

**What Exists:**
- MIL (reverse-engineered from Orion)
- ONNX (general purpose, not ANE-optimized)
- Proprietary formats (CoreML .mlmodel)

**What's Missing:**
- Open ANE IR (like LLVM IR for CPUs)
- Community contributions allowed
- Compiler passes documented
- Optimization strategies published

### Gap 3: No Standard Compiler Toolchain

**What Exists:**
- Xcode (black box, limited output)
- ONNX Runtime (relies on CoreML)
- Reverse-engineered compilers (Orion, NeuralForge)

**What's Missing:**
- Open-source ANE compiler
- Like LLVM (for CPUs) or nvcc (for CUDA)
- Modular compiler passes
- Community extensions

### Gap 4: No Debugging Tools

**What Exists:**
- Xcode model viewer (visualization)
- Timing estimates (rough)
- That's it

**What's Missing:**
- Profiler (which ops take time, ANE utilization)
- Debugger (step through, inspect values)
- Memory analyzer (SRAM usage, cache hits)
- Constraint violation detector (clear error messages)
- Custom kernel validator

### Gap 5: No Training Support (From Apple)

**What Exists:**
- Reverse-engineered training (NeuralForge)
- Private API usage (against TOS)

**What's Missing:**
- Official training APIs
- Apple publicly refusing (enforced in TOS)
- Legal fine-tuning path for developers

### Gap 6: No Community Standards

**What Exists:**
- Individual projects (MLX, vLLM-MLX, NeuralForge)
- Scattered documentation
- No coordination

**What's Missing:**
- ANDK (Apple Neural Development Kit) standard
- Community governance
- Standardized benchmarking
- Best practices documentation

---

## Part 4: Framework Design Implications

### What momo-kiji Must Do

Given the SDK gaps, momo-kiji needs to:

1. **Provide High-Level Abstractions**
   - Don't expose raw MIL IR
   - Python-like API (familiar to ML developers)
   - Composition-friendly (layers, models)

2. **Implement a Standard IR**
   - Design ANE IR (ANDK IL format)
   - Document thoroughly
   - Make open-source
   - Enable community contributions

3. **Build a Compiler**
   - Implement the 5-pass compiler (learn from Orion)
   - Add custom optimization passes
   - Provide clear error messages
   - Handle device-specific variations (M1-M5)

4. **Create Debugging Tools**
   - Profiler (ANE utilization, timing)
   - Constraint validator (catch errors early)
   - Memory analyzer (SRAM usage)
   - Operator coverage report

5. **Support Multiple Backends**
   - CoreML (reference, stable)
   - Custom (when momo-kiji compiler ready)
   - MLX GPU (fallback)
   - Future: Metal neural engine (when Apple releases)

6. **Document Comprehensively**
   - Collect all reverse-engineered knowledge
   - Explain why constraints exist
   - Provide optimization guides
   - Build community wiki

---

## Part 5: Comparison Matrix

### Official APIs vs Community Solutions

| Aspect | CoreML | ONNX Runtime | NeuralForge | Orion | momo-kiji (Vision) |
|--------|--------|--------------|-------------|-------|-------------------|
| **Purpose** | Inference | Inference | Training | Research | General (Inference+) |
| **ANE Support** | Automatic | Indirect | Direct | Theory | Direct (planned) |
| **Documentation** | Extensive | Good | Minimal | Academic | Comprehensive |
| **Training** | No | No | Yes (private APIs) | Theory | Yes (future) |
| **Debugging** | Poor | Poor | None | None | Excellent (planned) |
| **Customization** | Very Limited | Limited | High | N/A | High |
| **Risk Level** | Low | Low | High (TOS) | N/A | Medium (open-source) |
| **Community** | Apple | ONNX Org | Solo maintainer | Academic | TBD (building) |
| **Production Ready** | Yes | Yes | Mostly | No | Not yet (Q2 2026 target) |

---

## Part 6: Technical Opportunities for momo-kiji

### 1. Model Import Pipeline

**Challenge:** Developers currently use error-prone manual conversion

**Solution:** momo-kiji auto-import
```
PyTorch/TF → HuggingFace → Auto-detect ops → 
  Map to ANE (27 ops) → Fallback strategies → 
  Optimized ANE IR → Multi-backend compile
```

### 2. Quantization Strategy

**Challenge:** CoreML quantizes automatically, no user control

**Solution:** momo-kiji control
```
Model → Auto-profiling (where is compute heavy?) →
  Choose quantization (FP16, INT8, palettization) →
  Profile impact → Report tradeoffs
```

### 3. Performance Prediction

**Challenge:** No way to know if code will be fast until deployed

**Solution:** momo-kiji predictor
```
Model → Extract ops → Lookup ANE latencies →
  Account for memory bandwidth → Estimate TTFT/token speed →
  Flag bottlenecks
```

### 4. Constraint Validation

**Challenge:** Models compile to CoreML, fail silently in ANE

**Solution:** momo-kiji early detection
```
Model → Check all constraints (Orion's 20) →
  Identify violations early → Suggest fixes →
  "This op not supported on M4, use this instead"
```

### 5. Device Abstraction

**Challenge:** M1, M4, M5 ANE specs differ

**Solution:** momo-kiji device detection
```
Device → Read capabilities (ops supported, TFLOPS) →
  Adapt IR at compile time → 
  Optional fallback if unsupported
```

---

## Part 7: Competitive Advantage

### vs CUDA
- ✅ Open-source (CUDA proprietary)
- ✅ Apple-native (CUDA NVIDIA-only)
- ✅ Simpler hardware constraints (CUDA complex)
- ❌ Smaller ecosystem (CUDA massive)
- ❌ Younger technology (CUDA mature)

### vs OpenCL
- ✅ Tailored for ANE (OpenCL generic)
- ✅ Modern Python API (OpenCL C)
- ✅ Better documentation (OpenCL scattered)
- ❌ Narrower scope (OpenCL portable)

### vs MLX
- ✅ ANE-specific (MLX GPU-first)
- ✅ Training focus (MLX inference-first)
- ✅ Compiler-centric (MLX framework-centric)
- ❌ Larger team at Apple (MLX backed by Apple)

---

## Recommendations for momo-kiji

### Short-term (Q1-Q2 2026)
1. Document all reverse-engineered knowledge
2. Create ANDK IL specification (ANE standard IR)
3. Build reference compiler (Python prototype)
4. Release research documentation
5. Engage with Orion authors

### Medium-term (Q3-Q4 2026)
1. Implement production compiler (Rust/C++)
2. Build debugging tools (profiler, validator)
3. Create backend plugins (CoreML, custom)
4. Write comprehensive documentation
5. Release v0.1.0 (research-ready)

### Long-term (2027+)
1. Upstream improvements to Apple (if receptive)
2. Merge with MLX or other frameworks (ecosystem)
3. Release v1.0.0 (production-ready)
4. Build community of contributors
5. Support M6, M7, next-gen hardware

---

## Open Questions

1. **Will Apple ever release an official ANE SDK?**
   - Unlikely in next 2 years (they have CoreML)
   - Opportunity: Fill this gap ourselves

2. **Can we legally use reverse-engineered APIs?**
   - Research: Yes (academic freedom)
   - Production: Gray area (probably fine for personal use)
   - Solution: Publish findings; let Apple formalize if needed

3. **How does this integrate with MLX?**
   - Currently MLX focuses on GPU
   - momo-kiji could provide ANE backend
   - Complementary, not competitive

4. **What about iPhone/iPad ANE?**
   - A14 Pro, A17 Pro, A18, A19 have ANE
   - Same basic architecture (subset of M-series)
   - momo-kiji should support all Apple silicon

5. **Training or inference focus?**
   - Start: Inference (safer, CoreML baseline)
   - Future: Training (bigger impact)
   - Challenge: Apple restricts training APIs

---

## Conclusion

Apple Neural Engine is a powerful piece of hardware **without a proper SDK**.

**Current situation:**
- Developers use CoreML (black box)
- Power users reverse-engineer APIs (risky)
- Researchers publish findings (Orion, etc.)
- No unified standard

**momo-kiji opportunity:**
- Fill the SDK gap
- Standardize ANE development
- Build a community
- Create "CUDA for ANE"

**Timeline to success:**
- Q1-Q2 2026: Research & design
- Q3-Q4 2026: MVP & community
- 2027: Production maturity
- 2028+: Industry adoption

---

## Sources

### Official Apple
- developer.apple.com/coreml (CoreML framework)
- developer.apple.com/metal (Metal framework)
- WWDC videos (2017-2025)
- Xcode Help documentation

### Academic Research
- Orion (https://arxiv.org/pdf/2603.06728) ⭐
- Apple Intelligence Foundation LLMs (ArXiv 2407.21075)
- Native LLM Inference at Scale (ArXiv 2601.19139)

### Community
- neural-engine GitHub (hollance, 4K stars)
- NeuralForge GitHub (Khaeldur)
- Anemll GitHub
- r/LocalLLaMA discussions
- MLX GitHub discussions

### Media & Analysis
- insiderllm.com (detailed benchmarks)
- Medium posts on ANE optimization
- YouTube tutorials on CoreML

---

**Last Updated:** March 18, 2026  
**Status:** Complete research documentation  
**Next Step:** Framework design proposal

