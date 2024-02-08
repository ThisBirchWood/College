#STUDENT NUMBER: 122415616

from storage_part import StoragePart

class HDD(StoragePart):
    def __init__(self, manufacturer, model, generation, tdp, price, released, capacity, interface, form_factor, write_speed, read_speed):
        """
        Released format - Q1 2018 (First quarter of 2018), Q4 2022 (Last quarter of 2022)
        Capacity - TB
        Interface - SATA, SAS, SCSI, Fibre Channel, USB, FireWire, Ethernet, Fibre Channel over Ethernet, PCIe
        Form Factor - 3.5", 2.5", 1.8", 1.0", 0.85"
        """
        super().__init__(manufacturer, model, generation, tdp, price, released, capacity, "HDD")
        self._interface = interface
        self._form_factor = form_factor
        self._write_speed = write_speed
        self._read_speed = read_speed

    def get_interface(self):
        return self._interface
    
    def get_form_factor(self):
        return self._form_factor
    
    def get_write_speed(self):
        return self._write_speed
    
    def get_read_speed(self):
        return self._read_speed
    
    def __str__(self):
        return self._manufacturer + " " + self._model + " " + str(self._capacity) + "GB " + self._interface + " " + self._form_factor
    
    def get_performance(self):
        return (self._write_speed + self._read_speed) / 2
    
    interface = property(get_interface)
    form_factor = property(get_form_factor)
    write_speed = property(get_write_speed)
    read_speed = property(get_read_speed)

if __name__ == "__main__":
    hdd = HDD("Seagate", "Barracuda", 3, 5, 89.99, 2018, 500, "SATA", "3.5", 140, 150)
    print(hdd)
    print(hdd.get_performance())