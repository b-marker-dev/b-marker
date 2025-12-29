"""
MIT License | 2025 B-Marker Team
零依賴單元測試 - Alpha 0.1.0 協議核心
"""
from b-marker.core.src.protocol import *

def test_core():
    assert time_to_samples(1, 's') == 44100
    assert time_to_samples(500, 'ms') == 22050
    assert abs(convert_markers([48000], 48000, 44100)[0] - 44099) <= 1
    pulses = generate_simple_pulses([100, 200], 500)
    stats = validate_jitter(pulses, 100)
    assert stats['pulse_count'] == 2
    print("✅ K-Verify passed - ready for launch")

if __name__ == "__main__":
    test_core()
