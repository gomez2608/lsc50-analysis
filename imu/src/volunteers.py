"""Load and crop volunteer-level IMU data.

The original implementation lived in ``IMU/helper_functions.py``. The class
expects a directory layout matching the original (now deleted) data tree:

    {base_route}/INFO/Timestamps.xlsx
    {base_route}/INFO/Volunteer_{n}.txt
    {base_route}/RAW/Volunteer_{n}.xlsx
    {base_route}/OUT_OPENSIM/Volunteer_{n}.mot

See ``docs/DATA.md`` for the full schema.
"""

from __future__ import annotations

import os
from typing import Iterable

import pandas as pd
from tqdm import tqdm

# Columns of the OpenSim ``.mot`` file we want to retain when cropping.
DEFAULT_KEEP_TOKENS: tuple[str, ...] = ("time", "arm", "elbow", "pro", "wrist")

# Names of every IMU channel the original setup recorded.
AVAILABLE_IMU_CHANNELS: tuple[str, ...] = (
    "hand_l_imu",
    "hand_r_imu",
    "humerus_l_imu",
    "humerus_r_imu",
    "radius_l_imu",
    "radius_r_imu",
    "torso_imu",
)

# Spanish accent normalization used to derive filesystem-safe sign names.
_ACCENTS = "áéíúó"
_NO_ACCENTS = "aeiuo"


def clean_sign_name(name: str) -> str:
    """Strip accents and mark questions with a ``_q`` suffix."""
    out: list[str] = []
    has_question = False
    for ch in name:
        if ch in _ACCENTS:
            out.append(_NO_ACCENTS[_ACCENTS.index(ch)])
        elif ch in "¿?":
            has_question = True
        else:
            out.append(ch)
    if has_question:
        out.append("_q")
    return "".join(out)


def column_filter(name: str, keep_tokens: Iterable[str] = DEFAULT_KEEP_TOKENS) -> bool:
    """Return True if any token appears in the column name."""
    return any(token in name for token in keep_tokens)


class VolunteerInformation:
    """Bundle of timestamps, parameters, and motion data for one volunteer."""

    def __init__(self, volunteer_number: int, base_route: str):
        self.volunteer_number = volunteer_number
        self.base_route = base_route
        self.available_imu_channels = AVAILABLE_IMU_CHANNELS
        self.timestamps = self._load_timestamps()
        self.parameters = self._load_parameters()

    def _load_timestamps(self) -> pd.DataFrame:
        path = os.path.join(self.base_route, "INFO", "Timestamps.xlsx")
        # Sheet names are not uniform in LSC50 (e.g. "Volunteer  4"), so match ignoring whitespace.
        wanted = f"Volunteer{self.volunteer_number}"
        sheet = next(s for s in pd.ExcelFile(path).sheet_names if "".join(s.split()) == wanted)
        return pd.read_excel(
            path,
            sheet_name=sheet,
            index_col=0,
            header=0,
            names=["sign", "start", "end"],
        )

    def _load_parameters(self) -> dict[str, str]:
        path = os.path.join(self.base_route, "INFO", f"Volunteer_{self.volunteer_number}.txt")
        with open(path) as handle:
            raw = handle.read().split("\n")
        return {
            line.split(":")[0].strip(): line.split(":")[1].strip()
            for line in raw
            if line.strip()
        }

    def load_motion_file(self) -> pd.DataFrame:
        path = os.path.join(self.base_route, "OUT_OPENSIM", f"Volunteer_{self.volunteer_number}.mot")
        return pd.read_csv(path, sep="\t", header=6)

    def load_raw_data(self, imu_signal_name: str) -> pd.DataFrame | None:
        path = os.path.join(self.base_route, "RAW", f"Volunteer_{self.volunteer_number}.xlsx")
        try:
            return pd.read_excel(path, sheet_name=imu_signal_name)
        except (FileNotFoundError, ValueError) as exc:
            print(f"Could not load {imu_signal_name} for volunteer {self.volunteer_number}: {exc}")
            return None

    def crop_motion_to_signs(self, output_dir: str = "SIGNS") -> None:
        """Slice the motion file by each sign's timestamps and write per-sign CSVs."""
        os.makedirs(output_dir, exist_ok=True)
        motion = self.load_motion_file()

        for sign_idx in tqdm(range(len(self.timestamps)), desc=f"Volunteer {self.volunteer_number}"):
            row = self.timestamps.loc[sign_idx]
            name, start, end = row["sign"], row["start"], row["end"]
            segment = motion[(motion["time"] >= start) & (motion["time"] <= end)]

            sign_dir = os.path.join(output_dir, clean_sign_name(name))
            os.makedirs(sign_dir, exist_ok=True)

            export_cols = [c for c in segment.columns if column_filter(c)]
            segment.to_csv(
                os.path.join(sign_dir, f"nw_Volunteer_{self.volunteer_number}.csv"),
                columns=export_cols,
            )


def crop_all_volunteers(base_route: str, output_dir: str = "SIGNS", volunteers: Iterable[int] = range(1, 6)) -> None:
    """Crop motion files for every volunteer id in ``volunteers``."""
    for n in volunteers:
        vol = VolunteerInformation(n, base_route)
        vol.crop_motion_to_signs(output_dir=output_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Crop OpenSim motion files into per-sign CSVs.")
    parser.add_argument("--base-route", required=True, help="Path to the IMU data root (contains INFO/, RAW/, OUT_OPENSIM/).")
    parser.add_argument("--output-dir", default="SIGNS", help="Destination directory for per-sign CSVs.")
    parser.add_argument("--volunteers", type=int, nargs="+", default=list(range(1, 6)), help="Volunteer ids to process.")
    args = parser.parse_args()

    crop_all_volunteers(args.base_route, args.output_dir, args.volunteers)
