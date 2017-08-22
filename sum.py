"""
My experimental sum calculator
By: Emily Elizabeth Sanchez

emilyelizabethsanchez02@gmail.com
www.github.com/Emliz02
"""

show_every_step = True

def delta( a, b ):
    x = a - b
    return x * -1 if x < 0 else x

def to_num_array( string ):
    result = []
 
    for character in string:
        
        #only add it if we succeeded in conversion
        if int( character ):
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

def equalise_arrays( array_main, array ):
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
        updated.insert( 0, 0 )

    return updated
   

x = str( raw_input( "Enter your first number: " ) )
y = str( raw_input( "Enter your second number: " ) )

#turn them into number arrays
x = to_num_array( x )
y = to_num_array( y )

#if x and y are not equal, use "equalise_arrays"
if not len(x) == len(y):
    a = who_is_longer( x, y )
    b = who_is_shorter( x, y )

    if b == y:
        y = equalise_arrays( a, b )
    else:
        x = equalise_arrays( a, b )

#reverse them
x.reverse()
y.reverse()

carried_value = 0
sum = []

#calculate their sum
for step in range( len( x ) ):
    Xi = x[ step ]
    Yi = y[ step ]
    tsum = Xi + Yi + carried_value
    last_step = ( step == ( len(x) - 1 ) )
    
    if show_every_step:
        extra_message = " carry 1 " if carried_value == 1 else ""
        print "Step ", step + 1, " (", Xi, " + ", Yi, extra_message, " = ", tsum, " )"

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

#show result
print sum
