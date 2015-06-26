
# In[1]:

#OBJECTIVE: The objective of this program is to
#For target device...
#1. Measure the photodetector for target device
#2. Transition the film
#3. Measure the photodetector
#4. Store the data to file
#5. Repeat
import serial
import time
from time import gmtime, strftime
import pytz
import datetime


# To do: 1. Put shit in a loop
# 2. Get things to pipe to a terminal? or just print might work

# In[2]:

def kiethley_readpd(ser):
    print 'reading PD value\r'
    #Take a measurement of the photodetector
    ser.write('*RST\r\n')
    ser.write(':SYSTEM:BEEPER:STATE 0\r\n')
    #ser.write(':ROUT:TERM FRONT\r\n')
    #ser.write(':SOUR:FUNC VOLT\r\n')
    #ser.write(':SOUR:VOLT:MODE FIXED\r\n')
    #ser.write(':SOUR:VOLT:RANG 5\r\n')
    #ser.write(':SOUR:VOLT:LEV 0\r\n')
    ser.write(':SENS:FUNC "CURR"\r\n')
    ser.write(':OUTPUT ON\r\n')
    ser.write(':READ?\r\n')
    ser.write(':OUTPUT OFF\r\n')
    time.sleep(1)
    out = ser.readlines()
    ser.close()
    return out


# In[3]:

def store_current(fname, out):
    outstring = out[0]
    kdata=outstring.split(',')
    current = kdata[1]
    print current
    #Toby: now to write the data with a datetimestring
    fmt = '%Y-%m-%d %H:%M:%S'
    d = datetime.datetime.now(pytz.timezone("America/Los_Angeles"))
    d_string = d.strftime(fmt)
    d2 = datetime.datetime.strptime(d_string, fmt)
    line = d2.strftime(fmt)+'\t'+current+'\n'
    f = open(fname, 'ab+')
    f.write(line)
    f.close()
    


# In[4]:

def close_ports():
    for x in range(0,5):
        ser.close()


# In[5]:

def open_arduino(chip):
    for x in range(0,4):
        print ard.readline()
        time.sleep(0.1)
    chip = str(chip)
    ard.write('relay'+chip+'yes'+'\r')
    for x in range(0,4):
        print ard.readline()
        time.sleep(0.1)    


# In[6]:

def close_arduino(chip):
    for x in range(0,4):
        print ard.readline()
        time.sleep(0.1)
    chip = str(chip)
    #dev = str(dev)
    print 'opening arduino to '+str(chip)+'\r'
    ard.write('relay'+chip+'no'+'\r')
    for x in range(0,4):
        print ard.readline()
        time.sleep(0.1)    


# In[7]:

def transition(chip, volt, ser):
    print('setting voltage on '+str(chip)+' to '+str(volt)+' \r')
    #ser = serial.Serial(2, 9600, timeout=1)
    #pd = str(dev)
    chip = str(chip)
    #dev = str(dev+1)
# WARNING: voltages must be entered as a floating point decimal for this thing to run


    ser.flushInput()
    ser.flushOutput()

    step = str(volt/20)
    volt = str(volt) 
    ser.write('*RST\r\n')

    ser.write(':SYSTEM:BEEPER:STATE 0\r\n')
    ser.write(':SOUR:FUNC:MODE VOLT\r\n')
    ser.write(':SOUR:VOLT:STAR 0\r\n') 
    if volt.find('.') == -1:
        ser.write(':SOUR:VOLT:STOP '+volt+'\r\n')
    else:
        places = volt.split('.')
        ser.write(':SOUR:VOLT:STOP '+places[0]+'.'+places[1]+'\r\n')
    if step.find('.') == -1:
        ser.write(':SOUR:VOLT:STEP '+step+'\r\n')
    else:
        places = step.split('.')
        ser.write(':SOUR:VOLT:STEP '+places[0]+'.'+places[1]+'\r\n')

    ser.write(':SOUR:CLE:AUTO OFF\r\n') #THIS was originally on enable auto off mode
    ser.write(':SOUR:VOLT:MODE SWE\r\n')
    ser.write(':SOUR:SWE:SPAC LIN\r\n')
    ser.write(':SOUR:DEL:AUTO OFF\r\n') #sets remote source delay to off
    ser.write(':SOUR:DEL 0\r\n') #sets source delay to 0 which doesn't even make sense

    ser.write(':SENS:FUNC "CURR"\r\n')
    ser.write(':SENS:CURR:RANG:AUTO ON\r\n')

    ser.write(':SENS:CURR:PROT:LEV 0.005\r\n')

    ser.write(':FORM:ELEM:SENS CURR,VOLT\r\n')
    ser.write(':TRIG:COUN 21\r\n')
    ser.write(':TRIG:DEL 0.5\r\n')
    ser.write(':OUTP ON\r\n')
    ser.write(':READ?\r\n')

    while True:
        xdata = ser.readlines()
        if xdata != []:
            break


    #ser.write('*RST\r\n')
    #ser.write(':SYSTEM:BEEPER:STATE 0\r\n')

    ser.write(':SOUR:VOLT:MODE FIXED\r\n')
    ser.write(':SOUR:VOLT:RANG 5\r\n')
    ser.write(':SOUR:VOLT:LEV '+str(volt)+'\r\n')

    ser.write(':SENS:CURR:RANG:AUTO ON\r\n')
    ser.write(':SENS:CURR:PROT:LEV 0.005\r\n')
    ser.write(':FORM:ELEM:SENS CURR,VOLT\r\n')
    ser.write(':TRIG:COUN 51\n') #OMG OMG OMG PLEASE CHANGE ME!!!!!!!
    #ser.write(':TRAC:FEED:CONT NEXT\r\n')
    ser.write(':TRIG:SOURCE IMM\r\n') #caused an error
    ser.write(':TRIG:DEL 1\r\n')
    ser.write(':OUTP ON\r\n')
    ser.write(':READ?\r\n')

    #ser.write(':TRAC:DATA?\r\n')
    ser.write(':OUTP OFF\r\n')
    while True:
        holddata = ser.readlines()
        if holddata != []:
            for meas in holddata:
                xdata.append(meas)
            break
    print 'resetting sub '+str(chip)+' to open\r'
    #ard.write('sub2no '+str(chip)+' no\r')
    #for x in range(0,4):
    #    print ard.readline()
    #    time.sleep(0.1)
    #return xdata

# This subroutine was used
#    ard.write('sub2no '+chip+' no\r')
#    for x in range(0,4):
#        print ard.readline()
#        time.sleep(0.1)
#    ard.write('pin2no '+chip+' '+pd+' \r')
#    print 'reading current from '+str(chip)+' '+str(pd)+' to '+str(volt)+' \r'
#    for x in range(0,4):
#        print ard.readline()
#        time.sleep(0.1)


    ser.write(':SOUR:VOLT:MODE FIXED\r\n')
    ser.write(':SOUR:VOLT:RANG 5\r\n')
    ser.write(':SOUR:VOLT:LEV '+str(volt)+'\r\n')

    ser.write(':SENS:CURR:RANG:AUTO ON\r\n')
    ser.write(':SENS:CURR:PROT:LEV 0.005\r\n')
    ser.write(':FORM:ELEM:SENS CURR,VOLT\r\n')
    ser.write(':TRIG:COUN 51\n') #OMG OMG OMG PLEASE CHANGE ME!!!!!!!
    #ser.write(':TRAC:FEED:CONT NEXT\r\n')
    ser.write(':TRIG:SOURCE IMM\r\n') #caused an error
    ser.write(':TRIG:DEL 1\r\n')
    ser.write(':OUTP ON\r\n')
    ser.write(':READ?\r\n')

    #ser.write(':TRAC:DATA?\r\n')
    ser.write(':OUTP OFF\r\n')
    while True:
        holddata = ser.readlines()
        if holddata != []:
            for meas in holddata:
                xdata.append(meas)
            break
    ser.close()
    return xdata


# In[8]:

def write_xdata(xdata,xname):
    fmt = '%Y-%m-%d %H:%M:%S'
    d = datetime.datetime.now(pytz.timezone("America/Los_Angeles"))
    d_string = d.strftime(fmt)
    d2 = datetime.datetime.strptime(d_string, fmt)
    f = open(xname, 'ab+')
    dateline = d2.strftime(fmt)+'\t'
    f.write(dateline)
    xsdata = xdata
    for x in range(0,len(xsdata)):
        datum = xsdata[x]
        cleaned = datum[2:-3]
       # print cleaned
        xline  = cleaned + '\t'
        f.write(xline)
    f.write('\r')
    f.close()


# In[9]:

def timediff(start):
    d2 = datetime.datetime.now(pytz.timezone("America/Los_Angeles"))
    diff = d2 - start
    diff = str(diff)
    ndiff = str.split(diff,'.')
    ndigest = str(ndiff[0])
    ndigest2 = ndigest.replace(':','-')
    timeval = ndigest2
    return timeval


# In[10]:

#Define the serial ports that we'll use
#Define the start time
start = datetime.datetime.now(pytz.timezone("America/Los_Angeles"))

ard = serial.Serial(3, 57600, timeout=1)
chipdev = [
    [1],[2],[3],[4]
    ]

volts = [
    [-1.0,1.5],
    [-2.0,1.5],
    [-3.0,1.5],
    [-4.0,1.5],
    ]
volt = 2 # if this value is positive, a negative voltage (reduction) will be applied
while True:
    count = 0
    volt = volt*-1
    
    for devname in ['20150608_pedot7_liclo4spe_ito_d08','20150608_pedot_liclo4spe_ito_d13', 
                    '20150608_pedot7_liclo4spe_ito_d11','blank_20141011_d04']:
        voltset = volts[count]
        cchipdev = chipdev[count]
        chip = cchipdev[0]
        count = count+1 
        
        if volt < 0:
            actvolt = voltset[0]
        if volt > 0:
            actvolt = voltset[1]
            
        ser = serial.Serial(5, 9600, timeout=1)
        timeval = timediff(start)
        suffix = devname+'.txt'
        fname = 'C:\\Users\\toby\\Dropbox\\NSF_SBIR_Grant\\AgingData\\Test'+suffix
        xname = 'C:\\Users\\toby\\Dropbox\\NSF_SBIR_Grant\\AgingData\\Test'+suffix
        #2. Transition the film and write it to file
        open_arduino(chip)
        xdata=transition(chip, actvolt, ser)
        write_xdata(xdata,xname)
        close_arduino(chip)
        #5. Repeat

    print('waiting')
    #Transition the flim
    time.sleep(1)
    time.sleep(672) # wait compensate the fact that there is not 10 samples
    time.sleep(1488) # wait to equal the wait on the life tester = 2448 sec. (2448-960sec for 10 samples)
# In[ ]:

ser.close()
ard.close()
