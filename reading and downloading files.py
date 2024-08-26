import pandas as pd
import requests
import os

## Download images
def download_imgs(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Image successfully downloaded to path: {save_path}")
        else:
            print(f"Failed to retrive image from {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

## Read excel
def url_from_excel(excel_file, url_column_name, output_dir):
    df = pd.read_excel(excel_file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for index, row in df.iterrows():
        url = row[url_column_name]

        if pd.notna(url):
            filename = os.path.join(output_dir, f"image_{index+1}.jpg")
            download_imgs(url, filename)
        
if __name__ == '__main__':
    file = '../CHIC/Little_box_scraping.xlsx'
    url_column_name = 'image'
    output_dir = 'Images'

    url_from_excel(file, url_column_name, output_dir)
        