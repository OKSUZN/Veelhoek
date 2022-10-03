import turtle as t

t.shape("turtle")
t.width(5)

def een_veelhoek(x):        # X = een variabel die kan veranderen bij aanroep, die het aantal hoeken voorsteld , een_cirkel is de functienaam.
    for i in range(x):    # Gekozen x = aantal loops dat ik heb
        t.forward(100)    
        t.left(360/x)     # 360 delen door mijn opgegeven aantal

een_veelhoek(10)     # hier geef ik x een waarde , bij deze 10.

t.mainloop()

