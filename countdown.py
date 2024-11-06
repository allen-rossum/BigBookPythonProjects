import sys,time
import sevseg #import our sevseg.py program

#(!) Change this to any number of seconds:

secondsLeft = 3600

try:
    while True: #Main program Loop
        #Clear the screen by printing several new lines
      print('\n' * 60)
      # Get the hours/minutes/seconds from secondsLeft:
      # For example: 7265 is 2 hours, 1 minute, 5 seconds.
      # So 7265 // 3600 is 2 hours:
      hours = str(secondsLeft // 3600)
      # And 7265 % 3600 is 65, and 65// 60 is 1 minute:
      minutes = str((secondsLeft % 3600)// 60)
      # And 7265 % 60 is 5 seconds:
      seconds = str(secondsLeft % 60)

      #Get the digits strings from the sevseg module:
      hDigits = sevseg.getSevSegStr(hours,2)
      hTopRow, hMiddleRow , hBottomRow = hDigits.splitlines()

      mDigits = sevseg.getSevSegStr(minutes,2)
      mTopRow, mMiddleRow , mBottomRow = mDigits.splitlines()

      sDigits = sevseg.getSevSegStr(seconds,2)
      sTopRow, sMiddleRow , sBottomRow = sDigits.splitlines()

      #Display the Digits
      print(hTopRow   + '     ' + mTopRow + '     '  + sTopRow)
      print(hMiddleRow+ '  *  ' +mMiddleRow+'  *  '  + sMiddleRow)
      print(hBottomRow+ '  *  ' +mBottomRow+'  *  '  + sBottomRow)

      if secondsLeft == 0:
          print()
          print('    * * * * BOOM * * * *')
          break
      print()
      print('Press Crtl-C to quit.')
      time.sleep(1) #Insert a 1 second pause
      secondsLeft -= 1
except KeyboardInterrupt:
    print("Countdown")
    sys.exit()