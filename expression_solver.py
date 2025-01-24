def equation(eqn):  #for splitting the equation into lhs and rhs
    lhs, rhs = eqn.split("=")
    
    def solving(expr):  #for calculation of all the terms in the equation
        x = 0
        constant = 0
        
        terms = expr.replace("-", "+-").split("+")  #for handling negative terms
        
        for term in terms:
            term = term.strip()
            if term == "X":  # +X
                x += 1
            elif term == "-X":  # -X
                x -= 1
            elif term:  # If it's a constant term
                constant += int(term)
        
        return x, constant
    
    #evaluating lhs and rhs
    lhs_x, lhs_const = solving(lhs)
    rhs_x, rhs_const = solving(rhs)
    
    #solving for x and other terms separately
    x1 = lhs_x - rhs_x
    constant = rhs_const - lhs_const
    
    #check if x1 is 0 to avoid division by zero
    if x1 == 0:
        if constant == 0:
            return "X = 0" 
    
    #solve for X
    x_value = constant / x1
    return x_value

eqn1 = input("")
print(equation(eqn1))