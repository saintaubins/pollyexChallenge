#####################################################################################
########################   This is my loan payment calculator   #####################
#####################################################################################

class LoanPaymentCalc:

    def __init__(self, amount, interest, downpayment, term):

        ''' Input for the calculator values '''
        self.amount = amount
        self.interest = interest
        self.downpayment = downpayment
        self.term = term

        ''' Some error handleing for human error cases '''
        if type(self.amount) != int:
            raise TypeError('Please enter a valid loan amount.')
        
        if type(self.term) != int:
            raise TypeError('Please enter a valid loan term, in years.')

        if type(self.interest) != float:
            raise TypeError('Please enter a valid interest rate, in percent with at least one decimal place.')

        if self.amount <= 0:
            raise ValueError('Please provide a valid number, it cannot be negative or zero.')

        if self.downpayment < 0:
            raise ValueError('Sorry the downpayment cannot be less than 0.')


    ''' Helper functions start here '''
    def __get_amount(self):
        return(self.amount)
    
    def __get_interest(self):
        return(self.interest)
    
    def __get_downpayment(self):
        return(self.downpayment)

    def __get_term(self):
        return(self.term)

    ''' Function to get monthly payment starts here '''
    def __get_monthly_payment(self, amount, interest, downpayment, term):

        ''' n is the number of payments '''
        n = 12 * self.term

        ''' r is interest rate (variable interest) converted to decimal and divided by 12 '''
        r = (self.interest / 100) / 12

        ''' value of the numenrator for the total loan cost '''
        numerator = self.amount - self.downpayment

        ''' value of the denominator for the total loan cost '''
        denominator = (((1+r)**n) -1) / (r*(1 + r)**n)

        ''' calculation of the monthly payment is numerator on the denominator '''
        monthly_payment =  numerator / denominator

        return(monthly_payment)

    ''' Function to get total interest starts here '''
    def __get_total_interest(self, amount, downpayment, term, monthly_pay):

        ''' This computes the loan amount or amount being financed '''
        loan_amount = self.amount - self.downpayment

        ''' This will get the monthly payments from the already computed function above '''
        monthly_p = monthly_pay

        ''' This is a variable that will return the amount of months on the loan '''
        length_in_months = 12 *(self.term/10)

        ''' As stated in the variable name total_interest_paid, this will store a computation for the total interest paid '''
        total_interest_paid = (monthly_p * length_in_months * 10) - loan_amount

        return(total_interest_paid)

    ''' Function to get total loan cost starts here '''
    def __get_total_loan_cost(self, term, get_monthly_pay):

        ''' storing fuction variable to local variable '''
        get_mnthly_pay = get_monthly_pay

        ''' computing total cost variable to memory  '''
        total_cost = get_mnthly_pay * 12 * self.term

        return(total_cost)

    ''' This function returns the json type formated data '''
    def __send_json(self, get_monthly_pay, get_total_interest, get_total_loan_cost):

        ''' converting the function variables to local variables '''
        g_mon_pay = get_monthly_pay
        g_t_int = get_total_interest
        g_t_pay = get_total_loan_cost

        ''' Formating the collection of data to a json like structure for iteration '''
        send_jsn = {
            "monthly_payment" : round(g_mon_pay, 2), 
            "total_interest": round(g_t_int, 2),  
            "total_cost": round(g_t_pay, 2)
        }
        return(send_jsn)



#####################################################################################
######################       Constants For Loan Go Here      ########################


''' Initilize the loan payment constants here all are US Dollars for this program '''
principal = 100000   # This value shall be the Loan principal amaount i.e. 100000.
downpayment = 20000   # This value shall be equal to, or greater than 0 i.e. 20000.
term_in_years = 30   # This value shall be in years i.e. 30.
interest_rate_percent = 5.5   # This value shall be in percentage form i.e 5.5.


#######################         End this block       ###############################
####################################################################################


''' Initilizing instance of the class and loading constants to memory '''
loan_calc_instance = LoanPaymentCalc(principal, interest_rate_percent, downpayment, term_in_years)

''' Calling helper functions and allocating space for them in memory '''
get_a = loan_calc_instance._LoanPaymentCalc__get_amount()
get_i = loan_calc_instance._LoanPaymentCalc__get_interest()
get_d = loan_calc_instance._LoanPaymentCalc__get_downpayment()
get_t = loan_calc_instance._LoanPaymentCalc__get_term()

''' Calling main methods to drive the results and allocating them in memory '''
get_monthly_pay = loan_calc_instance._LoanPaymentCalc__get_monthly_payment(get_a, get_i, get_d, get_t)
get_total_iterst = loan_calc_instance._LoanPaymentCalc__get_total_interest(get_a, get_d, get_t, get_monthly_pay)
get_total_pay = loan_calc_instance._LoanPaymentCalc__get_total_loan_cost(get_t, get_monthly_pay)
send_json = loan_calc_instance._LoanPaymentCalc__send_json(get_monthly_pay, get_total_iterst, get_total_pay)


####################################################################################
##################    Confirm Inputs and Outputs are Here     ######################


''' Printing out the results for both inputs and outputs '''
print('get_monthly_payment:',get_monthly_pay)
print('get_total_interest:' , get_total_iterst)
print('get_total_loan_cost:' , get_total_pay)
print('send_json: ', send_json)


#######################         End this block       ###############################
####################################################################################





