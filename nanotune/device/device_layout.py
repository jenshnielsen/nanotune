# Copyright (c) 2021 Jana Darulova
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import List, Tuple

class IDeviceLayout(ABC):
    """Interface for device layout defining classes.

    Abstract class methods
    need to return gate IDs of gates fulfilling the function the method's name
    suggests.
    """

    @classmethod
    @abstractmethod
    def helper_gate(self) -> int:
        """Returns the `gate_id` of the additional gate such as a top barrier
        of a 2D layout or bottom gate below a 1D device.
        """
        pass

    @classmethod
    @abstractmethod
    def barriers(self) -> List[int]:
        """Returns a list of `gate_id` of barrier gates. E.g. left,
        central and right barrier. The order of gate IDs determines the
        order they are swept."""
        pass

    @classmethod
    @abstractmethod
    def plungers(self) -> List[int]:
        """Returns a list of `gate_id` of plunger gates, such as
        left and right plunger. The order of gate IDs determines the
        order they are swept."""
        pass

    @classmethod
    @abstractmethod
    def outer_barriers(self) -> List[int]:
        """Returns a list of `gate_id` of outer barrier gates.
        The order of gate IDs determines the order they are swept."""
        pass

    @classmethod
    @abstractmethod
    def central_barrier(self) -> int:
        """Returns the `gate_id` of the central barrier."""
        pass

    @classmethod
    @abstractmethod
    def plunger_barrier_pairs(self) ->List[Tuple[int, int]]:
        """Returns a list of tuples, where the first
        item of each tuple is a plunger and the second a barrier ID. These
        pairs belong to capacitiveley coupled plungers and barriers and
        indicated which barrier needs to be changed if a plunger reached
        its safety range when swept."""
        pass


@dataclass
class DataClassMixin:
    """A dataclass mixin."""


class DeviceLayout(DataClassMixin, IDeviceLayout):
    """An abstract data class."""


@dataclass
class DoubleDotLayout(DeviceLayout):
    """DeviceLayout subclass defining a 2D double dot layout. The attributes'
    values are the gates' IDs.
    """
    top_barrier = 0
    left_barrier = 1
    left_plunger = 2
    central_barrier_ = 3
    right_plunger = 4
    right_barrier = 5

    @classmethod
    def barriers(self) -> List[int]:
        """Returns list with left, central and right barrier IDs."""
        main_barriers = [
            self.left_barrier, self.central_barrier_, self.right_barrier,
        ]
        return main_barriers

    @classmethod
    def plungers(self) -> List[int]:
        """Returns list with left and right plunger IDs."""
        return [self.left_plunger, self.right_plunger]

    @classmethod
    def outer_barriers(self) -> List[int]:
        """Returns list with left and right barrier IDs."""
        return [self.left_barrier, self.right_barrier]

    @classmethod
    def plunger_barrier_pairs(self) ->List[Tuple[int, int]]:
        """Returns a list of tuples, where the left plunger forms a tuple with
        the left barrier and the right plunger with the right barrier. It
        indicates which barrier needs to be adjusted when a plunger reaches its
        safety range when swept.

        Returns:
            list: [(plunger ID, barrier ID)]
        """
        p_b_pairs = [
            (self.left_plunger, self.left_barrier),
            (self.right_plunger, self.right_barrier)
        ]
        return p_b_pairs

    @classmethod
    def central_barrier(self) -> int:
        """Returns the central barrier's gate ID."""
        return self.central_barrier_

    @classmethod
    def helper_gate(self) -> int:
        """Returns the top barrier's gate ID."""
        return self.top_barrier
