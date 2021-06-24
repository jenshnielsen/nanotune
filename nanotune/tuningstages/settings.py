# Copyright (c) 2021 Jana Darulova
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from __future__ import annotations
from dataclasses import dataclass, asdict, is_dataclass
from typing import Optional, Sequence, Callable, Any, Union, Dict
import qcodes as qc
import nanotune as nt
from nanotune.classification.classifier import Classifier
from nanotune.device.device import NormalizationConstants


class Settings:
    def update(
        self,
        new_settings: Union[
            Dict[str, Sequence[Any]], Settings],
    ) -> None:
        if is_dataclass(new_settings):
            new_constants_dict = asdict(new_settings)
        elif isinstance(new_settings, Dict):
            new_constants_dict = new_settings
        else:
            raise ValueError('Invalid settings. Use the appropriate \
                 dataclass or a Dict instead.')

        for sett_type, setting in new_constants_dict.items():
            if not hasattr(self, sett_type):
                raise KeyError(f'Invalid setting subfield.')
            setattr(self, sett_type, setting)


@dataclass
class DataSettings(Settings):
    db_name: str = nt.config['db_name']
    db_folder: str = nt.config['db_folder']
    normalization_constants: Optional[NormalizationConstants] = None
    experiment_id: Optional[int] = None
    segment_db_name: str = f'segmented_{nt.config["db_name"]}'
    segment_db_folder: str = nt.config['db_folder']
    segment_experiment_id: Optional[int] = None
    segment_size: float = 0.02


@dataclass
class SetpointSettings(Settings):
    voltage_precision: float
    parameters_to_sweep: Optional[Sequence[qc.Parameter]] = None
    ranges_to_sweep: Optional[Sequence[Sequence[float]]] = None
    safety_voltage_ranges: Optional[Sequence[Sequence[float]]] = None
    setpoint_method: Optional[
        Callable[[Any], Sequence[Sequence[float]]]] = None


@dataclass
class Classifiers:
    pinchoff: Optional[Classifier] = None
    singledot: Optional[Classifier] = None
    doubledot: Optional[Classifier] = None
    dotregime: Optional[Classifier] = None