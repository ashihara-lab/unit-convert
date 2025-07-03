import numpy as np
from typing import Union, Tuple

class UnitConverter:
    """
    物理量の単位変換を行うクラス
    対応物理量: フルエンス、波長、波数、周波数、電場、intensity
    """
    
    # 物理定数
    C = 299792458.0  # 光速 [m/s]
    H = 6.62607015e-34  # プランク定数 [J⋅s]
    HBAR = 1.054571817e-34  # 換算プランク定数 [J⋅s]
    EPSILON0 = 8.8541878128e-12  # 真空の誘電率 [F/m]
    MU0 = 1.25663706212e-6  # 真空の透磁率 [H/m]
    
    def __init__(self):
        # 単位変換の辞書を初期化
        self._init_conversion_factors()
    
    def _init_conversion_factors(self):
        """単位変換係数を初期化"""
        # 長さの変換係数
        self.length_factors = {
            'm': 1.0,
            'cm': 1e-2,
            'mm': 1e-3,
            'um': 1e-6,
            'nm': 1e-9,
            'pm': 1e-12,
            'angstrom': 1e-10,
            'ft': 0.3048,
            'in': 0.0254
        }
        
        # 時間の変換係数
        self.time_factors = {
            's': 1.0,
            'ms': 1e-3,
            'us': 1e-6,
            'ns': 1e-9,
            'ps': 1e-12,
            'fs': 1e-15
        }
        
        # エネルギーの変換係数
        self.energy_factors = {
            'J': 1.0,
            'mJ': 1e-3,
            'uJ': 1e-6,
            'nJ': 1e-9,
            'pJ': 1e-12,
            'eV': 1.602176634e-19,
            'meV': 1.602176634e-22,
            'keV': 1.602176634e-16,
            'MeV': 1.602176634e-13
        }
        
        # 周波数の変換係数
        self.frequency_factors = {
            'Hz': 1.0,
            'kHz': 1e3,
            'MHz': 1e6,
            'GHz': 1e9,
            'THz': 1e12
        }
        
        # 電場の変換係数
        self.electric_field_factors = {
            'V/m': 1.0,
            'kV/m': 1e3,
            'MV/m': 1e6,
            'GV/m': 1e9
        }
        
        # 強度の変換係数
        self.intensity_factors = {
            'W/m2': 1.0,
            'mW/m2': 1e-3,
            'uW/m2': 1e-6,
            'nW/m2': 1e-9,
            'W/cm2': 1e4,
            'mW/cm2': 10.0,
            'uW/cm2': 1e-2,
            'nW/cm2': 1e-5
        }
    
    def convert_wavelength(self, wavelength: Union[float, np.ndarray], 
                          from_unit: str, to_unit: str) -> Union[float, np.ndarray]:
        """
        波長の単位変換
        
        Args:
            wavelength: 波長の値または配列
            from_unit: 変換前の単位 ('m', 'nm', 'um', 'angstrom' など)
            to_unit: 変換後の単位
            
        Returns:
            変換後の波長の値または配列
        """
        if from_unit not in self.length_factors or to_unit not in self.length_factors:
            raise ValueError(f"サポートされていない単位: {from_unit} または {to_unit}")
        
        # 基本単位（メートル）に変換
        base_value = wavelength * self.length_factors[from_unit]
        # 目標単位に変換
        return base_value / self.length_factors[to_unit]
    
    def convert_frequency(self, frequency: Union[float, np.ndarray], 
                         from_unit: str, to_unit: str) -> Union[float, np.ndarray]:
        """
        周波数の単位変換
        
        Args:
            frequency: 周波数の値または配列
            from_unit: 変換前の単位 ('Hz', 'kHz', 'THz' など)
            to_unit: 変換後の単位
            
        Returns:
            変換後の周波数の値または配列
        """
        if from_unit not in self.frequency_factors or to_unit not in self.frequency_factors:
            raise ValueError(f"サポートされていない単位: {from_unit} または {to_unit}")
        
        # 基本単位（Hz）に変換
        base_value = frequency * self.frequency_factors[from_unit]
        # 目標単位に変換
        return base_value / self.frequency_factors[to_unit]
    
    def convert_wavenumber(self, wavenumber: Union[float, np.ndarray], 
                          from_unit: str, to_unit: str) -> Union[float, np.ndarray]:
        """
        波数の単位変換
        
        Args:
            wavenumber: 波数の値または配列
            from_unit: 変換前の単位 ('1/m', '1/cm', '1/mm' など)
            to_unit: 変換後の単位
            
        Returns:
            変換後の波数の値または配列
        """
        # 波数の単位変換係数
        wavenumber_factors = {
            '1/m': 1.0,
            '1/cm': 1e2,
            '1/mm': 1e3,
            '1/um': 1e6,
            '1/nm': 1e9
        }
        
        if from_unit not in wavenumber_factors or to_unit not in wavenumber_factors:
            raise ValueError(f"サポートされていない単位: {from_unit} または {to_unit}")
        
        # 基本単位（1/m）に変換
        base_value = wavenumber * wavenumber_factors[from_unit]
        # 目標単位に変換
        return base_value / wavenumber_factors[to_unit]
    
    def convert_fluence(self, fluence: Union[float, np.ndarray], 
                       from_unit: str, to_unit: str) -> Union[float, np.ndarray]:
        """
        フルエンス（エネルギー密度）の単位変換
        
        Args:
            fluence: フルエンスの値または配列
            from_unit: 変換前の単位 ('J/m2', 'mJ/cm2', 'uJ/cm2' など)
            to_unit: 変換後の単位
            
        Returns:
            変換後のフルエンスの値または配列
        """
        # フルエンスの単位変換係数
        fluence_factors = {
            'J/m2': 1.0,
            'mJ/m2': 1e-3,
            'uJ/m2': 1e-6,
            'nJ/m2': 1e-9,
            'J/cm2': 1e4,
            'mJ/cm2': 10.0,
            'uJ/cm2': 1e-2,
            'nJ/cm2': 1e-5
        }
        
        if from_unit not in fluence_factors or to_unit not in fluence_factors:
            raise ValueError(f"サポートされていない単位: {from_unit} または {to_unit}")
        
        # 基本単位（J/m2）に変換
        base_value = fluence * fluence_factors[from_unit]
        # 目標単位に変換
        return base_value / fluence_factors[to_unit]
    
    def convert_electric_field(self, electric_field: Union[float, np.ndarray], 
                              from_unit: str, to_unit: str) -> Union[float, np.ndarray]:
        """
        電場の単位変換
        
        Args:
            electric_field: 電場の値または配列
            from_unit: 変換前の単位 ('V/m', 'kV/m', 'MV/m' など)
            to_unit: 変換後の単位
            
        Returns:
            変換後の電場の値または配列
        """
        if from_unit not in self.electric_field_factors or to_unit not in self.electric_field_factors:
            raise ValueError(f"サポートされていない単位: {from_unit} または {to_unit}")
        
        # 基本単位（V/m）に変換
        base_value = electric_field * self.electric_field_factors[from_unit]
        # 目標単位に変換
        return base_value / self.electric_field_factors[to_unit]
    
    def convert_intensity(self, intensity: Union[float, np.ndarray], 
                         from_unit: str, to_unit: str) -> Union[float, np.ndarray]:
        """
        強度（Intensity）の単位変換
        
        Args:
            intensity: 強度の値または配列
            from_unit: 変換前の単位 ('W/m2', 'W/cm2', 'mW/cm2' など)
            to_unit: 変換後の単位
            
        Returns:
            変換後の強度の値または配列
        """
        if from_unit not in self.intensity_factors or to_unit not in self.intensity_factors:
            raise ValueError(f"サポートされていない単位: {from_unit} または {to_unit}")
        
        # 基本単位（W/m2）に変換
        base_value = intensity * self.intensity_factors[from_unit]
        # 目標単位に変換
        return base_value / self.intensity_factors[to_unit]
    
    def wavelength_to_frequency(self, wavelength: Union[float, np.ndarray], 
                               wavelength_unit: str, frequency_unit: str) -> Union[float, np.ndarray]:
        """
        波長から周波数への変換
        
        Args:
            wavelength: 波長の値または配列
            wavelength_unit: 波長の単位
            frequency_unit: 周波数の単位
            
        Returns:
            周波数の値または配列
        """
        # 波長をメートルに変換
        wavelength_m = self.convert_wavelength(wavelength, wavelength_unit, 'm')
        # 周波数を計算 (f = c/λ)
        frequency_hz = self.C / wavelength_m
        # 目標単位に変換
        return self.convert_frequency(frequency_hz, 'Hz', frequency_unit)
    
    def frequency_to_wavelength(self, frequency: Union[float, np.ndarray], 
                               frequency_unit: str, wavelength_unit: str) -> Union[float, np.ndarray]:
        """
        周波数から波長への変換
        
        Args:
            frequency: 周波数の値または配列
            frequency_unit: 周波数の単位
            wavelength_unit: 波長の単位
            
        Returns:
            波長の値または配列
        """
        # 周波数をHzに変換
        frequency_hz = self.convert_frequency(frequency, frequency_unit, 'Hz')
        # 波長を計算 (λ = c/f)
        wavelength_m = self.C / frequency_hz
        # 目標単位に変換
        return self.convert_wavelength(wavelength_m, 'm', wavelength_unit)
    
    def wavelength_to_wavenumber(self, wavelength: Union[float, np.ndarray], 
                                wavelength_unit: str, wavenumber_unit: str) -> Union[float, np.ndarray]:
        """
        波長から波数への変換
        
        Args:
            wavelength: 波長の値または配列
            wavelength_unit: 波長の単位
            wavenumber_unit: 波数の単位
            
        Returns:
            波数の値または配列
        """
        # 波長をメートルに変換
        wavelength_m = self.convert_wavelength(wavelength, wavelength_unit, 'm')
        # 波数を計算 (k = 2π/λ)
        wavenumber_perm = 2 * np.pi / wavelength_m
        # 目標単位に変換
        return self.convert_wavenumber(wavenumber_perm, '1/m', wavenumber_unit)
    
    def wavenumber_to_wavelength(self, wavenumber: Union[float, np.ndarray], 
                                wavenumber_unit: str, wavelength_unit: str) -> Union[float, np.ndarray]:
        """
        波数から波長への変換
        
        Args:
            wavenumber: 波数の値または配列
            wavenumber_unit: 波数の単位
            wavelength_unit: 波長の単位
            
        Returns:
            波長の値または配列
        """
        # 波数を1/mに変換
        wavenumber_perm = self.convert_wavenumber(wavenumber, wavenumber_unit, '1/m')
        # 波長を計算 (λ = 2π/k)
        wavelength_m = 2 * np.pi / wavenumber_perm
        # 目標単位に変換
        return self.convert_wavelength(wavelength_m, 'm', wavelength_unit)
    
    def intensity_to_electric_field(self, intensity: Union[float, np.ndarray], 
                                   intensity_unit: str, electric_field_unit: str) -> Union[float, np.ndarray]:
        """
        強度から電場への変換
        
        Args:
            intensity: 強度の値または配列
            intensity_unit: 強度の単位
            electric_field_unit: 電場の単位
            
        Returns:
            電場の値または配列
        """
        # 強度をW/m2に変換
        intensity_wpm2 = self.convert_intensity(intensity, intensity_unit, 'W/m2')
        # 電場を計算 (E = sqrt(2*I/(c*ε0)))
        electric_field_vpm = np.sqrt(2 * intensity_wpm2 / (self.C * self.EPSILON0))
        # 目標単位に変換
        return self.convert_electric_field(electric_field_vpm, 'V/m', electric_field_unit)
    
    def electric_field_to_intensity(self, electric_field: Union[float, np.ndarray], 
                                   electric_field_unit: str, intensity_unit: str) -> Union[float, np.ndarray]:
        """
        電場から強度への変換
        
        Args:
            electric_field: 電場の値または配列
            electric_field_unit: 電場の単位
            intensity_unit: 強度の単位
            
        Returns:
            強度の値または配列
        """
        # 電場をV/mに変換
        electric_field_vpm = self.convert_electric_field(electric_field, electric_field_unit, 'V/m')
        # 強度を計算 (I = (1/2)*c*ε0*E^2)
        intensity_wpm2 = 0.5 * self.C * self.EPSILON0 * electric_field_vpm**2
        # 目標単位に変換
        return self.convert_intensity(intensity_wpm2, 'W/m2', intensity_unit)


# 使用例とテスト用の関数
def example_usage():
    """使用例"""
    converter = UnitConverter()
    
    # 波長の変換例
    wavelength_nm = np.array([400, 500, 600, 700, 800])
    wavelength_um = converter.convert_wavelength(wavelength_nm, 'nm', 'um')
    print(f"波長変換: {wavelength_nm} nm = {wavelength_um} um")
    
    # 波長から周波数への変換
    frequency_thz = converter.wavelength_to_frequency(wavelength_nm, 'nm', 'THz')
    print(f"波長から周波数: {wavelength_nm} nm = {frequency_thz} THz")
    
    # 強度の変換例
    intensity_wpm2 = np.array([1e12, 1e13, 1e14])
    intensity_wpcm2 = converter.convert_intensity(intensity_wpm2, 'W/m2', 'W/cm2')
    print(f"強度変換: {intensity_wpm2} W/m2 = {intensity_wpcm2} W/cm2")
    
    # 強度から電場への変換
    electric_field_vpm = converter.intensity_to_electric_field(intensity_wpm2, 'W/m2', 'V/m')
    print(f"強度から電場: {intensity_wpm2} W/m2 = {electric_field_vpm} V/m")


if __name__ == "__main__":
    example_usage() 