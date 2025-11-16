# CT Perfusion Auto-Analysis (Open Source)

파이썬 기반 **자동 CT Perfusion 분석 도구**입니다.  
DICOM 폴더를 입력하면 자동으로 주요 perfusion 지표와 결과 이미지를 생성합니다.

---

## 🚀 Quick Start

### 1. 설치
```bash
git clone https://github.com/USERNAME/ct-perfusion-auto.git
cd ct-perfusion-auto
pip install -r requirements.txt
```

> ⚠️ Python 3.9+ 권장

### 2. 실행
```bash
python ct_perfusion_auto.py \
  --dicom_dir ./DICOM_CASE01 \
  --out_dir ./results_case01
```

옵션:
- `--roi_mask`: 병변측 cortex ROI (NIfTI)
- `--contra_mask`: 반대측 cortex ROI (NIfTI)

### 3. 출력 결과
- **NIfTI 맵**: `cbf.nii.gz`, `cbv.nii.gz`, `mtt.nii.gz`, `tmax.nii.gz`, `rcbf.nii.gz`
- **마스크**: `hypoperf_mask_tmax6.nii.gz`, `core_mask_rcbf30.nii.gz`
- **메트릭**: `metrics.json`, `metrics.csv`
- **QA 이미지**: AIF/VOF 곡선, Tmax MIP, Core/Penumbra MIP PNG

---

## 📊 계산 지표 (자동)
- Hypoperfusion (Tmax > 6s)
- Infarct Core (rCBF < 30% ∩ Tmax > 6s)
- Penumbra, Mismatch Ratio
- PRR (%), Corrected / Conventional CBV Index
- HIR (Hypoperfusion Intensity Ratio)
- PVT (Prolonged Venous Transit)

---

## 📖 문헌 근거
- Koneru M, et al. *J NeuroIntervent Surg.* 2025. CBV Index cutoffs (0.8 LVO, 0.7 MeVO)【95†source】
- Sun A, et al. *Front Neurol.* 2024. High CBV Index → good 90-day outcome in late EVT【96†source】
- Imaoka Y, et al. *J Neuroradiol.* 2023. HIR ≤0.22 & CBV Index ≥0.9 → ICAS 예측【97†source】
- Rao VL, et al. *J Cereb Blood Flow Metab.* 2020. HIR & CBV Index → collateral robustness【100†source】
- Yedavalli VS, et al. *Stroke Vasc Interv Neurol.* 2024. CBV Index ≤0.7 → HT 위험 in MeVO【101†source】
- Liebeskind DS, et al. *J NeuroIntervent Surg.* 2024. Collaterals at angiography (HERMES dataset)【98†source】
- Potreck A, et al. *AJNR Am J Neuroradiol.* 2022. rCBF/CBV Index/HIR와 collateral status 비교【103†source】

---

## 📂 저장소 구조
```
ct-perfusion-auto/
├── ct_perfusion_auto.py     # 메인 파이썬 코드
├── requirements.txt         # 필요한 패키지 목록
├── README.md                # 사용법 설명 (현재 문서)
├── LICENSE                  # MIT 라이선스
└── examples/                # 샘플 데이터/결과 (옵션)
```


## 🧬 Research Reproduction Guide

Validation of a CTP-Derived Corrected CBV Index as a Surrogate of DSA-Based ASITN/SIR Collateral in Anterior Circulation Ischemia
(Jang et al., 2025, submitted)

⸻

### 🩻 1. Overview

This open-source pipeline reproduces all perfusion-derived indices used in our study:

Metric	Definition (automated in code)
Corrected CBV Index	Mean CBV in Tmax>6 s region / Mean contralateral cortical CBV
Conventional CBV Index	Mean CBV in lesion cortex ROI / contralateral CBV
HIR (Hypoperfusion Intensity Ratio)	Volume (Tmax ≥ 10 s) / Volume (Tmax ≥ 6 s)
PVT (Perfusion Volume Threshold)	Volume of tissue with Tmax > 6 s
Mismatch Ratio	Hypoperfusion volume / Core volume
PRR (%)	100 × (Baseline − Follow-up hypoperfusion volume) / Baseline volume
PVT Delay (sec)	AIF–VOF time-to-peak difference (proxy for venous outflow delay)

All indices are automatically computed using Python scripts, identical to those described in the Methods section of the paper ￼.

⸻

### 🧠 2. Environment setup

git clone https://github.com/HyukJang1/ct-perfusion-auto.git
cd ct-perfusion-auto
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

Dependencies: numpy, nibabel, pandas, scipy, pillow.

⸻

### 📂 3. Input data structure

Prepare the following maps (NIfTI format) and MIP image:

input_case01/
 ┣ MIP_case01.png             # MIP with yellow ROI overlay
 ┣ Tmax_case01.nii.gz         # Tmax perfusion map
 ┣ CBV_case01.nii.gz          # CBV map
 ┣ rCBF_case01.nii.gz         # Relative CBF map (optional)
 ┣ aif.csv                    # Columns: time_sec,aif
 ┗ vof.csv                    # Columns: time_sec,vof

⚠️ All maps should be co-registered, identical voxel size, and same orientation.

⸻

### ⚙️ 4. Run full auto-analysis (one-shot pipeline)

python scripts/one_shot_from_mip.py \
  --mip input_case01/MIP_case01.png \
  --tmax input_case01/Tmax_case01.nii.gz \
  --cbv input_case01/CBV_case01.nii.gz \
  --rcbf input_case01/rCBF_case01.nii.gz \
  --aif_csv input_case01/aif.csv \
  --vof_csv input_case01/vof.csv \
  --out_dir results_case01

Outputs are saved to results_case01/:

results_case01/
 ┣ metrics.json        # All computed indices
 ┣ log.txt
 ┗ masks/
     ┣ core_mask.nii.gz
     ┣ hypoperfusion_mask.nii.gz
     ┗ penumbra_mask.nii.gz


⸻

### 📊 5. Example result (metrics.json)

{
  "Corrected_CBV_Index": 0.72,
  "Conventional_CBV_Index": 0.68,
  "HIR": 0.21,
  "Mismatch_Ratio": 1.83,
  "PVT_sec": 1.8,
  "PRR_percent": 15.2,
  "hypoperfusion_vox": 87412,
  "core_vox": 46213,
  "penumbra_vox": 41199
}


⸻

### 🧩 6. Reproducing the Paper Results

To reproduce Table 2–5 and Figures 1–6 from the paper:
	1.	Generate metrics for each case (N=123 in the original cohort).
	2.	Compile all metrics.json outputs into a CSV using:

python -m ctperf.utils.aggregate_metrics --input_dir results_all/ --output summary.csv


	3.	Run the statistical analysis (ROC, logistic regression, calibration) in R or Python:
	•	Python: statsmodels, scikit-learn
	•	R: pROC, OptimalCutpoints, rms

⸻

### 🔄 7. Notes on Reproducibility
	•	CTP Processing software: Siemens syngo.CT Neuro Perfusion VB40 (consistent with original acquisition).
	•	Thresholds follow exactly the study definitions:
	•	Tmax > 6 s for hypoperfusion
	•	Tmax > 10 s for severe delay
	•	rCBF < 0.3 × contralateral mean for core
	•	ROI extraction is identical to Figure 2 in the paper, automated via analyze_mip_image.py.
	•	Cross-validation and AUC values will replicate Table 2 (Corrected CBV Index AUC = 0.83 ± 0.07).

⸻

### 🧾 8. Citation

If you use this code or reproduce the analysis, please cite:

Jang H, Jang J, Jang D-K, Sung J-H, Lee H-J, Park H-K.
Validation of a CTP-Derived Corrected CBV Index as a Surrogate of DSA-Based ASITN/SIR Collateral in Anterior Circulation Ischemia.
2025.
DOI: (TBD)

and reference this repository:

Park HK & Jang H. CT Perfusion Auto-Analysis Pipeline (open-source).
https://github.com/HyukJang1/ct-perfusion-auto

⸻

### 🧑‍💻 9. License

MIT License — free for academic and clinical research use.
For commercial use, please contact the corresponding author (parkoct@catholic.ac.kr).

-------
### 10.  GUI Applications
Window: https://drive.google.com/file/d/1FbqzhjpfomITy4sU3DBUJndHzGybAyV2/view?usp=drive_link

MAC OS: https://drive.google.com/file/d/1NKntR6uFOv5j_wsJTfJuYs_MRDzft29G/view?usp=drive_link

PC환경에 Python 3.8이상 깔려 있어야 동작합니다
더 자세한 설명 필요시 다른 개발자분의 링크도 참고해주세요
https://github.com/JoonHaJang/ct-perfusion-auto

-------

## 🤝 Contributing
- Issue, Pull Request 환영합니다!
- 버그 리포트, 기능 제안은 GitHub Issues 사용해주세요.
-  GUI Applications 지속적 개선 중
---

## ⚠️ Disclaimer
이 소프트웨어는 **연구 및 교육 목적으로 제공**됩니다.  
임상 진단이나 치료 의사결정을 대체할 수 없으며, 의료 전문인의 판단을 보조하는 용도로만 사용해야 합니다.  
분석 결과를 임상에 적용하기 전 반드시 전문가의 검증이 필요합니다.

## 📜 License
MIT License © 2025 [Your Name]
