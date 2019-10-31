from __future__ import print_function
import pandas as pd
import os
import sys
from SUPPORT_FUNCTIONS.export_data import export_msise00
import SUPPORT_FUNCTIONS.variable_classes as variable_classes
from SUPPORT_FUNCTIONS.variable_classes import input_parameters_past
from SUPPORT_FUNCTIONS.load_data import *
from Wind_perp_to_B.run_Wind_perp_to_B import *


def load_data_wind_perp_to_B(hwm_file_full_path, igrf_file_full_path):
    if hwm_file_full_path is None or len(igrf_file_full_path) == 0:
        return ""
    subname = os.path.splitext(os.path.basename(hwm_file_full_path))[0].split("_")[0]
    export_name = os.path.dirname(hwm_file_full_path) + '/' + subname + '_' + 'Wind_perp_to_B.csv'
    input_igrf_data_file = pd.read_csv(igrf_file_full_path)
    input_hwm_data_file = pd.read_csv(hwm_file_full_path)
    igrf_no_rows = input_igrf_data_file.shape[0]
    hwm_no_rows = input_hwm_data_file.shape[0]

    if (igrf_no_rows == hwm_no_rows) :
        no_rows = igrf_no_rows
        Input = [input_wind_perp_to_B() for _ in range(no_rows)]
        load_data_wind_perp_to_B(input_igrf_data_file, Input, no_rows)
        run_wind_perp_to_B(Input, no_rows)
        df_results = pd.DataFrame({'V_O2plus_sec^-1': Outputs["V_O2plus"],
                                   'V_Oplus_sec^-1': Outputs["V_Oplus"],
                                   'V_NOplus_sec^-1': Outputs["V_NOplus"],
                                   'V_e_sec^-1': Outputs["V_e"],
                                   'Omega_O2plus_sec^-1': Outputs["V_O2plus"],
                                   'Omega_Oplus_sec^-1': Outputs["V_Oplus"],
                                   'Omega_NOplus_sec^-1': Outputs["V_NOplus"],
                                   'Omega_e_sec^-1': Outputs["V_e"],
                                   'r_O2plus': Outputs["V_O2plus"],
                                   'r_Oplus': Outputs["V_Oplus"],
                                   'r_NOplus': Outputs["V_NOplus"],
                                   'r_e': Outputs["V_e"],
                                   'sigmap_S/m': Outputs["sigmap"]  # ,
                                   # 'sigmap_error_S/m': Outputs["sigmap_error"],
                                   # 'sigmap_error_percentage': Outputs["sigmap_error_percentage"]
                                   },
                                  index=input_msise_data_file.index)
        basic_inform = input_msise_data_file.filter(
            items=['Epoch(UTCG)', 'Lat_GEOD(deg)', 'Lon_GEOD(deg)', 'Height_WGS84 (km)'])
        export_dataframe = pd.concat([basic_inform, df_results], axis=1, sort=False)
        export_dataframe.to_csv(export_name, index=None)
        return export_name
    else:
        return "files cannot be processed because of different number of rows\n"
