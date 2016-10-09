class PinManager:
    def unexport_pin(self, pin):
        f = open('/sys/class/gpio/unexport', 'w')
        f.write(str(pin))
        f.close()

    def export_pin(self, pin):
        f = open('/sys/class/gpio/export', 'w')
        f.write(str(pin))
        f.close()

    def define_direction(self, pin, direction):
        path = '/sys/class/gpio/gpio' + str(pin) + '/direction'
        f = open(path, 'w')
        f.write(str(direction))
        f.close()

    def set_pin_value(self, pin, value):
        path = '/sys/class/gpio/gpio' + str(pin) + '/value'
        f = open(path, 'w')
        f.write(str(value))
        f.close()
