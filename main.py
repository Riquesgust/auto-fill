#------ IMPORTS
from concurrent.futures import process
from pathlib import Path
from xml.etree.ElementInclude import include  # provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory
import pandas as pd  # flexible open source data analysis/manipulation tool
import os
import pathlib

#--------


def main():

    my_list = [ident,nFatura,mes,dataEmi,dataVenc,entregaACI,iluPlub,valorLiq, darf, valorBru]

            # append my list as a row in the dataframe.
    my_list = pd.Series(my_list)

            # append the list of keywords as a row to my dataframe.
    my_dataframe = my_dataframe.append(my_list, ignore_index=True)


    # rename dataframe columns using dictionaries.
    my_dataframe = my_dataframe.rename(
        columns={
            0: "Identificador",
            1: "N° Fatura",
            2: "Mês",
            3: "Data Emissão",
            4: "Data Vencimento",
            5: "Entrega ACI",
            6: "Iluminação Pública",
            7: "Valor Líquido",
            8: "DARF",
            9: "Valor Bruto",
        }
    )

    # extract my dataframe to an .xlsx file!
    my_dataframe.to_excel("sample_excel.xlsx", sheet_name="my dataframe")
    print("")
    print(my_dataframe)


if __name__ == "__main__":
    main()