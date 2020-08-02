class ROInvestment:

    def calc_income(self, rental_income, laundry, storage, misc):
        self.rental_income = rental_income
        self.laundry = laundry
        self.storage = storage
        self.misc = misc
        self.income = rental_income + laundry + storage + misc

    def expenses(self,tax, insurance, utilities, HOA, lawn_snow, vacancy, repairs, capex, property_manag, mortage):
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.HOA = HOA
        self.lawn_snow = lawn_snow
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.property_manag = property_manag
        self.mortage = mortage
        self.total_expenses = tax + insurance + utilities + HOA + lawn_snow + vacancy + repairs + capex + property_manag + mortage


    def calc_cash_flow(self):
        self.total_cashflow = self.income - self.total_expenses

    def cash_on_cashROI(self,down_payment,closing_costs,rehab_budget,misc1):
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc1 = misc1
        return (down_payment + closing_costs + rehab_budget + misc1) / self.total_cashflow


total_roinvestment = ROInvestment()  
total_roinvestment.calc_income(30000,700,350,100)
total_roinvestment.expenses(2000,120,450,300,120,140,230,50,60,1200)
total_roinvestment.calc_cash_flow()
final_ROI = total_roinvestment.cash_on_cashROI(20000,200,39,20)
print('{:.1%}'.format(final_ROI))



    