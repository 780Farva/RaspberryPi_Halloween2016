class PinManager:
    @staticmethod
    def unexport_pin(pin):
        f = open('/sys/class/gpio/unexport', 'w')
        f.write(str(pin))
        f.close()

    @staticmethod
    def export_pin(pin):
        f = open('/sys/class/gpio/export', 'w')
        f.write(str(pin))
        f.close()

    @staticmethod
    def define_direction(pin, direction):
        f = open('/sys/class/gpio/gpio' + str(pin) + '/direction', 'w')
        f.write(str(direction))
        f.close()

    @staticmethod
    def set_pin_value(pin, value):
        f = open('/sys/class/gpio/gpio' + str(pin) + '/value', 'w')
        f.write(str(value))
        f.close()
