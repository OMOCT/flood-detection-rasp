from RPLCD.i2c import CharLCD

lcd = CharLCD("PCF8574", 0x27)

def display(data1, data2):
    lcd.clear()
    lcd.cursor = (0,0)
    lcd.write_string(data1)
    lcd.cursor = (1,0)
    lcd.write_string(data2)

