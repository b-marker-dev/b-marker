"""
B-Marker Core Protocol - Alpha 0.1.0
核心協議層：實現「音頻作為時間語言」的基礎純函數。
MIT License | 版權所有 (c) 2025 B-Marker 開發團隊
"""

from typing import List, Dict, Optional

# ==================== 核心協議函數 ====================

def time_to_samples(value: float, unit: str, bpm: Optional[float] = None) -> int:
    """
    將時間值轉換為 44.1 kHz 採樣率下的音頻樣本數。

    Args:
        value: 時間數值
        unit: 時間單位，可選 's' (秒), 'ms' (毫秒), 'beat' (音樂節拍)
        bpm: 僅當 unit='beat' 時需要，表示每分鐘節拍數

    Returns:
        44.1 kHz 採樣率對應的樣本數（整數）

    Raises:
        ValueError: 當單位無效或參數不合法時
    """
    SAMPLE_RATE = 44100  # 基準採樣率 (Hz)

    if unit == 's':
        return int(value * SAMPLE_RATE)
    elif unit == 'ms':
        return int(value * SAMPLE_RATE / 1000.0)
    elif unit == 'beat':
        if bpm is None or bpm <= 0:
            raise ValueError("BPM must be positive when unit is 'beat'")
        seconds_per_beat = 60.0 / bpm
        return int(value * seconds_per_beat * SAMPLE_RATE)
    else:
        raise ValueError(f"Unsupported unit: {unit}. Use 's', 'ms', or 'beat'.")


def convert_markers(markers: List[int], from_rate: int, to_rate: int) -> List[int]:
    """
    將標記列表從一個採樣率轉換到另一個採樣率。

    Args:
        markers: 原始採樣率下的標記位置列表（樣本索引）
        from_rate: 原始採樣率 (Hz)
        to_rate: 目標採樣率 (Hz)

    Returns:
        目標採樣率下的新標記位置列表（四捨五入到整數）
    """
    if from_rate <= 0 or to_rate <= 0:
        raise ValueError("Sample rates must be positive.")

    ratio = to_rate / from_rate
    return [int(round(marker * ratio)) for marker in markers]


def generate_simple_pulses(markers: List[int], total_duration_samples: int) -> bytes:
    """
    根據標記列表生成一個簡單的二進制脈衝序列。

    Args:
        markers: 脈衝觸發位置的樣本索引列表
        total_duration_samples: 輸出序列的總長度（樣本數）

    Returns:
        二進制數據，每個樣本用一個位元表示（1 表示脈衝，0 表示靜默）。
        實際位元組長度為 ceil(total_duration_samples / 8)。
    """
    if total_duration_samples <= 0:
        raise ValueError("Total duration must be positive.")

    # 計算所需位元組數：每樣本1位，每字節8樣本
    byte_length = (total_duration_samples + 7) // 8
    pulse_data = bytearray(byte_length)

    for marker in markers:
        if 0 <= marker < total_duration_samples:
            byte_index = marker // 8
            bit_index = marker % 8
            pulse_data[byte_index] |= (1 << bit_index)

    return bytes(pulse_data)


def validate_jitter(pulse_data: bytes, expected_interval_samples: Optional[int] = None) -> Dict[str, float]:
    """
    分析脈衝數據的時間抖動（Jitter）基本統計。

    Args:
        pulse_data: generate_simple_pulses 生成的二進制數據
        expected_interval_samples: 預期的脈衝間隔（樣本數，可選）

    Returns:
        包含均值、標準差等統計量的字典
    """
    # 將位元組數據還原為脈衝位置列表
    pulse_positions = []
    for byte_idx, byte_val in enumerate(pulse_data):
        for bit_idx in range(8):
            if byte_val & (1 << bit_idx):
                sample_idx = byte_idx * 8 + bit_idx
                pulse_positions.append(sample_idx)

    if len(pulse_positions) < 2:
        return {
            "mean_interval": 0.0,
            "std_deviation": 0.0,
            "pulse_count": len(pulse_positions),
            "note": "Insufficient pulses for jitter analysis."
        }

    # 計算相鄰脈衝的間隔
    intervals = []
    for i in range(1, len(pulse_positions)):
        intervals.append(pulse_positions[i] - pulse_positions[i-1])

    # 基礎統計
    import statistics
    mean_interval = statistics.mean(intervals) if intervals else 0.0
    std_deviation = statistics.stdev(intervals) if len(intervals) > 1 else 0.0

    result = {
        "pulse_count": len(pulse_positions),
        "interval_count": len(intervals),
        "mean_interval_samples": mean_interval,
        "std_deviation_samples": std_deviation,
    }

    if expected_interval_samples:
        result["expected_interval"] = expected_interval_samples
        result["mean_error_samples"] = mean_interval - expected_interval_samples
        result["relative_jitter"] = std_deviation / expected_interval_samples if expected_interval_samples != 0 else float('inf')

    return result


# ==================== 簡易測試（可刪除） ====================
if __name__ == "__main__":
    # 測試 time_to_samples
    print("Testing time_to_samples:")
    print(f"  1秒 -> {time_to_samples(1.0, 's')} samples")
    print(f"  2拍 @120BPM -> {time_to_samples(2.0, 'beat', 120)} samples")

    # 測試 convert_markers
    markers_48k = [48000, 96000]  # 在48kHz下1秒和2秒的位置
    markers_44k = convert_markers(markers_48k, 48000, 44100)
    print(f"\nConvert markers 48k->44.1k: {markers_48k} -> {markers_44k}")

    # 測試 generate_simple_pulses 與 validate_jitter
    test_markers = [100, 200, 300]
    pulses = generate_simple_pulses(test_markers, 500)
    print(f"\nGenerated {len(pulses)} bytes of pulse data.")
    stats = validate_jitter(pulses, expected_interval_samples=100)
    print("Jitter analysis:", stats)
    print("\n✅ Protocol layer core functions are ready.")
