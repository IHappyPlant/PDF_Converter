"""This module contains utility functions for pdf converter."""
import os
import shutil
import tempfile
from os.path import basename, splitext

from numpy import array
from pdf2image import convert_from_path
from PIL import Image


class TempFolder:
    """
    This is a class to operate with temporary folder.

    :param str prefix: prefix for temp folder
    :param str suffix: suffix for temp folder
    """

    def __init__(self, prefix="pdf_converter_", suffix="_tmp", **kwargs):
        self.dirpath = tempfile.mkdtemp(
            prefix=prefix, suffix=suffix, **kwargs)

    def __getitem__(self, item):
        # noinspection PyTypeChecker
        return self.list_files()[item]

    def __len__(self):
        return len(self.list_files())

    def __iter__(self):
        self._itercnt = 0
        return self

    def __next__(self):
        if self._itercnt < len(self):
            item = self[self._itercnt]
            self._itercnt += 1
            return item
        raise StopIteration

    def __del__(self):
        self.remove()

    def read_by_index(self, index, as_array=True):
        """
        Read image by index as numpy array or Pillow image.

        :param int index: index of image in folder
        :param bool as_array: if True, read as numpy array
        """
        img = Image.open(self[index])
        # noinspection PyTypeChecker
        return array(img) if as_array else img

    def remove(self):
        """Remove temporary folder."""
        shutil.rmtree(self.dirpath, ignore_errors=True)

    def list_files(self):
        """Get names of files in temporary folder."""
        return [os.path.join(self.dirpath, f)
                for f in os.listdir(self.dirpath)]


def convert(file, dpi=300, image_format='jpg', color_mode='rgb'):
    """
    Convert pdf file to selected format.

    :param str file: Path to PDF file that need to be converted
    :param int dpi: DPI of converter
    :param str image_format: format of output file.
        Possible formats: ['jpg', 'png']
    :param str color_mode: Color mode of output images.
        Possible modes: ['rgb', 'rgba', 'grayscale']
    :return: temp folder with converted images
    :rtype: TempFolder
    """
    cpu_count = os.cpu_count() or 1

    transparent = color_mode == 'rgba'
    grayscale = color_mode == 'grayscale'

    output_folder = TempFolder()
    convert_from_path(file, dpi, fmt=image_format, transparent=transparent,
                      grayscale=grayscale, thread_count=cpu_count,
                      output_folder=output_folder.dirpath)

    return output_folder


def get_file_name(file_path):
    """
    :param str file_path: Path to file
    :return: Name of file without extension
    :rtype: str
    """
    return splitext(basename(file_path))[0]
