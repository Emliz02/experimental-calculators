"""
My experimental difference calculator
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

def decimalize( x ):
    return float( "0." + str( x ) )

def cut_around_zeroes( string ):
    if len(string) > 1:
        result = string
        found_non_zero = False
        current_character = 0
        
        while not found_non_zero or current_character < len( result ):
            if not result[ current_character ] == "0":
                found_non_zero = True
                break
            
            current_character += 1

        return result[ current_character : len( result ) ]
    else:
        return string

#see Concept - How can we identify which number is larger.txt
def estimate_size( base, decimal = [0] ):
    base_0 = base[ 0 ]
    decimal_0 = decimal[ 0 ]
    base_l = len( base )
    decimal_l = len( decimal )
    
    result = ( base_0 * base_l ) + decimalize( decimal_0 * decimal_l )
    return result

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
is_decimal = False

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
    
    is_decimal = True

#turn them into number arrays
x = to_num_array( x )
y = to_num_array( y )

if is_decimal:
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
        
if is_decimal:
    if not len(Dx) == len(Dy):
        a = who_is_longer( Dx, Dy )
        b = who_is_shorter( Dx, Dy )

        if b == Dy:
            Dy = equalise_arrays( a, b, True )
        else:
            Dx = equalise_arrays( a, b, True )

#calculate size of numbers
if is_decimal:
    size_of_x = estimate_size( x, Dx )
    size_of_y = estimate_size( y, Dy )
else:
    size_of_x = estimate_size( x )
    size_of_y = estimate_size( y )

if show_every_step:
    print "S(x) = ", size_of_x
    print "S(y) = ", size_of_y

is_negative = True if size_of_x < size_of_y else False

if is_negative:
    _x = x
    _y = y
    
    if is_decimal:
        _dx = Dx
        _dy = Dy
    
    x = _y
    y = _x
    
    if is_decimal:
        Dx = _dy
        Dy = _dx

#reverse them
x.reverse()
y.reverse()

if is_decimal:
    Dx.reverse()
    Dy.reverse()

has_borrowed = False
operation_finished = False

difference = []
decimal_difference = []

#calculate their difference
    
print "---------------------"
    
#base number difference
    
for step in range( len( Dx ) ):
    Xi = Dx[ step ] if not has_borrowed else Dx[ step ] - 1
    Yi = Dy[ step ]
    
    if has_borrowed:
        operation_finished = not operation_finished

    if operation_finished:
        has_borrowed = False
        operation_finished = False
    
    #borrow if X is smaller than Y
    if Xi < Yi:
        Xi += 10
        has_borrowed = True

    tdifference = Xi - Yi
    
    if show_every_step:
        extra_message = " (borrowed) " if has_borrowed else ""
        print "Step (D) ", step + 1, " (", Xi, " - ", Yi, extra_message, " = ", tdifference, " )"
    
    decimal_difference.append( tdifference )
    
#base number difference

for step in range( len( x ) ):
    Xi = x[ step ] if not has_borrowed else x[ step ] - 1
    Yi = y[ step ]
    
    if has_borrowed:
        operation_finished = not operation_finished

    if operation_finished:
        has_borrowed = False
        operation_finished = False
    
    if Xi < Yi:
        Xi += 10
        has_borrowed = True

    tdifference = Xi - Yi
    
    if show_every_step:
        extra_message = " (borrowed) " if has_borrowed else ""
        print "Step (B) ", step + 1, " (", Xi, " - ", Yi, extra_message, " = ", tdifference, " )"
    
    difference.append( tdifference )
    

#and finally, reverse the difference and turn it back into string
difference.reverse()
difference = to_string( difference )

if is_decimal:
    decimal_difference.reverse()
    decimal_difference = to_string( decimal_difference )
    difference = difference + '.' + decimal_difference

difference = cut_around_zeroes( difference )

#show result
print difference if not is_negative else "-" + difference
