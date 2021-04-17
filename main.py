#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import ctypes
import argparse

import cv2 as cv
import pyautogui
import numpy as np
from PIL import ImageGrab


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file_ext", type=str, default='jpg')
    parser.add_argument("--output_path", type=str, default='screenshot')

    parser.add_argument('--unuse_debug_window', action='store_true')

    args = parser.parse_args()

    return args


def main():
    # 引数解析 #################################################################
    args = get_args()

    file_ext = args.file_ext
    output_path = args.output_path

    unuse_debug_window = args.unuse_debug_window

    # 出力ディレクトリ作成 ######################################################
    os.makedirs(output_path, exist_ok=True)

    #  ########################################################################
    prev_key_state = 0x0000
    start_x, start_y = None, None
    prev_image = None

    capture_count = len(os.listdir(output_path))

    try:
        while True:
            # CTRLキー状態取得
            key_state = ctypes.windll.user32.GetAsyncKeyState(0x11)
            # マウス座標
            x, y = pyautogui.position()

            # CTRL 押し始め
            if (key_state == 0x8000) and (prev_key_state == 0x0000):
                start_x, start_y = x, y
                prev_key_state = key_state
            # CTRL 離す
            if (key_state == 0x0000) and (prev_key_state == 0x8000):
                # キャプチャ保存
                path_image_file = os.path.join(
                    output_path, '{:06}.'.format(capture_count) + file_ext)
                cv.imwrite(path_image_file, prev_image)
                capture_count = capture_count + 1

                # 変数リセット
                start_x, start_x = None, None
                prev_key_state = key_state
                prev_image = None

            # 選択範囲計算
            if start_x is not None and start_y is not None:
                select_width = x - start_x
                select_height = y - start_y

                if select_width > 0:
                    x1 = start_x
                    x2 = x1 + select_width
                else:
                    x1 = start_x + select_width
                    x2 = start_x

                if select_height > 0:
                    y1 = start_y
                    y2 = y1 + select_height
                else:
                    y1 = start_y + select_height
                    y2 = start_y

                # 前フレームの選択範囲がある場合はデバッグ表示
                if (prev_image is not None) and (unuse_debug_window == False):
                    debug_image = cv.resize(prev_image, (256, 256))
                    cv.imshow('ScreenShot Image', debug_image)

                # 選択範囲が0以上のサイズの場合、スクリーンショット取得
                if abs(select_width) > 0 and abs(select_height) > 0:
                    grab_image = np.array(ImageGrab.grab(bbox=(x1, y1, x2,
                                                               y2)))
                    grab_image = cv.cvtColor(grab_image, cv.COLOR_RGB2BGR)
                    prev_image = grab_image

            key = cv.waitKey(1)
            if key == 27:  # ESC
                break

        cv.destroyAllWindows()
    except KeyboardInterrupt:
        cv.destroyAllWindows()
        print('KeyboardInterrupt')


if __name__ == '__main__':
    main()
