
import requests

def download_file(url, address):
    answer = requests.get(url, stream=True)
    if answer.status_code == requests.codes.OK:
        with open(address, 'wb') as new_file:
            for part in answer.iter_content(chunk_size=256):
                new_file.write(part)
        print('Download finished. Save in: {}'.format(address))
    else:
        answer.raise_for_status()

def file_type(file_download_link):
    file_type = file_download_link.split('.')
    
    return file_type[-1]

def attachment_number(file_download_link):
    attachment_number = file_download_link.split('/')
    attachment_number = file_download_link.split('_')

    return attachment_number[1]