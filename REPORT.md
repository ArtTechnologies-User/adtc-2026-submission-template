# Technical Report — Offline AI Tutor for WAEC Smart Learning Without Internet

**Team ID:** offline-ai-waec-tutor-team  
**Domain:** coding_assistants  
**Model:** WAEC-Tutor-Q4_K_M

---

## Problem

<!-- What problem are you solving? Who is the target user? Why does this matter in an African context? -->

Across West Africa, millions of students prepare for the WAEC exams every year. For many of them, reliable internet access is a luxury, and hiring private tutors is simply out of reach. This leaves a huge gap: bright, motivated learners who want to succeed but don’t have the tools or support they need.

Our project is designed for these students — young people in secondary schools who are determined to pass their exams but face challenges like:

1. Unstable or expensive internet connections

2. Limited access to high‑end devices

3. A shortage of affordable, quality tutoring resources

Running the model offline, directly on budget laptops matters because it removes the barriers that usually block students from accessing advanced learning support. Instead of depending on costly online platforms or constant connectivity, they can study anytime, anywhere, with an AI tutor that lives on their own device. This approach not only makes exam preparation more accessible, but also empowers students to take control of their learning journey without worrying about data costs or privacy concerns.

---

## Design Decisions

<!-- What model did you start from? Why that base model and quantization? What alternatives did you consider and reject? -->

When I started building WAEC Tutor, my first challenge was choosing a model that could actually run on the kinds of laptops students in West Africa already use. I experimented with bigger models like Mistral 7B and Phi‑3 Mini, but they quickly showed their limits — they were powerful, yes, but far too heavy for budget hardware. The experience was slow, sometimes unusable, and I knew that wouldn’t work for students who need quick, reliable answers.

That’s why I settled on a smaller LLaMA‑based model with about 1.1B parameters. It gave me enough reasoning ability to explain concepts clearly, but it was light enough to run locally without draining resources.

Base model: A compact LLaMA‑based model (~1.1B parameters). I tested larger options like Mistral 7B and Phi‑3 Mini, but they were too heavy for the laptops most West African students use. The smaller LLaMA variant gave me enough reasoning ability to explain concepts clearly while staying lightweight enough to run locally.

Quantization: GGUF Q4_K_M was chosen because it keeps the memory footprint small while preserving answer quality. This balance meant students could get clear, step‑by‑step explanations without waiting too long or crashing their system — a critical factor when running on budget laptops.

Alternatives considered:

Q8_0 produced slightly better accuracy but required more than 8 GB of RAM, which exceeded the limits of typical laptops in our context.

Q2_K ran faster but degraded the quality of answers too aggressively, making it unsuitable for tutoring.

Larger models like Mistral 7B or Phi‑3 Mini were rejected because they demanded too many resources for offline deployment in West Africa.

This choice — WAEC‑Tutor‑Q4_K_M — was about more than just technical specs. It was about making sure the model truly fits the lives of students preparing for WAEC exams, giving them a reliable offline tutor that works on the hardware they already have.

---

## Constraints

<!-- What hardware, connectivity, power, or data constraints shaped your choices? -->

Hardware, Connectivity, and Data Constraints
Target hardware: The model is built to run on laptops with 8 GB RAM, integrated GPU, and Ubuntu 22.04. This reflects the reality of what most students in West Africa have access to — modest machines that need efficient solutions.

Inference setup: There is no GPU acceleration. All inference runs purely on the CPU via llama.cpp, ensuring that even laptops without dedicated graphics cards can still benefit from the tutor. This choice was deliberate: it keeps the solution inclusive for students who only have entry‑level devices.

Connectivity constraints: Many students face unreliable or expensive internet access. That’s why WAEC Tutor is designed to run entirely offline. Once installed, it doesn’t need connectivity to answer questions, generate quizzes, or track progress. This makes learning possible in rural areas and during power or network outages.

Data availability constraints: Students often lack access to premium online learning platforms or large datasets. By embedding WAEC‑style quizzes and enabling offline Q&A, the tutor provides meaningful study support without requiring external downloads. Everything they need is packaged inside the app, ready to use.

---

## Benchmarks

<!-- What inference speed and memory numbers did you observe on your development machine? -->

| Metric | Value |
| --- | --- |
| **Machine** | ThinkPad X1 (Intel i5, Ubuntu 22.04) |
| **RAM at peak** | ~3.8 GB |
| **Time to first token** | ~420 ms |
| **Generation speed** | ~18.4 tokens/second |
| **Thermal throttling** | None observed |

These are self-reported development benchmarks. Official scores are measured by the ADTC profiler on the standard evaluation machine.
