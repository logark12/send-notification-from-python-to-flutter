from lib2to3.pgen2 import token
import FCMManager as fcm
from firebase_admin import db

tes2 = "SqNoEk5TtGHEFDN9NSEaa:APA91bFdZrhjFJaPWzq9LFg5r1INT21wSjRfpl7hGPVANHyaa_MDNc3DPoKQKAD0gK9fNHxsF6fLnzB37mIRJN2GJ2r-KitWQdfmPCd1OFDhA8JrwUeEm93AkC5nSKPWTR2Fu3w42lWS"
test = "cSzHXZT2S6maFXgNTB_YXP:APA91bH2uGaU2jF74_2p5zCsU00BhwMIlujnRrlX1s_PbVzMYepQFgjXC2BV6farDBlnG-FuLzWGgY03nEXaUDpY7scjqGVa0tRnjTQc709KBj4pPNBdFobWHsCrVddBAEjn6tqggWWe"
not_test_mob = "cOph-2MwTaCarUhByXLYr3:APA91bGbVd7as_ZIwHbaNN-z4z3dNsNY2YVo9jV9w1oHOFcgt_WQkwQr7Ktb0FMthSbLAwE49TrdOK9iOdsSnYjk5v8F8NgU6HAPA4BY-NOQn1eOgjhQVgWkCzcRNLoc5ymRXCbFs2R7"
auth_app_im = "eEennTk8SKKXZ-mQq2d8gX:APA91bEFwJCmCP0wJVPqw-dwWwBdG0G9K0HWJljuNihqcisN44tdvxs_Qjo_IEvSjIzZ-NlllprbYJ-c7TfGVEkhrdMJd26mXpQ-ht4ipxfq7oqSL-ycJ9Bfr4Rb0dTyrZ_Pt1-2Tqb8"
auth_app_mob = "dsJFJnMaRxWGWpbXUDe8m1:APA91bEnskfF4cxs-VHRnZnN84hv0FO9NhT68wFe7bD7Mmu87wHiVmqwvHpgh_b301R8xVA6Rtf8xQ6dc-L1JawrnSLf55TskBmGRUCzqhvzUovNSMFrNhHssI9Aj6CzuoWG8pC7Mbht"
# tokens = [auth_app_im]

last = 'fhL1oNQlT9CUX9WXrNjODn:APA91bECqgo-nz-uVxqkKojenxzjI2DcDxTJoH3ggxeuFPnpaZPl3MZZA5rseTt1RhaRydHeLdIyv-usLYnBNSX1TXg0YijzewRV-3Ir4u-HhjTkbGi3uBVjKV8K7Bx_pZm1k05lOGAN'

ref = db.reference("/")

mob_token = ref.get()

tokens = set()

for x in mob_token:
	if(mob_token[x]["useraprove"]):
		tokens.add(str(mob_token[x]["token"]))

tokens = list(tokens)
print(tokens)
fcm.sendPush("EspD server", "motion detected blah", tokens)



