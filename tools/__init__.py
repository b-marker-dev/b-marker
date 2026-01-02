'''python
"""
B-Marker Tools Package
Copyright (c) 2025 B-Marker Development Team.

This package is governed by the B-Marker Tools Commercial License.
For details, see LICENSE-COMMERCIAL.md in this directory or visit https://b-marker.com.
Commercial inquiries: sales@b-marker.com
"""
# b-marker/tools/__init__.py
from .converters import (
    frames_to_ms,
    beats_to_ms,
    samples_to_ms,
    ms_to_frames,
    batch_frames_to_ms
)
__all__ = ['frames_to_ms', 'beats_to_ms', 'samples_to_ms', 'ms_to_frames', 'batch_frames_to_ms']
