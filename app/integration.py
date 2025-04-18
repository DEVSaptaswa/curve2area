def integrate(f, a, b, n=1000):
    h = (b-a)/n
    area = 0.5*(f(a)+f(b))

    for i in range(n):
        x = a + i*h
        area += f(x)
    
    area*=h
    return round(area, 3)