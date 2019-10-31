from __future__ import print_function
from SUPPORT_FUNCTIONS.variable_classes import *
from PedersenConductivity.collission_freq_calc import *
from Wind_perp_to_B.run_Wind_perp_to_B import *
from var


def run_wind_perp_to_B(dataframe, no_rows):
    for i in range(no_rows):
        B_vector=np.array([dataframe.Bx[i],dataframe.By[i],dataframe.Bz[i]])
        wind_vector=np.array([dataframe.v[i],dataframe.u[i],0])
        B_vector_square=B_vector**2
        B_norm_square=B_vector_square[0]+B_vector_square[1],B_vector_square[2]
        W_mult_B=B_vector*wind_vector
        W_dot_B=W_mult_B[0]+W_mult_B[1]+W_mult_B[2]
        Dot_to_Norm=W_dot_B/B_norm_square
        Wind_paral_B=Dot_to_Norm*B_vector

