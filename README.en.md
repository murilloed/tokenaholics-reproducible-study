# Tokenaholics: reproducible research

[Português](README.md)

**Author:** Murillo Edson de Carvalho Souza, University of Brasília (UnB), Department of Computer Science.

The English manuscript is a translation of research edition **v0.3.1**, retaining its scope, numerical results, 29 references, and three figures. It contains **20 pages including references**. The Portuguese edition remains available. Translation files are a subsequent repository addition; the original `v0.3.1` tag identifies the Portuguese research edition and does not include this addition.

- [English PDF](paper/Tokenaholics-v0.3.1-en.pdf)
- [English LaTeX](paper/main_en.tex) and [bibliography](paper/reference_en.bib)
- [English figure-rendering script](scripts/render_english_figures.py)
- [English document-validation record](results/document_validation_en.json)
- [Source and literature audits (Portuguese)](docs/AUDITORIA_FONTES.md)
- [Scientific literature audit (Portuguese)](docs/LITERATURA_AUDITORIA.md)
- [Data dictionary and provenance (Portuguese)](data/README.md)

## Scope and interpretation

The study combines a critical interdisciplinary review and exploratory secondary analysis of public aggregates from 2025 and 2026. It examines country usage profiles, SOC occupational groups, token and spending shares, an ecological GitHub--Anthropic comparison, short-horizon forecasting, and conditional budget scenarios.

**Tokenaholics is an unvalidated conceptual proposal, not a diagnosis.** Platform aggregates do not measure individual regulation, understanding, or functional impairment. They cannot establish dependence prevalence or causality. Occupational groups are not industrial sectors; platform shares are not absolute global volumes. The paper explains each figure's axes, denominators, construction, interpretation, and limitations.

## Reproduce the numerical analysis

Requirements: Git and Python 3.14. No GPU, provider API key, or private logs are needed. This is a private repository; cloning requires authorized access. Dependency installation initially requires internet; the numerical pipeline uses only the six included fixed inputs.

```bash
git clone https://github.com/murilloed/tokenaholics-reproducible-study.git
cd tokenaholics-reproducible-study
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` on Linux/macOS, then run:

```bash
python -m pip install -r requirements.txt
python scripts/reproduce.py
```

For an exact rerun, first check out the commit associated with the files being used and record it with `git rev-parse HEAD`. The original numerical research edition is tagged `v0.3.1`; translation files require the later commit that introduced them. The numerical reference intentionally remains the unchanged v0.3.0 reference, also used by v0.3.1.

The pipeline checks SHA-256 hashes of six inputs, recalculates analyses, compares five numerical summaries with fixed references (`rtol=1e-7`, `atol=1e-8`), and runs integrity tests. It records environment, commit, working-tree status, packages, and output hashes in ignored `runs/latest.json`. CI runs on Linux and Windows. This verifies numerical reproducibility, not causal, clinical, or population validity.

## Build the English manuscript

Install Tectonic separately. After numerical reproduction, run:

```bash
python scripts/build_paper.py --language en
python scripts/validate_document.py --language en
```

If Tectonic is not on PATH, append `--tectonic /full/path/to/tectonic` to the build command. English charts are rendered from canonical result tables without refitting models or modifying Portuguese figures. The build uses `paper/build/en/` and writes `paper/Tokenaholics-v0.3.1-en.pdf`. Default builds without `--language en` still produce the Portuguese edition.

Document validation checks the 25-page limit, LaTeX warnings, citation-key equivalence, and figure labels. Visual review is separate: render and inspect every page, then use `--visual-reviewed` only after inspecting that exact PDF. The checked-in validation record includes PDF and source hashes.

For Overleaf, upload the English package supplied with the release and select `main.tex` as the main document. It contains the English manuscript, bibliography, template files, and English figures; no private raw data or third-party full texts are included.

## Reuse and citation

See [CITATION.cff](CITATION.cff) for research-project attribution, [LICENSE](LICENSE) for code, and dataset provenance for third-party terms. Cite original data suppliers and scientific papers as appropriate. No DOI has been assigned. Repository access and third-party full-text redistribution remain subject to their respective permissions and rights.
