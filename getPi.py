import os

class getPi(object):
    # Return CPU temperature as a character string                                     
    def getCPUtemperature(self):
        res = os.popen('vcgencmd measure_temp').readline()
        return(res.replace("temp=","").replace("'C\n",""))
     
    # Return RAM information (unit=kb) in a list                                      
    # Index 0: total RAM                                                              
    # Index 1: used RAM                                                                
    # Index 2: free RAM                                                                
    def getRAMinfo(self):
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                return(line.split()[1:4])
     
    # Return % of CPU used by user as a character string                               
    def getCPUuse(self):
        return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
     
    # Return information about disk space as a list (unit included)                    
    # Index 0: total disk space                                                        
    # Index 1: used disk space                                                        
    # Index 2: remaining disk space                                                    
    # Index 3: percentage of disk used                                                 
    def getDiskSpace(self):
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i +1
            line = p.readline()
            if i==2:
                return(line.split()[1:5])
 
    def __init__(self):
        # CPU informatiom
        self.CPU_temp = self.getCPUtemperature()
        self.CPU_usage = self.getCPUuse()
         
        # RAM information
        # Output is in kb, here I convert it in Mb for readability
        self.RAM_stats = self.getRAMinfo()
        self.RAM_total = round(int(self.RAM_stats[0]) / 1000,1)
        self.RAM_used = round(int(self.RAM_stats[1]) / 1000,1)
        self.RAM_free = round(int(self.RAM_stats[2]) / 1000,1)
        self.RAM_perc = round((self.RAM_used/self.RAM_total)*100,1)
        self.RAM_info = "%s/%sMB" % (self.RAM_used,self.RAM_total)
         
        # Disk information
        self.DISK_stats = self.getDiskSpace()
        self.DISK_total = self.DISK_stats[0]
        self.DISK_used = self.DISK_stats[1]
        self.DISK_perc = self.DISK_stats[3]
        self.DISK_perc = self.DISK_perc[:-1]
        self.DISK_info = "%sB/%sB" % (self.DISK_used,self.DISK_total)
        
if __name__ == '__main__':
    print('')
    print('CPU Temperature = '+CPU_temp)
    print('CPU Use = '+CPU_usage)
    print('')
    print('RAM Total = '+str(RAM_total)+' MB')
    print('RAM Used = '+str(RAM_used)+' MB')
    print('RAM Free = '+str(RAM_free)+' MB')
    print('') 
    print('DISK Total Space = '+str(DISK_total)+'B')
    print('DISK Used Space = '+str(DISK_used)+'B')
    print('DISK Used Percentage = '+str(DISK_perc))