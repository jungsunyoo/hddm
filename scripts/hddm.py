#!/usr/bin/python
import hddm

if __name__=='__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print "hddm.py <filename>"
        sys.exit(-1)
        
    hddm.utils.parse_config_file(sys.argv[1])
