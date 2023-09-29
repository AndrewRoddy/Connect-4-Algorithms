#all code written by Andrew Roddy
GameRunning,Winner,playAgain = True,"Nobody","yes"
def BigText():
	 print("\n   ____                            _     _  _\n  / ___|___  _ __  _ __   ___  ___| |_  | || |\n | |   / _ \| '_ \| '_ \ / _ \/ __| __| | || |_\n | |__| (_) | | | | | | |  __/ (__| |_  |__   _|\n  \____\___/|_| |_|_| |_|\___|\___|\__|    |_|\n\n\n")
def Variables():
	global aa,ab,ac,ad,ae,af,ba,bb,bc,bd,be,bf,ca,cb,cc,cd,ce,cf,da,db,dc,dd,de,df,ea,eb,ec,ed,ee,ef,fa,fb,fc,fd,fe,ff,ga,gb,gc,gd,ge,gf
	aa,ab,ac,ad,ae,af,ba,bb,bc,bd,be,bf,ca,cb,cc,cd,ce,cf,da,db,dc,dd,de,df,ea,eb,ec,ed,ee,ef,fa,fb,fc,fd,fe,ff,ga,gb,gc,gd,ge,gf,GameRunning,Winner = "_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_", True,"Nobody"
	Winner = "Nobody"
def DisplayBoard():
	global aa,ab,ac,ad,ae,af,ba,bb,bc,bd,be,bf,ca,cb,cc,cd,ce,cf,da,db,dc,dd,de,df,ea,eb,ec,ed,ee,ef,fa,fb,fc,fd,fe,ff,ga,gb,gc,gd,ge,gf,board
	board = [af,bf,cf,df,ef,ff,gf,ae,be,ce,de,ee,fe,ge,ad,bd,cd,dd,ed,fd,gd,ac,bc,cc,dc,ec,fc,gc,ab,bb,cb,db,eb,fb,gb,aa,ba,ca,da,ea,fa,ga]
	print(f"""1 2 3 4 5 6 7""")
	print (*board[0:7], sep =' ')
	print (*board[7:14], sep =' ')
	print (*board[14:21], sep =' ')
	print (*board[21:28], sep =' ')
	print (*board[28:35], sep =' ')
	print (*board[35:42], sep =' ')
	print(f"""1 2 3 4 5 6 7""")
def playerTurn():
	global aa,ab,ac,ad,ae,af,ba,bb,bc,bd,be,bf,ca,cb,cc,cd,ce,cf,da,db,dc,dd,de,df,ea,eb,ec,ed,ee,ef,fa,fb,fc,fd,fe,ff,ga,gb,gc,gd,ge,gf,turnNumber
	if turnNumber == "1":
		if aa == "_":aa = player
		elif ab == "_":ab = player
		elif ac == "_":ac = player
		elif ad == "_":ad = player
		elif ae == "_":ae = player
		elif af == "_":af = player
	if turnNumber == "2":
		if ba == "_":ba = player
		elif bb == "_":bb = player
		elif bc == "_":bc = player
		elif bd == "_":bd = player
		elif be == "_":be = player
		elif bf == "_":bf = player
	if turnNumber == "3":
		if ca == "_":ca = player
		elif cb == "_":cb = player
		elif cc == "_":cc = player
		elif cd == "_":cd = player
		elif ce == "_":ce = player
		elif cf == "_":cf = player
	if turnNumber == "4":
		if da == "_":da = player
		elif db == "_":db = player
		elif dc == "_":dc = player
		elif dd == "_":dd = player
		elif de == "_":de = player
		elif df == "_":df = player
	if turnNumber == "5":
		if ea == "_":ea = player
		elif eb == "_":eb = player
		elif ec == "_":ec = player
		elif ed == "_":ed = player
		elif ee == "_":ee = player
		elif ef == "_":ef = player
	if turnNumber == "6":
		if fa == "_":fa = player
		elif fb == "_":fb = player
		elif fc == "_":fc = player
		elif fd == "_":fd = player
		elif fe == "_":fe = player
		elif ff == "_":ff = player
	if turnNumber == "7":
		if ga == "_":ga = player
		elif gb == "_":gb = player
		elif gc == "_":gc = player
		elif gd == "_":gd = player
		elif ge == "_":ge = player
		elif gf == "_":gf = player
def checkWinVert():
	global GameRunning, Winner
	check,check2,check3,check4,finder = -1,6,13,20,False
	while finder == False:
		check += 1
		check2 += 1
		check3 += 1
		check4 += 1
		if board[check] == player and board[check2] == player and board[check3] == player and board[check4] == player:
			finder, GameRunning, Winner = True, False, player
		if check4 == 41:
			finder = True
def checkWinHoriz():
	global GameRunning, Winner
	check,check2,check3,check4,finder = -1,0,1,2,False
	while finder == False:
		check += 1
		check2 += 1
		check3 += 1
		check4 += 1
		if board[check] == player and board[check2] == player and board[check3] == player and board[check4] == player:
			finder, GameRunning, Winner = True, False, player
		if check4 == 6 or check4 ==  13 or  check4 == 20 or  check4 == 27 or  check4 == 34:
			check += 3
			check2 += 3
			check3 += 3
			check4 += 3
		if check4 == 41:
			finder = True
def checkWinDiag():
	global GameRunning, Winner
	check,check2,check3,check4,finder = 20,14,8,2,False
	while finder == False:
		check += 1
		check2 += 1
		check3 += 1
		check4 += 1
		if board[check] == player and board[check2] == player and board[check3] == player and board[check4] == player:
			finder, GameRunning, Winner = True, False, player
		if check4 == 6 or check4 ==  13:
			check += 3
			check2 += 3
			check3 += 3
			check4 += 3
		if check4 == 20:
			finder = True
def checkWinBackDiag():
	global GameRunning, Winner
	check,check2,check3,check4,finder = -1,7,15,23,False
	while finder == False:
		check += 1
		check2 += 1
		check3 += 1
		check4 += 1
		if board[check] == player and board[check2] == player and board[check3] == player and board[check4] == player:
			finder, GameRunning, Winner = True, False, player
		if check4 == 27 or check4 ==  34:
			check += 3
			check2 += 3
			check3 += 3
			check4 += 3
		if check4 == 41:
			finder = True
def checkWin():
	global player
	checkWinVert()
	checkWinHoriz()
	checkWinDiag()
	checkWinBackDiag()
def RunGame():
	global player,turnNumber,GameRunning
	DisplayBoard()
	while GameRunning == True:
		player,turnNumber = "M","000"
		turnNumber = input("M's Turn:  ")
		while turnNumber != "1" and turnNumber != "2" and turnNumber != "3" and turnNumber != "4" and turnNumber != "5" and turnNumber != "6" and turnNumber != "7":
				turnNumber = input("M's Turn:  ")
		playerTurn()
		DisplayBoard()
		checkWin()
		if GameRunning == True:
			player,turnNumber = "O","000"
			turnNumber = input("O's Turn:  ")
			while turnNumber != "1" and turnNumber != "2" and turnNumber != "3" and turnNumber != "4" and turnNumber != "5" and turnNumber != "6" and turnNumber != "7":
					turnNumber = input("O's Turn:  ")
			playerTurn()
			DisplayBoard()
			checkWin()
	print(f"{Winner} Wins!!!")
BigText()
while playAgain.lower() == "yes"  or playAgain.lower() == "y"  or playAgain.lower() == "si"  or playAgain.lower() == "play"  or playAgain == "1":
	GameRunning = True
	Variables()
	RunGame()
	playAgain = input("Would you like to play again?\n")
print("Thanks for playing!!")
