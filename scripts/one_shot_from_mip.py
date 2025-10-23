#!/usr/bin/env python3
import argparse, os, subprocess, json

def main():
    ap = argparse.ArgumentParser(description="One-shot: MIP(노란영역) -> ROI -> metrics")
    ap.add_argument("--mip", required=True, help="MIP image (PNG/JPG)")
    ap.add_argument("--tmax", required=True, help="Tmax NIfTI")
    ap.add_argument("--cbv", help="CBV NIfTI")
    ap.add_argument("--rcbf", help="rCBF NIfTI")
    ap.add_argument("--vof_csv", help="VOF CSV (time_sec,vof)")
    ap.add_argument("--aif_csv", help="AIF CSV (time_sec,aif)")
    ap.add_argument("--axis", default="z", choices=["z","y","x"], help="MIP projection axis")
    ap.add_argument("--out_dir", default="outputs_one_shot")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    roi_contra = os.path.join(args.out_dir, "contra_roi_from_mip.nii.gz")

    cmd1 = [
        "python", "scripts/analyze_mip_image.py",
        "--mip", args.mip, "--ref", args.tmax,
        "--axis", args.axis, "--out_mask", roi_contra
    ]
    subprocess.check_call(cmd1)

    cmd2 = [
        "python", "scripts/compute_metrics.py",
        "--tmax", args.tmax, "--roi_contra", roi_contra,
        "--out_dir", args.out_dir, "--save_masks"
    ]
    if args.cbv: cmd2 += ["--cbv", args.cbv]
    if args.rcbf: cmd2 += ["--rcbf", args.rcbf]
    if args.vof_csv and args.aif_csv:
        cmd2 += ["--vof_csv", args.vof_csv, "--aif_csv", args.aif_csv]

    subprocess.check_call(cmd2)
    print(json.dumps({"status":"ok","out_dir":args.out_dir}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
