```python

"""
B-Marker Tools - [Converters for Creators]
Copyright (c) 2025 B-Marker Development Team.

This source code is governed by the B-Marker Tools Commercial License.
本原始碼受《B-Marker 工具集商業許可協議》約束。

YOU MAY USE THIS CODE FREELY UNDER THE TERMS OF THE FREE LICENSE GRANTED IN THE
COMMERCIAL LICENSE AGREEMENT (FOR PERSONAL, NON-COMMERCIAL, OR SMALL-SCALE USE).
根據《商業許可協議》中授予的免費許可條款，您可以自由使用此代碼（用於個人、非商業或小規模用途）。

IF YOU INTEND TO USE THIS CODE FOR COMMERCIAL PURPOSES AS DEFINED IN THE
AGREEMENT, YOU MUST OBTAIN A COMMERCIAL USE LICENSE.
如果您意圖根據協議定義將此代碼用於商業用途，您必須獲取商業使用許可。

For the full license text and contact information, please see:
詳細許可協議全文與聯繫方式，請參見：
- The LICENSE-COMMERCIAL.md file in this directory.
- 本目錄下的 LICENSE-COMMERCIAL.md 文件。
- https://bmarker.com

Email: dev@b-marker.com (General) / sales@b-marker.com (Commercial)
"""

from typing import Union
# 導入bmarker 核心
from bmarker.core.src import protocol

# 默認參數（符合行業常見標準）
_DEFAULT_FPS = 24.0      # 標準影片幀率
_DEFAULT_BPM = 120.0     # 常見音樂速度

def frames_to_ms(
    frames: Union[int, float],
    fps: float = _DEFAULT_FPS
) -> float:
    """
    將影片幀數轉換為毫秒。

    Args:
        frames: 幀數。
        fps: 每秒幀數 (Frames Per Second)。默認為 24.0。

    Returns:
        float: 對應的毫秒數。

    Example:
        >>> frames_to_ms(24, 24.0)
        1000.0  # 24幀 @24fps 正好是1秒
    """
    if fps <= 0:
        raise ValueError(f"FPS must be positive, got {fps}")

    # 核心邏輯：使用協議層進行轉換
    # 1. 幀 -> 秒 (通過除以fps)
    seconds = frames / fps
    # 2. 秒 -> 基準樣本數
    samples = protocol.time_to_samples(seconds, unit='s')
    # 3. 樣本數 -> 毫秒 (基於44.1kHz基準：44.1樣本/毫秒)
    milliseconds = samples / 44.1
    return milliseconds

def beats_to_ms(
    beats: Union[int, float],
    bpm: float = _DEFAULT_BPM
) -> float:
    """
    將音樂節拍數轉換為毫秒。

    Args:
        beats: 節拍數（如：1小節常為4拍）。
        bpm: 每分鐘節拍數 (Beats Per Minute)。默認為 120.0。

    Returns:
        float: 對應的毫秒數。

    Example:
        >>> beats_to_ms(4, 120)
        2000.0  # 4拍 @120bpm 正好是2秒
    """
    if bpm <= 0:
        raise ValueError(f"BPM must be positive, got {bpm}")

    # 核心邏輯：直接使用協議層的「節拍」單位轉換
    samples = protocol.time_to_samples(beats, unit='beat', bpm=bpm)
    # 樣本數 -> 毫秒
    milliseconds = samples / 44.1
    return milliseconds

def samples_to_ms(
    samples: int,
    sample_rate: int = 44100
) -> float:
    """
    將給定採樣率下的音頻樣本數轉換為毫秒。

    Args:
        samples: 樣本數。
        sample_rate: 採樣率 (Hz)。默認為 44100。

    Returns:
        float: 對應的毫秒數。

    Example:
        >>> samples_to_ms(44100, 44100)
        1000.0  # 44100個樣本 @44.1kHz 正好是1秒
    """
    if sample_rate <= 0:
        raise ValueError(f"Sample rate must be positive, got {sample_rate}")

    # 核心邏輯：樣本 -> 秒 -> 毫秒
    seconds = samples / sample_rate
    milliseconds = seconds * 1000.0
    return milliseconds

def ms_to_frames(
    milliseconds: Union[int, float],
    fps: float = _DEFAULT_FPS
) -> float:
    """
    將毫秒轉換為影片幀數（返回浮點數以便精確）。

    Args:
        milliseconds: 毫秒數。
        fps: 每秒幀數 (Frames Per Second)。默認為 24.0。

    Returns:
        float: 對應的幀數（可能包含小數）。

    Example:
        >>> ms_to_frames(1000, 24.0)
        24.0  # 1000毫秒 @24fps 正好是24幀
    """
    if fps <= 0:
        raise ValueError(f"FPS must be positive, got {fps}")

    # 核心邏輯：毫秒 -> 秒 -> 樣本數 -> 計算幀數
    seconds = milliseconds / 1000.0
    samples = protocol.time_to_samples(seconds, unit='s')
    # 幀時間 = 1秒 / fps， 樣本數對應的秒數 = samples / 44.1k
    total_seconds = samples / 44100.0
    frames = total_seconds * fps
    return frames

# 可選：提供一個批量處理的便利函數示例
def batch_frames_to_ms(
    frames_list: list,
    fps: float = _DEFAULT_FPS
) -> list:
    """
    批量將幀數列表轉換為毫秒列表。
    """
    return [frames_to_ms(f, fps) for f in frames_list]
