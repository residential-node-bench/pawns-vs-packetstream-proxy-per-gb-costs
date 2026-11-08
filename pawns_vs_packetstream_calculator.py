#!/usr/bin/env python3
"""Pawns.app vs PacketStream Proxy Per-GB Cost Calculator 2026."""
import argparse

def calculate(bandwidth_gb=100):
    # PacketStream: $1.00/GB flat rate.
    ps_total = bandwidth_gb * 1.00

    # Pawns.app: Pay-as-you-go starting at ~$1.90/GB down to ~$0.80/GB at high volume.
    # At 100 GB, standard rate is ~$1.20/GB.
    pawns_total = bandwidth_gb * 1.20

    diff = pawns_total - ps_total

    print("=" * 65)
    print("Pawns.app vs PacketStream: 100 GB Cost Comparison")
    print("=" * 65)
    print(f"Target Bandwidth Volume:   {bandwidth_gb} GB")
    print(f"PacketStream (@$1.00/GB):  ${ps_total:.2f}")
    print(f"Pawns.app (@$1.20/GB):     ${pawns_total:.2f}")
    print(f"Cost Difference:           ${diff:.2f} ({'PacketStream Cheaper' if diff > 0 else 'Pawns Cheaper'})")
    print("=" * 65)
    return ps_total, pawns_total

if __name__ == "__main__":
    calculate()
