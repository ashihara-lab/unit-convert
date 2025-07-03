#!/usr/bin/env python3
"""
UnitConverterクラスの使用例とテスト
"""

import numpy as np
from unit_converter import UnitConverter

def test_basic_conversions():
    """基本的な単位変換のテスト"""
    print("=== 基本的な単位変換のテスト ===")
    converter = UnitConverter()
    
    # 波長の変換テスト
    wavelength_nm = np.array([400, 500, 600, 700, 800])
    wavelength_um = converter.convert_wavelength(wavelength_nm, 'nm', 'um')
    print(f"波長変換: {wavelength_nm} nm = {wavelength_um} um")
    
    # 周波数の変換テスト
    frequency_hz = np.array([1e12, 2e12, 3e12])
    frequency_thz = converter.convert_frequency(frequency_hz, 'Hz', 'THz')
    print(f"周波数変換: {frequency_hz} Hz = {frequency_thz} THz")
    
    # フルエンスの変換テスト
    fluence_jpm2 = np.array([1e3, 1e4, 1e5])
    fluence_mjpcm2 = converter.convert_fluence(fluence_jpm2, 'J/m2', 'mJ/cm2')
    print(f"フルエンス変換: {fluence_jpm2} J/m2 = {fluence_mjpcm2} mJ/cm2")
    
    # 電場の変換テスト
    electric_field_vpm = np.array([1e6, 1e7, 1e8])
    electric_field_kvpm = converter.convert_electric_field(electric_field_vpm, 'V/m', 'kV/m')
    print(f"電場変換: {electric_field_vpm} V/m = {electric_field_kvpm} kV/m")
    
    # 強度の変換テスト
    intensity_wpm2 = np.array([1e12, 1e13, 1e14])
    intensity_wpcm2 = converter.convert_intensity(intensity_wpm2, 'W/m2', 'W/cm2')
    print(f"強度変換: {intensity_wpm2} W/m2 = {intensity_wpcm2} W/cm2")
    
    print()

def test_physical_conversions():
    """物理量間の変換テスト"""
    print("=== 物理量間の変換テスト ===")
    converter = UnitConverter()
    
    # 波長から周波数への変換
    wavelength_nm = np.array([400, 500, 600, 700, 800])
    frequency_thz = converter.wavelength_to_frequency(wavelength_nm, 'nm', 'THz')
    print(f"波長から周波数: {wavelength_nm} nm = {frequency_thz} THz")
    
    # 周波数から波長への変換（逆変換の確認）
    wavelength_nm_back = converter.frequency_to_wavelength(frequency_thz, 'THz', 'nm')
    print(f"周波数から波長: {frequency_thz} THz = {wavelength_nm_back} nm")
    print(f"逆変換の誤差: {np.abs(wavelength_nm - wavelength_nm_back)} nm")
    
    # 波長から波数への変換
    wavenumber_perm = converter.wavelength_to_wavenumber(wavelength_nm, 'nm', '1/m')
    print(f"波長から波数: {wavelength_nm} nm = {wavenumber_perm} 1/m")
    
    # 波数から波長への変換（逆変換の確認）
    wavelength_nm_back2 = converter.wavenumber_to_wavelength(wavenumber_perm, '1/m', 'nm')
    print(f"波数から波長: {wavenumber_perm} 1/m = {wavelength_nm_back2} nm")
    print(f"逆変換の誤差: {np.abs(wavelength_nm - wavelength_nm_back2)} nm")
    
    # 強度から電場への変換
    intensity_wpm2 = np.array([1e12, 1e13, 1e14])
    electric_field_vpm = converter.intensity_to_electric_field(intensity_wpm2, 'W/m2', 'V/m')
    print(f"強度から電場: {intensity_wpm2} W/m2 = {electric_field_vpm} V/m")
    
    # 電場から強度への変換（逆変換の確認）
    intensity_wpm2_back = converter.electric_field_to_intensity(electric_field_vpm, 'V/m', 'W/m2')
    print(f"電場から強度: {electric_field_vpm} V/m = {intensity_wpm2_back} W/m2")
    print(f"逆変換の誤差: {np.abs(intensity_wpm2 - intensity_wpm2_back)} W/m2")
    
    print()

def test_single_values():
    """単一値の変換テスト"""
    print("=== 単一値の変換テスト ===")
    converter = UnitConverter()
    
    # 単一値での変換
    wavelength_nm = 532.0
    wavelength_um = converter.convert_wavelength(wavelength_nm, 'nm', 'um')
    print(f"単一波長変換: {wavelength_nm} nm = {wavelength_um} um")
    
    frequency_thz = converter.wavelength_to_frequency(wavelength_nm, 'nm', 'THz')
    print(f"単一波長から周波数: {wavelength_nm} nm = {frequency_thz} THz")
    
    intensity_wpm2 = 1e14
    electric_field_vpm = converter.intensity_to_electric_field(intensity_wpm2, 'W/m2', 'V/m')
    print(f"単一強度から電場: {intensity_wpm2} W/m2 = {electric_field_vpm} V/m")
    
    print()

def test_error_handling():
    """エラーハンドリングのテスト"""
    print("=== エラーハンドリングのテスト ===")
    converter = UnitConverter()
    
    try:
        # サポートされていない単位での変換
        result = converter.convert_wavelength(100, 'invalid_unit', 'nm')
    except ValueError as e:
        print(f"期待されるエラー: {e}")
    
    try:
        # 無効な波長（ゼロ）での変換
        result = converter.wavelength_to_frequency(0, 'nm', 'THz')
    except ZeroDivisionError as e:
        print(f"期待されるエラー: {e}")
    
    print()

def practical_example():
    """実用的な例"""
    print("=== 実用的な例 ===")
    converter = UnitConverter()
    
    # レーザーパルスの例
    print("レーザーパルスの物理量変換例:")
    
    # 波長: 800 nm
    wavelength_nm = 800.0
    print(f"波長: {wavelength_nm} nm")
    
    # 対応する周波数
    frequency_thz = converter.wavelength_to_frequency(wavelength_nm, 'nm', 'THz')
    print(f"周波数: {frequency_thz:.2f} THz")
    
    # 対応する波数
    wavenumber_perm = converter.wavelength_to_wavenumber(wavelength_nm, 'nm', '1/m')
    print(f"波数: {wavenumber_perm:.2e} 1/m")
    
    # パルス強度: 1 TW/cm2
    intensity_twpcm2 = 1.0
    intensity_wpm2 = converter.convert_intensity(intensity_twpcm2, 'TW/cm2', 'W/m2')
    print(f"強度: {intensity_twpcm2} TW/cm2 = {intensity_wpm2:.2e} W/m2")
    
    # 対応する電場強度
    electric_field_vpm = converter.intensity_to_electric_field(intensity_wpm2, 'W/m2', 'V/m')
    print(f"電場強度: {electric_field_vpm:.2e} V/m")
    
    # 電場をGV/mに変換
    electric_field_gvpm = converter.convert_electric_field(electric_field_vpm, 'V/m', 'GV/m')
    print(f"電場強度: {electric_field_gvpm:.2f} GV/m")
    
    print()

def main():
    """メイン関数"""
    print("UnitConverter テストプログラム")
    print("=" * 50)
    
    test_basic_conversions()
    test_physical_conversions()
    test_single_values()
    test_error_handling()
    practical_example()
    
    print("すべてのテストが完了しました。")

if __name__ == "__main__":
    main() 