#! /usr/bin/python

import cleware

def device_id_to_string(device_type):
        if device_type == cleware.CUSBaccess.POWER_DEVICE:
                return "Power"
        if device_type == cleware.CUSBaccess.WATCHDOGXP_DEVICE:
                return "WatchdogXP"
        if device_type == cleware.CUSBaccess.LED_DEVICE:
                return "LED"
        if device_type == cleware.CUSBaccess.WATCHDOG_DEVICE:
                return "Watchdog"
        if device_type == cleware.CUSBaccess.AUTORESET_DEVICE:
                return "Autoreset device"
        if device_type == cleware.CUSBaccess.SWITCH1_DEVICE:
                return "Switch1"
        if device_type == cleware.CUSBaccess.SWITCH2_DEVICE:
                return "Switch2"
        if device_type == cleware.CUSBaccess.SWITCH3_DEVICE:
                return "Switch3"
        if device_type == cleware.CUSBaccess.SWITCH4_DEVICE:
                return "Switch4"
        if device_type == cleware.CUSBaccess.SWITCH5_DEVICE:
                return "Switch5"
        if device_type == cleware.CUSBaccess.SWITCH6_DEVICE:
                return "Switch6"
        if device_type == cleware.CUSBaccess.SWITCH7_DEVICE:
                return "Switch7"
        if device_type == cleware.CUSBaccess.SWITCH8_DEVICE:
                return "Switch8"
        if device_type == cleware.CUSBaccess.SWITCHX_DEVICE:
                return "SwitchX"
        if device_type == cleware.CUSBaccess.TEMPERATURE_DEVICE:
                return "Temperature sensor"
        if device_type == cleware.CUSBaccess.TEMPERATURE2_DEVICE:
                return "Temperature 2 sensor"
        if device_type == cleware.CUSBaccess.TEMPERATURE5_DEVICE:
                return "Temperature 5 sensor"
        if device_type == cleware.CUSBaccess.HUMIDITY1_DEVICE:
                return "Humidity sensor"
        if device_type == cleware.CUSBaccess.CONTACT00_DEVICE:
                return "Contact 00 device"
        if device_type == cleware.CUSBaccess.CONTACT01_DEVICE:
                return "Contact 01 device"
        if device_type == cleware.CUSBaccess.CONTACT02_DEVICE:
                return "Contact 02 device"
        if device_type == cleware.CUSBaccess.CONTACT03_DEVICE:
                return "Contact 03 device"
        if device_type == cleware.CUSBaccess.CONTACT04_DEVICE:
                return "Contact 04 device"
        if device_type == cleware.CUSBaccess.CONTACT05_DEVICE:
                return "Contact 05 device"
        if device_type == cleware.CUSBaccess.CONTACT06_DEVICE:
                return "Contact 06 device"
        if device_type == cleware.CUSBaccess.CONTACT07_DEVICE:
                return "Contact 07 device"
        if device_type == cleware.CUSBaccess.CONTACT08_DEVICE:
                return "Contact 08 device"
        if device_type == cleware.CUSBaccess.CONTACT09_DEVICE:
                return "Contact 09 device"
        if device_type == cleware.CUSBaccess.CONTACT10_DEVICE:
                return "Contact 10 device"
        if device_type == cleware.CUSBaccess.CONTACT11_DEVICE:
                return "Contact 11 device"
        if device_type == cleware.CUSBaccess.CONTACT12_DEVICE:
                return "Contact 12 device"
        if device_type == cleware.CUSBaccess.CONTACT13_DEVICE:
                return "Contact 13 device"
        if device_type == cleware.CUSBaccess.CONTACT14_DEVICE:
                return "Contact 14 device"
        if device_type == cleware.CUSBaccess.CONTACT15_DEVICE:
                return "Contact 15 device"
        if device_type == cleware.CUSBaccess.ENCODER01_DEVICE:
                return "Encoder 01 device"
        if device_type == cleware.CUSBaccess.F4_DEVICE:
                return "F4 device"
        if device_type == cleware.CUSBaccess.KEYC01_DEVICE:
                return "Keyc01 device"
        if device_type == cleware.CUSBaccess.KEYC16_DEVICE:
                return "Keyc16 device"
        if device_type == cleware.CUSBaccess.ADC0800_DEVICE:
                return "AC0800 device"
        if device_type == cleware.CUSBaccess.ADC0801_DEVICE:
                return "AC0801 device"
        if device_type == cleware.CUSBaccess.ADC0802_DEVICE:
                return "AC0802 device"
        if device_type == cleware.CUSBaccess.ADC0803_DEVICE:
                return "AC0803 device"
        if device_type == cleware.CUSBaccess.COUNTER00_DEVICE:
                return "Counter device"
        if device_type == cleware.CUSBaccess.BUTTON_NODEVICE:
                return "Button no device"
        return "device type not recognized!"


c = cleware.CUSBaccess()

n_devices = c.OpenCleware()

print "Number of devices: %d" % (n_devices)

for i in range(n_devices):
	devType = c.GetUSBType(i);
	devTypeStr = device_id_to_string(devType)
	version = c.GetVersion(i)
	serial = c.GetSerialNumber(i)

	print "device: %d, type: %s (%d), version: %d, serial number: %d" % (i, devTypeStr, devType, version, serial)

	# these two are not neccessary normally for reading temperatures
	# they're here as an example
	# rc is 0 for failure, 1 for ok
	rc = c.ResetDevice(i);
	rc = c.StartDevice(i);

	if 0:
		if devType == cleware.CUSBaccess.TEMPERATURE_DEVICE or devType == cleware.CUSBaccess.TEMPERATURE2_DEVICE or devType == cleware.CUSBaccess.TEMPERATURE5_DEVICE:
			temperature = c.GetTemperatureSimple(i)

			print "\tcurrent temperature: %f" % (temperature)

	if devType == cleware.CUSBaccess.HUMIDITY1_DEVICE:
		humidity = c.GetHumiditySimple(i)

		print "\tcurrent humidity: %f" % (humidity)

	# Note: the "ampel" (traffic light) is also a switch device, with actually 3 switches (one per light)
	if devType == cleware.CUSBaccess.SWITCH1_DEVICE or devType == cleware.CUSBaccess.SWITCH2_DEVICE or devType == cleware.CUSBaccess.SWITCH3_DEVICE or devType == cleware.CUSBaccess.SWITCH4_DEVICE or devType == cleware.CUSBaccess.SWITCH5_DEVICE or devType == cleware.CUSBaccess.SWITCH6_DEVICE or devType == cleware.CUSBaccess.SWITCH7_DEVICE or devType == cleware.CUSBaccess.SWITCH8_DEVICE or devType == cleware.CUSBaccess.SWITCHX_DEVICE:

		switch_nr = 0 # 0...15
		state = c.GetSwitch(i, 16 + switch_nr)
		print "\tswitch %d state: %d" % (switch_nr, state)

		new_state = 1 # 0 or 1
		rc = c.SetSwitch(i, 16 + switch_nr, new_state)

	if devType == c.CONTACT00_DEVICE:
		state = c.GetMultiSwitchSimple(i)
		print "\tstate: %d" % state

	if devType == c.LED_DEVICE:
		led = 1 # 0...3
		value = 10 # 0...15
		rc = c.SetLED(i, led, value)

	if devType == c.ADC0800_DEVICE or devType == c.ADC0801_DEVICE or devType == c.ADC0802_DEVICE or devType == c.ADC0803_DEVICE:
		channel = 1 # 0 or 1
		rc = c.SelectADCChannel(i, channel)

		scale = 0 # 0...2 for 5, 13 or 24V
		voltage = c.GetADCValue(i, scale)
		print "\tmeasured voltage: %f" % (voltage)
