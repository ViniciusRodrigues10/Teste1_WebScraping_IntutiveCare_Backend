<p align="center">
  <img src="https://user-images.githubusercontent.com/76957963/171772753-2ec5e2b4-16a6-46ba-9d15-e2988bd5efc2.png">
</p>

<h1 align="center"> Teste 1 WebScraping IntuitiveCare - Backend </h1>

## Descrição do projeto 

Teste 1 - WebScraping

Todas as tarefas deste teste devem ser executadas em código nas linguagens Python ou Java

1.1 - Acessar o site: https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude

1.2 - Baixar os Anexos I ao Anexo IV

![Untitled](https://user-images.githubusercontent.com/76957963/171771865-47104c73-a58e-40b0-ba2a-233dedb49340.png)

1.3 - Agrupar os anexos em um mesmo arquivo compactado (ZIP, RAR, ...)

## :computer: Tecnologias e Ferramentas 

- `Python 3`

- `Visual Studio Code`

- `Git & Github`

## :hammer: Funcionalidades do projeto

- `Funcionalidade 1`: Download de arquivos do site gov.br

- `Funcionalidade 2`: Gerar pastas para armazenar os arquivos obtidos

- `Funcionalidade 2a`: Compactar a pasta criado em um arquivo ZIP

## 📚: Bibliotecas utilizada

- `os`
- `zipfile`
- `requests`

## Funções desenvolvidas

   ### Função download_file(url, address)
   
   
      def download_file(url, address):
          answer = requests.get(url, stream=True)
          if answer.status_code == requests.codes.OK:
              with open(address, 'wb') as new_file:
                  for part in answer.iter_content(chunk_size=256):
                      new_file.write(part)
              print('Download finished. Save in: {}'.format(address))
          else:
              answer.raise_for_status()
    
   Função que tem como retorno void, utilizada apenas para acessar a url informada, fazer o dowload do arquivo e armazena-lo na pasta desejada
    
   #### Parâmetro: url
                      Recebe a url do arquivo que deseja realizar o download

   #### Parâmetro: address
                      Recebe o caminho que o arquivo deve ser armazenado
                      
   ### Função file_type(file_download_link)
    
      def file_type(file_download_link):
          file_type = file_download_link.split('.')

          return file_type[-1]
     
   Função que retorno uma string com o tipo do arquivo
     
   #### Parâmetro: file_download_link
                      Recebe o link do arquivo que deseja realizar o download
     
   ### Função attachment_number(file_download_link)
     
      def attachment_number(file_download_link):
          attachment_number = file_download_link.split('/')
          attachment_number = file_download_link.split('_')

          return attachment_number[1]
     
   Função que retorno uma string com o numero do anexo
     
   #### Parâmetro: file_download_link
                       Recebe o link do arquivo que deseja realizar o download

## Função main

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
    
## Autor

[<img src="https://user-images.githubusercontent.com/76957963/171774831-f51b4f04-1beb-498a-b7ab-a47a7af1d382.jpeg" width=115><br><sub>Vinícius Rodrigues</sub>](https://github.com/ViniciusRodrigues10)


