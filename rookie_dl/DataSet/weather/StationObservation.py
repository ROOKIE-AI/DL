import os
import gzip
import datetime
import requests
from typing import Union

import pandas as pd
import numpy as np
from loguru import logger


class NoaaStationObs:
    """

    """

    def __init__(self, site_no: str, year: Union[str, int]):
        self.site_no = site_no
        self.year = year
        self.raw_fp = self._download(site_no, year)  # 下载数据
        self.var_names = (
            'time', 'AirTemperature', 'DewPointTemperature',
            'SeaLevelPressure', 'WindDirection', 'WindSpeedRate'
        )
        self.units = (
            'UTC', '℃', '℃', 'hPa', '°', 'm/s'
        )

        self.data = self._handle(self.raw_fp)

    def _download(self, site_no: str, year: Union[str, int]) -> str:
        """
        下载文件
        :params url: 下载路径
        return:
            文件路径
        """
        url = f"https://www.ncei.noaa.gov/pub/data/noaa/isd-lite/{year}/{site_no}-{year}.gz"
        gz_filepath = download_file_from_url(url, ".")
        ungz_filepath = gz_filepath.replace('.gz', '')  # 解压后文件路径
        gfile = gzip.GzipFile(gz_filepath)
        with open(ungz_filepath, 'wb+') as unf:
            unf.write(gfile.read())
        gfile.close()
        os.remove(gz_filepath)

        return ungz_filepath

    def _handle(self, raw_fp):
        """
        处理原始文件
        :params raw_fp: 下载的原始数据路径
        return: 处理后的文件
        """
        with open(raw_fp, 'r') as f:
            lines = [line.split() for line in f.readlines()]
            table = [[datetime.datetime.strptime(f"{line[0]}-{line[1]}-{line[2]} {line[3]}", "%Y-%m-%d %H"), *line[4:9]]
                     for
                     line in lines]
            df = pd.DataFrame(columns=self.var_names, data=table)
            df = df.replace("-9999", np.nan)
            df = df.astype({k: float for k in self.var_names[1:]})

            # 缩放值还原
            for k in ('AirTemperature', 'DewPointTemperature', 'SeaLevelPressure', 'WindSpeedRate'):
                df[k] /= 10
            # # 将Temperature转为开尔文温度
            # df['AirTemperature'] += 273.15
            # df['DewPointTemperature'] += 273.15

            # 对数据进行逐小时补齐
            df.set_index('time', inplace=True)
            year = df.index[0].year
            full_index = pd.date_range(f'{year}-01-01', f'{year + 1}-01-01', freq='h')
            df = df.reindex(full_index, method='nearest').iloc[:-1]

            # 对缺测数据插值质控
            df.interpolate(method='linear', inplace=True)

        return df


def download_file_from_url(url, save_dir):
    """
    根据给定的URL下载文件并保存到指定目录,文件名自动处理。

    Args:
        url (str): 要下载的文件的URL。
        save_dir (str): 保存文件的目录路径。

    Returns:
        filepath (str): 下载文件路径
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        filename = os.path.basename(url)  # 获取URL中的文件名
        with open(os.path.join(save_dir, filename), 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return os.path.join(save_dir, filename)
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while downloading the file: {e}")
    except FileNotFoundError as e:
        logger.error(f"An error occurred while saving the file: {e}")


if __name__ == '__main__':
    # download_file_from_url('https://www.ncei.noaa.gov/pub/data/noaa/isd-lite/2020/545110-99999-2020.gz', '.')
    noaa_data = NoaaStationObs('545110-99999', 2010)
    print(noaa_data.data)
