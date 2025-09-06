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

## ⚠️ Disclaimer
이 소프트웨어는 **연구 및 교육 목적으로 제공**됩니다.  
임상 진단이나 치료 의사결정을 대체할 수 없으며, 의료 전문인의 판단을 보조하는 용도로만 사용해야 합니다.  
분석 결과를 임상에 적용하기 전 반드시 전문가의 검증이 필요합니다.

## 📜 License
MIT License © 2025 [Hyuk Jang, Asan Medical Center]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

MEDICAL USE DISCLAIMER: The Software is provided for **research and educational
purposes only** and is **not intended for diagnosis, treatment, or other clinical
use**. The authors and contributors make no representation that the outputs are
accurate for medical decision-making. Users are solely responsible for validating
results and obtaining appropriate regulatory approvals before any clinical use,
and the authors disclaim all liability arising from any clinical application of
the Software.
```
