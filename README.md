# UnitConverter - 物理量単位変換ライブラリ

物理量の単位変換を行うPythonライブラリです。numpy配列と単一値の両方に対応し、光学・レーザー物理学でよく使用される物理量の変換をサポートしています。

## 対応物理量

- **フルエンス** (Fluence) - エネルギー密度
- **波長** (Wavelength) - 光の波長
- **波数** (Wavenumber) - 空間周波数
- **周波数** (Frequency) - 時間周波数
- **電場** (Electric Field) - 電場強度
- **強度** (Intensity) - 光強度

## インストール

```bash
pip install -r requirements.txt
```

## 基本的な使用方法

```python
import numpy as np
from unit_converter import UnitConverter

# コンバーターの初期化
converter = UnitConverter()

# 波長の変換
wavelength_nm = np.array([400, 500, 600, 700, 800])
wavelength_um = converter.convert_wavelength(wavelength_nm, 'nm', 'um')

# 波長から周波数への変換
frequency_thz = converter.wavelength_to_frequency(wavelength_nm, 'nm', 'THz')

# 強度から電場への変換
intensity_wpm2 = np.array([1e12, 1e13, 1e14])
electric_field_vpm = converter.intensity_to_electric_field(intensity_wpm2, 'W/m2', 'V/m')
```

## サポートされている単位

### 波長
- `m`, `cm`, `mm`, `um`, `nm`, `pm`, `angstrom`, `ft`, `in`

### 周波数
- `Hz`, `kHz`, `MHz`, `GHz`, `THz`

### 波数
- `1/m`, `1/cm`, `1/mm`, `1/um`, `1/nm`

### フルエンス
- `J/m2`, `mJ/m2`, `uJ/m2`, `nJ/m2`, `J/cm2`, `mJ/cm2`, `uJ/cm2`, `nJ/cm2`

### 電場
- `V/m`, `kV/m`, `MV/m`, `GV/m`

### 強度
- `W/m2`, `mW/m2`, `uW/m2`, `nW/m2`, `W/cm2`, `mW/cm2`, `uW/cm2`, `nW/cm2`

## 主要なメソッド

### 基本的な単位変換
- `convert_wavelength(wavelength, from_unit, to_unit)`
- `convert_frequency(frequency, from_unit, to_unit)`
- `convert_wavenumber(wavenumber, from_unit, to_unit)`
- `convert_fluence(fluence, from_unit, to_unit)`
- `convert_electric_field(electric_field, from_unit, to_unit)`
- `convert_intensity(intensity, from_unit, to_unit)`

### 物理量間の変換
- `wavelength_to_frequency(wavelength, wavelength_unit, frequency_unit)`
- `frequency_to_wavelength(frequency, frequency_unit, wavelength_unit)`
- `wavelength_to_wavenumber(wavelength, wavelength_unit, wavenumber_unit)`
- `wavenumber_to_wavelength(wavenumber, wavenumber_unit, wavelength_unit)`
- `intensity_to_electric_field(intensity, intensity_unit, electric_field_unit)`
- `electric_field_to_intensity(electric_field, electric_field_unit, intensity_unit)`

## 使用例

### レーザーパルスの物理量変換

```python
converter = UnitConverter()

# 波長: 800 nm
wavelength_nm = 800.0

# 対応する周波数
frequency_thz = converter.wavelength_to_frequency(wavelength_nm, 'nm', 'THz')
print(f"周波数: {frequency_thz:.2f} THz")

# 対応する波数
wavenumber_perm = converter.wavelength_to_wavenumber(wavelength_nm, 'nm', '1/m')
print(f"波数: {wavenumber_perm:.2e} 1/m")

# パルス強度: 1 TW/cm2
intensity_twpcm2 = 1.0
intensity_wpm2 = converter.convert_intensity(intensity_twpcm2, 'TW/cm2', 'W/m2')

# 対応する電場強度
electric_field_vpm = converter.intensity_to_electric_field(intensity_wpm2, 'W/m2', 'V/m')
electric_field_gvpm = converter.convert_electric_field(electric_field_vpm, 'V/m', 'GV/m')
print(f"電場強度: {electric_field_gvpm:.2f} GV/m")
```

### 配列データの一括変換

```python
# 複数の波長を一度に変換
wavelengths_nm = np.array([400, 500, 600, 700, 800])
wavelengths_um = converter.convert_wavelength(wavelengths_nm, 'nm', 'um')
frequencies_thz = converter.wavelength_to_frequency(wavelengths_nm, 'nm', 'THz')

print("波長と周波数の対応:")
for w_nm, w_um, f_thz in zip(wavelengths_nm, wavelengths_um, frequencies_thz):
    print(f"{w_nm} nm = {w_um:.3f} um = {f_thz:.2f} THz")
```

## 物理定数

ライブラリには以下の物理定数が含まれています：

- 光速: `C = 299792458.0 m/s`
- プランク定数: `H = 6.62607015e-34 J⋅s`
- 換算プランク定数: `HBAR = 1.054571817e-34 J⋅s`
- 真空の誘電率: `EPSILON0 = 8.8541878128e-12 F/m`
- 真空の透磁率: `MU0 = 1.25663706212e-6 H/m`

## テストの実行

```bash
python example_usage.py
```

## エラーハンドリング

サポートされていない単位を使用した場合、`ValueError`が発生します：

```python
try:
    result = converter.convert_wavelength(100, 'invalid_unit', 'nm')
except ValueError as e:
    print(f"エラー: {e}")
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
