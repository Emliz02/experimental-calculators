"""
My experimental sum calculator
By: Emily Elizabeth Sanchez

emilyelizabethsanchez02@gmail.com
www.github.com/Emliz02
"""

show_every_step = True

def default_decimal( string ):
    return string + ".0" if not '.' in string else string

def delta( a, b ):
    x = a - b
    return x * -1 if x < 0 else x

def to_num_array( string ):
    result = []
 
    for character in string:
        if not character == ".":
            result.append( int( character ) )

    return result

def to_string( array ):
    string = ""

    for item in array:
        string += str( item )

    return string

def who_is_longer( a, b ):
    return a if len(a) > len(b) else b

def who_is_shorter( a, b ):
    return a if len(a) < len(b) else b

def equalise_arrays( array_main, array, should_append = False ):
    updated = array

    size_main = len( array_main )
    size_array = len( updated )

    #we'll only continue if they're not equal
    if size_main == size_array:
        return updated

    #size_delta = how far apart these two arrays are
    size_delta = delta( size_main, size_array )

    #pad list with zeroes
    for _ in range( size_delta ):
        if not should_append:
            updated.insert( 0, 0 )
        else:
            updated.append( 0 )

    return updated
   

x = str( raw_input( "Enter your first number: " ) )
y = str( raw_input( "Enter your second number: " ) )

#D* = decimal partition of a variable
Dx, Dy = "", ""
isDecimal = False

#split them into two parts (if they have decimals)
if '.' in x or '.' in y:
    x = default_decimal( x )
    y = default_decimal( y )
    
    x_parts = x.split( '.' )
    y_parts = y.split( '.' )
    
    #x and y will be the base number part
    x = x_parts[ 0 ]
    y = y_parts[ 0 ]
    
    #Dx and Dy will be the decimal number part
    Dx = x_parts[ len( x_parts ) - 1 ]
    Dy = y_parts[ len( y_parts ) - 1 ]
    
    isDecimal = True

#turn them into number arrays
x = to_num_array( x )
y = to_num_array( y )

if isDecimal:
    Dx = to_num_array( Dx )
    Dy = to_num_array( Dy )

#if x and y are not equal, use "equalise_arrays"
if not len(x) == len(y):
    a = who_is_longer( x, y )
    b = who_is_shorter( x, y )

    if b == y:
        y = equalise_arrays( a, b )
    else:
        x = equalise_arrays( a, b )
        
if isDecimal:
    if not len(Dx) == len(Dy):
        a = who_is_longer( Dx, Dy )
        b = who_is_shorter( Dx, Dy )

        if b == Dy:
            Dy = equalise_arrays( a, b, True )
        else:
            Dx = equalise_arrays( a, b, True )

#reverse them
x.reverse()
y.reverse()

if isDecimal:
    Dx.reverse()
    Dy.reverse()

carried_value = 0
sum = []
decimalSum = []

#calculate their sum

#decimal sum

if isDecimal:
    for step in range( len( Dx ) ):
        Xi = Dx[ step ]
        Yi = Dy[ step ]
        tsum = Xi + Yi + carried_value
        
        if show_every_step:
            extra_message = " carry 1 " if carried_value == 1 else ""
            print "Step (D) ", step + 1, " (", Xi, " + ", Yi, extra_message, " = ", tsum, " )"

        #do we need to carry?
        carried_value = 1 if tsum > 9 else 0

        if tsum > 9:
            temporary_tsum = str( tsum )
            length = len( temporary_tsum )

            last_character = temporary_tsum[ length - 1 ]
            tsum = last_character  
            
        decimalSum.append( tsum )

#add newline    
print
    
#base number sum
    
for step in range( len( x ) ):
    Xi = x[ step ]
    Yi = y[ step ]
    tsum = Xi + Yi + carried_value
    last_step = ( step == ( len(x) - 1 ) )
    
    if show_every_step:
        extra_message = " carry 1 " if carried_value == 1 else ""
        print "Step (B) ", step + 1, " (", Xi, " + ", Yi, extra_message, " = ", tsum, " )"

    #do we need to carry?
    carried_value = 1 if tsum > 9 else 0

    if tsum > 9 and not last_step:
        temporary_tsum = str( tsum )
        length = len( temporary_tsum )

        last_character = temporary_tsum[ length - 1 ]
        tsum = last_character  

    sum.append( str( tsum ) )

#and finally, reverse the sum and turn it back into string
sum.reverse()
sum = to_string( sum )

if isDecimal:
    decimalSum.reverse()
    decimalSum = to_string( decimalSum )
    sum = sum + '.' + decimalSum

#show result
print sum
