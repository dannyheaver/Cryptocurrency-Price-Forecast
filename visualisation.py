import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('crypto_prices', path='https://www.kaggle.com/datasets/eisgandar/internet-of-things-coins-historical-prices', unzip=True)
