# by Carl Monk (@ForToffee)
# github.com/ForToffee/Robosapien

# command codes from http://www.aibohack.com/robosap/ir_codes.htm
import robo
import time

rs = robo.Robo(21)  # create Robo object for GPIO 21
for x in range (10):
	rs.send_code(0xC4)  # Hi 5
	time.sleep(2)
