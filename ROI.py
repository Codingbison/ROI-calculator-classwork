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
        self.expenses = tax + insurance + utilities + HOA + lawn_snow + vacancy + repairs + capex + property_manag + mortage


    def calculate_total_cash_flow(self, total_monthly_expenses):
    
        self.total_monthly_expenses = total_monthly_expenses
        self.total_cash_flow = self.income - self.expenses


    def cash_on_cashROI(self,down_payment,closing_costs,rehab_budget,misc):
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc = misc
        return (down_payment + closing_costs + rehab_budget + misc) / self.total_cash_flow

    