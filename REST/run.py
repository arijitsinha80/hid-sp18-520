from eve import Eve
import sys
import json
import random
import requests
import platform
import psutil
from flask import jsonify

app = Eve()

# To Get Virtual Memory
@app.route('/ubuntu/ram', methods=['GET'])
def ram():
    ramdata = {
            "Total Virtual Memory": psutil.virtual_memory().total,
            "Used Virtual Memory": psutil.virtual_memory().used,
            "Free Virtual Memory": psutil.virtual_memory().free
            }
    return (jsonify(ramdata))

# To Get Processor and System Details
@app.route('/ubuntu/processorName', methods=['GET'])
def processor():
    processordata = {
            "ProcessorName": platform.processor(),
            "ProcessorVersion": platform.version(),
            "System": platform.system()
            }
    return (jsonify(processordata))

# To Get Disk details
@app.route("/ubuntu/diskspace", methods=['GET'])
def Diskdetail():
    Diskdata = {
		"Total Disk": psutil.disk_usage('/').total,
            	"Used Disk": psutil.disk_usage('/').used,
            	"Free Disk": psutil.disk_usage('/').free	
            }
    return(jsonify(Diskdata))

# To Get CPU details
@app.route("/ubuntu/CPUDetails", methods=['GET'])
def CPUdetail():
    CPUdata = {
            "CPU Count": psutil.cpu_count(),
	    "Terminal": psutil.users()[0].terminal	
            }
    return(jsonify(CPUdata))


if __name__=='__main__':
    app.run()
    
    


