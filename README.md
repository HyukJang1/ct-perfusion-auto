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

---

## 🤝 Contributing
- Issue, Pull Request 환영합니다!
- 버그 리포트, 기능 제안은 GitHub Issues 사용해주세요.

---

## 📜 License
MIT License © 2025 [Your Name]
