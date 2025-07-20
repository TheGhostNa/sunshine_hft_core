# sunshine_hft_core/meta/memory_bridge.py

import subprocess
from pathlib import Path


def run_cpp_allocator():
    exe_path = Path(__file__).resolve().parent.parent / "allocators_cpp" / "allocator_cpp.exe"
    if not exe_path.exists():
        raise FileNotFoundError(f"C++ allocator not found at: {exe_path}")

    result = subprocess.run([str(exe_path)], capture_output=True, text=True)
    return result.stdout.strip()


def run_rust_allocator():
    exe_path = (
        Path(__file__).resolve().parent.parent
        / "allocators_rust"
        / "target"
        / "release"
        / "rust_allocator.exe"
    )
    if not exe_path.exists():
        raise FileNotFoundError(f"Rust allocator not found at: {exe_path}")

    result = subprocess.run([str(exe_path)], capture_output=True, text=True)
    return result.stdout.strip()
