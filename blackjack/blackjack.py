import pyautogui as pgui,cv2,webbrowser,time,random,threading,tkinter

def deal():
    #ディールを押す
    pos=0
    A=False
    for pos in pgui.locateAllOnScreen("img\Deal.PNG",confidence=.6):
        if len(pos)>0:
            A=True
            break
    if A==True:
        x, y = pgui.center(pos)
        time.sleep(0.1)
        pgui.click(x, y)

def line_select():
    #3つの線を判断してクリック
    A=False
    LINE=["img\Redline.PNG","img\Greenline.PNG","img\Brueline.PNG"]
    pos=0
    for i in LINE:
        for pos in pgui.locateAllOnScreen(i,confidence=.6):
            if len(pos)>0:
                A=True
                break
    if A==True:
        x, y = pgui.center(pos)
        time.sleep(0.1)
        pgui.click(x+10, y)

def judge():
    #勝利判定
    Judge=False
    win=False
    lose=False
    even=False
    Line=False

    for i in range(50):
        for mark in pgui.locateAllOnScreen("img\Mark.PNG",confidence=.8):
            if len(mark)>0:
                Line=True
                Judge=True
                break
        for PING in pgui.locateAllOnScreen("img\Win.PNG",confidence=.5):
            if len(PING)>0:
                win=True
                Judge=True
                break
        for PING in pgui.locateAllOnScreen("img\Win.PNG",confidence=.5):
            if len(PING)>0:
                win=True
                Judge=True
                break
        for Lose in pgui.locateAllOnScreen("img\Rebet.PNG",confidence=.6):
            if len(Lose)>0:
                lose=True
                Judge=True
                break
        for Even in pgui.locateAllOnScreen("img\Even.PNG",confidence=.6):
            if len(Even)>0:
                even=True
                Judge=True
                break
        if Judge==True:
            break

    if Line==True:
        return "Line"
    elif win==True:
        return "win"
    elif even==True:
        return "even"
    else:
        return "lose"

def bet(count):
    pos=0
    for pos in pgui.locateAllOnScreen("img\Bet.PNG",confidence=.6):
            if len(pos)>0:
                A=True
                break
    if A==True:
        x, y = pgui.center(pos)
        for i in range(count):
            time.sleep(0.2)
            pgui.click(x, y)

def cont():
    #６０分経過後のコンティニューを押す
    pos=0
    A=False
    time.sleep(0.3)
    for pos in pgui.locateAllOnScreen("img\Continue.PNG",confidence=.6):
        if len(pos)>0:
            A=True
            break
    if A==True:
        x, y = pgui.center(pos)
        pgui.click(150, 150) 
        time.sleep(1)
        pgui.click(x, y)

#実装
def game(count):
    Judge="cat"
    cont()
    time.sleep(2)
    bet(count)
    time.sleep(3)
    deal()
    time.sleep(3)
    for i in range(12):
        Judge=judge()
        time.sleep(0.1)
        if Judge=="Line":
            line_select()
        if Judge=="win":
            return "win"
            break
        if Judge=="lose":
            return "lose"
            break
        if Judge=="even":
            return "even"
            break

def start():
    global flg
    #1-3-2-4システム
    Blist=[1,3,2,4]
    Bcount=0
    total_benef=0
    game_count2=0
    win_count=0
    even_count=0
    lose_count=0
    game_count=int(txt.get())

    
    for i in range(game_count):
        cont()
        game_count2+=1
        betting2=Blist[Bcount]
        result=game(betting2)
        print(str(betting2)+result,end=" ")
        if result=="win":
            win_count+=1
            Bcount+=1
            total_benef+=betting2
            if Bcount==4:
                Bcount=0
        elif result=="lose":
            lose_count+=1
            Bcount=0
            total_benef-=betting2
        elif result=="even":
            even_count+=1
        label_gamecount["text"] = str(game_count2)
        label_wincount["text"] = str(win_count)
        label_evencount["text"] = str(even_count)
        label_losecount["text"] = str(lose_count)
        label_total["text"] = str(total_benef)
        
        #矯正停止
        if flg==False:
            break
def stop():
    global flg
    flg = False    

#ウィンドウ作成
import tkinter
flg=True


# Tkクラス生成
frm = tkinter.Tk()
# 画面サイズ
frm.geometry('600x400')
# 画面タイトル
frm.title('ブラックジャック自働化')
# ボタン：開始
btn = tkinter.Button(frm, text='1-3-2-4法開始',bg='#f0e68c',width=20 ,command=start)
btn.place(x=50, y=50)
# ラベル
lbl = tkinter.Label(text='試行回数')
lbl.place(x=50, y=90)
txt = tkinter.Entry(width=10)
txt.place(x=120, y=90)
txt.insert(tkinter.END,"10")


# ラベル ゲーム数
label_gamecount_tag = tkinter.Label(text = 'ゲーム数:')
label_gamecount_tag.place(x=50, y=120)
label_gamecount = tkinter.Label()
label_gamecount.place(x=120, y=120)
# ラベル win数
label_wincount_tag = tkinter.Label(text = 'win:')
label_wincount_tag.place(x=50, y=150)
label_wincount = tkinter.Label()
label_wincount.place(x=100, y=150)
# ラベル even数
label_evencount_tag = tkinter.Label(text = 'even:')
label_evencount_tag.place(x=150, y=150)
label_evencount = tkinter.Label()
label_evencount.place(x=200, y=150)
# ラベル lose数
label_losecount_tag = tkinter.Label(text = 'lose:')
label_losecount_tag.place(x=250, y=150)
label_losecount = tkinter.Label()
label_losecount.place(x=300, y=150)
# ラベル 損益
label_total_tag = tkinter.Label(text = 'total:')
label_total_tag.place(x=50, y=170)
label_total = tkinter.Label()
label_total.place(x=100, y=170)


# ボタン：停止
btn2 = tkinter.Button(text="停止",bg='#f0e68c',width=20,command=stop)
btn2.place(x=50, y=220)

# 画面をそのまま表示



if __name__ == '__main__':
    frm.mainloop()