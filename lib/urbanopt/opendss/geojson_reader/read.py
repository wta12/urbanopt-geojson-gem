import math
import logging
import os
import pandas as pd
import json

from ditto.readers.abstract_reader import AbstractReader
from ditto.store import Store
from ditto.models.node import Node
from ditto.models.line import Line
from ditto.models.wire import Wire
from ditto.models.powertransformer import PowerTransformer
from ditto.models.winding import Winding
from ditto.models.phase_winding import PhaseWinding
from ditto.models.base import Unicode
from ditto.models.position import Position
from ditto.models.feeder_metadata import Feeder_metadata
from ditto.models.capacitor import Capacitor
from ditto.models.phase_capacitor import PhaseCapacitor
from ditto.models.load import Load
from ditto.models.phase_load import PhaseLoad

class Reader(AbstractReader):
    """
    Reader for the Urbanopt geojson file with supporting database files
    """
    register_names = ["geojson","GeoJson"]
    
    def __init__(self, **kwargs):
        super(Reader,self).__init__(**kwargs)

        if "geojson_file" in kwargs:
            self.geojson_file = kwargs["geojson_file"]
            self.geojson_content = None
        else:
            raise ValueError("No geojson_file parameter provided")
        if "equipment_file" in kwargs:
            self.equipment_file = kwargs["equipment_file"]
            self.equipment_data = None
        else:
            raise ValueError("No equipment_file parameter provided")
        if "load_file" in kwargs:
            self.load_file = kwargs["load_file"]
            self.load_data = None
        else:
            raise ValueError("No load_file parameter provided")

    def get_geojson_data(self, filename):
        """
        Helper method to save all the json data in the geojson file
        """
        content = []
        try:
            with open(filename,"r") as f:
                content = json.load(f)
        except:
            raise IOError("Problem trying to read json from file "+filename)
        return content

    def get_equipment_data(self, filename):
        """
        Helper method to save all the json data in the equipment file
        """
        content = []
        try:
            with open(filename,"r") as f:
                content = json.load(f)
        except:
            raise IOError("Problem trying to read json from file "+filename)
        return content

    def get_load_data(self, filename):
        """
        Helper method to save all the json data in the load file
        """
        content = []
        # Populate this once we know the format
        return content

    def parse(self, model, **kwargs):
        """General parse function.
        Responsible for calling the sub-parsers and logging progress.
        :param model: DiTTo model
        :type model: DiTTo model
        :param verbose: Set verbose mode. Optional. Default=False
        :type verbose: bool
        :returns: 1 for success, -1 for failure
        :rtype: int
        """

        self.geojson_content = get_geojson_data(self.geojson_file)
        self.equipment_data = get_equipment_data(self.equipment_file)
        self.load_data = get_load_data(self.load_file)

        # Call parse from abstract reader class
        super(Reader, self).parse(model, **kwargs)
        return 1

    def parse_lines(self, model, **kwargs):
        """Line parser.
        :param model: DiTTo model
        :type model: DiTTo model
        :returns: 1 for success, -1 for failure
        :rtype: int
        """

        return 1

    def parse_nodes(self, model, **kwargs):
        """Node parser.
        :param model: DiTTo model
        :type model: DiTTo model
        :returns: 1 for success, -1 for failure
        :rtype: int
        """

        return 1

    def parse_transformers(self, model, **kwargs):
        """Transformer parser.
        :param model: DiTTo model
        :type model: DiTTo model
        :returns: 1 for success, -1 for failure
        :rtype: int
        """

        return 1

    def parse_capacitors(self, model, **kwargs):
        """Capacitor parser.
        :param model: DiTTo model
        :type model: DiTTo model
        :returns: 1 for success, -1 for failure
        :rtype: int
        """

        return 1

    def parse_loads(self, model, **kwargs):
        """Load parser.
        :param model: DiTTo model
        :type model: DiTTo model
        :returns: 1 for success, -1 for failure
        :rtype: int
        """

        return 1

            
    def parse_dg(self, model, **kwargs):
        """PV parser.
        :param model: DiTTo model
        :type model: DiTTo model
        :returns: 1 for success, -1 for failure
        :rtype: int
        """

        return 1

