#!/usr/bin/env python3
"""
ESDP1 HW2 - Daily processing pipeline (ERA5 example)

- loads sub-daily ERA5 data for one day (or reads local cached file)
- aggregates to daily mean
- (optional) regrids
- writes output to zarr (or netcdf)
"""

from __future__ import annotations
import argparse
from pathlib import Path
import sys
import xarray as xr

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Daily processing pipeline for ESDP HW2")
    p.add_argument("--input", type=str, required=True, help="Path to input netCDF/GRIB (local file)")
    p.add_argument("--var", type=str, default="q", help="Variable name (default: q)")
    p.add_argument("--date", type=str, required=True, help="Date to process, format YYYY-MM-DD")
    p.add_argument("--outdir", type=str, default="hw2/output", help="Output directory")
    p.add_argument("--to-zarr", action="store_true", help="Write Zarr output (default)")
    p.add_argument("--to-netcdf", action="store_true", help="Write NetCDF output instead of Zarr")
    return p.parse_args()

def load_day(ds: xr.Dataset, date: str) -> xr.Dataset:
    # expects a time coordinate
    t0 = f"{date}T00:00:00"
    t1 = f"{date}T23:59:59"
    return ds.sel(time=slice(t0, t1))

def daily_mean(ds: xr.Dataset, var: str) -> xr.Dataset:
    if var not in ds:
        raise KeyError(f"Variable '{var}' not found. Available: {list(ds.data_vars)}")
    out = ds[[var]].resample(time="1D").mean()
    return out

def main() -> int:
    args = parse_args()
    inpath = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not inpath.exists():
        print(f"[ERROR] Input file not found: {inpath}", file=sys.stderr)
        return 2

    # NOTE: for GRIB you may need: engine="cfgrib"
    ds = xr.open_dataset(inpath)

    ds_day = load_day(ds, args.date)
    ds_daily = daily_mean(ds_day, args.var)

    stem = f"{args.var}_dailymean_{args.date}"
    if args.to_netcdf:
        outfile = outdir / f"{stem}.nc"
        ds_daily.to_netcdf(outfile)
        print(f"[OK] Wrote NetCDF: {outfile}")
    else:
        # default: zarr
        outfile = outdir / f"{stem}.zarr"
        ds_daily.to_zarr(outfile, mode="w")
        print(f"[OK] Wrote Zarr: {outfile}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
