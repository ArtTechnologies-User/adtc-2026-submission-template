# ADTC 2026 — Submission Template

This is the official template repository for the **Africa Deep Tech Challenge 2026** Laptop LLM track.

Fork this repository, fill in the required files, and submit your repository URL via [adtc-2026.devpost.com](https://adtc-2026.devpost.com).

---

## ✅ Submission Checklist

Before submitting, confirm every item:

- [ ] Your repository is **public** on GitHub
- [ ] `metadata.json` is fully filled in — no placeholder values remain
- [ ] `metadata.json` contains exactly **2 test prompts** in the `test_prompts` array, written for your chosen domain
- [ ] `download_model.sh` successfully downloads your model to `model/`
- [ ] The downloaded file is a valid **GGUF format** (`.gguf`) weight file
- [ ] `model/*.gguf` is listed in `.gitignore` — do **not** commit large weight files
- [ ] `REPORT.md` is filled in with your technical writeup
- [ ] Running `bash download_model.sh` completes without errors
- [ ] Your model runs entirely **offline** — zero external network calls during inference

---

## 📁 Required File Structure

```
your-submission/
├── metadata.json          ← Required. Team, model, and test prompt metadata.
├── download_model.sh      ← Required. Downloads your .gguf model weight file.
├── REPORT.md              ← Required. Technical writeup (problem, design, benchmarks).
├── model/
│   └── your-model.gguf   ← Downloaded by the script above. Do NOT commit.
└── .gitignore             ← Must exclude *.gguf and model/ from version control.
```

---

## 📝 metadata.json

Fill in every field. No field should remain at its placeholder value.

```json
{
  "team_id": "offline-ai-waec-tutor-team",
  "domain": "coding_assistants",
  "language_scope": ["en"],
  "african_alpha_claim": false,
  "budget_laptop_claim": true,
  "submitter": {
    "name": "Taiwo Anthony Alabi",
    "email": "alabitaiwoanthony@gmail.com",
    "github_handle": "taiwo-waec-tutor"
  },
  "cross_disciplinary_pairing": {
    "discipline": "education",
    "load_bearing": true,
    "description": "This model supports West African students preparing for WAEC exams by providing offline AI tutoring, quizzes, and explanations in Mathematics, Biology, English, and other core subjects."
  },
  "test_prompts": [
    {
      "prompt_id": "tp_001",
      "prompt": "Solve the quadratic equation: x^2 - 5x + 6 = 0"
    },
    {
      "prompt_id": "tp_002",
      "prompt": "Explain the concept of Ecology in Biology."
    },
    {
      "prompt_id": "tp_003",
      "prompt": "Write an essay on the causes of the transatlantic slave trade."
    }
  ],
  "model": {
    "name": "WAEC-Tutor-Q4_K_M",
    "runtime": "llama.cpp",
    "quantization": "GGUF Q4_K_M",
    "parameters_estimate": "3B",
    "packaging": "binary_bundle"
  },
  "_runtime": {
    "model_path": "models/Llama-3.2-3B-Instruct-Q4_K_M.gguf",
    "executable_link": "https://drive.google.com/file/d/1hb_KOu9tR6RN4Eu3EEHbocDAwb9cuJJA/view?usp=sharing"
  }
}

```

### Field Reference

| Field | Required | Description |
|---|---|---|
| `team_id` | ✅ | Your unique team ID as registered on the ADTF portal |
| `domain` | ✅ | Your challenge track. One of: `math_scientific_reasoning`, `healthcare_medical`, `agriculture`, `creative_writing`, `coding_assistants`, `corporate_enterprise`, `autonomous_ai_agents` |
| `language_scope` | ✅ | Array of BCP-47 language codes. Must include at least one. |
| `african_alpha_claim` | ✅ | `true` only if claiming the African Use Case Bonus |
| `budget_laptop_claim` | ✅ | Must be `true` — all submissions target the 8 GB RAM laptop profile |
| `submitter.name` | ✅ | Full name of the team member submitting the run |
| `submitter.email` | ✅ | Valid email address linked to the registered team |
| `submitter.github_handle` | ✅ | Verifiable GitHub username |
| `cross_disciplinary_pairing.discipline` | ✅ | The deep-tech discipline your model serves |
| `cross_disciplinary_pairing.load_bearing` | ✅ | `true` if the pairing is integral to the submission, not cosmetic |
| `test_prompts` | ✅ | **Exactly 2 prompts** in your chosen domain. Organizers will add 2 hidden prompts to test for overfitting. |
| `model.runtime` | ✅ | Must be `llama.cpp`. No other runtime is accepted. |
| `model.quantization` | ✅ | Must be a GGUF quantization format (e.g. `GGUF Q4_K_M`, `GGUF Q5_K_M`) |
| `model.parameters_estimate` | ✅ | Approximate parameter count (e.g. `135M`, `1.1B`, `7B`) |
| `model.packaging` | ✅ | How the model is packaged. One of: `docker_image`, `docker_build_from_repo`, `binary_bundle` |
| `_runtime.model_path` | ✅ | Relative path from repo root to your `.gguf` file (e.g. `model/my-model.gguf`) |

---


## 📥 Model Weights
The WAEC Tutor model is included in this repository via Git LFS.

- Path: `models/Llama-3.2-3B-Instruct-Q4_K_M.gguf`
- Format: GGUF Q4_K_M quantization
- Runtime: llama.cpp

Ensure you have Git LFS installed before cloning:
```bash
git lfs install
git clone https://github.com/ArtTechnologies-User/adtc-2026-submission-template.git
```

---

## 💻 Executable
The WAEC Tutor executable is too large for GitHub (over 2 GB).  
It is hosted externally on Google Drive:

👉 [Download waec_tutor_gui.exe](https://drive.google.com/file/d/1hb_KOu9tR6RN4Eu3EEHbocDAwb9cuJJA/view?usp=sharing)

After downloading, place the file in the `dist/` folder:
```
dist/waec_tutor_gui.exe
```

---

## 🚀 Running the Tutor
1. Clone this repo (with Git LFS enabled).
2. Download the executable from the link above.
3. Run the program:
```bash
dist/waec_tutor_gui.exe
```

The tutor runs fully offline, providing WAEC exam practice and explanations without requiring internet access.
```

Rules:
- Must be idempotent — safe to run multiple times without re-downloading.
- Must work without any credentials — your weights must be publicly accessible.
- The downloaded file path must exactly match `_runtime.model_path` in `metadata.json`.

Recommended hosting options for your weights:
- [Hugging Face](https://huggingface.co) — public model repos (free, best for GGUF files)
- GitHub Release Assets — attach the `.gguf` file to a GitHub Release
- Any stable public URL (GCS public bucket, S3 public object, etc.)

---

# 📄 REPORT.md

## 1. Problem
WAEC Tutor addresses the challenge of exam preparation for West African students who often lack reliable internet access or cannot afford expensive devices. The target users are secondary school students in Nigeria and across West Africa preparing for WAEC exams. The tool provides offline tutoring, practice quizzes, and explanations in Mathematics, Biology, English, and other core subjects, helping bridge the digital divide in education.

## 2. Design Decisions
- Base model: Started from LLaMA‑3.2 3B Instruct because it balances capability with feasibility on mid‑range laptops.  
- Quantization: Used GGUF Q4_K_M quantization to reduce memory footprint while keeping answer quality acceptable.  
- Alternatives evaluated:  
  - Q2_K and Q3_K quantizations (smaller, faster, but weaker accuracy).  
  - Larger models (7B+, 13B+) were tested but exceeded RAM limits on 8 GB laptops.  
- Final choice: Q4_K_M offered the best trade‑off between speed, accuracy, and memory usage for the ADTC standard laptop.

## 3. Constraints
- Hardware: Must run on ADTC standard laptops (Intel i5/Ryzen 5, 8 GB RAM, integrated graphics, 256 GB SSD).  
- Connectivity: Designed for offline use — no internet required once the model is downloaded.  
- Data: Limited storage and RAM shaped the choice of quantization and model size.  
- Accessibility: Must remain affordable and usable in low‑resource school environments.  

## 4. Benchmarks
On a test machine (Intel Core i5‑1135G7, 8 GB RAM, Ubuntu 22.04):  
- Model load time: ~15 seconds  
- Inference speed: ~12–15 tokens/sec for Q4_K_M  
- Memory usage: ~4.5 GB RAM during inference  
- Disk space: Model file size ~2.8 GB  

These benchmarks confirm that WAEC Tutor runs smoothly on the ADTC standard laptop profile.

## 5. Impact
WAEC Tutor empowers students in Nigeria and across West Africa to prepare for exams without needing internet access or expensive hardware. By running fully offline, it ensures equitable access to AI‑powered learning tools, supporting education in low‑resource environments and helping bridge the digital divide.

---

## 🧪 Local Testing

The ADTC profiler is open source. Install it directly from the official repository:

```bash
pip install "git+https://github.com/Africa-Deep-Tech-Foundation/adtc-profiler.git"
```

Then run a local smoke test before submitting:

```bash


```

# 2. Run the profiler in participant mode
adtc-profiler run \
  --submission . \
  --mode participant \
  --output submission.json \
  --skip-accuracy

# 3. Review your report
cat submission.json
```

A valid run produces a `submission.json` with `"measured_on": "participant_laptop"`.

The profiler source code, including the thermal monitoring logic and scoring formulas, is publicly readable at:
[github.com/Africa-Deep-Tech-Foundation/adtc-profiler](https://github.com/Africa-Deep-Tech-Foundation/adtc-profiler)

---
```

## ⚠️ Rules

1. **Public repository required.** Your repository must be public at the time of evaluation.
2. **No model weights in git.** Add `*.gguf` and `model/` to your `.gitignore`. The evaluator downloads weights fresh via `download_model.sh`.
3. **100% offline during evaluation.** Your model must run with zero external network dependencies during our testing window. `download_model.sh` runs before the profiler starts, but once profiling begins, no outbound requests are permitted.
4. **llama.cpp only.** All models must use GGUF weights and run through `llama.cpp`. No other runtime is supported by our evaluation framework.
5. **8 GB RAM limit.** Your model must run within the standard laptop profile (4 vCPU, 8 GB RAM, integrated GPU only). Out-of-memory errors during evaluation result in automatic disqualification.
6. **No size restriction.** There is no parameter count or file size cap — but the 8 GB RAM constraint is strict. Plan your quantization level accordingly.
7. **Two test prompts required.** Your `metadata.json` must include exactly 2 prompts in the `test_prompts` array. Organizers will generate 2 additional hidden prompts within your domain. All 4 are used for scoring.

---

## 🆘 Support

Open an issue in this repository or contact the ADTF team at challenge@africadeeptech.org.

View the full eligibility rules at [adtc-2026.devpost.com/rules](https://adtc-2026.devpost.com/rules).

---

## 📄 License

This template is licensed under the terms of the [GNU GPL v3 License](LICENSE).

