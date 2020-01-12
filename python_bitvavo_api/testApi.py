from python_bitvavo_api.bitvavo import Bitvavo
import sys
import signal
import time
import json

from time import strftime

""" 
* This is an example utilising all functions of the python Bitvavo API wrapper.
* The APIKEY and APISECRET should be replaced by your own key and secret.
* For public functions the APIKEY and SECRET can be removed.
* Documentation: https://docs.bitvavo.com
* Bitvavo: https://bitvavo.com
* README: https://github.com/bitvavo/php-bitvavo-api
"""

#EUR Pairs
currBTCEURAsk = 0.0
currBTCEURBid = 0.0

currETHEURAsk = 0.0
currETHEURBid = 0.0

currXRPEURAsk = 0.0
currXRPEURBid = 0.0

currADAEURAsk = 0.0
currADAEURBid = 0.0

currAEEURAsk = 0.0
currAEEURBid = 0.0

currAIONEURAsk = 0.0
currAIONEURBid = 0.0

currANTEURAsk = 0.0
currANTEURBid = 0.0

currARKEURAsk = 0.0
currARKEURBid = 0.0

currBATEURAsk = 0.0
currBATEURBid = 0.0

currBCHEURAsk = 0.0
currBCHEURBid = 0.0

currBSVEURAsk = 0.0
currBSVEURBid = 0.0

currCMTEURAsk = 0.0
currCMTEURBid = 0.0

currDCREURAsk = 0.0
currDCREURBid = 0.0

currDGBEURAsk = 0.0
currDGBEURBid = 0.0

currELFEURAsk = 0.0
currELFEURBid = 0.0

currENJEURAsk = 0.0
currENJEURBid = 0.0

currEOSEURAsk = 0.0
currEOSEURBid = 0.0

currETCEURAsk = 0.0
currETCEURBid = 0.0

currGASEURAsk = 0.0
currGASEURBid = 0.0

currGNTEURAsk = 0.0
currGNTEURBid = 0.0

currHOTEURAsk = 0.0
currHOTEURBid = 0.0

currICXEURAsk = 0.0
currICXEURBid = 0.0

currIOSTEURAsk = 0.0
currIOSTEURBid = 0.0

currKMDEURAsk = 0.0
currKMDEURBid = 0.0

currLINKEURAsk = 0.0
currLINKEURBid = 0.0

currLRCEURAsk = 0.0
currLRCEURBid = 0.0

currLSKEURAsk = 0.0
currLSKEURBid = 0.0

currLTCEURAsk = 0.0
currLTCEURBid = 0.0

currMIOTAEURAsk = 0.0
currMIOTAEURBid = 0.0

currNANOEURAsk = 0.0
currNANOEURBid = 0.0

currNASEURAsk = 0.0
currNASEURBid = 0.0

currNEOEURAsk = 0.0
currNEOEURBid = 0.0

currNPXSEURAsk = 0.0
currNPXSEURBid = 0.0

currNULSEURAsk = 0.0
currNULSEURBid = 0.0

currOMGEURAsk = 0.0
currOMGEURBid = 0.0

currONGEURAsk = 0.0
currONGEURBid = 0.0

currONTEURAsk = 0.0
currONTEURBid = 0.0

currPOWREURAsk = 0.0
currPOWREURBid = 0.0

currQTUMEURAsk = 0.0
currQTUMEURBid = 0.0

currRDDEURAsk = 0.0
currRDDEURBid = 0.0

currREQEURAsk = 0.0
currREQEURBid = 0.0

currRVNEURAsk = 0.0
currRVNEURBid = 0.0

currSNTEURAsk = 0.0
currSNTEURBid = 0.0

currSTEEMEURAsk = 0.0
currSTEEMEURBid = 0.0

currSTORMEURAsk = 0.0
currSTORMEURBid = 0.0

currSTRATEURAsk = 0.0
currSTRATEURBid = 0.0

currTRXEURAsk = 0.0
currTRXEURBid = 0.0

currVETEURAsk = 0.0
currVETEURBid = 0.0

currVTCEURAsk = 0.0
currVTCEURBid = 0.0

currVTHOEURAsk = 0.0
currVTHOEURBid = 0.0

currWAVESEURAsk = 0.0
currWAVESEURBid = 0.0

currWTCEURAsk = 0.0
currWTCEURBid = 0.0

currXEMEURAsk = 0.0
currXEMEURBid = 0.0

currXLMEURAsk = 0.0
currXLMEURBid = 0.0

currXTZEURAsk = 0.0
currXTZEURBid = 0.0

currXVGEURAsk = 0.0
currXVGEURBid = 0.0

currZILEURAsk = 0.0
currZILEURBid = 0.0

currZRXEURAsk = 0.0
currZRXEURBid = 0.0

#BTC Pairs
currETHBTCAsk = 0.0
currETHBTCBid = 0.0

currADABTCAsk = 0.0
currADABTCBid = 0.0

currAEBTCAsk = 0.0
currAEBTCBid = 0.0

currAIONBTCAsk = 0.0
currAIONBTCBid = 0.0

currANTBTCAsk = 0.0
currANTBTCBid = 0.0

currARKBTCAsk = 0.0
currARKBTCBid = 0.0

currBATBTCAsk = 0.0
currBATBTCBid = 0.0

currBCHBTCAsk = 0.0
currBCHBTCBid = 0.0

currBSVBTCAsk = 0.0
currBSVBTCBid = 0.0

currCMTBTCAsk = 0.0
currCMTBTCBid = 0.0

currDCRBTCAsk = 0.0
currDCRBTCBid = 0.0

currDGBBTCAsk = 0.0
currDGBBTCBid = 0.0

currELFBTCAsk = 0.0
currELFBTCBid = 0.0

currENJBTCAsk = 0.0
currENJBTCBid = 0.0

currEOSBTCAsk = 0.0
currEOSBTCBid = 0.0

currETCBTCAsk = 0.0
currETCBTCBid = 0.0

currGASBTCAsk = 0.0
currGASBTCBid = 0.0

currGNTBTCAsk = 0.0
currGNTBTCBid = 0.0

currHOTBTCAsk = 0.0
currHOTBTCBid = 0.0

currICXBTCAsk = 0.0
currICXBTCBid = 0.0

currIOSTBTCAsk = 0.0
currIOSTBTCBid = 0.0

currKMDBTCAsk = 0.0
currKMDBTCBid = 0.0

currLINKBTCAsk = 0.0
currLINKBTCBid = 0.0

currLRCBTCAsk = 0.0
currLRCBTCBid = 0.0

currLSKBTCAsk = 0.0
currLSKBTCBid = 0.0

currLTCBTCAsk = 0.0
currLTCBTCBid = 0.0

currMIOTABTCAsk = 0.0
currMIOTABTCBid = 0.0

currNANOBTCAsk = 0.0
currNANOBTCBid = 0.0

currNASBTCAsk = 0.0
currNASBTCBid = 0.0

currNEOBTCAsk = 0.0
currNEOBTCBid = 0.0

currNPXSBTCAsk = 0.0
currNPXSBTCBid = 0.0

currNULSBTCAsk = 0.0
currNULSBTCBid = 0.0

currOMGBTCAsk = 0.0
currOMGBTCBid = 0.0

currONGBTCAsk = 0.0
currONGBTCBid = 0.0

currONTBTCAsk = 0.0
currONTBTCBid = 0.0

currPOWRBTCAsk = 0.0
currPOWRBTCBid = 0.0

currQTUMBTCAsk = 0.0
currQTUMBTCBid = 0.0

currRDDBTCAsk = 0.0
currRDDBTCBid = 0.0

currREQBTCAsk = 0.0
currREQBTCBid = 0.0

currRVNBTCAsk = 0.0
currRVNBTCBid = 0.0

currSNTBTCAsk = 0.0
currSNTBTCBid = 0.0

currSTEEMBTCAsk = 0.0
currSTEEMBTCBid = 0.0

currSTORMBTCAsk = 0.0
currSTORMBTCBid = 0.0

currSTRATBTCAsk = 0.0
currSTRATBTCBid = 0.0

currTRXBTCAsk = 0.0
currTRXBTCBid = 0.0

currVETBTCAsk = 0.0
currVETBTCBid = 0.0

currVTCBTCAsk = 0.0
currVTCBTCBid = 0.0

currVTHOBTCAsk = 0.0
currVTHOBTCBid = 0.0

currWAVESBTCAsk = 0.0
currWAVESBTCBid = 0.0

currWTCBTCAsk = 0.0
currWTCBTCBid = 0.0

currXEMBTCAsk = 0.0
currXEMBTCBid = 0.0

currXLMBTCAsk = 0.0
currXLMBTCBid = 0.0

currXRPBTCAsk = 0.0
currXRPBTCBid = 0.0

currXTZBTCAsk = 0.0
currXTZBTCBid = 0.0

currXVGBTCAsk = 0.0
currXVGBTCBid = 0.0

currZILBTCAsk = 0.0
currZILBTCBid = 0.0

currZRXBTCAsk = 0.0
currZRXBTCBid = 0.0


def main():
  bitvavo = Bitvavo({
    'APIKEY': 'REPLACE_WITH_YOUR_APIKEY',
    'APISECRET': 'REPLACE_WITH_YOUR_APISECRET',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
  })
  testREST(bitvavo)
  testWebsockets(bitvavo)

def testREST(bitvavo):

  #Init EUR variables
  global currBTCEURAsk
  global currBTCEURBid

  global currETHEURAsk
  global currETHEURBid

  global currXRPEURAsk
  global currXRPEURBid

  global currADAEURAsk
  global currADAEURBid

  global currAEEURAsk
  global currAEEURBid

  global currAIONEURAsk
  global currAIONEURBid

  global currANTEURAsk
  global currANTEURBid

  global currARKEURAsk
  global currARKEURBid

  global currBATEURAsk
  global currBATEURBid

  global currBCHEURAsk
  global currBCHEURBid

  global currBSVEURAsk
  global currBSVEURBid

  global currCMTEURAsk
  global currCMTEURBid

  global currDCREURAsk
  global currDCREURBid

  global currDGBEURAsk
  global currDGBEURBid

  global currELFEURAsk
  global currELFEURBid

  global currENJEURAsk
  global currENJEURBid

  global currEOSEURAsk
  global currEOSEURBid

  global currETCEURAsk
  global currETCEURBid

  global currGASEURAsk
  global currGASEURBid

  global currGNTEURAsk
  global currGNTEURBid

  global currHOTEURAsk
  global currHOTEURBid

  global currICXEURAsk
  global currICXEURBid

  global currIOSTEURAsk
  global currIOSTEURBid

  global currKMDEURAsk
  global currKMDEURBid

  global currLINKEURAsk
  global currLINKEURBid

  global currLRCEURAsk
  global currLRCEURBid

  global currLSKEURAsk
  global currLSKEURBid

  global currLTCEURAsk
  global currLTCEURBid

  global currMIOTAEURAsk
  global currMIOTAEURBid

  global currNANOEURAsk
  global currNANOEURBid

  global currNASEURAsk
  global currNASEURBid

  global currNEOEURAsk
  global currNEOEURBid

  global currNPXSEURAsk
  global currNPXSEURBid

  global currNULSEURAsk
  global currNULSEURBid

  global currOMGEURAsk
  global currOMGEURBid

  global currONGEURAsk
  global currONGEURBid

  global currONTEURAsk
  global currONTEURBid

  global currPOWREURAsk
  global currPOWREURBid

  global currQTUMEURAsk
  global currQTUMEURBid

  global currRDDEURAsk
  global currRDDEURBid

  global currREQEURAsk
  global currREQEURBid

  global currRVNEURAsk
  global currRVNEURBid

  global currSNTEURAsk
  global currSNTEURBid

  global currSTEEMEURAsk
  global currSTEEMEURBid

  global currSTORMEURAsk
  global currSTORMEURBid

  global currSTRATEURAsk
  global currSTRATEURBid

  global currTRXEURAsk
  global currTRXEURBid

  global currVETEURAsk
  global currVETEURBid

  global currVTCEURAsk
  global currVTCEURBid

  global currVTHOEURAsk
  global currVTHOEURBid

  global currWAVESEURAsk
  global currWAVESEURBid

  global currWTCEURAsk
  global currWTCEURBid

  global currXEMEURAsk
  global currXEMEURBid

  global currXLMEURAsk
  global currXLMEURBid

  global currXTZEURAsk
  global currXTZEURBid

  global currXVGEURAsk
  global currXVGEURBid

  global currZILEURAsk
  global currZILEURBid

  global currZRXEURAsk
  global currZRXEURBid

  #Init BTC variables
  global currETHBTCAsk
  global currETHBTCBid

  global currADABTCAsk
  global currADABTCBid

  global currAEBTCAsk
  global currAEBTCBid

  global currAIONBTCAsk
  global currAIONBTCBid

  global currANTBTCAsk
  global currANTBTCBid

  global currARKBTCAsk
  global currARKBTCBid

  global currBATBTCAsk
  global currBATBTCBid

  global currBCHBTCAsk
  global currBCHBTCBid

  global currBSVBTCAsk
  global currBSVBTCBid

  global currCMTBTCAsk
  global currCMTBTCBid

  global currDCRBTCAsk
  global currDCRBTCBid

  global currDGBBTCAsk
  global currDGBBTCBid

  global currELFBTCAsk
  global currELFBTCBid

  global currENJBTCAsk
  global currENJBTCBid

  global currEOSBTCAsk
  global currEOSBTCBid

  global currETCBTCAsk
  global currETCBTCBid

  global currGASBTCAsk
  global currGASBTCBid

  global currGNTBTCAsk
  global currGNTBTCBid

  global currHOTBTCAsk
  global currHOTBTCBid

  global currICXBTCAsk
  global currICXBTCBid

  global currIOSTBTCAsk
  global currIOSTBTCBid

  global currKMDBTCAsk
  global currKMDBTCBid

  global currLINKBTCAsk
  global currLINKBTCBid

  global currLRCBTCAsk
  global currLRCBTCBid

  global currLSKBTCAsk
  global currLSKBTCBid

  global currLTCBTCAsk
  global currLTCBTCBid

  global currMIOTABTCAsk
  global currMIOTABTCBid

  global currNANOBTCAsk
  global currNANOBTCBid

  global currNASBTCAsk
  global currNASBTCBid

  global currNEOBTCAsk
  global currNEOBTCBid

  global currNPXSBTCAsk
  global currNPXSBTCBid

  global currNULSBTCAsk
  global currNULSBTCBid

  global currOMGBTCAsk
  global currOMGBTCBid

  global currONGBTCAsk
  global currONGBTCBid

  global currONTBTCAsk
  global currONTBTCBid

  global currPOWRBTCAsk
  global currPOWRBTCBid

  global currQTUMBTCAsk
  global currQTUMBTCBid

  global currRDDBTCAsk
  global currRDDBTCBid

  global currREQBTCAsk
  global currREQBTCBid

  global currRVNBTCAsk
  global currRVNBTCBid

  global currSNTBTCAsk
  global currSNTBTCBid

  global currSTEEMBTCAsk
  global currSTEEMBTCBid

  global currSTORMBTCAsk
  global currSTORMBTCBid

  global currSTRATBTCAsk
  global currSTRATBTCBid

  global currTRXBTCAsk
  global currTRXBTCBid

  global currVETBTCAsk
  global currVETBTCBid

  global currVTCBTCAsk
  global currVTCBTCBid

  global currVTHOBTCAsk
  global currVTHOBTCBid

  global currWAVESBTCAsk
  global currWAVESBTCBid

  global currWTCBTCAsk
  global currWTCBTCBid

  global currXEMBTCAsk
  global currXEMBTCBid

  global currXLMBTCAsk
  global currXLMBTCBid

  global currXRPBTCAsk
  global currXRPBTCBid

  global currXTZBTCAsk
  global currXTZBTCBid

  global currXVGBTCAsk
  global currXVGBTCBid

  global currZILBTCAsk
  global currZILBTCBid

  global currZRXBTCAsk
  global currZRXBTCBid

  
  #Show My Limits
  limit = bitvavo.getRemainingLimit()
  print('Remaining ratelimit is', limit)


  #Get first price init
  i=0 
  response = bitvavo.tickerBook({})
  print("Available Markets: ")
  for market in response:
    
    if(response[i]["market"] == "BTC-EUR"):
        currBTCEURBid = float(response[i]["bid"])
        currBTCEURAsk = float(response[i]["ask"])
        print("€ BTC Bid: " +str(currBTCEURBid) +" | BTC Ask: " +str(currBTCEURAsk))

    if(response[i]["market"] == "ETH-EUR"):
        currETHEURBid = float(response[i]["bid"])
        currETHEURAsk = float(response[i]["ask"])
        print("€ ETH Bid: " +str(currETHEURBid) +" | ETH Ask: " +str(currETHEURAsk))

    if(response[i]["market"] == "XRP-EUR"):
        currXRPEURBid = float(response[i]["bid"])
        currXRPEURAsk = float(response[i]["ask"])
        print("€ XRP Bid: " +str(currXRPEURBid) +" | XRP Ask: " +str(currXRPEURAsk))

    if(response[i]["market"] == "ADA-EUR"):
        currADAEURBid = float(response[i]["bid"])
        currADAEURAsk = float(response[i]["ask"])
        print("€ ADA Bid: " +str(currADAEURBid) +" | ADA Ask: " +str(currADAEURAsk))

    if(response[i]["market"] == "AE-EUR"):
        currAEEURBid = float(response[i]["bid"])
        currAEEURAsk = float(response[i]["ask"])
        print("€ AE Bid: " +str(currAEEURBid) +" | AE Ask: " +str(currAEEURAsk))

    if(response[i]["market"] == "AION-EUR"):
        currAIONEURBid = float(response[i]["bid"])
        currAIONEURAsk = float(response[i]["ask"])
        print("€ AION Bid: " +str(currAIONEURBid) +" | AION Ask: " +str(currAIONEURAsk))

    if(response[i]["market"] == "ANT-EUR"):
        currANTEURBid = float(response[i]["bid"])
        currANTEURAsk = float(response[i]["ask"])
        print("€ ANT Bid: " +str(currANTEURBid) +" | ANT Ask: " +str(currANTEURAsk))

    if(response[i]["market"] == "ARK-EUR"):
        currARKEURBid = float(response[i]["bid"])
        currARKEURAsk = float(response[i]["ask"])
        print("€ ARK Bid: " +str(currARKEURBid) +" | ARK Ask: " +str(currARKEURAsk))

    if(response[i]["market"] == "BAT-EUR"):
        currBATEURBid = float(response[i]["bid"])
        currBATEURAsk = float(response[i]["ask"])
        print("€ BAT Bid: " +str(currBATEURBid) +" | BAT Ask: " +str(currBATEURAsk))

    if(response[i]["market"] == "BCH-EUR"):
        currBCHEURBid = float(response[i]["bid"])
        currBCHEURAsk = float(response[i]["ask"])
        print("€ BCH Bid: " +str(currBCHEURBid) +" | BCH Ask: " +str(currBCHEURAsk))

    if(response[i]["market"] == "BSV-EUR"):
        currBSVEURBid = float(response[i]["bid"])
        currBSVEURAsk = float(response[i]["ask"])
        print("€ BSV Bid: " +str(currBSVEURBid) +" | BSV Ask: " +str(currBSVEURAsk))

    if(response[i]["market"] == "CMT-EUR"):
        currCMTEURBid = float(response[i]["bid"])
        currCMTEURAsk = float(response[i]["ask"])
        print("€ CMT Bid: " +str(currCMTEURBid) +" | CMT Ask: " +str(currCMTEURAsk))

    if(response[i]["market"] == "DCR-EUR"):
        currDCREURBid = float(response[i]["bid"])
        currDCREURAsk = float(response[i]["ask"])
        print("€ DCR Bid: " +str(currDCREURBid) +" | DCR Ask: " +str(currDCREURAsk))

    if(response[i]["market"] == "DGB-EUR"):
        currDGBEURBid = float(response[i]["bid"])
        currDGBEURAsk = float(response[i]["ask"])
        print("€ DGB Bid: " +str(currDGBEURBid) +" | DGB Ask: " +str(currDGBEURAsk))

    if(response[i]["market"] == "ELF-EUR"):
        currELFEURBid = float(response[i]["bid"])
        currELFEURAsk = float(response[i]["ask"])
        print("€ ELF Bid: " +str(currELFEURBid) +" | ELF Ask: " +str(currELFEURAsk))

    if(response[i]["market"] == "ENJ-EUR"):
        currENJEURBid = float(response[i]["bid"])
        currENJEURAsk = float(response[i]["ask"])
        print("€ ENJ Bid: " +str(currENJEURBid) +" | ENJ Ask: " +str(currENJEURAsk))

    if(response[i]["market"] == "EOS-EUR"):
        currEOSEURBid = float(response[i]["bid"])
        currEOSEURAsk = float(response[i]["ask"])
        print("€ EOS Bid: " +str(currEOSEURBid) +" | EOS Ask: " +str(currEOSEURAsk))

    if(response[i]["market"] == "ETC-EUR"):
        currETCEURBid = float(response[i]["bid"])
        currETCEURAsk = float(response[i]["ask"])
        print("€ ETC Bid: " +str(currETCEURBid) +" | ETC Ask: " +str(currETCEURAsk))

    if(response[i]["market"] == "GAS-EUR"):
        currGASEURBid = float(response[i]["bid"])
        currGASEURAsk = float(response[i]["ask"])
        print("€ GAS Bid: " +str(currGASEURBid) +" | GAS Ask: " +str(currGASEURAsk))

    if(response[i]["market"] == "GNT-EUR"):
        currGNTEURBid = float(response[i]["bid"])
        currGNTEURAsk = float(response[i]["ask"])
        print("€ GNT Bid: " +str(currGNTEURBid) +" | GNT Ask: " +str(currGNTEURAsk))

    if(response[i]["market"] == "HOT-EUR"):
        currHOTEURBid = float(response[i]["bid"])
        currHOTEURAsk = float(response[i]["ask"])
        print("€ HOT Bid: " +str(currHOTEURBid) +" | GNT Ask: " +str(currHOTEURAsk))

    if(response[i]["market"] == "ICX-EUR"):
        currICXEURBid = float(response[i]["bid"])
        currICXEURAsk = float(response[i]["ask"])
        print("€ ICX Bid: " +str(currICXEURBid) +" | ICX Ask: " +str(currICXEURAsk))

    if(response[i]["market"] == "IOST-EUR"):
        currIOSTEURBid = float(response[i]["bid"])
        currIOSTEURAsk = float(response[i]["ask"])
        print("€ IOST Bid: " +str(currIOSTEURBid) +" | IOST Ask: " +str(currIOSTEURAsk))

    if(response[i]["market"] == "KMD-EUR"):
        currKMDEURBid = float(response[i]["bid"])
        currKMDEURAsk = float(response[i]["ask"])
        print("€ KMD Bid: " +str(currKMDEURBid) +" | KMD Ask: " +str(currKMDEURAsk))

    if(response[i]["market"] == "LINK-EUR"):
        currLINKEURBid = float(response[i]["bid"])
        currLINKEURAsk = float(response[i]["ask"])
        print("€ LINK Bid: " +str(currLINKEURBid) +" | LINK Ask: " +str(currLINKEURAsk))

    if(response[i]["market"] == "LRC-EUR"):
        currLRCEURBid = float(response[i]["bid"])
        currLRCEURAsk = float(response[i]["ask"])
        print("€ LRC Bid: " +str(currLRCEURBid) +" | LRC Ask: " +str(currLRCEURAsk))

    if(response[i]["market"] == "LSK-EUR"):
        currLSKEURBid = float(response[i]["bid"])
        currLSKEURAsk = float(response[i]["ask"])
        print("€ LSK Bid: " +str(currLSKEURBid) +" | LSK Ask: " +str(currLSKEURAsk))

    if(response[i]["market"] == "LTC-EUR"):
        currLTCEURBid = float(response[i]["bid"])
        currLTCEURAsk = float(response[i]["ask"])
        print("€ LTC Bid: " +str(currLTCEURBid) +" | LTC Ask: " +str(currLTCEURAsk))

    if(response[i]["market"] == "MIOTA-EUR"):
        currMIOTAEURBid = float(response[i]["bid"])
        currMIOTAEURAsk = float(response[i]["ask"])
        print("€ MIOTA Bid: " +str(currMIOTAEURBid) +" | MIOTA Ask: " +str(currMIOTAEURAsk))

    if(response[i]["market"] == "NANO-EUR"):
        currNANOEURBid = float(response[i]["bid"])
        currNANOEURAsk = float(response[i]["ask"])
        print("€ NANO Bid: " +str(currNANOEURBid) +" | NANO Ask: " +str(currNANOEURAsk))

    if(response[i]["market"] == "NAS-EUR"):
        currNASEURBid = float(response[i]["bid"])
        currNASEURAsk = float(response[i]["ask"])
        print("€ NAS Bid: " +str(currNASEURBid) +" | NAS Ask: " +str(currNASEURAsk))

    if(response[i]["market"] == "NEO-EUR"):
        currNEOEURBid = float(response[i]["bid"])
        currNEOEURAsk = float(response[i]["ask"])
        print("€ NEO Bid: " +str(currNEOEURBid) +" | NEO Ask: " +str(currNEOEURAsk))

    if(response[i]["market"] == "NPXS-EUR"):
        currNPXSEURBid = float(response[i]["bid"])
        currNPXSEURAsk = float(response[i]["ask"])
        print("€ NPXS Bid: " +str(currNPXSEURBid) +" | NPXS Ask: " +str(currNPXSEURAsk))

    if(response[i]["market"] == "NULS-EUR"):
        currNULSEURBid = float(response[i]["bid"])
        currNULSEURAsk = float(response[i]["ask"])
        print("€ NULS Bid: " +str(currNULSEURBid) +" | NULS Ask: " +str(currNULSEURAsk))

    if(response[i]["market"] == "OMG-EUR"):
        currOMGEURBid = float(response[i]["bid"])
        currOMGEURAsk = float(response[i]["ask"])
        print("€ OMG Bid: " +str(currOMGEURBid) +" | OMG Ask: " +str(currOMGEURAsk))

    if(response[i]["market"] == "ONG-EUR"):
        currONGEURBid = float(response[i]["bid"])
        currONGEURAsk = float(response[i]["ask"])
        print("€ ONG Bid: " +str(currONGEURBid) +" | ONG Ask: " +str(currONGEURAsk))

    if(response[i]["market"] == "ONT-EUR"):
        currONTEURBid = float(response[i]["bid"])
        currONTEURAsk = float(response[i]["ask"])
        print("€ ONT Bid: " +str(currONTEURBid) +" | ONT Ask: " +str(currONTEURAsk))

    if(response[i]["market"] == "POWR-EUR"):
        currPOWREURBid = float(response[i]["bid"])
        currPOWREURAsk = float(response[i]["ask"])
        print("€ POWR Bid: " +str(currPOWREURBid) +" | POWR Ask: " +str(currPOWREURAsk))

    if(response[i]["market"] == "QTUM-EUR"):
        currQTUMEURBid = float(response[i]["bid"])
        currQTUMEURAsk = float(response[i]["ask"])
        print("€ QTUM Bid: " +str(currQTUMEURBid) +" | QTUM Ask: " +str(currQTUMEURAsk))

    if(response[i]["market"] == "RDD-EUR"):
        currRDDEURBid = float(response[i]["bid"])
        currRDDEURAsk = float(response[i]["ask"])
        print("€ RDD Bid: " +str(currRDDEURBid) +" | RDD Ask: " +str(currRDDEURAsk))

    if(response[i]["market"] == "REQ-EUR"):
        currREQEURBid = float(response[i]["bid"])
        currREQEURAsk = float(response[i]["ask"])
        print("€ REQ Bid: " +str(currREQEURBid) +" | REQ Ask: " +str(currREQEURAsk))

    if(response[i]["market"] == "RVN-EUR"):
        currRVNEURBid = float(response[i]["bid"])
        currRVNEURAsk = float(response[i]["ask"])
        print("€ RVN Bid: " +str(currRVNEURBid) +" | RVN Ask: " +str(currRVNEURAsk))

    if(response[i]["market"] == "SNT-EUR"):
        currSNTEURBid = float(response[i]["bid"])
        currSNTEURAsk = float(response[i]["ask"])
        print("€ SNT Bid: " +str(currSNTEURBid) +" | SNT Ask: " +str(currSNTEURAsk))

    if(response[i]["market"] == "STEEM-EUR"):
        currSTEEMEURBid = float(response[i]["bid"])
        currSTEEMEURAsk = float(response[i]["ask"])
        print("€ STEEM Bid: " +str(currSTEEMEURBid) +" | STEEM Ask: " +str(currSTEEMEURAsk))

    if(response[i]["market"] == "STORM-EUR"):
        currSTORMEURBid = float(response[i]["bid"])
        currSTORMEURAsk = float(response[i]["ask"])
        print("€ STORM Bid: " +str(currSTORMEURBid) +" | STORM Ask: " +str(currSTORMEURAsk))

    if(response[i]["market"] == "STRAT-EUR"):
        currSTRATEURBid = float(response[i]["bid"])
        currSTRATEURAsk = float(response[i]["ask"])
        print("€ STRAT Bid: " +str(currSTRATEURBid) +" | STRAT Ask: " +str(currSTRATEURAsk))

    if(response[i]["market"] == "TRX-EUR"):
        currTRXEURBid = float(response[i]["bid"])
        currTRXEURAsk = float(response[i]["ask"])
        print("€ TRX Bid: " +str(currTRXEURBid) +" | TRX Ask: " +str(currTRXEURAsk))

    if(response[i]["market"] == "VET-EUR"):
        currVETEURBid = float(response[i]["bid"])
        currVETEURAsk = float(response[i]["ask"])
        print("€ VET Bid: " +str(currVETEURBid) +" | VET Ask: " +str(currVETEURAsk))

    if(response[i]["market"] == "VTC-EUR"):
        currVTCEURBid = float(response[i]["bid"])
        currVTCEURAsk = float(response[i]["ask"])
        print("€ VTC Bid: " +str(currVTCEURBid) +" | VTC Ask: " +str(currVTCEURAsk))

    if(response[i]["market"] == "VTHO-EUR"):
        currVTHOEURBid = float(response[i]["bid"])
        currVTHOEURAsk = float(response[i]["ask"])
        print("€ VTHO Bid: " +str(currVTHOEURBid) +" | VTHO Ask: " +str(currVTHOEURAsk))

    if(response[i]["market"] == "WAVES-EUR"):
        currWAVESEURBid = float(response[i]["bid"])
        currWAVESEURAsk = float(response[i]["ask"])
        print("€ WAVES Bid: " +str(currWAVESEURBid) +" | WAVES Ask: " +str(currWAVESEURAsk))

    if(response[i]["market"] == "WTC-EUR"):
        currWTCEURBid = float(response[i]["bid"])
        currWTCEURAsk = float(response[i]["ask"])
        print("€ WTC Bid: " +str(currWTCEURBid) +" | WTC Ask: " +str(currWTCEURAsk))

    if(response[i]["market"] == "XEM-EUR"):
        currXEMEURBid = float(response[i]["bid"])
        currXEMEURAsk = float(response[i]["ask"])
        print("€ XEM Bid: " +str(currXEMEURBid) +" | XEM Ask: " +str(currXEMEURAsk))

    if(response[i]["market"] == "XLM-EUR"):
        currXLMEURBid = float(response[i]["bid"])
        currXLMEURAsk = float(response[i]["ask"])
        print("€ XLM Bid: " +str(currXLMEURBid) +" | XLM Ask: " +str(currXLMEURAsk))

    if(response[i]["market"] == "XTZ-EUR"):
        currXTZEURBid = float(response[i]["bid"])
        currXTZEURAsk = float(response[i]["ask"])
        print("€ XTZ Bid: " +str(currXTZEURBid) +" | XTZ Ask: " +str(currXTZEURAsk))

    if(response[i]["market"] == "XVG-EUR"):
        currXVGEURBid = float(response[i]["bid"])
        currXVGEURAsk = float(response[i]["ask"])
        print("€ XVG Bid: " +str(currXVGEURBid) +" | XVG Ask: " +str(currXVGEURAsk))

    if(response[i]["market"] == "ZIL-EUR"):
        currZILEURBid = float(response[i]["bid"])
        currZILEURAsk = float(response[i]["ask"])
        print("€ ZIL Bid: " +str(currZILEURBid) +" | ZIL Ask: " +str(currZILEURAsk))

    if(response[i]["market"] == "ZRX-EUR"):
        currZRXEURBid = float(response[i]["bid"])
        currZRXEURAsk = float(response[i]["ask"])
        print("€ ZRX Bid: " +str(currZRXEURBid) +" | ZRX Ask: " +str(currZRXEURAsk))



    if(response[i]["market"] == "ETH-BTC"):
        currETHBTCBid = float(response[i]["bid"])
        currETHBTCAsk = float(response[i]["ask"])
        print("B ETH Bid: " +str(currETHBTCBid) +" | ETH Ask: " +str(currETHBTCAsk))

    if(response[i]["market"] == "ADA-BTC"):
        currADABTCBid = float(response[i]["bid"])
        currADABTCAsk = float(response[i]["ask"])
        print("B ADA Bid: " +str("%.10f" % currADABTCBid) +" | ADA Ask: " +str("%.10f" % currADABTCAsk))

    if(response[i]["market"] == "AE-BTC"):
        currAEBTCBid = float(response[i]["bid"])
        currAEBTCAsk = float(response[i]["ask"])
        print("B AE Bid: " +str("%.9f" % currAEBTCBid) +" | AE Ask: " +str("%.9f" % currAEBTCAsk))

    if(response[i]["market"] == "AION-BTC"):
        currAIONBTCBid = float(response[i]["bid"])
        currAIONBTCAsk = float(response[i]["ask"])
        print("B AION Bid: " +str("%.10f" % currAIONBTCBid) +" | AION Ask: " +str("%.10f" % currAIONBTCAsk))

    if(response[i]["market"] == "ANT-BTC"):
        currANTBTCBid = float(response[i]["bid"])
        currANTBTCAsk = float(response[i]["ask"])
        print("B ANT Bid: " +str("%.9f" % currANTBTCBid) +" | ANT Ask: " +str("%.9f" % currANTBTCAsk))

    if(response[i]["market"] == "ARK-BTC"):
        currARKBTCBid = float(response[i]["bid"])
        currARKBTCAsk = float(response[i]["ask"])
        print("B ARK Bid: " +str("%.9f" % currARKBTCBid) +" | ARK Ask: " +str("%.9f" % currARKBTCAsk))

    if(response[i]["market"] == "BAT-BTC"):
        currBATBTCBid = float(response[i]["bid"])
        currBATBTCAsk = float(response[i]["ask"])
        print("B BAT Bid: " +str("%.9f" % currBATBTCBid) +" | BAT Ask: " +str("%.9f" % currBATBTCAsk))

    if(response[i]["market"] == "BCH-BTC"):
        currBCHBTCBid = float(response[i]["bid"])
        currBCHBTCAsk = float(response[i]["ask"])
        print("B BCH Bid: " +str("%.6f" % currBCHBTCBid) +" | BCH Ask: " +str("%.6f" % currBCHBTCAsk))

    if(response[i]["market"] == "BSV-BTC"):
        currBSVBTCBid = float(response[i]["bid"])
        currBSVBTCAsk = float(response[i]["ask"])
        print("B BSV Bid: " +str("%.6f" % currBSVBTCBid) +" | BSV Ask: " +str("%.6f" % currBSVBTCAsk))

    if(response[i]["market"] == "CMT-BTC"):
        currCMTBTCBid = float(response[i]["bid"])
        currCMTBTCAsk = float(response[i]["ask"])
        print("B CMT Bid: " +str("%.10f" % currCMTBTCBid) +" | CMT Ask: " +str("%.10f" % currCMTBTCAsk))

    if(response[i]["market"] == "DCR-BTC"):
        currDCRBTCBid = float(response[i]["bid"])
        currDCRBTCAsk = float(response[i]["ask"])
        print("B DCR Bid: " +str("%.7f" % currDCRBTCBid) +" | DCR Ask: " +str("%.7f" % currDCRBTCAsk))

    if(response[i]["market"] == "DGB-BTC"):
        currDGBBTCBid = float(response[i]["bid"])
        currDGBBTCAsk = float(response[i]["ask"])
        print("B DGB Bid: " +str("%.11f" % currDGBBTCBid) +" | DGB Ask: " +str("%.11f" % currDGBBTCAsk))

    if(response[i]["market"] == "ELF-BTC"):
        currELFBTCBid = float(response[i]["bid"])
        currELFBTCAsk = float(response[i]["ask"])
        print("B ELF Bid: " +str("%.10f" % currELFBTCBid) +" | ELF Ask: " +str("%.10f" % currELFBTCAsk))

    if(response[i]["market"] == "ENJ-BTC"):
        currENJBTCBid = float(response[i]["bid"])
        currENJBTCAsk = float(response[i]["ask"])
        print("B ENJ Bid: " +str("%.10f" % currENJBTCBid) +" | ENJ Ask: " +str("%.10f" % currENJBTCAsk))

    if(response[i]["market"] == "EOS-BTC"):
        currEOSBTCBid = float(response[i]["bid"])
        currEOSBTCAsk = float(response[i]["ask"])
        print("B EOS Bid: " +str("%.8f" % currEOSBTCBid) +" | EOS Ask: " +str("%.8f" % currEOSBTCAsk))

    if(response[i]["market"] == "ETC-BTC"):
        currETCBTCBid = float(response[i]["bid"])
        currETCBTCAsk = float(response[i]["ask"])
        print("B ETC Bid: " +str("%.8f" % currETCBTCBid) +" | ETC Ask: " +str("%.8f" % currETCBTCAsk))

    if(response[i]["market"] == "GAS-BTC"):
        currGASBTCBid = float(response[i]["bid"])
        currGASBTCAsk = float(response[i]["ask"])
        print("B GAS Bid: " +str("%.8f" % currGASBTCBid) +" | GAS Ask: " +str("%.8f" % currGASBTCAsk))

    if(response[i]["market"] == "GNT-BTC"):
        currGNTBTCBid = float(response[i]["bid"])
        currGNTBTCAsk = float(response[i]["ask"])
        print("B GNT Bid: " +str("%.10f" % currGNTBTCBid) +" | GNT Ask: " +str("%.10f" % currGNTBTCAsk))

    if(response[i]["market"] == "HOT-BTC"):
        currHOTBTCBid = float(response[i]["bid"])
        currHOTBTCAsk = float(response[i]["ask"])
        print("B HOT Bid: " +str("%.12f" % currHOTBTCBid) +" | HOT Ask: " +str("%.12f" % currHOTBTCAsk))

    if(response[i]["market"] == "ICX-BTC"):
        currICXBTCBid = float(response[i]["bid"])
        currICXBTCAsk = float(response[i]["ask"])
        print("B ICX Bid: " +str("%.9f" % currICXBTCBid) +" | ICX Ask: " +str("%.9f" % currICXBTCAsk))

    if(response[i]["market"] == "IOST-BTC"):
        currIOSTBTCBid = float(response[i]["bid"])
        currIOSTBTCAsk = float(response[i]["ask"])
        print("B IOST Bid: " +str("%.11f" % currIOSTBTCBid) +" | IOST Ask: " +str("%.11f" % currIOSTBTCAsk))

    if(response[i]["market"] == "KMD-BTC"):
        currKMDBTCBid = float(response[i]["bid"])
        currKMDBTCAsk = float(response[i]["ask"])
        print("B KMD Bid: " +str("%.9f" % currKMDBTCBid) +" | KMD Ask: " +str("%.9f" % currKMDBTCAsk))

    if(response[i]["market"] == "LINK-BTC"):
        currLINKBTCBid = float(response[i]["bid"])
        currLINKBTCAsk = float(response[i]["ask"])
        print("B LINK Bid: " +str("%.8f" % currLINKBTCBid) +" | LINK Ask: " +str("%.8f" % currLINKBTCAsk))

    if(response[i]["market"] == "LRC-BTC"):
        currLRCBTCBid = float(response[i]["bid"])
        currLRCBTCAsk = float(response[i]["ask"])
        print("B LRC Bid: " +str("%.10f" % currLRCBTCBid) +" | LRC Ask: " +str("%.8f" % currLRCBTCAsk))

    if(response[i]["market"] == "LSK-BTC"):
        currLSKBTCBid = float(response[i]["bid"])
        currLSKBTCAsk = float(response[i]["ask"])
        print("B LSK Bid: " +str("%.9f" % currLSKBTCBid) +" | LSK Ask: " +str("%.9f" % currLSKBTCAsk))

    if(response[i]["market"] == "LTC-BTC"):
        currLTCBTCBid = float(response[i]["bid"])
        currLTCBTCAsk = float(response[i]["ask"])
        print("B LTC Bid: " +str("%.7f" % currLTCBTCBid) +" | LTC Ask: " +str("%.7f" % currLTCBTCAsk))

    if(response[i]["market"] == "MIOTA-BTC"):
        currMIOTABTCBid = float(response[i]["bid"])
        currMIOTABTCAsk = float(response[i]["ask"])
        print("B MIOTA Bid: " +str("%.9f" % currMIOTABTCBid) +" | MIOTA Ask: " +str("%.9f" % currMIOTABTCAsk))

    if(response[i]["market"] == "NANO-BTC"):
        currNANOBTCBid = float(response[i]["bid"])
        currNANOBTCAsk = float(response[i]["ask"])
        print("B NANO Bid: " +str("%.9f" % currNANOBTCBid) +" | NANO Ask: " +str("%.9f" % currNANOBTCAsk))

    if(response[i]["market"] == "NAS-BTC"):
        currNASBTCBid = float(response[i]["bid"])
        currNASBTCAsk = float(response[i]["ask"])
        print("B NAS Bid: " +str("%.9f" % currNASBTCBid) +" | NAS Ask: " +str("%.9f" % currNASBTCAsk))

    if(response[i]["market"] == "NEO-BTC"):
        currNEOBTCBid = float(response[i]["bid"])
        currNEOBTCAsk = float(response[i]["ask"])
        print("B NEO Bid: " +str("%.7f" % currNEOBTCBid) +" | NEO Ask: " +str("%.7f" % currNEOBTCAsk))

    if(response[i]["market"] == "NPXS-BTC"):
        currNPXSBTCBid = float(response[i]["bid"])
        currNPXSBTCAsk = float(response[i]["ask"])
        print("B NPXS Bid: " +str("%.12f" % currNPXSBTCBid) +" | NPXS Ask: " +str("%.12f" % currNPXSBTCAsk))

    if(response[i]["market"] == "NULS-BTC"):
        currNULSBTCBid = float(response[i]["bid"])
        currNULSBTCAsk = float(response[i]["ask"])
        print("B NULS Bid: " +str("%.9f" % currNULSBTCBid) +" | NULS Ask: " +str("%.9f" % currNULSBTCAsk))

    if(response[i]["market"] == "OMG-BTC"):
        currOMGBTCBid = float(response[i]["bid"])
        currOMGBTCAsk = float(response[i]["ask"])
        print("B OMG Bid: " +str("%.9f" % currOMGBTCBid) +" | OMG Ask: " +str("%.9f" % currOMGBTCAsk))

    if(response[i]["market"] == "ONG-BTC"):
        currONGBTCBid = float(response[i]["bid"])
        currONGBTCAsk = float(response[i]["ask"])
        print("B ONG Bid: " +str("%.9f" % currONGBTCBid) +" | ONG Ask: " +str("%.9f" % currONGBTCAsk))

    if(response[i]["market"] == "ONT-BTC"):
        currONTBTCBid = float(response[i]["bid"])
        currONTBTCAsk = float(response[i]["ask"])
        print("B ONT Bid: " +str("%.9f" % currONTBTCBid) +" | ONT Ask: " +str("%.9f" % currONTBTCAsk))

    if(response[i]["market"] == "POWR-BTC"):
        currPOWRBTCBid = float(response[i]["bid"])
        currPOWRBTCAsk = float(response[i]["ask"])
        print("B POWR Bid: " +str("%.10f" % currPOWRBTCBid) +" | POWR Ask: " +str("%.10f" % currPOWRBTCAsk))

    if(response[i]["market"] == "QTUM-BTC"):
        currQTUMBTCBid = float(response[i]["bid"])
        currQTUMBTCAsk = float(response[i]["ask"])
        print("B QTUM Bid: " +str("%.8f" % currQTUMBTCBid) +" | QTUM Ask: " +str("%.8f" % currQTUMBTCAsk))

    if(response[i]["market"] == "RDD-BTC"):
        currRDDBTCBid = float(response[i]["bid"])
        currRDDBTCAsk = float(response[i]["ask"])
        print("B RDD Bid: " +str("%.12f" % currRDDBTCBid) +" | RDD Ask: " +str("%.12f" % currRDDBTCAsk))

    if(response[i]["market"] == "REQ-BTC"):
        currREQBTCBid = float(response[i]["bid"])
        currREQBTCAsk = float(response[i]["ask"])
        print("B REQ Bid: " +str("%.10f" % currREQBTCBid) +" | REQ Ask: " +str("%.10f" % currREQBTCAsk))

    if(response[i]["market"] == "RVN-BTC"):
        currRVNBTCBid = float(response[i]["bid"])
        currRVNBTCAsk = float(response[i]["ask"])
        print("B RVN Bid: " +str("%.10f" % currRVNBTCBid) +" | RVN Ask: " +str("%.10f" % currRVNBTCAsk))

    if(response[i]["market"] == "SNT-BTC"):
        currSNTBTCBid = float(response[i]["bid"])
        currSNTBTCAsk = float(response[i]["ask"])
        print("B SNT Bid: " +str("%.10f" % currSNTBTCBid) +" | SNT Ask: " +str("%.10f" % currSNTBTCAsk))

    if(response[i]["market"] == "STEEM-BTC"):
        currSTEEMBTCBid = float(response[i]["bid"])
        currSTEEMBTCAsk = float(response[i]["ask"])
        print("B STEEM Bid: " +str("%.9f" % currSTEEMBTCBid) +" | STEEM Ask: " +str("%.9f" % currSTEEMBTCAsk))

    if(response[i]["market"] == "STORM-BTC"):
        currSTORMBTCBid = float(response[i]["bid"])
        currSTORMBTCAsk = float(response[i]["ask"])
        print("B STORM Bid: " +str("%.11f" % currSTORMBTCBid) +" | STORM Ask: " +str("%.11f" % currSTORMBTCAsk))

    if(response[i]["market"] == "STRAT-BTC"):
        currSTRATBTCBid = float(response[i]["bid"])
        currSTRATBTCAsk = float(response[i]["ask"])
        print("B STRAT Bid: " +str("%.9f" % currSTRATBTCBid) +" | STRAT Ask: " +str("%.9f" % currSTRATBTCAsk))

    if(response[i]["market"] == "TRX-BTC"):
        currTRXBTCBid = float(response[i]["bid"])
        currTRXBTCAsk = float(response[i]["ask"])
        print("B TRX Bid: " +str("%.10f" % currTRXBTCBid) +" | TRX Ask: " +str("%.10f" % currTRXBTCAsk))

    if(response[i]["market"] == "VET-BTC"):
        currVETBTCBid = float(response[i]["bid"])
        currVETBTCAsk = float(response[i]["ask"])
        print("B VET Bid: " +str("%.11f" % currVETBTCBid) +" | VET Ask: " +str("%.11f" % currVETBTCAsk))

    if(response[i]["market"] == "VTC-BTC"):
        currVTCBTCBid = float(response[i]["bid"])
        currVTCBTCAsk = float(response[i]["ask"])
        print("B VTC Bid: " +str("%.9f" % currVTCBTCBid) +" | VTC Ask: " +str("%.9f" % currVTCBTCAsk))

    if(response[i]["market"] == "VTHO-BTC"):
        currVTHOBTCBid = float(response[i]["bid"])
        currVTHOBTCAsk = float(response[i]["ask"])
        print("B VTHO Bid: " +str("%.12f" % currVTHOBTCBid) +" | VTHO Ask: " +str("%.12f" % currVTHOBTCAsk))

    if(response[i]["market"] == "WAVES-BTC"):
        currWAVESBTCBid = float(response[i]["bid"])
        currWAVESBTCAsk = float(response[i]["ask"])
        print("B WAVES Bid: " +str("%.8f" % currWAVESBTCBid) +" | WAVES Ask: " +str("%.8f" % currWAVESBTCAsk))

    if(response[i]["market"] == "WTC-BTC"):
        currWTCBTCBid = float(response[i]["bid"])
        currWTCBTCAsk = float(response[i]["ask"])
        print("B WTC Bid: " +str("%.9f" % currWTCBTCBid) +" | WTC Ask: " +str("%.9f" % currWTCBTCAsk))

    if(response[i]["market"] == "XEM-BTC"):
        currXEMBTCBid = float(response[i]["bid"])
        currXEMBTCAsk = float(response[i]["ask"])
        print("B XEM Bid: " +str("%.10f" % currXEMBTCBid) +" | XEM Ask: " +str("%.10f" % currXEMBTCAsk))

    if(response[i]["market"] == "XLM-BTC"):
        currXLMBTCBid = float(response[i]["bid"])
        currXLMBTCAsk = float(response[i]["ask"])
        print("B XLM Bid: " +str("%.10f" % currXLMBTCBid) +" | XLM Ask: " +str("%.10f" % currXLMBTCAsk))

    if(response[i]["market"] == "XRP-BTC"):
        currXRPBTCBid = float(response[i]["bid"])
        currXRPBTCAsk = float(response[i]["ask"])
        print("B XRP Bid: " +str("%.9f" % currXRPBTCBid) +" | XRP Ask: " +str("%.9f" % currXRPBTCAsk))

    if(response[i]["market"] == "XTZ-BTC"):
        currXTZBTCBid = float(response[i]["bid"])
        currXTZBTCAsk = float(response[i]["ask"])
        print("B XTZ Bid: " +str("%.8f" % currXTZBTCBid) +" | XTZ Ask: " +str("%.8f" % currXTZBTCAsk))

    if(response[i]["market"] == "XVG-BTC"):
        currXVGBTCBid = float(response[i]["bid"])
        currXVGBTCAsk = float(response[i]["ask"])
        print("B XVG Bid: " +str("%.11f" % currXVGBTCBid) +" | XVG Ask: " +str("%.11f" % currXVGBTCAsk))

    if(response[i]["market"] == "ZIL-BTC"):
        currZILBTCBid = float(response[i]["bid"])
        currZILBTCAsk = float(response[i]["ask"])
        print("B ZIL Bid: " +str("%.11f" % currZILBTCBid) +" | ZIL Ask: " +str("%.11f" % currZILBTCAsk))

    if(response[i]["market"] == "ZRX-BTC"):
        currZRXBTCBid = float(response[i]["bid"])
        currZRXBTCAsk = float(response[i]["ask"])
        print("B ZRX Bid: " +str("%.9f" % currZRXBTCBid) +" | ZRX Ask: " +str("%.9f" % currZRXBTCAsk))
            
    print(response[i]["market"])
    i=i+1

      

# Normally you would define a seperate callback for every function.
def callback(response):
  #print("Callback:", json.dumps(response, indent=2))
  #print(strftime("[%H:%M] ") +"Callback Received")

  #Init EUR variables
  global currBTCEURAsk
  global currBTCEURBid

  global currETHEURAsk
  global currETHEURBid

  global currXRPEURAsk
  global currXRPEURBid

  global currADAEURAsk
  global currADAEURBid

  global currAEEURAsk
  global currAEEURBid

  global currAIONEURAsk
  global currAIONEURBid

  global currANTEURAsk
  global currANTEURBid

  global currARKEURAsk
  global currARKEURBid

  global currBATEURAsk
  global currBATEURBid

  global currBCHEURAsk
  global currBCHEURBid

  global currBSVEURAsk
  global currBSVEURBid

  global currCMTEURAsk
  global currCMTEURBid

  global currDCREURAsk
  global currDCREURBid

  global currDGBEURAsk
  global currDGBEURBid

  global currELFEURAsk
  global currELFEURBid

  global currENJEURAsk
  global currENJEURBid

  global currEOSEURAsk
  global currEOSEURBid

  global currETCEURAsk
  global currETCEURBid

  global currGASEURAsk
  global currGASEURBid

  global currGNTEURAsk
  global currGNTEURBid

  global currHOTEURAsk
  global currHOTEURBid

  global currICXEURAsk
  global currICXEURBid

  global currIOSTEURAsk
  global currIOSTEURBid

  global currKMDEURAsk
  global currKMDEURBid

  global currLINKEURAsk
  global currLINKEURBid

  global currLRCEURAsk
  global currLRCEURBid

  global currLSKEURAsk
  global currLSKEURBid

  global currLTCEURAsk
  global currLTCEURBid

  global currMIOTAEURAsk
  global currMIOTAEURBid

  global currNANOEURAsk
  global currNANOEURBid

  global currNASEURAsk
  global currNASEURBid

  global currNEOEURAsk
  global currNEOEURBid

  global currNPXSEURAsk
  global currNPXSEURBid

  global currNULSEURAsk
  global currNULSEURBid

  global currOMGEURAsk
  global currOMGEURBid

  global currONGEURAsk
  global currONGEURBid

  global currONTEURAsk
  global currONTEURBid

  global currPOWREURAsk
  global currPOWREURBid

  global currQTUMEURAsk
  global currQTUMEURBid

  global currRDDEURAsk
  global currRDDEURBid

  global currREQEURAsk
  global currREQEURBid

  global currRVNEURAsk
  global currRVNEURBid

  global currSNTEURAsk
  global currSNTEURBid

  global currSTEEMEURAsk
  global currSTEEMEURBid

  global currSTORMEURAsk
  global currSTORMEURBid

  global currSTRATEURAsk
  global currSTRATEURBid

  global currTRXEURAsk
  global currTRXEURBid

  global currVETEURAsk
  global currVETEURBid

  global currVTCEURAsk
  global currVTCEURBid

  global currVTHOEURAsk
  global currVTHOEURBid

  global currWAVESEURAsk
  global currWAVESEURBid

  global currWTCEURAsk
  global currWTCEURBid

  global currXEMEURAsk
  global currXEMEURBid

  global currXLMEURAsk
  global currXLMEURBid

  global currXTZEURAsk
  global currXTZEURBid

  global currXVGEURAsk
  global currXVGEURBid

  global currZILEURAsk
  global currZILEURBid

  global currZRXEURAsk
  global currZRXEURBid

  #Init BTC variables
  global currETHBTCAsk
  global currETHBTCBid

  global currADABTCAsk
  global currADABTCBid

  global currAEBTCAsk
  global currAEBTCBid

  global currAIONBTCAsk
  global currAIONBTCBid

  global currANTBTCAsk
  global currANTBTCBid

  global currARKBTCAsk
  global currARKBTCBid

  global currBATBTCAsk
  global currBATBTCBid

  global currBCHBTCAsk
  global currBCHBTCBid

  global currBSVBTCAsk
  global currBSVBTCBid

  global currCMTBTCAsk
  global currCMTBTCBid

  global currDCRBTCAsk
  global currDCRBTCBid

  global currDGBBTCAsk
  global currDGBBTCBid

  global currELFBTCAsk
  global currELFBTCBid

  global currENJBTCAsk
  global currENJBTCBid

  global currEOSBTCAsk
  global currEOSBTCBid

  global currETCBTCAsk
  global currETCBTCBid

  global currGASBTCAsk
  global currGASBTCBid

  global currGNTBTCAsk
  global currGNTBTCBid

  global currHOTBTCAsk
  global currHOTBTCBid

  global currICXBTCAsk
  global currICXBTCBid

  global currIOSTBTCAsk
  global currIOSTBTCBid

  global currKMDBTCAsk
  global currKMDBTCBid

  global currLINKBTCAsk
  global currLINKBTCBid

  global currLRCBTCAsk
  global currLRCBTCBid

  global currLSKBTCAsk
  global currLSKBTCBid

  global currLTCBTCAsk
  global currLTCBTCBid

  global currMIOTABTCAsk
  global currMIOTABTCBid

  global currNANOBTCAsk
  global currNANOBTCBid

  global currNASBTCAsk
  global currNASBTCBid

  global currNEOBTCAsk
  global currNEOBTCBid

  global currNPXSBTCAsk
  global currNPXSBTCBid

  global currNULSBTCAsk
  global currNULSBTCBid

  global currOMGBTCAsk
  global currOMGBTCBid

  global currONGBTCAsk
  global currONGBTCBid

  global currONTBTCAsk
  global currONTBTCBid

  global currPOWRBTCAsk
  global currPOWRBTCBid

  global currQTUMBTCAsk
  global currQTUMBTCBid

  global currRDDBTCAsk
  global currRDDBTCBid

  global currREQBTCAsk
  global currREQBTCBid

  global currRVNBTCAsk
  global currRVNBTCBid

  global currSNTBTCAsk
  global currSNTBTCBid

  global currSTEEMBTCAsk
  global currSTEEMBTCBid

  global currSTORMBTCAsk
  global currSTORMBTCBid

  global currSTRATBTCAsk
  global currSTRATBTCBid

  global currTRXBTCAsk
  global currTRXBTCBid

  global currVETBTCAsk
  global currVETBTCBid

  global currVTCBTCAsk
  global currVTCBTCBid

  global currVTHOBTCAsk
  global currVTHOBTCBid

  global currWAVESBTCAsk
  global currWAVESBTCBid

  global currWTCBTCAsk
  global currWTCBTCBid

  global currXEMBTCAsk
  global currXEMBTCBid

  global currXLMBTCAsk
  global currXLMBTCBid

  global currXRPBTCAsk
  global currXRPBTCBid

  global currXTZBTCAsk
  global currXTZBTCBid

  global currXVGBTCAsk
  global currXVGBTCBid

  global currZILBTCAsk
  global currZILBTCBid

  global currZRXBTCAsk
  global currZRXBTCBid
  

  #BTC-EUR
  if(response["market"] == "BTC-EUR" and "bestBid" in response):
    currBTCEURBid = float(response["bestBid"])
    #print("€ BTC Bid: " +str(currBTCEURBid) +" | BTC Ask: " +str(currBTCEURAsk))

  if(response["market"] == "BTC-EUR" and "bestAsk" in response):
    currBTCEURAsk = float(response["bestAsk"])
    #print("€ BTC Bid: " +str(currBTCEURBid) +" | BTC Ask: " +str(currBTCEURAsk))

  #ETH-EUR
  if(response["market"] == "ETH-EUR" and "bestBid" in response):
    currETHEURBid = float(response["bestBid"])
    #print("€ ETH Bid: " +str(currETHEURBid) +" | ETH Ask: " +str(currETHEURAsk))

  if(response["market"] == "ETH-EUR" and "bestAsk" in response):
    currETHEURAsk = float(response["bestAsk"])
    #print("€ ETH Bid: " +str(currETHEURBid) +" | ETH Ask: " +str(currETHEURAsk))

  #XRP-EUR
  if(response["market"] == "XRP-EUR" and "bestBid" in response):
    currXRPEURBid = float(response["bestBid"])
    #print("€ XRP Bid: " +str(currXRPEURBid) +" | XRP Ask: " +str(currXRPEURAsk))

  if(response["market"] == "XRP-EUR" and "bestAsk" in response):
    currXRPEURAsk = float(response["bestAsk"])
    #print("€ XRP Bid: " +str(currXRPEURBid) +" | XRP Ask: " +str(currXRPEURAsk))

  #ADA-EUR
  if(response["market"] == "ADA-EUR" and "bestBid" in response):
    currADAEURBid = float(response["bestBid"])
    #print("€ ADA Bid: " +str(currADAEURBid) +" | ADA Ask: " +str(currADAEURAsk))

  if(response["market"] == "ADA-EUR" and "bestAsk" in response):
    currADAEURAsk = float(response["bestAsk"])
    #print("€ ADA Bid: " +str(currADAEURBid) +" | ADA Ask: " +str(currADAEURAsk))

  #AE-EUR
  if(response["market"] == "AE-EUR" and "bestBid" in response):
    currAEEURBid = float(response["bestBid"])
    #print("€ AE Bid: " +str(currAEEURBid) +" | AE Ask: " +str(currAEEURAsk))

  if(response["market"] == "AE-EUR" and "bestAsk" in response):
    currAEEURAsk = float(response["bestAsk"])
    #print("€ AE Bid: " +str(currAEEURBid) +" | AE Ask: " +str(currAEEURAsk))

  #AION-EUR
  if(response["market"] == "AION-EUR" and "bestBid" in response):
    currAIONEURBid = float(response["bestBid"])
    #print("€ AION Bid: " +str(currAIONEURBid) +" | AION Ask: " +str(currAIONEURAsk))

  if(response["market"] == "AION-EUR" and "bestAsk" in response):
    currAIONEURAsk = float(response["bestAsk"])
    #print("€ AION Bid: " +str(currAIONEURBid) +" | AION Ask: " +str(currAIONEURAsk))

  #ANT-EUR
  if(response["market"] == "ANT-EUR" and "bestBid" in response):
    currANTEURBid = float(response["bestBid"])
    #print("€ ANT Bid: " +str(currANTEURBid) +" | ANT Ask: " +str(currANTEURAsk))

  if(response["market"] == "ANT-EUR" and "bestAsk" in response):
    currANTEURAsk = float(response["bestAsk"])
    #print("€ ANT Bid: " +str(currANTEURBid) +" | ANT Ask: " +str(currANTEURAsk))

  #ARK-EUR
  if(response["market"] == "ARK-EUR" and "bestBid" in response):
    currARKEURBid = float(response["bestBid"])
    #print("€ ARK Bid: " +str(currARKEURBid) +" | ARK Ask: " +str(currARKEURAsk))

  if(response["market"] == "ARK-EUR" and "bestAsk" in response):
    currARKEURAsk = float(response["bestAsk"])
    #print("€ ARK Bid: " +str(currARKEURBid) +" | ARK Ask: " +str(currARKEURAsk))

  #BAT-EUR
  if(response["market"] == "BAT-EUR" and "bestBid" in response):
    currBATEURBid = float(response["bestBid"])
    #print("€ BAT Bid: " +str(currBATEURBid) +" | BAT Ask: " +str(currBATEURAsk))

  if(response["market"] == "BAT-EUR" and "bestAsk" in response):
    currBATEURAsk = float(response["bestAsk"])
    #print("€ BAT Bid: " +str(currBATEURBid) +" | BAT Ask: " +str(currBATEURAsk))

  #BCH-EUR
  if(response["market"] == "BCH-EUR" and "bestBid" in response):
    currBCHEURBid = float(response["bestBid"])
    #print("€ BCH Bid: " +str(currBCHEURBid) +" | BCH Ask: " +str(currBCHEURAsk))

  if(response["market"] == "BCH-EUR" and "bestAsk" in response):
    currBCHEURAsk = float(response["bestAsk"])
    #print("€ BCH Bid: " +str(currBCHEURBid) +" | BCH Ask: " +str(currBCHEURAsk))

  #BSV-EUR
  if(response["market"] == "BSV-EUR" and "bestBid" in response):
    currBSVEURBid = float(response["bestBid"])
    #print("€ BSV Bid: " +str(currBSVEURBid) +" | BSV Ask: " +str(currBSVEURAsk))

  if(response["market"] == "BSV-EUR" and "bestAsk" in response):
    currBSVEURAsk = float(response["bestAsk"])
    #print("€ BSV Bid: " +str(currBSVEURBid) +" | BSV Ask: " +str(currBSVEURAsk))

  #CMT-EUR
  if(response["market"] == "CMT-EUR" and "bestBid" in response):
    currCMTEURBid = float(response["bestBid"])
    #print("€ CMT Bid: " +str(currCMTEURBid) +" | CMT Ask: " +str(currCMTEURAsk))

  if(response["market"] == "CMT-EUR" and "bestAsk" in response):
    currCMTEURAsk = float(response["bestAsk"])
    #print("€ CMT Bid: " +str(currCMTEURBid) +" | CMT Ask: " +str(currCMTEURAsk))

  #DCR-EUR
  if(response["market"] == "DCR-EUR" and "bestBid" in response):
    currDCREURBid = float(response["bestBid"])
    #print("€ DCR Bid: " +str(currDCREURBid) +" | DCR Ask: " +str(currDCREURAsk))

  if(response["market"] == "DCR-EUR" and "bestAsk" in response):
    currDCREURAsk = float(response["bestAsk"])
    #print("€ DCR Bid: " +str(currDCREURBid) +" | DCR Ask: " +str(currDCREURAsk))

  #DGB-EUR
  if(response["market"] == "DGB-EUR" and "bestBid" in response):
    currDGBEURBid = float(response["bestBid"])
    #print("€ DGB Bid: " +str(currDGBEURBid) +" | DGB Ask: " +str(currDGBEURAsk))

  if(response["market"] == "DGB-EUR" and "bestAsk" in response):
    currDGBEURAsk = float(response["bestAsk"])
    #print("€ DGB Bid: " +str(currDGBEURBid) +" | DGB Ask: " +str(currDGBEURAsk))

  #ELF-EUR
  if(response["market"] == "ELF-EUR" and "bestBid" in response):
    currELFEURBid = float(response["bestBid"])
    #print("€ ELF Bid: " +str(currELFEURBid) +" | ELF Ask: " +str(currELFEURAsk))

  if(response["market"] == "ELF-EUR" and "bestAsk" in response):
    currELFEURAsk = float(response["bestAsk"])
    #print("€ ELF Bid: " +str(currELFEURBid) +" | ELF Ask: " +str(currELFEURAsk))

  #ENJ-EUR
  if(response["market"] == "ENJ-EUR" and "bestBid" in response):
    currENJEURBid = float(response["bestBid"])
    #print("€ ENJ Bid: " +str(currELFEURBid) +" | ENJ Ask: " +str(currENJEURAsk))

  if(response["market"] == "ENJ-EUR" and "bestAsk" in response):
    currENJEURAsk = float(response["bestAsk"])
    #print("€ ENJ Bid: " +str(currENJEURBid) +" | ENJ Ask: " +str(currENJEURAsk))

  #EOS-EUR
  if(response["market"] == "EOS-EUR" and "bestBid" in response):
    currEOSEURBid = float(response["bestBid"])
    #print("€ EOS Bid: " +str(currEOSEURBid) +" | EOS Ask: " +str(currEOSEURAsk))

  if(response["market"] == "EOS-EUR" and "bestAsk" in response):
    currEOSEURAsk = float(response["bestAsk"])
    #print("€ EOS Bid: " +str(currEOSEURBid) +" | EOS Ask: " +str(currEOSEURAsk))

  #ETC-EUR
  if(response["market"] == "ETC-EUR" and "bestBid" in response):
    currETCEURBid = float(response["bestBid"])
    #print("€ ETC Bid: " +str(currETCEURBid) +" | ETC Ask: " +str(currETCEURAsk))

  if(response["market"] == "ETC-EUR" and "bestAsk" in response):
    currETCEURAsk = float(response["bestAsk"])
    #print("€ ETC Bid: " +str(currETCEURBid) +" | ETC Ask: " +str(currETCEURAsk))

  #GAS-EUR
  if(response["market"] == "GAS-EUR" and "bestBid" in response):
    currGASEURBid = float(response["bestBid"])
    #print("€ GAS Bid: " +str(currGASEURBid) +" | GAS Ask: " +str(currGASEURAsk))

  if(response["market"] == "GAS-EUR" and "bestAsk" in response):
    currGASEURAsk = float(response["bestAsk"])
    #print("€ GAS Bid: " +str(currGASEURBid) +" | GAS Ask: " +str(currGASEURAsk))

  #GNT-EUR
  if(response["market"] == "GNT-EUR" and "bestBid" in response):
    currGNTEURBid = float(response["bestBid"])
    #print("€ GNT Bid: " +str(currGNTEURBid) +" | GNT Ask: " +str(currGNTEURAsk))

  if(response["market"] == "GNT-EUR" and "bestAsk" in response):
    currGNTEURAsk = float(response["bestAsk"])
    #print("€ GNT Bid: " +str(currGNTEURBid) +" | GNT Ask: " +str(currGNTEURAsk))

  #HOT-EUR
  if(response["market"] == "HOT-EUR" and "bestBid" in response):
    currHOTEURBid = float(response["bestBid"])
    #print("€ HOT Bid: " +str(currHOTEURBid) +" | HOT Ask: " +str(currHOTEURAsk))

  if(response["market"] == "HOT-EUR" and "bestAsk" in response):
    currHOTEURAsk = float(response["bestAsk"])
    #print("€ HOT Bid: " +str(currHOTEURBid) +" | HOT Ask: " +str(currHOTEURAsk))

  #ICX-EUR
  if(response["market"] == "ICX-EUR" and "bestBid" in response):
    currICXEURBid = float(response["bestBid"])
    #print("€ ICX Bid: " +str(currICXEURBid) +" | ICX Ask: " +str(currICXEURAsk))

  if(response["market"] == "ICX-EUR" and "bestAsk" in response):
    currICXEURAsk = float(response["bestAsk"])
    #print("€ ICX Bid: " +str(currICXEURBid) +" | ICX Ask: " +str(currICXEURAsk))

  #IOST-EUR
  if(response["market"] == "IOST-EUR" and "bestBid" in response):
    currIOSTEURBid = float(response["bestBid"])
    #print("€ IOST Bid: " +str(currIOSTEURBid) +" | IOST Ask: " +str(currIOSTEURAsk))

  if(response["market"] == "IOST-EUR" and "bestAsk" in response):
    currIOSTEURAsk = float(response["bestAsk"])
    #print("€ IOST Bid: " +str(currIOSTEURBid) +" | IOST Ask: " +str(currIOSTEURAsk))

  #KMD-EUR
  if(response["market"] == "KMD-EUR" and "bestBid" in response):
    currKMDEURBid = float(response["bestBid"])
    #print("€ KMD Bid: " +str(currKMDEURBid) +" | KMD Ask: " +str(currKMDEURAsk))

  if(response["market"] == "KMD-EUR" and "bestAsk" in response):
    currKMDEURAsk = float(response["bestAsk"])
    #print("€ KMD Bid: " +str(currKMDEURBid) +" | KMD Ask: " +str(currKMDEURAsk))

  #LINK-EUR
  if(response["market"] == "LINK-EUR" and "bestBid" in response):
    currLINKEURBid = float(response["bestBid"])
    #print("€ LINK Bid: " +str(currLINKEURBid) +" | LINK Ask: " +str(currLINKEURAsk))

  if(response["market"] == "LINK-EUR" and "bestAsk" in response):
    currLINKEURAsk = float(response["bestAsk"])
    #print("€ LINK Bid: " +str(currLINKEURBid) +" | LINK Ask: " +str(currLINKEURAsk))

  #LRC-EUR
  if(response["market"] == "LRC-EUR" and "bestBid" in response):
    currLRCEURBid = float(response["bestBid"])
    #print("€ LRC Bid: " +str(currLRCEURBid) +" | LRC Ask: " +str(currLRCEURAsk))

  if(response["market"] == "LRC-EUR" and "bestAsk" in response):
    currLRCEURAsk = float(response["bestAsk"])
    #print("€ LRC Bid: " +str(currLRCEURBid) +" | LRC Ask: " +str(currLRCEURAsk))

  #LSK-EUR
  if(response["market"] == "LSK-EUR" and "bestBid" in response):
    currLSKEURBid = float(response["bestBid"])
    #print("€ LSK Bid: " +str(currLSKEURBid) +" | LSK Ask: " +str(currLSKEURAsk))

  if(response["market"] == "LSK-EUR" and "bestAsk" in response):
    currLSKEURAsk = float(response["bestAsk"])
    #print("€ LSK Bid: " +str(currLSKEURBid) +" | LSK Ask: " +str(currLSKEURAsk))

  #LTC-EUR
  if(response["market"] == "LTC-EUR" and "bestBid" in response):
    currLTCEURBid = float(response["bestBid"])
    #print("€ LTC Bid: " +str(currLTCEURBid) +" | LTC Ask: " +str(currLTCEURAsk))

  if(response["market"] == "LTC-EUR" and "bestAsk" in response):
    currLTCEURAsk = float(response["bestAsk"])
    #print("€ LTC Bid: " +str(currLTCEURBid) +" | LTC Ask: " +str(currLTCEURAsk))

  #MIOTA-EUR
  if(response["market"] == "MIOTA-EUR" and "bestBid" in response):
    currMIOTAEURBid = float(response["bestBid"])
    #print("€ MIOTA Bid: " +str(currMIOTAEURBid) +" | MIOTA Ask: " +str(currMIOTAEURAsk))

  if(response["market"] == "MIOTA-EUR" and "bestAsk" in response):
    currMIOTAEURAsk = float(response["bestAsk"])
    #print("€ MIOTA Bid: " +str(currMIOTAEURBid) +" | MIOTA Ask: " +str(currMIOTAEURAsk))

  #NANO-EUR
  if(response["market"] == "NANO-EUR" and "bestBid" in response):
    currNANOEURBid = float(response["bestBid"])
    #print("€ NANO Bid: " +str(currNANOEURBid) +" | NANO Ask: " +str(currNANOEURAsk))

  if(response["market"] == "NANO-EUR" and "bestAsk" in response):
    currNANOEURAsk = float(response["bestAsk"])
    #print("€ NANO Bid: " +str(currNANOEURBid) +" | NANO Ask: " +str(currNANOEURAsk))

  #NAS-EUR
  if(response["market"] == "NAS-EUR" and "bestBid" in response):
    currNASEURBid = float(response["bestBid"])
    #print("€ NAS Bid: " +str(currNASEURBid) +" | NAS Ask: " +str(currNASEURAsk))

  if(response["market"] == "NAS-EUR" and "bestAsk" in response):
    currNASEURAsk = float(response["bestAsk"])
    #print("€ NAS Bid: " +str(currNASEURBid) +" | NAS Ask: " +str(currNASEURAsk))

  #NEO-EUR
  if(response["market"] == "NEO-EUR" and "bestBid" in response):
    currNEOEURBid = float(response["bestBid"])
    #print("€ NEO Bid: " +str(currNEOEURBid) +" | NEO Ask: " +str(currNEOEURAsk))

  if(response["market"] == "NEO-EUR" and "bestAsk" in response):
    currNEOEURAsk = float(response["bestAsk"])
    #print("€ NEO Bid: " +str(currNEOEURBid) +" | NEO Ask: " +str(currNEOEURAsk))

  #NPXS-EUR
  if(response["market"] == "NPXS-EUR" and "bestBid" in response):
    currNPXSEURBid = float(response["bestBid"])
    #print("€ NPXS Bid: " +str(currNPXSEURBid) +" | NPXS Ask: " +str(currNPXSEURAsk))

  if(response["market"] == "NPXS-EUR" and "bestAsk" in response):
    currNPXSEURAsk = float(response["bestAsk"])
    #print("€ NPXS Bid: " +str(currNPXSEURBid) +" | NPXS Ask: " +str(currNPXSEURAsk))

  #NULS-EUR
  if(response["market"] == "NULS-EUR" and "bestBid" in response):
    currNULSEURBid = float(response["bestBid"])
    #print("€ NULS Bid: " +str(currNULSEURBid) +" | NULS Ask: " +str(currNULSEURAsk))

  if(response["market"] == "NULS-EUR" and "bestAsk" in response):
    currNULSEURAsk = float(response["bestAsk"])
    #print("€ NULS Bid: " +str(currNULSEURBid) +" | NULS Ask: " +str(currNULSEURAsk))

  #OMG-EUR
  if(response["market"] == "OMG-EUR" and "bestBid" in response):
    currOMGEURBid = float(response["bestBid"])
    #print("€ OMG Bid: " +str(currOMGEURBid) +" | OMG Ask: " +str(currOMGEURAsk))

  if(response["market"] == "OMG-EUR" and "bestAsk" in response):
    currOMGEURAsk = float(response["bestAsk"])
    #print("€ OMG Bid: " +str(currOMGEURBid) +" | OMG Ask: " +str(currOMGEURAsk))

  #ONG-EUR
  if(response["market"] == "ONG-EUR" and "bestBid" in response):
    currONGEURBid = float(response["bestBid"])
    #print("€ ONG Bid: " +str(currONGEURBid) +" | ONG Ask: " +str(currONGEURAsk))

  if(response["market"] == "ONG-EUR" and "bestAsk" in response):
    currONGEURAsk = float(response["bestAsk"])
    #print("€ ONG Bid: " +str(currONGEURBid) +" | ONG Ask: " +str(currONGEURAsk))

  #ONT-EUR
  if(response["market"] == "ONT-EUR" and "bestBid" in response):
    currONTEURBid = float(response["bestBid"])
    #print("€ ONT Bid: " +str(currONTEURBid) +" | ONT Ask: " +str(currONTEURAsk))

  if(response["market"] == "ONT-EUR" and "bestAsk" in response):
    currONTEURAsk = float(response["bestAsk"])
    #print("€ ONT Bid: " +str(currONTEURBid) +" | ONT Ask: " +str(currONTEURAsk))

  #POWR-EUR
  if(response["market"] == "POWR-EUR" and "bestBid" in response):
    currPOWREURBid = float(response["bestBid"])
    #print("€ POWR Bid: " +str(currPOWREURBid) +" | POWR Ask: " +str(currPOWREURAsk))

  if(response["market"] == "POWR-EUR" and "bestAsk" in response):
    currPOWREURAsk = float(response["bestAsk"])
    #print("€ POWR Bid: " +str(currPOWREURBid) +" | POWR Ask: " +str(currPOWREURAsk))

  #QTUM-EUR
  if(response["market"] == "QTUM-EUR" and "bestBid" in response):
    currQTUMEURBid = float(response["bestBid"])
    #print("€ QTUM Bid: " +str(currQTUMEURBid) +" | QTUM Ask: " +str(currQTUMEURAsk))

  if(response["market"] == "QTUM-EUR" and "bestAsk" in response):
    currQTUMEURAsk = float(response["bestAsk"])
    #print("€ QTUM Bid: " +str(currQTUMEURBid) +" | QTUM Ask: " +str(currQTUMEURAsk))

  #RDD-EUR
  if(response["market"] == "RDD-EUR" and "bestBid" in response):
    currRDDEURBid = float(response["bestBid"])
    #print("€ RDD Bid: " +str(currRDDEURBid) +" | RDD Ask: " +str(currRDDEURAsk))

  if(response["market"] == "RDD-EUR" and "bestAsk" in response):
    currRDDEURAsk = float(response["bestAsk"])
    #print("€ RDD Bid: " +str(currRDDEURBid) +" | RDD Ask: " +str(currRDDEURAsk))

  #REQ-EUR
  if(response["market"] == "REQ-EUR" and "bestBid" in response):
    currREQEURBid = float(response["bestBid"])
    #print("€ REQ Bid: " +str(currREQEURBid) +" | REQ Ask: " +str(currREQEURAsk))

  if(response["market"] == "REQ-EUR" and "bestAsk" in response):
    currREQEURAsk = float(response["bestAsk"])
    #print("€ REQ Bid: " +str(currREQEURBid) +" | REQ Ask: " +str(currREQEURAsk))

  #RVN-EUR
  if(response["market"] == "RVN-EUR" and "bestBid" in response):
    currRVNEURBid = float(response["bestBid"])
    #print("€ RVN Bid: " +str(currRVNEURBid) +" | RVN Ask: " +str(currRVNEURAsk))

  if(response["market"] == "RVN-EUR" and "bestAsk" in response):
    currRVNEURAsk = float(response["bestAsk"])
    #print("€ RVN Bid: " +str(currRVNEURBid) +" | RVN Ask: " +str(currRVNEURAsk))

  #SNT-EUR
  if(response["market"] == "SNT-EUR" and "bestBid" in response):
    currSNTEURBid = float(response["bestBid"])
    #print("€ SNT Bid: " +str(currSNTEURBid) +" | SNT Ask: " +str(currSNTEURAsk))

  if(response["market"] == "SNT-EUR" and "bestAsk" in response):
    currSNTEURAsk = float(response["bestAsk"])
    #print("€ SNT Bid: " +str(currSNTEURBid) +" | SNT Ask: " +str(currSNTEURAsk))

  #STEEM-EUR
  if(response["market"] == "STEEM-EUR" and "bestBid" in response):
    currSTEEMEURBid = float(response["bestBid"])
    #print("€ STEEM Bid: " +str(currSTEEMEURBid) +" | STEEM Ask: " +str(currSTEEMEURAsk))

  if(response["market"] == "STEEM-EUR" and "bestAsk" in response):
    currSTEEMEURAsk = float(response["bestAsk"])
    #print("€ STEEM Bid: " +str(currSTEEMEURBid) +" | STEEM Ask: " +str(currSTEEMEURAsk))

  #STORM-EUR
  if(response["market"] == "STORM-EUR" and "bestBid" in response):
    currSTORMEURBid = float(response["bestBid"])
    #print("€ STORM Bid: " +str(currSTORMEURBid) +" | STORM Ask: " +str(currSTORMEURAsk))

  if(response["market"] == "STORM-EUR" and "bestAsk" in response):
    currSTORMEURAsk = float(response["bestAsk"])
    #print("€ STORM Bid: " +str(currSTORMEURBid) +" | STORM Ask: " +str(currSTORMEURAsk))

  #STRAT-EUR
  if(response["market"] == "STRAT-EUR" and "bestBid" in response):
    currSTRATEURBid = float(response["bestBid"])
    #print("€ STRAT Bid: " +str(currSTRATEURBid) +" | STRAT Ask: " +str(currSTRATEURAsk))

  if(response["market"] == "STRAT-EUR" and "bestAsk" in response):
    currSTRATEURAsk = float(response["bestAsk"])
    #print("€ STRAT Bid: " +str(currSTRATEURBid) +" | STRAT Ask: " +str(currSTRATEURAsk))

  #TRX-EUR
  if(response["market"] == "TRX-EUR" and "bestBid" in response):
    currTRXEURBid = float(response["bestBid"])
    #print("€ TRX Bid: " +str(currTRXEURBid) +" | TRX Ask: " +str(currTRXEURAsk))

  if(response["market"] == "TRX-EUR" and "bestAsk" in response):
    currTRXEURAsk = float(response["bestAsk"])
    #print("€ TRX Bid: " +str(currTRXEURBid) +" | TRX Ask: " +str(currTRXEURAsk))

  #VET-EUR
  if(response["market"] == "VET-EUR" and "bestBid" in response):
    currVETEURBid = float(response["bestBid"])
    #print("€ VET Bid: " +str(currVETEURBid) +" | VET Ask: " +str(currVETEURAsk))

  if(response["market"] == "VET-EUR" and "bestAsk" in response):
    currVETEURAsk = float(response["bestAsk"])
    #print("€ VET Bid: " +str(currVETEURBid) +" | VET Ask: " +str(currVETEURAsk))

  #VTC-EUR
  if(response["market"] == "VTC-EUR" and "bestBid" in response):
    currVTCEURBid = float(response["bestBid"])
    #print("€ VTC Bid: " +str(currVTCEURBid) +" | VTC Ask: " +str(currVTCEURAsk))

  if(response["market"] == "VTC-EUR" and "bestAsk" in response):
    currVTCEURAsk = float(response["bestAsk"])
    #print("€ VTC Bid: " +str(currVTCEURBid) +" | VTC Ask: " +str(currVTCEURAsk))

  #VTHO-EUR
  if(response["market"] == "VTHO-EUR" and "bestBid" in response):
    currVTHOEURBid = float(response["bestBid"])
    #print("€ VTHO Bid: " +str(currVTHOEURBid) +" | VTHO Ask: " +str(currVTHOEURAsk))

  if(response["market"] == "VTHO-EUR" and "bestAsk" in response):
    currVTHOEURAsk = float(response["bestAsk"])
    #print("€ VTHO Bid: " +str(currVTHOEURBid) +" | VTHO Ask: " +str(currVTHOEURAsk))

  #WAVES-EUR
  if(response["market"] == "WAVES-EUR" and "bestBid" in response):
    currWAVESEURBid = float(response["bestBid"])
    #print("€ WAVES Bid: " +str(currWAVESEURBid) +" | WAVES Ask: " +str(currWAVESEURAsk))

  if(response["market"] == "WAVES-EUR" and "bestAsk" in response):
    currWAVESEURAsk = float(response["bestAsk"])
    #print("€ WAVES Bid: " +str(currWAVESEURBid) +" | WAVES Ask: " +str(currWAVESEURAsk))

  #WTC-EUR
  if(response["market"] == "WTC-EUR" and "bestBid" in response):
    currWTCEURBid = float(response["bestBid"])
    #print("€ WTC Bid: " +str(currWTCEURBid) +" | WTC Ask: " +str(currWTCEURAsk))

  if(response["market"] == "WTC-EUR" and "bestAsk" in response):
    currWTCEURAsk = float(response["bestAsk"])
    #print("€ WTC Bid: " +str(currWTCEURBid) +" | WTC Ask: " +str(currWTCEURAsk))

  #XEM-EUR
  if(response["market"] == "XEM-EUR" and "bestBid" in response):
    currXEMEURBid = float(response["bestBid"])
    #print("€ XEM Bid: " +str(currXEMEURBid) +" | XEM Ask: " +str(currXEMEURAsk))

  if(response["market"] == "XEM-EUR" and "bestAsk" in response):
    currXEMEURAsk = float(response["bestAsk"])
    #print("€ XEM Bid: " +str(currXEMEURBid) +" | XEM Ask: " +str(currXEMEURAsk))

  #XLM-EUR
  if(response["market"] == "XLM-EUR" and "bestBid" in response):
    currXLMEURBid = float(response["bestBid"])
    #print("€ XLM Bid: " +str(currXLMEURBid) +" | XLM Ask: " +str(currXLMEURAsk))

  if(response["market"] == "XLM-EUR" and "bestAsk" in response):
    currXLMEURAsk = float(response["bestAsk"])
    #print("€ XLM Bid: " +str(currXLMEURBid) +" | XLM Ask: " +str(currXLMEURAsk))

  #XTZ-EUR
  if(response["market"] == "XTZ-EUR" and "bestBid" in response):
    currXTZEURBid = float(response["bestBid"])
    #print("€ XTZ Bid: " +str(currXTZEURBid) +" | XTZ Ask: " +str(currXTZEURAsk))

  if(response["market"] == "XTZ-EUR" and "bestAsk" in response):
    currXTZEURAsk = float(response["bestAsk"])
    #print("€ XTZ Bid: " +str(currXTZEURBid) +" | XTZ Ask: " +str(currXTZEURAsk))

  #XVG-EUR
  if(response["market"] == "XVG-EUR" and "bestBid" in response):
    currXVGEURBid = float(response["bestBid"])
    #print("€ XVG Bid: " +str(currXVGEURBid) +" | XVG Ask: " +str(currXVGEURAsk))

  if(response["market"] == "XVG-EUR" and "bestAsk" in response):
    currXVGEURAsk = float(response["bestAsk"])
    #print("€ XVG Bid: " +str(currXVGEURBid) +" | XVG Ask: " +str(currXVGEURAsk))

  #ZIL-EUR
  if(response["market"] == "ZIL-EUR" and "bestBid" in response):
    currZILEURBid = float(response["bestBid"])
    #print("€ ZIL Bid: " +str(currZILEURBid) +" | ZIL Ask: " +str(currZILEURAsk))

  if(response["market"] == "ZIL-EUR" and "bestAsk" in response):
    currZILEURAsk = float(response["bestAsk"])
    #print("€ ZIL Bid: " +str(currZILEURBid) +" | ZIL Ask: " +str(currZILEURAsk))

  #ZRX-EUR
  if(response["market"] == "ZRX-EUR" and "bestBid" in response):
    currZRXEURBid = float(response["bestBid"])
    #print("€ ZRX Bid: " +str(currZRXEURBid) +" | ZRX Ask: " +str(currZRXEURAsk))

  if(response["market"] == "ZRX-EUR" and "bestAsk" in response):
    currZRXEURAsk = float(response["bestAsk"])
    #print("€ ZRX Bid: " +str(currZRXEURBid) +" | ZRX Ask: " +str(currZRXEURAsk))


  #ETH-BTC
  if(response["market"] == "ETH-BTC" and "bestBid" in response):
    currETHBTCBid = float(response["bestBid"])
    #print("B ETH Bid: " +str(currETHBTCBid) +" | ETH Ask: " +str(currETHBTCAsk))

  if(response["market"] == "ETH-BTC" and "bestAsk" in response):
    currETHBTCAsk = float(response["bestAsk"])
    #print("B ETH Bid: " +str(currETHBTCBid) +" | ETH Ask: " +str(currETHBTCAsk))

  #ADA-BTC
  if(response["market"] == "ADA-BTC" and "bestBid" in response):
    currADABTCBid = float(response["bestBid"])
    #print("B ADA Bid: " +str("%.10f" % currADABTCBid) +" | ADA Ask: " +str("%.10f" % currADABTCAsk))

  if(response["market"] == "ADA-BTC" and "bestAsk" in response):
    currADABTCAsk = float(response["bestAsk"])
    #print("B ADA Bid: " +str("%.10f" % currADABTCBid) +" | ADA Ask: " +str("%.10f" % currADABTCAsk))

  #AE-BTC
  if(response["market"] == "AE-BTC" and "bestBid" in response):
    currAEBTCBid = float(response["bestBid"])
    #print("B AE Bid: " +str("%.9f" % currAEBTCBid) +" | AE Ask: " +str("%.9f" % currAEBTCAsk))

  if(response["market"] == "AE-BTC" and "bestAsk" in response):
    currAEBTCAsk = float(response["bestAsk"])
    #print("B AE Bid: " +str("%.9f" % currAEBTCBid) +" | AE Ask: " +str("%.9f" % currAEBTCAsk))

  #AION-BTC
  if(response["market"] == "AION-BTC" and "bestBid" in response):
    currAIONBTCBid = float(response["bestBid"])
    #print("B AION Bid: " +str("%.10f" % currAIONBTCBid) +" | AION Ask: " +str("%.10f" % currAIONBTCAsk))

  if(response["market"] == "AION-BTC" and "bestAsk" in response):
    currAIONBTCAsk = float(response["bestAsk"])
    #print("B AION Bid: " +str("%.10f" % currAIONBTCBid) +" | AION Ask: " +str("%.10f" % currAIONBTCAsk))

  #ANT-BTC
  if(response["market"] == "ANT-BTC" and "bestBid" in response):
    currANTBTCBid = float(response["bestBid"])
    #print("B ANT Bid: " +str("%.9f" % currANTBTCBid) +" | ANT Ask: " +str("%.9f" % currANTBTCAsk))

  if(response["market"] == "ANT-BTC" and "bestAsk" in response):
    currANTBTCAsk = float(response["bestAsk"])
    #print("B ANT Bid: " +str("%.9f" % currANTBTCBid) +" | ANT Ask: " +str("%.9f" % currANTBTCAsk))

  #ARK-BTC
  if(response["market"] == "ARK-BTC" and "bestBid" in response):
    currARKBTCBid = float(response["bestBid"])
    #print("B ARK Bid: " +str("%.9f" % currARKBTCBid) +" | ARK Ask: " +str("%.9f" % currARKBTCAsk))

  if(response["market"] == "ARK-BTC" and "bestAsk" in response):
    currARKBTCAsk = float(response["bestAsk"])
    #print("B ARK Bid: " +str("%.9f" % currARKBTCBid) +" | ARK Ask: " +str("%.9f" % currARKBTCAsk))

  #BAT-BTC
  if(response["market"] == "BAT-BTC" and "bestBid" in response):
    currBATBTCBid = float(response["bestBid"])
    #print("B BAT Bid: " +str("%.9f" % currBATBTCBid) +" | BAT Ask: " +str("%.9f" % currBATBTCAsk))

  if(response["market"] == "BAT-BTC" and "bestAsk" in response):
    currBATBTCAsk = float(response["bestAsk"])
    #print("B BAT Bid: " +str("%.9f" % currBATBTCBid) +" | BAT Ask: " +str("%.9f" % currBATBTCAsk))

  #BCH-BTC
  if(response["market"] == "BCH-BTC" and "bestBid" in response):
    currBCHBTCBid = float(response["bestBid"])
    #print("B BCH Bid: " +str("%.6f" % currBCHBTCBid) +" | BCH Ask: " +str("%.6f" % currBCHBTCAsk))

  if(response["market"] == "BCH-BTC" and "bestAsk" in response):
    currBCHBTCAsk = float(response["bestAsk"])
    #print("B BCH Bid: " +str("%.6f" % currBCHBTCBid) +" | BCH Ask: " +str("%.6f" % currBCHBTCAsk))

  #BSV-BTC
  if(response["market"] == "BSV-BTC" and "bestBid" in response):
    currBSVBTCBid = float(response["bestBid"])
    #print("B BSV Bid: " +str("%.6f" % currBSVBTCBid) +" | BSV Ask: " +str("%.6f" % currBSVBTCAsk))

  if(response["market"] == "BSV-BTC" and "bestAsk" in response):
    currBSVBTCAsk = float(response["bestAsk"])
    #print("B BSV Bid: " +str("%.6f" % currBSVBTCBid) +" | BSV Ask: " +str("%.6f" % currBSVBTCAsk))

  #CMT-BTC
  if(response["market"] == "CMT-BTC" and "bestBid" in response):
    currCMTBTCBid = float(response["bestBid"])
    #print("B CMT Bid: " +str("%.10f" % currCMTBTCBid) +" | CMT Ask: " +str("%.10f" % currCMTBTCAsk))

  if(response["market"] == "CMT-BTC" and "bestAsk" in response):
    currCMTBTCAsk = float(response["bestAsk"])
    #print("B CMT Bid: " +str("%.10f" % currCMTBTCBid) +" | CMT Ask: " +str("%.10f" % currCMTBTCAsk))

  #DCR-BTC
  if(response["market"] == "DCR-BTC" and "bestBid" in response):
    currDCRBTCBid = float(response["bestBid"])
    #print("B DCR Bid: " +str("%.7f" % currDCRBTCBid) +" | DCR Ask: " +str("%.7f" % currDCRBTCAsk))

  if(response["market"] == "DCR-BTC" and "bestAsk" in response):
    currDCRBTCAsk = float(response["bestAsk"])
    #print("B DCR Bid: " +str("%.7f" % currDCRBTCBid) +" | DCR Ask: " +str("%.7f" % currDCRBTCAsk))

  #DGB-BTC
  if(response["market"] == "DGB-BTC" and "bestBid" in response):
    currDGBBTCBid = float(response["bestBid"])
    #print("B DGB Bid: " +str("%.11f" % currDGBBTCBid) +" | DGB Ask: " +str("%.11f" % currDGBBTCAsk))

  if(response["market"] == "DGB-BTC" and "bestAsk" in response):
    currDGBBTCAsk = float(response["bestAsk"])
    #print("B DGB Bid: " +str("%.11f" % currDGBBTCBid) +" | DGB Ask: " +str("%.11f" % currDGBBTCAsk))

  #ELF-BTC
  if(response["market"] == "ELF-BTC" and "bestBid" in response):
    currELFBTCBid = float(response["bestBid"])
    #print("B ELF Bid: " +str("%.10f" % currELFBTCBid) +" | ELF Ask: " +str("%.10f" % currELFBTCAsk))

  if(response["market"] == "ELF-BTC" and "bestAsk" in response):
    currELFBTCAsk = float(response["bestAsk"])
    #print("B ELF Bid: " +str("%.10f" % currELFBTCBid) +" | ELF Ask: " +str("%.10f" % currELFBTCAsk))

  #ENJ-BTC
  if(response["market"] == "ENJ-BTC" and "bestBid" in response):
    currENJBTCBid = float(response["bestBid"])
    #print("B ENJ Bid: " +str("%.10f" % currENJBTCBid) +" | ENJ Ask: " +str("%.10f" % currENJBTCAsk))

  if(response["market"] == "ENJ-BTC" and "bestAsk" in response):
    currENJBTCAsk = float(response["bestAsk"])
    #print("B ENJ Bid: " +str("%.10f" % currENJBTCBid) +" | ENJ Ask: " +str("%.10f" % currENJBTCAsk))

  #EOS-BTC
  if(response["market"] == "EOS-BTC" and "bestBid" in response):
    currEOSBTCBid = float(response["bestBid"])
    #print("B EOS Bid: " +str("%.8f" % currEOSBTCBid) +" | EOS Ask: " +str("%.8f" % currEOSBTCAsk))

  if(response["market"] == "EOS-BTC" and "bestAsk" in response):
    currEOSBTCAsk = float(response["bestAsk"])
    #print("B EOS Bid: " +str("%.8f" % currEOSBTCBid) +" | EOS Ask: " +str("%.8f" % currEOSBTCAsk))

  #ETC-BTC
  if(response["market"] == "ETC-BTC" and "bestBid" in response):
    currETCBTCBid = float(response["bestBid"])
    #print("B ETC Bid: " +str("%.8f" % currETCBTCBid) +" | ETC Ask: " +str("%.8f" % currETCBTCAsk))

  if(response["market"] == "ETC-BTC" and "bestAsk" in response):
    currETCBTCAsk = float(response["bestAsk"])
    #print("B ETC Bid: " +str("%.8f" % currETCBTCBid) +" | ETC Ask: " +str("%.8f" % currETCBTCAsk))

  #GAS-BTC
  if(response["market"] == "GAS-BTC" and "bestBid" in response):
    currGASBTCBid = float(response["bestBid"])
    #print("B GAS Bid: " +str("%.8f" % currGASBTCBid) +" | GAS Ask: " +str("%.8f" % currGASBTCAsk))

  if(response["market"] == "GAS-BTC" and "bestAsk" in response):
    currGASBTCAsk = float(response["bestAsk"])
    #print("B GAS Bid: " +str("%.8f" % currGASBTCBid) +" | GAS Ask: " +str("%.8f" % currGASBTCAsk))

  #GNT-BTC
  if(response["market"] == "GNT-BTC" and "bestBid" in response):
    currGNTBTCBid = float(response["bestBid"])
    #print("B GNT Bid: " +str("%.8f" % currGNTBTCBid) +" | GNT Ask: " +str("%.8f" % currGNTBTCAsk))

  if(response["market"] == "GNT-BTC" and "bestAsk" in response):
    currGNTBTCAsk = float(response["bestAsk"])
    #print("B GNT Bid: " +str("%.8f" % currGNTBTCBid) +" | GNT Ask: " +str("%.8f" % currGNTBTCAsk))

  #HOT-BTC
  if(response["market"] == "HOT-BTC" and "bestBid" in response):
    currHOTBTCBid = float(response["bestBid"])
    #print("B HOT Bid: " +str("%.12f" % currHOTBTCBid) +" | HOT Ask: " +str("%.12f" % currHOTBTCAsk))

  if(response["market"] == "HOT-BTC" and "bestAsk" in response):
    currHOTBTCAsk = float(response["bestAsk"])
    #print("B HOT Bid: " +str("%.12f" % currHOTBTCBid) +" | HOT Ask: " +str("%.12f" % currHOTBTCAsk))

  #ICX-BTC
  if(response["market"] == "ICX-BTC" and "bestBid" in response):
    currICXBTCBid = float(response["bestBid"])
    #print("B ICX Bid: " +str("%.9f" % currICXBTCBid) +" | ICX Ask: " +str("%.9f" % currICXBTCAsk))

  if(response["market"] == "ICX-BTC" and "bestAsk" in response):
    currICXBTCAsk = float(response["bestAsk"])
    #print("B ICX Bid: " +str("%.9f" % currICXBTCBid) +" | ICX Ask: " +str("%.9f" % currICXBTCAsk))

  #IOST-BTC
  if(response["market"] == "IOST-BTC" and "bestBid" in response):
    currIOSTBTCBid = float(response["bestBid"])
    #print("B IOST Bid: " +str("%.11f" % currIOSTBTCBid) +" | IOST Ask: " +str("%.11f" % currIOSTBTCAsk))

  if(response["market"] == "IOST-BTC" and "bestAsk" in response):
    currIOSTBTCAsk = float(response["bestAsk"])
    #print("B IOST Bid: " +str("%.11f" % currIOSTBTCBid) +" | IOST Ask: " +str("%.11f" % currIOSTBTCAsk))

  #KMD-BTC
  if(response["market"] == "KMD-BTC" and "bestBid" in response):
    currKMDBTCBid = float(response["bestBid"])
    #print("B KMD Bid: " +str("%.9f" % currKMDBTCBid) +" | KMD Ask: " +str("%.9f" % currKMDBTCAsk))

  if(response["market"] == "KMD-BTC" and "bestAsk" in response):
    currKMDBTCAsk = float(response["bestAsk"])
    #print("B KMD Bid: " +str("%.9f" % currKMDBTCBid) +" | KMD Ask: " +str("%.9f" % currKMDBTCAsk))

  #LINK-BTC
  if(response["market"] == "LINK-BTC" and "bestBid" in response):
    currLINKBTCBid = float(response["bestBid"])
    #print("B LINK Bid: " +str("%.8f" % currLINKBTCBid) +" | LINK Ask: " +str("%.8f" % currLINKBTCAsk))

  if(response["market"] == "LINK-BTC" and "bestAsk" in response):
    currLINKBTCAsk = float(response["bestAsk"])
    #print("B LINK Bid: " +str("%.8f" % currLINKBTCBid) +" | LINK Ask: " +str("%.8f" % currLINKBTCAsk))

  #LRC-BTC
  if(response["market"] == "LRC-BTC" and "bestBid" in response):
    currLRCBTCBid = float(response["bestBid"])
    #print("B LRC Bid: " +str("%.10f" % currLRCBTCBid) +" | LRC Ask: " +str("%.10f" % currLRCBTCAsk))

  if(response["market"] == "LRC-BTC" and "bestAsk" in response):
    currLRCBTCAsk = float(response["bestAsk"])
    #print("B LRC Bid: " +str("%.10f" % currLRCBTCBid) +" | LRC Ask: " +str("%.10f" % currLRCBTCAsk))

  #LSK-BTC
  if(response["market"] == "LSK-BTC" and "bestBid" in response):
    currLSKBTCBid = float(response["bestBid"])
    #print("B LSK Bid: " +str("%.9f" % currLSKBTCBid) +" | LSK Ask: " +str("%.9f" % currLSKBTCAsk))

  if(response["market"] == "LSK-BTC" and "bestAsk" in response):
    currLSKBTCAsk = float(response["bestAsk"])
    #print("B LSK Bid: " +str("%.9f" % currLSKBTCBid) +" | LSK Ask: " +str("%.9f" % currLSKBTCAsk))

  #LTC-BTC
  if(response["market"] == "LTC-BTC" and "bestBid" in response):
    currLTCBTCBid = float(response["bestBid"])
    #print("B LTC Bid: " +str("%.7f" % currLTCBTCBid) +" | LTC Ask: " +str("%.7f" % currLTCBTCAsk))

  if(response["market"] == "LTC-BTC" and "bestAsk" in response):
    currLTCBTCAsk = float(response["bestAsk"])
    #print("B LTC Bid: " +str("%.7f" % currLTCBTCBid) +" | LTC Ask: " +str("%.7f" % currLTCBTCAsk))

  #MIOTA-BTC
  if(response["market"] == "MIOTA-BTC" and "bestBid" in response):
    currMIOTABTCBid = float(response["bestBid"])
    #print("B MIOTA Bid: " +str("%.9f" % currMIOTABTCBid) +" | MIOTA Ask: " +str("%.9f" % currMIOTABTCAsk))

  if(response["market"] == "MIOTA-BTC" and "bestAsk" in response):
    currMIOTABTCAsk = float(response["bestAsk"])
    #print("B MIOTA Bid: " +str("%.9f" % currMIOTABTCBid) +" | MIOTA Ask: " +str("%.9f" % currMIOTABTCAsk))

  #NANO-BTC
  if(response["market"] == "NANO-BTC" and "bestBid" in response):
    currNANOBTCBid = float(response["bestBid"])
    #print("B NANO Bid: " +str("%.9f" % currNANOBTCBid) +" | NANO Ask: " +str("%.9f" % currNANOBTCAsk))

  if(response["market"] == "NANO-BTC" and "bestAsk" in response):
    currNANOBTCAsk = float(response["bestAsk"])
    #print("B NANO Bid: " +str("%.9f" % currNANOBTCBid) +" | NANO Ask: " +str("%.9f" % currNANOBTCAsk))

  #NAS-BTC
  if(response["market"] == "NAS-BTC" and "bestBid" in response):
    currNASBTCBid = float(response["bestBid"])
    #print("B NAS Bid: " +str("%.9f" % currNASBTCBid) +" | NAS Ask: " +str("%.9f" % currNASBTCAsk))

  if(response["market"] == "NAS-BTC" and "bestAsk" in response):
    currNASBTCAsk = float(response["bestAsk"])
    #print("B NAS Bid: " +str("%.9f" % currNASBTCBid) +" | NAS Ask: " +str("%.9f" % currNASBTCAsk))

  #NEO-BTC
  if(response["market"] == "NEO-BTC" and "bestBid" in response):
    currNEOBTCBid = float(response["bestBid"])
    #print("B NEO Bid: " +str("%.7f" % currNEOBTCBid) +" | NEO Ask: " +str("%.7f" % currNEOBTCAsk))

  if(response["market"] == "NEO-BTC" and "bestAsk" in response):
    currNEOBTCAsk = float(response["bestAsk"])
    #print("B NEO Bid: " +str("%.7f" % currNEOBTCBid) +" | NEO Ask: " +str("%.7f" % currNEOBTCAsk))

  #NPXS-BTC
  if(response["market"] == "NPXS-BTC" and "bestBid" in response):
    currNPXSBTCBid = float(response["bestBid"])
    #print("B NPXS Bid: " +str("%.12f" % currNPXSBTCBid) +" | NPXS Ask: " +str("%.12f" % currNPXSBTCAsk))

  if(response["market"] == "NPXS-BTC" and "bestAsk" in response):
    currNPXSBTCAsk = float(response["bestAsk"])
    #print("B NPXS Bid: " +str("%.12f" % currNPXSBTCBid) +" | NPXS Ask: " +str("%.12f" % currNPXSBTCAsk))

  #NULS-BTC
  if(response["market"] == "NULS-BTC" and "bestBid" in response):
    currNULSBTCBid = float(response["bestBid"])
    #print("B NULS Bid: " +str("%.9f" % currNULSBTCBid) +" | NULS Ask: " +str("%.9f" % currNULSBTCAsk))

  if(response["market"] == "NULS-BTC" and "bestAsk" in response):
    currNULSBTCAsk = float(response["bestAsk"])
    #print("B NULS Bid: " +str("%.9f" % currNULSBTCBid) +" | NULS Ask: " +str("%.9f" % currNULSBTCAsk))

  #OMG-BTC
  if(response["market"] == "OMG-BTC" and "bestBid" in response):
    currOMGBTCBid = float(response["bestBid"])
    #print("B OMG Bid: " +str("%.9f" % currOMGBTCBid) +" | OMG Ask: " +str("%.9f" % currOMGBTCAsk))

  if(response["market"] == "OMG-BTC" and "bestAsk" in response):
    currOMGBTCAsk = float(response["bestAsk"])
    #print("B OMG Bid: " +str("%.9f" % currOMGBTCBid) +" | OMG Ask: " +str("%.9f" % currOMGBTCAsk))

  #ONG-BTC
  if(response["market"] == "ONG-BTC" and "bestBid" in response):
    currONGBTCBid = float(response["bestBid"])
    #print("B ONG Bid: " +str("%.9f" % currONGBTCBid) +" | ONG Ask: " +str("%.9f" % currONGBTCAsk))

  if(response["market"] == "ONG-BTC" and "bestAsk" in response):
    currONGBTCAsk = float(response["bestAsk"])
    #print("B ONG Bid: " +str("%.9f" % currONGBTCBid) +" | ONG Ask: " +str("%.9f" % currONGBTCAsk))

  #ONT-BTC
  if(response["market"] == "ONT-BTC" and "bestBid" in response):
    currONTBTCBid = float(response["bestBid"])
    #print("B ONT Bid: " +str("%.9f" % currONTBTCBid) +" | ONT Ask: " +str("%.9f" % currONTBTCAsk))

  if(response["market"] == "ONT-BTC" and "bestAsk" in response):
    currONTBTCAsk = float(response["bestAsk"])
    #print("B ONT Bid: " +str("%.9f" % currONTBTCBid) +" | ONT Ask: " +str("%.9f" % currONTBTCAsk))

  #POWR-BTC
  if(response["market"] == "POWR-BTC" and "bestBid" in response):
    currPOWRBTCBid = float(response["bestBid"])
    #print("B POWR Bid: " +str("%.10f" % currPOWRBTCBid) +" | POWR Ask: " +str("%.10f" % currPOWRBTCAsk))

  if(response["market"] == "POWR-BTC" and "bestAsk" in response):
    currPOWRBTCAsk = float(response["bestAsk"])
    #print("B POWR Bid: " +str("%.10f" % currPOWRBTCBid) +" | POWR Ask: " +str("%.10f" % currPOWRBTCAsk))

  #QTUM-BTC
  if(response["market"] == "QTUM-BTC" and "bestBid" in response):
    currQTUMBTCBid = float(response["bestBid"])
    #print("B QTUM Bid: " +str("%.8f" % currQTUMBTCBid) +" | QTUM Ask: " +str("%.8f" % currQTUMBTCAsk))

  if(response["market"] == "QTUM-BTC" and "bestAsk" in response):
    currQTUMBTCAsk = float(response["bestAsk"])
    #print("B QTUM Bid: " +str("%.8f" % currQTUMBTCBid) +" | QTUM Ask: " +str("%.8f" % currQTUMBTCAsk))

  #RDD-BTC
  if(response["market"] == "RDD-BTC" and "bestBid" in response):
    currRDDBTCBid = float(response["bestBid"])
    #print("B RDD Bid: " +str("%.12f" % currRDDBTCBid) +" | RDD Ask: " +str("%.12f" % currRDDBTCAsk))

  if(response["market"] == "RDD-BTC" and "bestAsk" in response):
    currRDDBTCAsk = float(response["bestAsk"])
    #print("B RDD Bid: " +str("%.12f" % currRDDBTCBid) +" | RDD Ask: " +str("%.12f" % currRDDBTCAsk))

  #REQ-BTC
  if(response["market"] == "REQ-BTC" and "bestBid" in response):
    currREQBTCBid = float(response["bestBid"])
    #print("B REQ Bid: " +str("%.10f" % currREQBTCBid) +" | REQ Ask: " +str("%.10f" % currREQBTCAsk))

  if(response["market"] == "REQ-BTC" and "bestAsk" in response):
    currREQBTCAsk = float(response["bestAsk"])
    #print("B REQ Bid: " +str("%.10f" % currREQBTCBid) +" | REQ Ask: " +str("%.10f" % currREQBTCAsk))

  #RVN-BTC
  if(response["market"] == "RVN-BTC" and "bestBid" in response):
    currRVNBTCBid = float(response["bestBid"])
    #print("B RVN Bid: " +str("%.10f" % currRVNBTCBid) +" | RVN Ask: " +str("%.10f" % currRVNBTCAsk))

  if(response["market"] == "RVN-BTC" and "bestAsk" in response):
    currRVNBTCAsk = float(response["bestAsk"])
    #print("B RVN Bid: " +str("%.10f" % currRVNBTCBid) +" | RVN Ask: " +str("%.10f" % currRVNBTCAsk))

  #SNT-BTC
  if(response["market"] == "SNT-BTC" and "bestBid" in response):
    currSNTBTCBid = float(response["bestBid"])
    #print("B SNT Bid: " +str("%.10f" % currSNTBTCBid) +" | SNT Ask: " +str("%.10f" % currSNTBTCAsk))

  if(response["market"] == "SNT-BTC" and "bestAsk" in response):
    currSNTBTCAsk = float(response["bestAsk"])
    #print("B SNT Bid: " +str("%.10f" % currSNTBTCBid) +" | SNT Ask: " +str("%.10f" % currSNTBTCAsk))

  #STEEM-BTC
  if(response["market"] == "STEEM-BTC" and "bestBid" in response):
    currSTEEMBTCBid = float(response["bestBid"])
    #print("B STEEM Bid: " +str("%.9f" % currSTEEMBTCBid) +" | STEEM Ask: " +str("%.9f" % currSTEEMBTCAsk))

  if(response["market"] == "STEEM-BTC" and "bestAsk" in response):
    currSTEEMBTCAsk = float(response["bestAsk"])
    #print("B STEEM Bid: " +str("%.9f" % currSTEEMBTCBid) +" | STEEM Ask: " +str("%.9f" % currSTEEMBTCAsk))

  #STORM-BTC
  if(response["market"] == "STORM-BTC" and "bestBid" in response):
    currSTORMBTCBid = float(response["bestBid"])
    #print("B STORM Bid: " +str("%.11f" % currSTORMBTCBid) +" | STORM Ask: " +str("%.11f" % currSTORMBTCAsk))

  if(response["market"] == "STORM-BTC" and "bestAsk" in response):
    currSTORMBTCAsk = float(response["bestAsk"])
    #print("B STORM Bid: " +str("%.11f" % currSTORMBTCBid) +" | STORM Ask: " +str("%.11f" % currSTORMBTCAsk))

  #STRAT-BTC
  if(response["market"] == "STRAT-BTC" and "bestBid" in response):
    currSTRATBTCBid = float(response["bestBid"])
    #print("B STRAT Bid: " +str("%.9f" % currSTRATBTCBid) +" | STRAT Ask: " +str("%.9f" % currSTRATBTCAsk))

  if(response["market"] == "STRAT-BTC" and "bestAsk" in response):
    currSTRATBTCAsk = float(response["bestAsk"])
    #print("B STRAT Bid: " +str("%.9f" % currSTRATBTCBid) +" | STRAT Ask: " +str("%.9f" % currSTRATBTCAsk))

  #TRX-BTC
  if(response["market"] == "TRX-BTC" and "bestBid" in response):
    currTRXBTCBid = float(response["bestBid"])
    #print("B TRX Bid: " +str("%.10f" % currTRXBTCBid) +" | TRX Ask: " +str("%.10f" % currTRXBTCAsk))

  if(response["market"] == "TRX-BTC" and "bestAsk" in response):
    currTRXBTCAsk = float(response["bestAsk"])
    #print("B TRX Bid: " +str("%.10f" % currTRXBTCBid) +" | TRX Ask: " +str("%.10f" % currTRXBTCAsk))

  #VET-BTC
  if(response["market"] == "VET-BTC" and "bestBid" in response):
    currVETBTCBid = float(response["bestBid"])
    #print("B VET Bid: " +str("%.11f" % currVETBTCBid) +" | VET Ask: " +str("%.11f" % currVETBTCAsk))

  if(response["market"] == "VET-BTC" and "bestAsk" in response):
    currVETBTCAsk = float(response["bestAsk"])
    #print("B VET Bid: " +str("%.11f" % currVETBTCBid) +" | VET Ask: " +str("%.11f" % currVETBTCAsk))

  #VTC-BTC
  if(response["market"] == "VTC-BTC" and "bestBid" in response):
    currVTCBTCBid = float(response["bestBid"])
    #print("B VTC Bid: " +str("%.9f" % currVTCBTCBid) +" | VTC Ask: " +str("%.9f" % currVTCBTCAsk))

  if(response["market"] == "VTC-BTC" and "bestAsk" in response):
    currVTCBTCAsk = float(response["bestAsk"])
    #print("B VTC Bid: " +str("%.9f" % currVTCBTCBid) +" | VTC Ask: " +str("%.9f" % currVTCBTCAsk))

  #VTHO-BTC
  if(response["market"] == "VTHO-BTC" and "bestBid" in response):
    currVTHOBTCBid = float(response["bestBid"])
    #print("B VTHO Bid: " +str("%.12f" % currVTHOBTCBid) +" | VTHO Ask: " +str("%.12f" % currVTHOBTCAsk))

  if(response["market"] == "VTHO-BTC" and "bestAsk" in response):
    currVTHOBTCAsk = float(response["bestAsk"])
    #print("B VTHO Bid: " +str("%.12f" % currVTHOBTCBid) +" | VTHO Ask: " +str("%.12f" % currVTHOBTCAsk))

  #WAVES-BTC
  if(response["market"] == "WAVES-BTC" and "bestBid" in response):
    currWAVESBTCBid = float(response["bestBid"])
    #print("B WAVES Bid: " +str("%.8f" % currWAVESBTCBid) +" | WAVES Ask: " +str("%.8f" % currWAVESBTCAsk))

  if(response["market"] == "WAVES-BTC" and "bestAsk" in response):
    currWAVESBTCAsk = float(response["bestAsk"])
    #print("B WAVES Bid: " +str("%.8f" % currWAVESBTCBid) +" | WAVES Ask: " +str("%.8f" % currWAVESBTCAsk))

  #WTC-BTC
  if(response["market"] == "WTC-BTC" and "bestBid" in response):
    currWTCBTCBid = float(response["bestBid"])
    #print("B WTC Bid: " +str("%.9f" % currWTCBTCBid) +" | WTC Ask: " +str("%.9f" % currWTCBTCAsk))

  if(response["market"] == "WTC-BTC" and "bestAsk" in response):
    currWTCBTCAsk = float(response["bestAsk"])
    #print("B WTC Bid: " +str("%.9f" % currWTCBTCBid) +" | WTC Ask: " +str("%.9f" % currWTCBTCAsk))

  #XEM-BTC
  if(response["market"] == "XEM-BTC" and "bestBid" in response):
    currXEMBTCBid = float(response["bestBid"])
    #print("B XEM Bid: " +str("%.10f" % currXEMBTCBid) +" | XEM Ask: " +str("%.10f" % currXEMBTCAsk))

  if(response["market"] == "XEM-BTC" and "bestAsk" in response):
    currXEMBTCAsk = float(response["bestAsk"])
    #print("B XEM Bid: " +str("%.10f" % currXEMBTCBid) +" | XEM Ask: " +str("%.10f" % currXEMBTCAsk))

  #XLM-BTC
  if(response["market"] == "XLM-BTC" and "bestBid" in response):
    currXLMBTCBid = float(response["bestBid"])
    #print("B XLM Bid: " +str("%.10f" % currXLMBTCBid) +" | XLM Ask: " +str("%.10f" % currXLMBTCAsk))

  if(response["market"] == "XLM-BTC" and "bestAsk" in response):
    currXLMBTCAsk = float(response["bestAsk"])
    #print("B XLM Bid: " +str("%.10f" % currXLMBTCBid) +" | XLM Ask: " +str("%.10f" % currXLMBTCAsk))

  #XRP-BTC
  if(response["market"] == "XRP-BTC" and "bestBid" in response):
    currXRPBTCBid = float(response["bestBid"])
    #print("B XRP Bid: " +str("%.9f" % currXRPBTCBid) +" | XRP Ask: " +str("%.9f" % currXRPBTCAsk))

  if(response["market"] == "XRP-BTC" and "bestAsk" in response):
    currXRPBTCAsk = float(response["bestAsk"])
    #print("B XRP Bid: " +str("%.9f" % currXRPBTCBid) +" | XRP Ask: " +str("%.9f" % currXRPBTCAsk))

  #XTZ-BTC
  if(response["market"] == "XTZ-BTC" and "bestBid" in response):
    currXTZBTCBid = float(response["bestBid"])
    #print("B XTZ Bid: " +str("%.8f" % currXTZBTCBid) +" | XTZ Ask: " +str("%.8f" % currXTZBTCAsk))

  if(response["market"] == "XTZ-BTC" and "bestAsk" in response):
    currXTZBTCAsk = float(response["bestAsk"])
    #print("B XTZ Bid: " +str("%.8f" % currXTZBTCBid) +" | XTZ Ask: " +str("%.8f" % currXTZBTCAsk))

  #XVG-BTC
  if(response["market"] == "XVG-BTC" and "bestBid" in response):
    currXVGBTCBid = float(response["bestBid"])
    #print("B XVG Bid: " +str("%.11f" % currXVGBTCBid) +" | XVG Ask: " +str("%.11f" % currXVGBTCAsk))

  if(response["market"] == "XVG-BTC" and "bestAsk" in response):
    currXVGBTCAsk = float(response["bestAsk"])
    #print("B XVG Bid: " +str("%.11f" % currXVGBTCBid) +" | XVG Ask: " +str("%.11f" % currXVGBTCAsk))

  #ZIL-BTC
  if(response["market"] == "ZIL-BTC" and "bestBid" in response):
    currZILBTCBid = float(response["bestBid"])
    #print("B ZIL Bid: " +str("%.11f" % currZILBTCBid) +" | ZIL Ask: " +str("%.11f" % currZILBTCAsk))

  if(response["market"] == "ZIL-BTC" and "bestAsk" in response):
    currZILBTCAsk = float(response["bestAsk"])
    #print("B ZIL Bid: " +str("%.11f" % currZILBTCBid) +" | ZIL Ask: " +str("%.11f" % currZILBTCAsk))

  #ZRX-BTC
  if(response["market"] == "ZRX-BTC" and "bestBid" in response):
    currZRXBTCBid = float(response["bestBid"])
    #print("B ZRX Bid: " +str("%.9f" % currZRXBTCBid) +" | ZRX Ask: " +str("%.9f" % currZRXBTCAsk))

  if(response["market"] == "ZRX-BTC" and "bestAsk" in response):
    currZRXBTCAsk = float(response["bestAsk"])
    #print("B ZRX Bid: " +str("%.9f" % currZRXBTCBid) +" | ZRX Ask: " +str("%.9f" % currZRXBTCAsk))


  #Calculate arbitrage profits (triangular)
  min_profit = 0.10 #minimum profit required to show print NOTE: Fees are not included in min_profit -> so real profit = min_profit - taker_fee*3

  #ETH
  arb1_profitA = safe_division((currETHEURBid - (currETHBTCAsk*currBTCEURAsk))*100.0,currETHBTCAsk*currBTCEURAsk)
  if arb1_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ETH " +str(currETHBTCAsk) +" -> Sell ETH for " +str(currETHEURBid) +"€ = " +str("%.3f" % arb1_profitA))

  arb1_profitB = safe_division((currETHBTCBid*currBTCEURBid - currETHEURAsk)*100.0,currETHEURAsk)
  if arb1_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ETH " +str(currETHEURAsk) +"€ -> Sell ETH " +str(currETHBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb1_profitB))

  #XRP
  arb2_profitA = safe_division((currXRPEURBid - (currXRPBTCAsk*currBTCEURAsk))*100.0,currXRPBTCAsk*currBTCEURAsk)
  if arb2_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy XRP " +str(currXRPBTCAsk) +" -> Sell XRP for " +str(currXRPEURBid) +"€ = " +str("%.3f" % arb2_profitA))

  arb2_profitB = safe_division((currXRPBTCBid*currBTCEURBid - currXRPEURAsk)*100.0,currXRPEURAsk)
  if arb2_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy XRP " +str(currXRPEURAsk) +"€ -> Sell XRP " +str(currXRPBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb2_profitB))

  #ADA
  arb3_profitA = safe_division((currADAEURBid - (currADABTCAsk*currBTCEURAsk))*100.0,currADABTCAsk*currBTCEURAsk)
  if arb3_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ADA " +str(currADABTCAsk) +" -> Sell ADA for " +str(currADAEURBid) +"€ = " +str("%.3f" % arb3_profitA))

  arb3_profitB = safe_division((currADABTCBid*currBTCEURBid - currADAEURAsk)*100.0,currADAEURAsk)
  if arb3_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ADA " +str(currADAEURAsk) +"€ -> Sell ADA " +str(currADABTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb3_profitB))

  #AE
  arb4_profitA = safe_division((currAEEURBid - (currAEBTCAsk*currBTCEURAsk))*100.0,currAEBTCAsk*currBTCEURAsk)
  if arb4_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy AE " +str(currAEBTCAsk) +" -> Sell AE for " +str(currAEEURBid) +"€ = " +str("%.3f" % arb4_profitA))

  arb4_profitB = safe_division((currAEBTCBid*currBTCEURBid - currAEEURAsk)*100.0,currAEEURAsk)
  if arb4_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy AE " +str(currAEEURAsk) +"€ -> Sell AE " +str(currAEBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb4_profitB))

  #AION
  arb5_profitA = safe_division((currAIONEURBid - (currAIONBTCAsk*currBTCEURAsk))*100.0,currAIONBTCAsk*currBTCEURAsk)
  if arb5_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy AION " +str(currAIONBTCAsk) +" -> Sell AION for " +str(currAIONEURBid) +"€ = " +str("%.3f" % arb5_profitA))

  arb5_profitB = safe_division((currAIONBTCBid*currBTCEURBid - currAIONEURAsk)*100.0,currAIONEURAsk)
  if arb5_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy AION " +str(currAIONEURAsk) +"€ -> Sell AION " +str(currAIONBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb5_profitB))

  #ANT
  arb6_profitA = safe_division((currANTEURBid - (currANTBTCAsk*currBTCEURAsk))*100.0,currANTBTCAsk*currBTCEURAsk)
  if arb6_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ANT " +str(currANTBTCAsk) +" -> Sell ANT for " +str(currANTEURBid) +"€ = " +str("%.3f" % arb6_profitA))

  arb6_profitB = safe_division((currANTBTCBid*currBTCEURBid - currANTEURAsk)*100.0,currANTEURAsk)
  if arb6_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ANT " +str(currANTEURAsk) +"€ -> Sell ANT " +str(currANTBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb6_profitB))

  #ARK
  arb7_profitA = safe_division((currARKEURBid - (currARKBTCAsk*currBTCEURAsk))*100.0,currARKBTCAsk*currBTCEURAsk)
  if arb7_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ARK " +str(currARKBTCAsk) +" -> Sell ARK for " +str(currARKEURBid) +"€ = " +str("%.3f" % arb7_profitA))

  arb7_profitB = safe_division((currARKBTCBid*currBTCEURBid - currARKEURAsk)*100.0,currARKEURAsk)
  if arb7_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ARK " +str(currARKEURAsk) +"€ -> Sell ARK " +str(currARKBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb7_profitB))

  #BAT
  arb8_profitA = safe_division((currBATEURBid - (currBATBTCAsk*currBTCEURAsk))*100.0,currBATBTCAsk*currBTCEURAsk)
  if arb8_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy BAT " +str(currBATBTCAsk) +" -> Sell BAT for " +str(currBATEURBid) +"€ = " +str("%.3f" % arb8_profitA))

  arb8_profitB = safe_division((currBATBTCBid*currBTCEURBid - currBATEURAsk)*100.0,currBATEURAsk)
  if arb8_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BAT " +str(currBATEURAsk) +"€ -> Sell BAT " +str(currBATBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb8_profitB))

  #BCH
  arb9_profitA = safe_division((currBCHEURBid - (currBCHBTCAsk*currBTCEURAsk))*100.0,currBCHBTCAsk*currBTCEURAsk)
  if arb9_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy BCH " +str(currBCHBTCAsk) +" -> Sell BCH for " +str(currBCHEURBid) +"€ = " +str("%.3f" % arb9_profitA))

  arb9_profitB = safe_division((currBCHBTCBid*currBTCEURBid - currBCHEURAsk)*100.0,currBCHEURAsk)
  if arb9_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BCH " +str(currBCHEURAsk) +"€ -> Sell BCH " +str(currBCHBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb9_profitB))

  #BSV
  arb10_profitA = safe_division((currBSVEURBid - (currBSVBTCAsk*currBTCEURAsk))*100.0,currBSVBTCAsk*currBTCEURAsk)
  if arb10_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy BSV " +str(currBSVBTCAsk) +" -> Sell BSV for " +str(currBSVEURBid) +"€ = " +str("%.3f" % arb10_profitA))

  arb10_profitB = safe_division((currBSVBTCBid*currBTCEURBid - currBSVEURAsk)*100.0,currBSVEURAsk)
  if arb10_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BSV " +str(currBSVEURAsk) +"€ -> Sell BSV " +str(currBSVBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb10_profitB))

  #CMT
  arb11_profitA = safe_division((currCMTEURBid - (currCMTBTCAsk*currBTCEURAsk))*100.0,currCMTBTCAsk*currBTCEURAsk)
  if arb11_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy CMT " +str(currCMTBTCAsk) +" -> Sell CMT for " +str(currCMTEURBid) +"€ = " +str("%.3f" % arb11_profitA))

  arb11_profitB = safe_division((currCMTBTCBid*currBTCEURBid - currCMTEURAsk)*100.0,currCMTEURAsk)
  if arb11_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy CMT " +str(currCMTEURAsk) +"€ -> Sell CMT " +str(currCMTBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb11_profitB))

  #DCR
  arb12_profitA = safe_division((currDCREURBid - (currDCRBTCAsk*currBTCEURAsk))*100.0,currDCRBTCAsk*currBTCEURAsk)
  if arb12_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy DCR " +str(currDCRBTCAsk) +" -> Sell DCR for " +str(currDCREURBid) +"€ = " +str("%.3f" % arb12_profitA))

  arb12_profitB = safe_division((currDCRBTCBid*currBTCEURBid - currDCREURAsk)*100.0,currDCREURAsk)
  if arb12_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy DCR " +str(currDCREURAsk) +"€ -> Sell DCR " +str(currDCRBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb12_profitB))

  #DGB
  arb13_profitA = safe_division((currDGBEURBid - (currDGBBTCAsk*currBTCEURAsk))*100.0,currDGBBTCAsk*currBTCEURAsk)
  if arb13_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy DGB " +str(currDGBBTCAsk) +" -> Sell DGB for " +str(currDGBEURBid) +"€ = " +str("%.3f" % arb13_profitA))

  arb13_profitB = safe_division((currDGBBTCBid*currBTCEURBid - currDGBEURAsk)*100.0,currDGBEURAsk)
  if arb13_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy DGB " +str(currDGBEURAsk) +"€ -> Sell DGB " +str(currDGBBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb13_profitB))

  #ELF
  arb14_profitA = safe_division((currELFEURBid - (currELFBTCAsk*currBTCEURAsk))*100.0,currELFBTCAsk*currBTCEURAsk)
  if arb14_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ELF " +str(currELFBTCAsk) +" -> Sell ELF for " +str(currELFEURBid) +"€ = " +str("%.3f" % arb14_profitA))

  arb14_profitB = safe_division((currELFBTCBid*currBTCEURBid - currELFEURAsk)*100.0,currELFEURAsk)
  if arb14_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ELF " +str(currELFEURAsk) +"€ -> Sell ELF " +str(currELFBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb14_profitB))

  #ENJ
  arb15_profitA = safe_division((currENJEURBid - (currENJBTCAsk*currBTCEURAsk))*100.0,currENJBTCAsk*currBTCEURAsk)
  if arb15_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ENJ " +str(currENJBTCAsk) +" -> Sell ENJ for " +str(currENJEURBid) +"€ = " +str("%.3f" % arb15_profitA))

  arb15_profitB = safe_division((currENJBTCBid*currBTCEURBid - currENJEURAsk)*100.0,currENJEURAsk)
  if arb15_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ENJ " +str(currENJEURAsk) +"€ -> Sell ENJ " +str(currENJBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb15_profitB))

  #EOS
  arb16_profitA = safe_division((currEOSEURBid - (currEOSBTCAsk*currBTCEURAsk))*100.0,currEOSBTCAsk*currBTCEURAsk)
  if arb16_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy EOS " +str(currEOSBTCAsk) +" -> Sell EOS for " +str(currEOSEURBid) +"€ = " +str("%.3f" % arb16_profitA))

  arb16_profitB = safe_division((currEOSBTCBid*currBTCEURBid - currEOSEURAsk)*100.0,currEOSEURAsk)
  if arb16_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy EOS " +str(currEOSEURAsk) +"€ -> Sell EOS " +str(currEOSBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb16_profitB))

  #ETC
  arb17_profitA = safe_division((currETCEURBid - (currETCBTCAsk*currBTCEURAsk))*100.0,currETCBTCAsk*currBTCEURAsk)
  if arb17_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ETC " +str(currETCBTCAsk) +" -> Sell ETC for " +str(currETCEURBid) +"€ = " +str("%.3f" % arb17_profitA))

  arb17_profitB = safe_division((currETCBTCBid*currBTCEURBid - currETCEURAsk)*100.0,currETCEURAsk)
  if arb17_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ETC " +str(currETCEURAsk) +"€ -> Sell ETC " +str(currETCBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb17_profitB))

  #GAS
  arb18_profitA = safe_division((currGASEURBid - (currGASBTCAsk*currBTCEURAsk))*100.0,currGASBTCAsk*currBTCEURAsk)
  if arb18_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy GAS " +str(currGASBTCAsk) +" -> Sell GAS for " +str(currGASEURBid) +"€ = " +str("%.3f" % arb18_profitA))

  arb18_profitB = safe_division((currGASBTCBid*currBTCEURBid - currGASEURAsk)*100.0,currGASEURAsk)
  if arb18_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy GAS " +str(currGASEURAsk) +"€ -> Sell GAS " +str(currGASBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb18_profitB))

  #GNT
  arb19_profitA = safe_division((currGNTEURBid - (currGNTBTCAsk*currBTCEURAsk))*100.0,currGNTBTCAsk*currBTCEURAsk)
  if arb19_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy GNT " +str(currGNTBTCAsk) +" -> Sell GNT for " +str(currGNTEURBid) +"€ = " +str("%.3f" % arb19_profitA))

  arb19_profitB = safe_division((currGNTBTCBid*currBTCEURBid - currGNTEURAsk)*100.0,currGNTEURAsk)
  if arb19_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy GNT " +str(currGNTEURAsk) +"€ -> Sell GNT " +str(currGNTBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb19_profitB))

  #HOT
  arb20_profitA = safe_division((currHOTEURBid - (currHOTBTCAsk*currBTCEURAsk))*100.0,currHOTBTCAsk*currBTCEURAsk)
  if arb20_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy HOT " +str(currHOTBTCAsk) +" -> Sell HOT for " +str(currHOTEURBid) +"€ = " +str("%.3f" % arb20_profitA))

  arb20_profitB = safe_division((currHOTBTCBid*currBTCEURBid - currHOTEURAsk)*100.0,currHOTEURAsk)
  if arb20_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy HOT " +str(currHOTEURAsk) +"€ -> Sell HOT " +str(currHOTBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb20_profitB))

  #ICX
  arb21_profitA = safe_division((currICXEURBid - (currICXBTCAsk*currBTCEURAsk))*100.0,currICXBTCAsk*currBTCEURAsk)
  if arb21_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ICX " +str(currICXBTCAsk) +" -> Sell ICX for " +str(currICXEURBid) +"€ = " +str("%.3f" % arb21_profitA))

  arb21_profitB = safe_division((currICXBTCBid*currBTCEURBid - currICXEURAsk)*100.0,currICXEURAsk)
  if arb21_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ICX " +str(currICXEURAsk) +"€ -> Sell ICX " +str(currICXBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb21_profitB))

  #IOST
  arb22_profitA = safe_division((currIOSTEURBid - (currIOSTBTCAsk*currBTCEURAsk))*100.0,currIOSTBTCAsk*currBTCEURAsk)
  if arb22_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy IOST " +str(currIOSTBTCAsk) +" -> Sell IOST for " +str(currIOSTEURBid) +"€ = " +str("%.3f" % arb22_profitA))

  arb22_profitB = safe_division((currIOSTBTCBid*currBTCEURBid - currIOSTEURAsk)*100.0,currIOSTEURAsk)
  if arb22_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy IOST " +str(currIOSTEURAsk) +"€ -> Sell IOST " +str(currIOSTBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb22_profitB))

  #KMD
  arb23_profitA = safe_division((currKMDEURBid - (currKMDBTCAsk*currBTCEURAsk))*100.0,currKMDBTCAsk*currBTCEURAsk)
  if arb23_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy KMD " +str(currKMDBTCAsk) +" -> Sell KMD for " +str(currKMDEURBid) +"€ = " +str("%.3f" % arb23_profitA))

  arb23_profitB = safe_division((currKMDBTCBid*currBTCEURBid - currKMDEURAsk)*100.0,currKMDEURAsk)
  if arb23_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy KMD " +str(currKMDEURAsk) +"€ -> Sell KMD " +str(currKMDBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb23_profitB))

  #LINK
  arb24_profitA = safe_division((currLINKEURBid - (currLINKBTCAsk*currBTCEURAsk))*100.0,currLINKBTCAsk*currBTCEURAsk)
  if arb24_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy LINK " +str(currLINKBTCAsk) +" -> Sell LINK for " +str(currLINKEURBid) +"€ = " +str("%.3f" % arb24_profitA))

  arb24_profitB = safe_division((currLINKBTCBid*currBTCEURBid - currLINKEURAsk)*100.0,currLINKEURAsk)
  if arb24_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy LINK " +str(currLINKEURAsk) +"€ -> Sell LINK " +str(currLINKBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb24_profitB))

  #LRC
  arb25_profitA = safe_division((currLRCEURBid - (currLRCBTCAsk*currBTCEURAsk))*100.0,currLRCBTCAsk*currBTCEURAsk)
  if arb25_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy LRC " +str(currLRCBTCAsk) +" -> Sell LRC for " +str(currLRCEURBid) +"€ = " +str("%.3f" % arb25_profitA))

  arb25_profitB = safe_division((currLRCBTCBid*currBTCEURBid - currLRCEURAsk)*100.0,currLRCEURAsk)
  if arb25_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy LRC " +str(currLRCEURAsk) +"€ -> Sell LRC " +str(currLRCBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb25_profitB))

  #LSK
  arb26_profitA = safe_division((currLSKEURBid - (currLSKBTCAsk*currBTCEURAsk))*100.0,currLSKBTCAsk*currBTCEURAsk)
  if arb26_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy LSK " +str(currLSKBTCAsk) +" -> Sell LSK for " +str(currLSKEURBid) +"€ = " +str("%.3f" % arb26_profitA))

  arb26_profitB = safe_division((currLSKBTCBid*currBTCEURBid - currLSKEURAsk)*100.0,currLSKEURAsk)
  if arb26_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy LSK " +str(currLSKEURAsk) +"€ -> Sell LSK " +str(currLSKBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb26_profitB))

  #LTC
  arb27_profitA = safe_division((currLTCEURBid - (currLTCBTCAsk*currBTCEURAsk))*100.0,currLTCBTCAsk*currBTCEURAsk)
  if arb27_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy LTC " +str(currLTCBTCAsk) +" -> Sell LTC for " +str(currLTCEURBid) +"€ = " +str("%.3f" % arb27_profitA))

  arb27_profitB = safe_division((currLTCBTCBid*currBTCEURBid - currLTCEURAsk)*100.0,currLTCEURAsk)
  if arb27_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy LTC " +str(currLTCEURAsk) +"€ -> Sell LTC " +str(currLTCBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb27_profitB))

  #MIOTA
  arb28_profitA = safe_division((currMIOTAEURBid - (currMIOTABTCAsk*currBTCEURAsk))*100.0,currMIOTABTCAsk*currBTCEURAsk)
  if arb28_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy MIOTA " +str(currMIOTABTCAsk) +" -> Sell MIOTA for " +str(currMIOTAEURBid) +"€ = " +str("%.3f" % arb28_profitA))

  arb28_profitB = safe_division((currMIOTABTCBid*currBTCEURBid - currMIOTAEURAsk)*100.0,currMIOTAEURAsk)
  if arb28_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy MIOTA " +str(currMIOTAEURAsk) +"€ -> Sell MIOTA " +str(currMIOTABTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb28_profitB))

  #NANO
  arb29_profitA = safe_division((currNANOEURBid - (currNANOBTCAsk*currBTCEURAsk))*100.0,currNANOBTCAsk*currBTCEURAsk)
  if arb29_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy NANO " +str(currNANOBTCAsk) +" -> Sell NANO for " +str(currNANOEURBid) +"€ = " +str("%.3f" % arb29_profitA))

  arb29_profitB = safe_division((currNANOBTCBid*currBTCEURBid - currNANOEURAsk)*100.0,currNANOEURAsk)
  if arb29_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy NANO " +str(currNANOEURAsk) +"€ -> Sell NANO " +str(currNANOBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb29_profitB))

  #NAS
  arb30_profitA = safe_division((currNASEURBid - (currNASBTCAsk*currBTCEURAsk))*100.0,currNASBTCAsk*currBTCEURAsk)
  if arb30_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy NAS " +str(currNASBTCAsk) +" -> Sell NAS for " +str(currNASEURBid) +"€ = " +str("%.3f" % arb30_profitA))

  arb30_profitB = safe_division((currNASBTCBid*currBTCEURBid - currNASEURAsk)*100.0,currNASEURAsk)
  if arb30_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy NAS " +str(currNASEURAsk) +"€ -> Sell NAS " +str(currNASBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb30_profitB))

  #NEO
  arb31_profitA = safe_division((currNEOEURBid - (currNEOBTCAsk*currBTCEURAsk))*100.0,currNEOBTCAsk*currBTCEURAsk)
  if arb31_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy NEO " +str(currNEOBTCAsk) +" -> Sell NEO for " +str(currNEOEURBid) +"€ = " +str("%.3f" % arb31_profitA))

  arb31_profitB = safe_division((currNEOBTCBid*currBTCEURBid - currNEOEURAsk)*100.0,currNEOEURAsk)
  if arb31_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy NEO " +str(currNEOEURAsk) +"€ -> Sell NEO " +str(currNEOBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb31_profitB))

  #NPXS
  arb32_profitA = safe_division((currNPXSEURBid - (currNPXSBTCAsk*currBTCEURAsk))*100.0,currNPXSBTCAsk*currBTCEURAsk)
  if arb32_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy NPXS " +str(currNPXSBTCAsk) +" -> Sell NPXS for " +str(currNPXSEURBid) +"€ = " +str("%.3f" % arb32_profitA))

  arb32_profitB = safe_division((currNPXSBTCBid*currBTCEURBid - currNPXSEURAsk)*100.0,currNPXSEURAsk)
  if arb32_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy NPXS " +str(currNPXSEURAsk) +"€ -> Sell NPXS " +str(currNPXSBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb32_profitB))

  #NULS
  arb33_profitA = safe_division((currNULSEURBid - (currNULSBTCAsk*currBTCEURAsk))*100.0,currNULSBTCAsk*currBTCEURAsk)
  if arb33_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy NULS " +str(currNULSBTCAsk) +" -> Sell NULS for " +str(currNULSEURBid) +"€ = " +str("%.3f" % arb33_profitA))

  arb33_profitB = safe_division((currNULSBTCBid*currBTCEURBid - currNULSEURAsk)*100.0,currNULSEURAsk)
  if arb33_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy NULS " +str(currNULSEURAsk) +"€ -> Sell NULS " +str(currNULSBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb33_profitB))

  #OMG
  arb34_profitA = safe_division((currOMGEURBid - (currOMGBTCAsk*currBTCEURAsk))*100.0,currOMGBTCAsk*currBTCEURAsk)
  if arb34_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy OMG " +str(currOMGBTCAsk) +" -> Sell OMG for " +str(currOMGEURBid) +"€ = " +str("%.3f" % arb34_profitA))

  arb34_profitB = safe_division((currOMGBTCBid*currBTCEURBid - currOMGEURAsk)*100.0,currOMGEURAsk)
  if arb34_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy OMG " +str(currOMGEURAsk) +"€ -> Sell OMG " +str(currOMGBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb34_profitB))

  #ONG
  arb35_profitA = safe_division((currONGEURBid - (currONGBTCAsk*currBTCEURAsk))*100.0,currONGBTCAsk*currBTCEURAsk)
  if arb35_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ONG " +str(currONGBTCAsk) +" -> Sell ONG for " +str(currONGEURBid) +"€ = " +str("%.3f" % arb35_profitA))

  arb35_profitB = safe_division((currONGBTCBid*currBTCEURBid - currONGEURAsk)*100.0,currONGEURAsk)
  if arb35_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ONG " +str(currONGEURAsk) +"€ -> Sell ONG " +str(currONGBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb35_profitB))

  #ONT
  arb36_profitA = safe_division((currONTEURBid - (currONTBTCAsk*currBTCEURAsk))*100.0,currONTBTCAsk*currBTCEURAsk)
  if arb36_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ONT " +str(currONTBTCAsk) +" -> Sell ONT for " +str(currONTEURBid) +"€ = " +str("%.3f" % arb36_profitA))

  arb36_profitB = safe_division((currONTBTCBid*currBTCEURBid - currONTEURAsk)*100.0,currONTEURAsk)
  if arb36_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ONT " +str(currONTEURAsk) +"€ -> Sell ONT " +str(currONTBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb36_profitB))

  #POWR
  arb37_profitA = safe_division((currPOWREURBid - (currPOWRBTCAsk*currBTCEURAsk))*100.0,currPOWRBTCAsk*currBTCEURAsk)
  if arb37_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy POWR " +str(currPOWRBTCAsk) +" -> Sell POWR for " +str(currPOWREURBid) +"€ = " +str("%.3f" % arb37_profitA))

  arb37_profitB = safe_division((currPOWRBTCBid*currBTCEURBid - currPOWREURAsk)*100.0,currPOWREURAsk)
  if arb37_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy POWR " +str(currPOWREURAsk) +"€ -> Sell POWR " +str(currPOWRBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb37_profitB))

  #QTUM
  arb38_profitA = safe_division((currQTUMEURBid - (currQTUMBTCAsk*currBTCEURAsk))*100.0,currQTUMBTCAsk*currBTCEURAsk)
  if arb38_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy QTUM " +str(currQTUMBTCAsk) +" -> Sell QTUM for " +str(currQTUMEURBid) +"€ = " +str("%.3f" % arb38_profitA))

  arb38_profitB = safe_division((currQTUMBTCBid*currBTCEURBid - currQTUMEURAsk)*100.0,currQTUMEURAsk)
  if arb38_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy QTUM " +str(currQTUMEURAsk) +"€ -> Sell QTUM " +str(currQTUMBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb38_profitB))

  #RDD
  arb39_profitA = safe_division((currRDDEURBid - (currRDDBTCAsk*currBTCEURAsk))*100.0,currRDDBTCAsk*currBTCEURAsk)
  if arb39_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy RDD " +str(currRDDBTCAsk) +" -> Sell RDD for " +str(currRDDEURBid) +"€ = " +str("%.3f" % arb39_profitA))

  arb39_profitB = safe_division((currRDDBTCBid*currBTCEURBid - currRDDEURAsk)*100.0,currRDDEURAsk)
  if arb39_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy RDD " +str(currRDDEURAsk) +"€ -> Sell RDD " +str(currRDDBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb39_profitB))

  #REQ
  arb40_profitA = safe_division((currREQEURBid - (currREQBTCAsk*currBTCEURAsk))*100.0,currREQBTCAsk*currBTCEURAsk)
  if arb40_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy REQ " +str(currREQBTCAsk) +" -> Sell REQ for " +str(currREQEURBid) +"€ = " +str("%.3f" % arb40_profitA))

  arb40_profitB = safe_division((currREQBTCBid*currBTCEURBid - currREQEURAsk)*100.0,currREQEURAsk)
  if arb40_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy REQ " +str(currREQEURAsk) +"€ -> Sell REQ " +str(currREQBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb40_profitB))

  #RVN
  arb41_profitA = safe_division((currRVNEURBid - (currRVNBTCAsk*currBTCEURAsk))*100.0,currRVNBTCAsk*currBTCEURAsk)
  if arb41_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy RVN " +str(currRVNBTCAsk) +" -> Sell RVN for " +str(currRVNEURBid) +"€ = " +str("%.3f" % arb41_profitA))

  arb41_profitB = safe_division((currRVNBTCBid*currBTCEURBid - currRVNEURAsk)*100.0,currRVNEURAsk)
  if arb41_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy RVN " +str(currRVNEURAsk) +"€ -> Sell RVN " +str(currRVNBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb41_profitB))

  #SNT
  arb42_profitA = safe_division((currSNTEURBid - (currSNTBTCAsk*currBTCEURAsk))*100.0,currSNTBTCAsk*currBTCEURAsk)
  if arb42_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy SNT " +str(currSNTBTCAsk) +" -> Sell SNT for " +str(currSNTEURBid) +"€ = " +str("%.3f" % arb42_profitA))

  arb42_profitB = safe_division((currSNTBTCBid*currBTCEURBid - currSNTEURAsk)*100.0,currSNTEURAsk)
  if arb42_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy SNT " +str(currSNTEURAsk) +"€ -> Sell SNT " +str(currSNTBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb42_profitB))

  #STEEM
  arb43_profitA = safe_division((currSTEEMEURBid - (currSTEEMBTCAsk*currBTCEURAsk))*100.0,currSTEEMBTCAsk*currBTCEURAsk)
  if arb43_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy STEEM " +str(currSTEEMBTCAsk) +" -> Sell STEEM for " +str(currSTEEMEURBid) +"€ = " +str("%.3f" % arb43_profitA))

  arb43_profitB = safe_division((currSTEEMBTCBid*currBTCEURBid - currSTEEMEURAsk)*100.0,currSTEEMEURAsk)
  if arb43_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy STEEM " +str(currSTEEMEURAsk) +"€ -> Sell STEEM " +str(currSTEEMBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb43_profitB))

  #STORM
  arb44_profitA = safe_division((currSTORMEURBid - (currSTORMBTCAsk*currBTCEURAsk))*100.0,currSTORMBTCAsk*currBTCEURAsk)
  if arb44_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy STORM " +str(currSTORMBTCAsk) +" -> Sell STORM for " +str(currSTORMEURBid) +"€ = " +str("%.3f" % arb44_profitA))

  arb44_profitB = safe_division((currSTORMBTCBid*currBTCEURBid - currSTORMEURAsk)*100.0,currSTORMEURAsk)
  if arb44_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy STORM " +str(currSTORMEURAsk) +"€ -> Sell STORM " +str(currSTORMBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb44_profitB))

  #STRAT
  arb45_profitA = safe_division((currSTRATEURBid - (currSTRATBTCAsk*currBTCEURAsk))*100.0,currSTRATBTCAsk*currBTCEURAsk)
  if arb45_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy STRAT " +str(currSTRATBTCAsk) +" -> Sell STRAT for " +str(currSTRATEURBid) +"€ = " +str("%.3f" % arb45_profitA))

  arb45_profitB = safe_division((currSTRATBTCBid*currBTCEURBid - currSTRATEURAsk)*100.0,currSTRATEURAsk)
  if arb45_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy STRAT " +str(currSTRATEURAsk) +"€ -> Sell STRAT " +str(currSTRATBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb45_profitB))

  #TRX
  arb46_profitA = safe_division((currTRXEURBid - (currTRXBTCAsk*currBTCEURAsk))*100.0,currTRXBTCAsk*currBTCEURAsk)
  if arb46_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy TRX " +str(currTRXBTCAsk) +" -> Sell TRX for " +str(currTRXEURBid) +"€ = " +str("%.3f" % arb46_profitA))

  arb46_profitB = safe_division((currTRXBTCBid*currBTCEURBid - currTRXEURAsk)*100.0,currTRXEURAsk)
  if arb46_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy TRX " +str(currTRXEURAsk) +"€ -> Sell TRX " +str(currTRXBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb46_profitB))

  #VET
  arb47_profitA = safe_division((currVETEURBid - (currVETBTCAsk*currBTCEURAsk))*100.0,currVETBTCAsk*currBTCEURAsk)
  if arb47_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy VET " +str(currVETBTCAsk) +" -> Sell VET for " +str(currVETEURBid) +"€ = " +str("%.3f" % arb47_profitA))

  arb47_profitB = safe_division((currVETBTCBid*currBTCEURBid - currVETEURAsk)*100.0,currVETEURAsk)
  if arb47_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy VET " +str(currVETEURAsk) +"€ -> Sell VET " +str(currVETBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb47_profitB))

  #VTC
  arb48_profitA = safe_division((currVTCEURBid - (currVTCBTCAsk*currBTCEURAsk))*100.0,currVTCBTCAsk*currBTCEURAsk)
  if arb48_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy VTC " +str(currVTCBTCAsk) +" -> Sell VTC for " +str(currVTCEURBid) +"€ = " +str("%.3f" % arb48_profitA))

  arb48_profitB = safe_division((currVTCBTCBid*currBTCEURBid - currVTCEURAsk)*100.0,currVTCEURAsk)
  if arb48_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy VTC " +str(currVTCEURAsk) +"€ -> Sell VTC " +str(currVTCBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb48_profitB))

  #VTHO
  arb49_profitA = safe_division((currVTHOEURBid - (currVTHOBTCAsk*currBTCEURAsk))*100.0,currVTHOBTCAsk*currBTCEURAsk)
  if arb49_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy VTHO " +str(currVTHOBTCAsk) +" -> Sell VTHO for " +str(currVTHOEURBid) +"€ = " +str("%.3f" % arb49_profitA))

  arb49_profitB = safe_division((currVTHOBTCBid*currBTCEURBid - currVTHOEURAsk)*100.0,currVTHOEURAsk)
  if arb49_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy VTHO " +str(currVTHOEURAsk) +"€ -> Sell VTHO " +str(currVTHOBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb49_profitB))

  #WAVES
  arb50_profitA = safe_division((currWAVESEURBid - (currWAVESBTCAsk*currBTCEURAsk))*100.0,currWAVESBTCAsk*currBTCEURAsk)
  if arb50_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy WAVES " +str(currWAVESBTCAsk) +" -> Sell WAVES for " +str(currWAVESEURBid) +"€ = " +str("%.3f" % arb50_profitA))

  arb50_profitB = safe_division((currWAVESBTCBid*currBTCEURBid - currWAVESEURAsk)*100.0,currWAVESEURAsk)
  if arb50_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy WAVES " +str(currWAVESEURAsk) +"€ -> Sell WAVES " +str(currWAVESBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb50_profitB))

  #WTC
  arb51_profitA = safe_division((currWTCEURBid - (currWTCBTCAsk*currBTCEURAsk))*100.0,currWTCBTCAsk*currBTCEURAsk)
  if arb51_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy WTC " +str(currWTCBTCAsk) +" -> Sell WTC for " +str(currWTCEURBid) +"€ = " +str("%.3f" % arb51_profitA))

  arb51_profitB = safe_division((currWTCBTCBid*currBTCEURBid - currWTCEURAsk)*100.0,currWTCEURAsk)
  if arb51_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy WTC " +str(currWTCEURAsk) +"€ -> Sell WTC " +str(currWTCBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb51_profitB))

  #XEM
  arb52_profitA = safe_division((currXEMEURBid - (currXEMBTCAsk*currBTCEURAsk))*100.0,currXEMBTCAsk*currBTCEURAsk)
  if arb52_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy XEM " +str(currXEMBTCAsk) +" -> Sell XEM for " +str(currXEMEURBid) +"€ = " +str("%.3f" % arb52_profitA))

  arb52_profitB = safe_division((currXEMBTCBid*currBTCEURBid - currXEMEURAsk)*100.0,currXEMEURAsk)
  if arb52_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy XEM " +str(currXEMEURAsk) +"€ -> Sell XEM " +str(currXEMBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb52_profitB))

  #XLM
  arb53_profitA = safe_division((currXLMEURBid - (currXLMBTCAsk*currBTCEURAsk))*100.0,currXLMBTCAsk*currBTCEURAsk)
  if arb53_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy XLM " +str(currXLMBTCAsk) +" -> Sell XLM for " +str(currXLMEURBid) +"€ = " +str("%.3f" % arb53_profitA))

  arb53_profitB = safe_division((currXLMBTCBid*currBTCEURBid - currXLMEURAsk)*100.0,currXLMEURAsk)
  if arb53_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy XLM " +str(currXLMEURAsk) +"€ -> Sell XLM " +str(currXLMBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb53_profitB))

  #XTZ
  arb54_profitA = safe_division((currXTZEURBid - (currXTZBTCAsk*currBTCEURAsk))*100.0,currXTZBTCAsk*currBTCEURAsk)
  if arb54_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy XTZ " +str(currXTZBTCAsk) +" -> Sell XTZ for " +str(currXTZEURBid) +"€ = " +str("%.3f" % arb54_profitA))

  arb54_profitB = safe_division((currXTZBTCBid*currBTCEURBid - currXTZEURAsk)*100.0,currXTZEURAsk)
  if arb54_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy XTZ " +str(currXTZEURAsk) +"€ -> Sell XTZ " +str(currXTZBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb54_profitB))

  #XVG
  arb55_profitA = safe_division((currXVGEURBid - (currXVGBTCAsk*currBTCEURAsk))*100.0,currXVGBTCAsk*currBTCEURAsk)
  if arb55_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy XVG " +str(currXVGBTCAsk) +" -> Sell XVG for " +str(currXVGEURBid) +"€ = " +str("%.3f" % arb55_profitA))

  arb55_profitB = safe_division((currXVGBTCBid*currBTCEURBid - currXVGEURAsk)*100.0,currXVGEURAsk)
  if arb55_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy XVG " +str(currXVGEURAsk) +"€ -> Sell XVG " +str(currXVGBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb55_profitB))

  #ZIL
  arb56_profitA = safe_division((currZILEURBid - (currZILBTCAsk*currBTCEURAsk))*100.0,currZILBTCAsk*currBTCEURAsk)
  if arb56_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ZIL " +str(currZILBTCAsk) +" -> Sell ZIL for " +str(currZILEURBid) +"€ = " +str("%.3f" % arb56_profitA))

  arb56_profitB = safe_division((currZILBTCBid*currBTCEURBid - currZILEURAsk)*100.0,currZILEURAsk)
  if arb56_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ZIL " +str(currZILEURAsk) +"€ -> Sell ZIL " +str(currZILBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb56_profitB))

  #ZRX
  arb57_profitA = safe_division((currZRXEURBid - (currZRXBTCAsk*currBTCEURAsk))*100.0,currZRXBTCAsk*currBTCEURAsk)
  if arb57_profitA >= min_profit:
    print(strftime("[%H:%M] ") +"Buy BTC " +str(currBTCEURAsk) +"€ -> Buy ZRX " +str(currZRXBTCAsk) +" -> Sell ZRX for " +str(currZRXEURBid) +"€ = " +str("%.3f" % arb57_profitA))

  arb57_profitB = safe_division((currZRXBTCBid*currBTCEURBid - currZRXEURAsk)*100.0,currZRXEURAsk)
  if arb57_profitB >= min_profit:
    print(strftime("[%H:%M] ") +"Buy ZRX " +str(currZRXEURAsk) +"€ -> Sell ZRX " +str(currZRXBTCBid) +" -> Sell BTC for " +str(currBTCEURBid) +"€ = " +str("%.3f" % arb57_profitB))





def errorCallback(error):
  print("Error callback:", json.dumps(error, indent=2))

def testWebsockets(bitvavo):
  websocket = bitvavo.newWebsocket()
  websocket.setErrorCallback(errorCallback)

  #Set Subscriptions
  websocket.subscriptionTicker('BTC-EUR', callback)
  websocket.subscriptionTicker('ETH-EUR', callback)
  websocket.subscriptionTicker('XRP-EUR', callback)
  websocket.subscriptionTicker('ADA-EUR', callback)
  websocket.subscriptionTicker('AE-EUR', callback)
  websocket.subscriptionTicker('AION-EUR', callback)
  websocket.subscriptionTicker('ANT-EUR', callback)
  websocket.subscriptionTicker('ARK-EUR', callback)
  websocket.subscriptionTicker('BAT-EUR', callback)
  websocket.subscriptionTicker('BCH-EUR', callback)
  websocket.subscriptionTicker('BSV-EUR', callback)
  websocket.subscriptionTicker('CMT-EUR', callback)
  websocket.subscriptionTicker('DCR-EUR', callback)
  websocket.subscriptionTicker('DGB-EUR', callback)
  websocket.subscriptionTicker('ELF-EUR', callback)
  websocket.subscriptionTicker('ENJ-EUR', callback)
  websocket.subscriptionTicker('EOS-EUR', callback)
  websocket.subscriptionTicker('ETC-EUR', callback)
  websocket.subscriptionTicker('GAS-EUR', callback)
  websocket.subscriptionTicker('GNT-EUR', callback)
  websocket.subscriptionTicker('HOT-EUR', callback)
  websocket.subscriptionTicker('ICX-EUR', callback)
  websocket.subscriptionTicker('IOST-EUR', callback)
  websocket.subscriptionTicker('KMD-EUR', callback)
  websocket.subscriptionTicker('LINK-EUR', callback)
  websocket.subscriptionTicker('LRC-EUR', callback)
  websocket.subscriptionTicker('LSK-EUR', callback)
  websocket.subscriptionTicker('LTC-EUR', callback)
  websocket.subscriptionTicker('MIOTA-EUR', callback)
  websocket.subscriptionTicker('NANO-EUR', callback)
  websocket.subscriptionTicker('NAS-EUR', callback)
  websocket.subscriptionTicker('NEO-EUR', callback)
  websocket.subscriptionTicker('NPXS-EUR', callback)
  websocket.subscriptionTicker('NULS-EUR', callback)
  websocket.subscriptionTicker('OMG-EUR', callback)
  websocket.subscriptionTicker('ONG-EUR', callback)
  websocket.subscriptionTicker('ONT-EUR', callback)
  websocket.subscriptionTicker('POWR-EUR', callback)
  websocket.subscriptionTicker('QTUM-EUR', callback)
  websocket.subscriptionTicker('RDD-EUR', callback)
  websocket.subscriptionTicker('REQ-EUR', callback)
  websocket.subscriptionTicker('RVN-EUR', callback)
  websocket.subscriptionTicker('SNT-EUR', callback)
  websocket.subscriptionTicker('STEEM-EUR', callback)
  websocket.subscriptionTicker('STORM-EUR', callback)
  websocket.subscriptionTicker('STRAT-EUR', callback)
  websocket.subscriptionTicker('TRX-EUR', callback)
  websocket.subscriptionTicker('VET-EUR', callback)
  websocket.subscriptionTicker('VTC-EUR', callback)
  websocket.subscriptionTicker('VTHO-EUR', callback)
  websocket.subscriptionTicker('WAVES-EUR', callback)
  websocket.subscriptionTicker('WTC-EUR', callback)
  websocket.subscriptionTicker('XEM-EUR', callback)
  websocket.subscriptionTicker('XLM-EUR', callback)
  websocket.subscriptionTicker('XTZ-EUR', callback)
  websocket.subscriptionTicker('XVG-EUR', callback)
  websocket.subscriptionTicker('ZIL-EUR', callback)
  websocket.subscriptionTicker('ZRX-EUR', callback)

  websocket.subscriptionTicker('ETH-BTC', callback)
  websocket.subscriptionTicker('ADA-BTC', callback)
  websocket.subscriptionTicker('AE-BTC', callback)
  websocket.subscriptionTicker('AION-BTC', callback)
  websocket.subscriptionTicker('ANT-BTC', callback)
  websocket.subscriptionTicker('ARK-BTC', callback)
  websocket.subscriptionTicker('BAT-BTC', callback)
  websocket.subscriptionTicker('BCH-BTC', callback)
  websocket.subscriptionTicker('BSV-BTC', callback)
  websocket.subscriptionTicker('CMT-BTC', callback)
  websocket.subscriptionTicker('DCR-BTC', callback)
  websocket.subscriptionTicker('DGB-BTC', callback)
  websocket.subscriptionTicker('ELF-BTC', callback)
  websocket.subscriptionTicker('ENJ-BTC', callback)
  websocket.subscriptionTicker('EOS-BTC', callback)
  websocket.subscriptionTicker('ETC-BTC', callback)
  websocket.subscriptionTicker('GAS-BTC', callback)
  websocket.subscriptionTicker('GNT-BTC', callback)
  websocket.subscriptionTicker('HOT-BTC', callback)
  websocket.subscriptionTicker('ICX-BTC', callback)
  websocket.subscriptionTicker('IOST-BTC', callback)
  websocket.subscriptionTicker('KMD-BTC', callback)
  websocket.subscriptionTicker('LINK-BTC', callback)
  websocket.subscriptionTicker('LRC-BTC', callback)
  websocket.subscriptionTicker('LSK-BTC', callback)
  websocket.subscriptionTicker('LTC-BTC', callback)
  websocket.subscriptionTicker('MIOTA-BTC', callback)
  websocket.subscriptionTicker('NANO-BTC', callback)
  websocket.subscriptionTicker('NAS-BTC', callback)
  websocket.subscriptionTicker('NEO-BTC', callback)
  websocket.subscriptionTicker('NPXS-BTC', callback)
  websocket.subscriptionTicker('NULS-BTC', callback)
  websocket.subscriptionTicker('OMG-BTC', callback)
  websocket.subscriptionTicker('ONG-BTC', callback)
  websocket.subscriptionTicker('ONT-BTC', callback)
  websocket.subscriptionTicker('POWR-BTC', callback)
  websocket.subscriptionTicker('QTUM-BTC', callback)
  websocket.subscriptionTicker('RDD-BTC', callback)
  websocket.subscriptionTicker('REQ-BTC', callback)
  websocket.subscriptionTicker('RVN-BTC', callback)
  websocket.subscriptionTicker('SNT-BTC', callback)
  websocket.subscriptionTicker('STEEM-BTC', callback)
  websocket.subscriptionTicker('STORM-BTC', callback)
  websocket.subscriptionTicker('STRAT-BTC', callback)
  websocket.subscriptionTicker('TRX-BTC', callback)
  websocket.subscriptionTicker('VET-BTC', callback)
  websocket.subscriptionTicker('VTC-BTC', callback)
  websocket.subscriptionTicker('VTHO-BTC', callback)
  websocket.subscriptionTicker('WAVES-BTC', callback)
  websocket.subscriptionTicker('WTC-BTC', callback)
  websocket.subscriptionTicker('XEM-BTC', callback)
  websocket.subscriptionTicker('XLM-BTC', callback)
  websocket.subscriptionTicker('XRP-BTC', callback)
  websocket.subscriptionTicker('XTZ-BTC', callback)
  websocket.subscriptionTicker('XVG-BTC', callback)
  websocket.subscriptionTicker('ZIL-BTC', callback)
  websocket.subscriptionTicker('ZRX-BTC', callback)

  limit = bitvavo.getRemainingLimit()
  try:
    while(limit > 0):
      time.sleep(0.5)
      limit = bitvavo.getRemainingLimit()

      #print(limit)
  except KeyboardInterrupt:
    websocket.closeSocket()


#Math helper
def safe_division(n, d):
    return n / d if d else 0.0
  

if __name__ == '__main__':
  main()
