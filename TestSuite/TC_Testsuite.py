import unittest

from AgodaSignIn.TC_SignInEmail import SigninEmail
from AgodaSignIn.TC_SignInMobile import SigninMobile
from AgodaLoginLogut.TC_LoginEmail import LoginEmail
from AgodaLoginLogut.TC_LoginMobile import LoginMobile
from AgodaBookingDates.TC_DayBooking import DayUseStay
from AgodaBookingDates.TC_NightBooking import OvernightStay
from AgodaSelectHotel.TC_DayHotel import DayHotelSelect
from AgodaSelectHotel.TC_NightHotel import NightHotelSelect
from AgodaPayment.TC_AgodaPaymentPage import PaymentPage

TC_001 = unittest.TestLoader().loadTestsFromTestCase(SigninEmail)
TC_002 = unittest.TestLoader().loadTestsFromTestCase(SigninMobile)
TC_003 = unittest.TestLoader().loadTestsFromTestCase(LoginEmail)
TC_004 = unittest.TestLoader().loadTestsFromTestCase(LoginMobile)
TC_005 = unittest.TestLoader().loadTestsFromTestCase(DayUseStay)
TC_006 = unittest.TestLoader().loadTestsFromTestCase(OvernightStay)
TC_007 = unittest.TestLoader().loadTestsFromTestCase(DayHotelSelect)
TC_008 = unittest.TestLoader().loadTestsFromTestCase(NightHotelSelect)
TC_009 = unittest.TestLoader().loadTestsFromTestCase(PaymentPage)

sanityTest = unittest.TestSuite([TC_001, TC_002, TC_003, TC_004])
functionalTest = unittest.TestSuite([TC_005, TC_006, TC_007, TC_008, TC_009])

unittest.TextTestRunner().run(sanityTest)
unittest.TextTestRunner().run(functionalTest)
