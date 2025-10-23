#!/usr/bin/env python3
import argparse, os, json, numpy as np
from ctperf.roi.mip_yellow_roi import yellow_mask_from_mip_png, mip_mask_to_3d
from ctperf.io.loaders import load_nifti, save_nifti_like

def main():
    ap = argparse.ArgumentParser(description="Extract yellow ROI from MIP image and export NIfTI mask")
    ap.add_argument("--mip", required=True, help="MIP image (PNG/JPG) with yellow ROI")
    ap.add_argument("--ref", required=True, help="Reference NIfTI (e.g., Tmax map) to copy shape/affine")
    ap.add_argument("--axis", default="z", choices=["z","y","x"], help="Projection axis to broadcast (default z)")
    ap.add_argument("--out_mask", default="mip_roi_mask.nii.gz", help="Output NIfTI mask path")
    args = ap.parse_args()

    ref_data, ref_img = load_nifti(args.ref)
    mask2d = yellow_mask_from_mip_png(args.mip)
    volmask = mip_mask_to_3d(mask2d, ref_data.shape, axis=args.axis)
    save_nifti_like(ref_img, volmask.astype(np.uint8), args.out_mask)

    result = {
        "ref_shape": tuple(int(x) for x in ref_data.shape),
        "roi_voxels": int((volmask>0).sum()),
        "output": args.out_mask
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
