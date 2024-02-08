#STUDENT NUMBER: 122415616

from storage_part import StoragePart

class SSD(StoragePart):
    def __init__(self, manufacturer, model, generation, tdp, price, released, capacity, interface, form_factor, write_speed, read_speed):
        """"
        Released format - Q1 2018 (First quarter of 2018), Q4 2022 (Last quarter of 2022)
        Capacity - TB
        Interface - SATA, SAS, SCSI, Fibre Channel, USB, FireWire, Ethernet, Fibre Channel over Ethernet, PCIe
        Form Factor - 3.5", 2.5", 1.8", 1.0", 0.85"
        """
        
        super().__init__(manufacturer, model, generation, tdp, price, released, capacity, "SSD")
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
        """Returns a rough estimate of the SSD's performance based on the write and read speeds."""
        return (self._write_speed + self._read_speed) / 2  # Average of write and read speeds
    
    interface = property(get_interface)
    form_factor = property(get_form_factor)
    write_speed = property(get_write_speed)
    read_speed = property(get_read_speed)


if __name__ == "__main__":
    ssd = SSD("Samsung", "970 EVO", 3, 5, 89.99, 2018, 500, "M.2", "2280", 3400, 3500)
    print(ssd)
    print(ssd.get_performance())