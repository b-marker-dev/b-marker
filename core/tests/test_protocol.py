"""
MIT License

Copyright (c) 2025 B-Marker Team

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

Zero-dependency Unit Test - Alpha 0.1.0 Protocol Core
零依賴單元測試 - Alpha 0.1.0 協議核心
"""
# Import core protocol functions from B-Marker core module
# 從B-Marker核心模塊導入協議核心函數
from core.src.protocol import (
    time_to_samples,
    convert_markers,
    generate_simple_pulses,
    validate_jitter
)

def test_core_protocol():
    """
    Unit test for B-Marker core time-audio conversion protocol
    驗證B-Marker核心音頻時間轉換協議的單元測試
    
    Test coverage:
    1. Time to audio sample conversion (second/millisecond units)
    2. Audio marker sample rate conversion (48kHz ↔ 44.1kHz)
    3. Simple pulse generation and jitter validation
    測試覆蓋範圍：
    1. 時間到音頻樣本數轉換（秒/毫秒單位）
    2. 音頻標記採樣率轉換（48kHz ↔ 44.1kHz）
    3. 簡易脈衝生成與抖動驗證
    """
    # 1. Test time to sample conversion (44.1kHz baseline)
    # 測試時間到樣本數轉換（基準44.1kHz）
    assert time_to_samples(1, 's') == 44100, \
        "1 second should convert to 44100 samples (44.1kHz standard)"
    assert time_to_samples(500, 'ms') == 22050, \
        "500 milliseconds should convert to 22050 samples (44.1kHz standard)"
    
    # 2. Test marker sample rate conversion (48kHz → 44.1kHz)
    # 測試標記採樣率轉換（48kHz 轉 44.1kHz）
    converted_marker = convert_markers([48000], 48000, 44100)[0]
    assert abs(converted_marker - 44100) <= 1, \
        "48000 samples @48kHz should convert to 44100 samples @44.1kHz (error ≤1)"
    
    # 3. Test pulse generation and jitter validation
    # 測試脈衝生成與抖動驗證
    pulses = generate_simple_pulses([100, 200], 500)
    jitter_stats = validate_jitter(pulses, 100)
    assert jitter_stats['pulse_count'] == 2, \
        "Generated pulse count should be 2 (match input marker list)"
    
    # Test success feedback
    # 測試成功反饋
    print("✅ B-Marker Core Protocol Verification Passed")
    print("✅ 驗證通過 - B-Marker核心協議功能正常，可上線部署")

if __name__ == "__main__":
    # Execute core protocol test suite
    # 執行核心協議測試套件
    test_core_protocol()