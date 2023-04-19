# The GPLv3 License (GPLv3)

# Copyright (c) 2023 Tushar Maharana, and Mihir Nallagonda

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Organism class and related stuff.

This module provides the Organism class, which represents an organism and its characteristics.
It also includes a function to generate a random organism.

Classes:
--------
    Organism: A class representing an organism.

Functions:
--------
    get_random_organism: A function to generate a random organism.

Note:
--------
Characteristics are stored as:
    0: ideal temperature
    1: trophic level
    2: energy requirement
    3: reproductive type
"""

from brain import NeuralNetwork
import genome as gn
import numpy as np
from typing import Union


class Organism:
    """
    A class representing an organism.

    Attributes:
    ---------
        genome: A string representing the organism's genome.

        characters: A NumPy array containing the organism's characteristics.

        neural_network: A neural network generated from the genome of the organism
    """

    def __init__(
        self,
        input_data: Union[str, np.ndarray],
        number_of_characters: int = 4,
    ) -> None:
        """
        Initializes an instance of the Organism class.

        Args:
        -----
            input_data : A string representing the organism's genome or a NumPy array
            containing the organism's characteristics.

            number_of_characters : The number of characteristics
        """

        # check if input is genome or characteristics

        if isinstance(input_data, np.ndarray):
            self.genome: str = gn.encode_organism_characteristics(
                input_data, number_of_characters
            )

            self.characters: np.ndarray = input_data

        elif isinstance(input_data, str):
            self.genome: str = input_data
            self.characters: np.ndarray = gn.decode_organism_characteristics(
                input_data, number_of_characters
            )

        # assign a neural_network generated from the the genome
        self.neural_network = NeuralNetwork(self.genome, np.array([2, 2]))


def get_random_organism(number_of_characters: int = 4) -> Organism:
    """
    Generate a random organism.

    Args:
    -----
        number_of_characters : The number of characteristics

    Returns:
    ---------
        Organism: A random instance of the Organism class.
    """
    return Organism(input_data=gn.get_random_genome(number_of_characters))
