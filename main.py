def on_forever():
    basic.show_number(pins.digital_read_pin(DigitalPin.P0))
    basic.pause(1000)
basic.forever(on_forever)
