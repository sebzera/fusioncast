from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Optional, Tuple
import numpy as np
import warnings

try:                                                        # error check the fmi module import for the sake of the program not crashing if it's not installed.
    from fmiopendata.wfs import download_stored_query
    FMI_AVAILABLE = True
except ImportError as err:
    FMI_AVAILABLE = False
    warnings.warn("FMI Open Data API could not be imported. Please check fmiopendata installation.")
    
class FMIDataLoader:
    def __init__(self, cache_dir: str = 'data/raw/fmi_cache/', data_dir: str = 'data/raw/fmi_data/'):               # init function and setting defaults
        if not FMI_AVAILABLE:
            raise ImportError("FMI Open Data API is not available. Please check fmiopendata installation.")         # more error checks for the fmi module import
        self.cache_dir = Path(cache_dir)
        self.data_dir = Path(data_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # space for adding messages when the loader is is finished; like a welcome message or something.
        
    def download_latest(self) -> Tuple[np.ndarray, datetime]:
        comp = download_stored_query(self.RADAR_QUERY)
        if not comp.data:
            raise ValueError("No data returned from FMI API.")
        latest_time = max(comp.times[-1])
        latest_data = comp.data[-1]
        return latest_data, latest_time
    
data = FMIDataLoader.download_latest
print(data)