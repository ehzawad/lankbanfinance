# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionMobileRecharge(Action):

    def name(self) -> Text:
        return "action_mobile_recharge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="This is the link from where you can directly recharge your mobile: https://payment.lankabangla.com/login")

        return []
    

class ActionCardCourierProblem(Action):

    def name(self) -> Text:
        return "action_card_courier_problem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hi, please communicate with the concern RM. He is supposed to give you the update. For any other query call 16325.")

        return []
    

class ActionDollarEndorseCapable(Action):

    def name(self) -> Text:
        return "action_dollar_endorse_capable"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        

        dispatcher.utter_message(text="Sorry, you can only used LBFL cards for domestically.")

        return []

class ActionBEFTNFee(Action):

    def name(self) -> Text:
        return "action_beftn_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        

        dispatcher.utter_message(text="Transaction fee 1.5% on total amount to be transferred + 15% vat on transaction fee or BDT 200 whichever is higher will be charged for each fund transfer")

        return []
    
class ActionTransferProcessBEFTN(Action):

    def name(self) -> Text:
        return "action_transfer_process_beftn"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text='For transfer money through BEFTN please call 16325')

        return []
    
class ActionBEFTNsignup(Action):

    def name(self) -> Text:
        return "action_beftn_signup"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text='Please visit given link for BEFTN enrollment process: https://www.lankabangla.com/beftn-platform/')

        return []
    

class ActionDefineBEFTN(Action):

    def name(self) -> Text:
        return "action_define_beftn"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text='BEFTN is a process through which you can transfer your unused Credit Card limit from your LankaBangla Mastercard to your own Bank Account.')

        return []
    

class ActionChequebookFee(Action):

    def name(self) -> Text:
        return "action_chequebook_fee"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text='BDT 200 for 1st book & onward.')

        return []
    

class ActionWrongCardCharge(Action):

    def name(self) -> Text:
        return "action_wrong_card_charge"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text='Please call 16325 or send a mail at myrequest@lankabangla.com for your problem and you get a solution from there.')

        return []
    

# action_various_update

class ActionVariousUpdate(Action):

    def name(self) -> Text:
        return "action_various_update"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text='For card pin or cheque or address change or profile upadate issue please call 16325')


# action_card_delivery_issue

class ActionCardDeliveryIssue(Action):

    def name(self) -> Text:
        return "action_card_delivery_issue"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        
        
        dispatcher.utter_message(text='please communicate with the concern RM. He is supposed to give you the update. For any other issue call 16325.')



# action_credit_care_yearly_charge

class ActionCreditCareYearlyCharge(Action):

    def name(self) -> Text:
        return "action_credit_care_yearly_charge"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        
        
        dispatcher.utter_message(text='If you made 15 transaction in a year then your charge will be free. But if it is less than 15 transaction then charge will be depends on your transaction.')


# action_documents_for_applying_card

class ActionDocumentsForApplyingCard(Action):

    def name(self) -> Text:
        return "action_documents_for_applying_card"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        
        
        dispatcher.utter_message(text='''
                                    Required documents for applying Card -
                                    1. Bank Statement authorization letter or Bank Verification Letter
                                    2. Trade License (Two years Business Length Proof for self-employed)
                                    3. CIB undertaking form
                                    4. Recent Passport size Photograph (Two copy)
                                    5. Business Card, Employee ID Card
                                    6. Salary Certificate or Pay Slip
                                    7. Copy of E-TIN, NID or Passport
                                    ''')   
        



# action_credit_card_payment_via_booth

class ActionCreditCardPaymentViaBooth(Action):

    def name(self) -> Text:
        return "action_credit_card_payment_via_booth"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        
        
        dispatcher.utter_message(text='You can pay LankaBangla Credit Card bills from anywhere using the Standard Chartered ATM Booth.')

# action_credit_card_bill_via_bank

class ActionCreditCardBillViaBank(Action):

    def name(self) -> Text:
        return "action_credit_card_bill_via_bank"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        
        
        dispatcher.utter_message(text='You can pay your credit cards bill through all branches of Dhaka Bank, AB Bank,Mercantile Bank Limited,ONE Bnak,Premier bank.')


#  action_fund_transfer_mobile_wallet

class ActionFundTransferMobileWallet(Action):
    
    def name(self) -> Text:
        return "action_fund_transfer_mobile_wallet"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        
        
        dispatcher.utter_message(text='1.5 percent of total withdrawal amount')



# action_ssl_wireless_payment_service

class ActionSSLWirelessPaymentService(Action):
    
    def name(self) -> Text:
        return "action_ssl_wireless_payment_service"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        
        
        dispatcher.utter_message(text='it depends on through which platform you make payment.')



# action_digital_payment_charges

class ActionDigitalPaymentCharges(Action):
        
    def name(self) -> Text:
        return "action_digital_payment_charges"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        
        
        dispatcher.utter_message(text='To know credit card payment charges please click this link: https://www.lankabangla.com/fees-charge')

# action_digital_payment_process

class ActionDigitalPaymentProcess(Action):

    def name(self) -> Text:
        return "action_digital_payment_process"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:        
        
        dispatcher.utter_message(text='Please follow this link: https://www.lankabangla.com/payment-solutions/')


# action_apply_for_deposit

class ActionApplyForDeposit(Action):

    def name(self) -> Text:
        return "action_apply_for_deposit"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text='Please provide your Name, Phone Number,location  for the purpose of deposit application. Our executive will communicate with you within a short time.')

# action_swasti_documents

class ActionSwastiDocuments(Action):

    def name(self) -> Text:
        return "action_swasti_documents"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text='''
                                    Required documents for applying SWASTI -
                                    • Duly filled application form and KYC form. 
                                    • 2 passport size photograph of applicant(s), nominee(s) attested by the applicant.
                                    • Photocopy of National ID/Voter ID/Passport/Driving License.
                                    • e-Tin.
                                    • Photocopy of National ID of Nominee. 
                                    • Other papers if required in future
                                    Good Health Declaration as per format provided by our designated Life Insurance Company''')
        

# action_protiva_documents

class ActionProtivaDocuments(Action):

    def name(self) -> Text:
        return "action_protiva_documents"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text='''
                                    Required documents for applying Protiva: 
                                    • Application form duly filled & signed
                                    • Recent 02 Passport Size Photographs of both Customer & Legal guardian
                                    • Copy of NID/Passport/ Birth Certificate of both Customer & Legal guardian (one copy).
                                    • National ID Card of Nominee
                                    • Nominee’s Photograph (Attested by the Customer/Legal guardian)
                                    • e-TIN (If any)
                                    • Account payee cheque/ pay order named LANKABANGLA FINANCE LTD.
                                    Good Health Declaration as per format provided by our designated Life Insurance Company''')
        


# action_normal_deposit_documents

class ActionNormalDepositDocuments(Action):

    def name(self) -> Text:
        return "action_normal_deposit_documents"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text='''
                                    Required documents for this deposit: 
                                    • Duly filled application form and KYC form. 
                                    • 2 passport size photograph of applicant(s), nominee(s) attested by the applicant.
                                    •Photocopy of cheque
                                    • Photocopy of National ID/Voter ID/Passport/Driving License.
                                    • e-Tin.
                                    • Photocopy of National ID of Nominee. 
                                    • Other papers if required in future ''')
        

# action_agroj_customer_age

class ActionAgrojCustomerAge(Action):

    def name(self) -> Text:
        return "action_agroj_customer_age"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text='This deposit scheme customised for our senior citizen age 50+')


# action_interest_related_query

class ActionInterestRelatedQuery(Action):

    def name(self) -> Text:
        return "action_interest_related_query"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text='To know more about interest rate please visit https://www.lankabangla.com/rate-of-interest/#deposit')



# action_account_details

class ActionAccountDetails(Action):

    def name(self) -> Text:
        return "action_account_details"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text='To know your account details please call 16325')


# action_deposit_amount_pay

class ActionDepositAmountPay(Action):

    def name(self) -> Text:
        return "action_deposit_amount_pay"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text='For deposit payment please visit https://www.lankabangla.com/fees-charge')



# action_deposit_payment_solution

class ActionDepositPaymentSolution(Action):

    def name(self) -> Text:
        return "action_deposit_payment_solution"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text='For deposit payment solution please visit https://www.lankabangla.com/payment-solutions/')


# action_take_loan
class ActionTakeLoan(Action):
    def name(self) -> Text:
        return "action_take_loan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='Please provide your Name, Phone Number,location  for the purpose of loan application. Our executive will communicate with you within a short time.')





# action_payment_update_time
class ActionPaymentUpdateTime(Action):
    def name(self) -> Text:
        return "action_payment_update_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='It will take one working day to update the payment. Ex. If customer make payment on Sunday it will adjust to the balance on Monday after 6 PM')


# action_applicable_charge
class ActionApplicableCharge(Action):
    def name(self) -> Text:
        return "action_applicable_charge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='0.80% (Including VAT) on actual amount as a service fee.')

# action_payment_amount_limit
class ActionPaymentAmountLimit(Action):
    def name(self) -> Text:
        return "action_payment_amount_limit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='There is no fixed minimum amount. You can pay any amount as you want as per Nagad personal wallet limit (wallet limit is BDT 200000).')

# action_documents_for_loan
class ActionDocumentsForLoan(Action):
    def name(self) -> Text:
        return "action_documents_for_loan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='''
                                    Required documents for loan: 
                                    •Application form duly filled & signed
                                    •Valid photo ID (Nid/passport/driving license
                                    • e-TIN Certificate along with IT-10B
                                    •Valid attested photo of applicant & guarantors
                                    •Bank statement last 12 month 
                                    •Other papers if required in future''')


# action_emi_settlement_outstanding
class ActionEmiSettlementOutstanding(Action):
    def name(self) -> Text:
        return "action_emi_settlement_outstanding"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='To know your EMI settlement please call 16325')

# action_interest_rate_home_loan
class ActionInterestRateHomeLoan(Action):
    def name(self) -> Text:
        return "action_interest_rate_home_loan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='our home loan interst rate is 10.99%')

# action_interest_rate_housing_loan
class ActionInterestRateHousingLoan(Action):
    def name(self) -> Text:
        return "action_interest_rate_housing_loan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='Our affordable housing loan interst rate is 11.99%')


# action_interest_rate_property_loan
class ActionInterestRatePropertyLoan(Action):
    def name(self) -> Text:
        return "action_interest_rate_property_loan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='Our loan against property loan interst rate is 11.49%')

# action_home_loan_other_charges
class ActionHomeLoanOtherCharges(Action):
    def name(self) -> Text:
        return "action_home_loan_other_charges"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='At actual plus 15% Vat')


# action_home_loan_processing_fee
class ActionHomeLoanProcessingFee(Action):
    def name(self) -> Text:
        return "action_home_loan_processing_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='At actual plus 15% Vat')

# action_penal_interest_charge
class ActionPenalInterestCharge(Action):
    def name(self) -> Text:
        return "action_penal_interest_charge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='2% Above the lending rate')


# action_personal_loan_for_salaried_person
class ActionPersonalLoanForSalariedPerson(Action):
    def name(self) -> Text:
        return "action_personal_loan_for_salaried_person"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='our personal loan interst rate is 11.99%')

# action_personal_loan_for_land_lord
class ActionPersonalLoanForLandLord(Action):
    def name(self) -> Text:
        return "action_personal_loan_for_land_lord"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='our personal loan land lord/lady interst rate is 13.99%')

# action_personal_Loan_for_unsecured_businessperson
class ActionPersonalLoanForUnsecuredBusinessperson(Action):
    def name(self) -> Text:
        return "action_personal_Loan_for_unsecured_businessperson"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='our personal loan (bonik) interst rate is 14.99%')

# action_tdr_against_short_term_loan_rate
class ActionTdrAgainstShortTermLoanRate(Action):
    def name(self) -> Text:
        return "action_tdr_against_short_term_loan_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='2% plus TDR rate')


# action_define_finsmart
class ActionDefineFinsmart(Action):
    def name(self) -> Text:
        return "action_define_finsmart"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='It’s a Mobile App of LBFL.')

# action_finsmart_app_issue
class ActionFinsmartAppIssue(Action):
    def name(self) -> Text:
        return "action_finsmart_app_issue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='Please unstall your existing FinSmart App then Again Install the app.')

# action_finsmart_registration_process
class ActionFinsmartRegistrationProcess(Action):
    def name(self) -> Text:
        return "action_finsmart_registration_process"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='For the registation process of FinSmart visit: https://www.lankabangla.com/finsmart')
