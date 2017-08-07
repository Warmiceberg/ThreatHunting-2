from selenium import webdriver
from depot.manager import DepotManager
count = 0
pth = raw_input("Enter the path of the domain list")
depot = DepotManager.get()
driver = webdriver.PhantomJS()
driver.set_window_size(800, 800) # set the window size that you need
with open(pth, "r") as f: 
    for line in f.readlines():
        try:
            count = count + 1  
            print 'Taking screenshot for site - '+line
            driver.get(str(line.strip()))
            filename = line.replace('/','~')
            print filename
            driver.save_screenshot(str(str(filename)+'.png'))
        except Exception,e:
            print str(e)