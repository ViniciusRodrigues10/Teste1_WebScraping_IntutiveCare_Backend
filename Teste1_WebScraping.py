import os
from zipfile import *
from util import *

if __name__ == "__main__":

    BASE_URL = ['https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf', 
                'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf',
                'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf',
                'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf',
                'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.xlsx']
    OUTPUT_DIR = 'output'
    os.mkdir('./output')

    for i in range(len(BASE_URL)):
        name_file = os.path.join(OUTPUT_DIR, 'ANEXO_{}.{}'.format(attachment_number(BASE_URL[i]), file_type(BASE_URL[i])))
        download_file(BASE_URL[i], name_file)
    
    with ZipFile('dados.zip', 'w') as file_zip:
        for i in range(len(BASE_URL)):
            file_zip.write('output\ANEXO_{}.{}'.format(attachment_number(BASE_URL[i]), file_type(BASE_URL[i])))
                