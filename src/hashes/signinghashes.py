import win32com.client
import os, sys
import json
import datetime
import base64
import comtypes

import storingfiles as sf


CADES_BES = 1
CADES_DEFAULT = 0
CAPICOM_ENCODE_BASE64 = 0
CAPICOM_CURRENT_USER_STORE = 2
CAPICOM_MY_STORE = 'My'
CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED = 2
CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256 = 101


def format_serial_number(serialNumber):
  serialNumber = serialNumber.replace(' ', '')
  serialNumber = serialNumber.upper()
  return serialNumber

# Searching needed certificate
def select_certificate():
  certificateSerialNumber = sf.load_json_file("data/settings_setted.json")["Certificate Serial Number"]

  oStore = win32com.client.Dispatch("CAdESCOM.Store")
  oStore.Open(CAPICOM_CURRENT_USER_STORE, CAPICOM_MY_STORE, CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED)
  for val in oStore.Certificates:
      if val.SerialNumber == certificateSerialNumber:
          oCert = val
  oStore.Close
  return oCert

def create_signer_object():
  # Objects for signing and giving attributes
  oSigner = win32com.client.Dispatch("CAdESCOM.CPSigner") # объект, который будет подписывать
  oSigner.Certificate = select_certificate()
  
  oSigningTimeAttr = win32com.client.Dispatch("CAdESCOM.CPAttribute") # объект который добавляет атрибут к подписи
  oSigningTimeAttr.Name = 0
  oSigningTimeAttr.Value = datetime.datetime.now()
  oSigner.AuthenticatedAttributes2.Add(oSigningTimeAttr)

  return oSigner

def sign_hash(hashToSign):
  oSigner = create_signer_object()

  # Improved signature
  oSignedHash = win32com.client.Dispatch("CAdESCOM.CadesSignedData") # объект усовершенствованной подписи
  oSignedHash.ContentEncoding = 1

  oHash = win32com.client.Dispatch("CAdESCOM.HashedData")
  oHash.Algorithm = CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256
  oHash.SetHashValue(hashToSign)
  
  # Signed hash
  return oSignedHash.SignHash(oHash, oSigner, CADES_BES, CAPICOM_ENCODE_BASE64)


# Hash to sign
"""
hashToSign = '625f2a9064c66e0322894f545a1ccd9528fb95bc90adcfa8d889145983860416'
sSignedHash = sign_hash(hashToSign)
"""

# Authentication code
"""
url = "https://api.mdlp.crpt.ru/api/v1/auth"

client_id = ''
client_secret = ''
user_id = ''

params = {
    'client_id':client_id,
    'client_secret':client_secret,
    'user_id':user_id,
    'auth_type':'SIGNED_CODE'
} 

win_http = win32com.client.Dispatch('WinHTTP.WinHTTPRequest.5.1')
win_http.Open("POST", url, False)
win_http.SetRequestHeader("Content-Type","application/json;charset=UTF-8")
win_http.SetRequestHeader("Accept","application/json;charset=UTF-8")
win_http.Send(json.dumps(params))
win_http.WaitForResponse()
print(win_http.ResponseText)
items  = json.loads(win_http.ResponseText)
"""

# Receive session key
"""url = "https://api.mdlp.crpt.ru/api/v1/token"
paramskey ={
  'code': CodeAuth,
  'signature': sSignedData
}
print(json.dumps(paramskey))
win_http.Open("POST", url, False)
win_http.SetRequestHeader("Content-Type","application/json;charset=UTF-8")
win_http.SetRequestHeader("Accept","application/json;charset=UTF-8")
win_http.Send(json.dumps(paramskey))
win_http.WaitForResponse()
print(win_http.ResponseText)"""
