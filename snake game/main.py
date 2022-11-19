# pygameを読み込む
import pygame
# sysライブラリを読み込む
import sys
# pygameのlocalsファイルにあるすべての変数、関数、クラスを読み込む
from pygame.locals import *
# GUI表示ライブラリtkinterを読み込む
import tkinter as tk
# os関連の処理をするosライブラリを読み込む
import os
# snake.pyにあるすべての変数、関数、クラスを読み込む
from snake import *
# food.pyにあるすべての変数、関数、クラスを読み込む
from food import *
# background.pyにあるすべての変数、関数、クラスを読み込む
from background import *
# effects.pyにあるすべての変数、関数、クラスを読み込む
from effects import *

class Game:
  """
  Gameクラス
  Game全体を管理するクラス
  """
  #画面の大きさ
  SIZE = WIDTH,HEIGHT=(800,800)
  #色情報をRGBで管理
  WHITE =(255,255,255)
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)

  #frame per second、1秒あたりのフレーム数。フレーム数が多いと滑らかになるが処理が遅くなる
  fps =20
  #スコア
  score = 0

  def __init__(self):
    """
    初期化関数
    """
    # 謎の処理
    os.environ["SDL_VIDEO_WINDOW_POS"] = f'{(tk.Tk().winfo_screenwidth() - self.WIDTH) // 2},' \
      f'{(tk.Tk().winfo_screenheight() - self.HEIGHT) // 2}'
    
    #pygame mixerの初期設定
    pygame.mixer.pre_init(44100,-16,2,2048)
    pygame.mixer.init()
    # pygameの初期化
    pygame.init()
    #MIDファイルのロード
    pygame.mixer.music.load("System/Sounds/music.mid")
    # 音楽を再生
    pygame.mixer.music.play(9)
    # ゲーム表示画面のキャプション名を設定
    pygame.display.set_caption("snake")

    