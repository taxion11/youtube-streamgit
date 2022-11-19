import PyAutoGUI as pgui
import time
 
#キーボードのWinキーを押す
pgui.press('win')
#キーボードでexcelと入力
pgui.write('excel')
#画面が表示されるまで待機
time.sleep(1)
#キーボードのエンターを入力してEXCELを起動
pgui.press('enter')
#エクセルが起動するまで待機する。時間が読めないので、次の操作で使う画像の認識で判定
while pgui.locateOnScreen('empty_book.jpg' , confidence=0.9) is None:
    time.sleep(1)
#空白のブックアイコンの座標を取得
position=pgui.locateOnScreen('empty_book.jpg' , confidence=0.9)
#空白のブックアイコンをクリック
pgui.click(position)
#選択されているセルに任意の文字列を入力
pgui.write('Hello PyAutoGui')
#入力が完了するまで待機する
time.sleep(3)
#上書き保存のショートカットを入力
pgui.hotkey('ctrl','s')
#名前を付けて保存画面が表示されるのを待機する
time.sleep(3)
#このPCアイコンの座標を取得
position=pgui.locateOnScreen('this_pc.jpg' , confidence=0.9)
#このPCアイコンをクリック
pgui.click(position)
#画面遷移を待機する
time.sleep(1)
#キーボードのtabを3回押してファイル名入力のテキストボックスまで移動
pgui.press('tab',presses=3)
#キーボードでファイル名を入力
pgui.write('pytest')
#キーボードのエンターキーを押す
pgui.press('enter')
#キーボードのALT+F4を押してでExcel終了
pgui.hotkey('alt','f4')