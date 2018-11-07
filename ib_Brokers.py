#%%
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np

import time
from datetime import datetime
from IBWrapper import IBWrapper, contract
from ib.ext.ScannerSubscription import ScannerSubscription
from ib.ext.EClientSocket import EClientSocket

accountName = "DU1025213"
callback = IBWrapper()
tws = EClientSocket(callback)
host = ""
port = 7497
clientId = 0



# tws.eDisconnect()
tws.eConnect(host, port, clientId)

tws.setServerLogLevel(5)
print(tws.isConnected())

tws.reqAccountUpdates(1, accountName)






