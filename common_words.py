def checkio(first, second):
    first = first.split(',')
    second = second.split(',')
    first = [s for s in first if s in second]
    return ','.join(sorted(first))
 
        

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
