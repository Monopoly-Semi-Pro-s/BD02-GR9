# %% [markdown]
# # Week 1
# %% [markdown]
# ## opdracht 2
# Ontwerp inductief een methode om ```n!``` te berekenen


def p(n):
    if n == 1:
        return 1
    else:
        return n * p(n - 1)


p(5)
# p(1) => 1

# p(2) => 2 * 1
# p(2) => 2 * p(1)

# p(3) => 3 * 2 * 1
# p(3) => 3 * 2 * p(1)
# p(3) => 3 * p(2)

# p(n) => n * p(n - 1)
# %% [markdown]
# ## opdracht 3
# Ontwerp inductief een methode om ```3^n``` te berekenen


def p(n):
    if n == 0:
        return 1
    else:
        return 3 * p(n - 1)


p(5)
# p(0) => 1

# p(1) => 3 * 1
# p(1) => 3 * p(0)

# p(2) => 3 * 3 * 1
# p(2) => 3 * 3 * p(0)
# p(2) => 3 * p(1)

# p(n) => 3 * p(n - 1)
# %% [markdown]
# ## opdracht 4
# Sorteer een rij inductief met de strategie decrease and conquer


def p(n):
    if len(n) == 1:
        return n
    else:
        m = max(n)
        del n[n.index(m)]
        return p(n) + [m]


p([3, 5, 2])  # => [2, 3, 5]
# %% [markdown]
# ## opdracht 5
# Sorteer een rij inductief met de strategie divide and conquer


def p(n):
    pass
# %% [markdown]
# ## opdracht 6
# Implementeer de functie machtsverheffen (exponent n= 0, 1, 2, 3,…) met de
# strategie decrease and conquer, waarbij n niet met een term maar met een
# factor verkleind wordt


def p(n):
    pass

# %% [markdown]
# ## opdracht 7
# Bereken de op een na grootste waarde van een rij. Gebruik indien nodig
# versterking van de IH.


def p(n):
    pass

# %% [markdown]
# ## opdracht 8
# Bepaal wie in een gezelschap de beroemdheid is.  Wees selectief in de wijze
# van verkleinen.
# > Toelichting: een beroemdheid is hier iemand die door elk ander lid van het
# gezelschap gekend wordt maar die zelf niemand van het gezelschap kent
# (behalve zichzelf).


def p(n):
    pass

# %% [markdown]
# ## Overige oefeningen
# Onderzoek het verloop van de grafieken van functies van de onderstaande
# soort en breng een rangorde aan met betrekking tot de big-O-notatie.


from IPython.display import display, SVG  # nopep8
display(SVG("./Big-O.svg"))
# %% [markdown]
# Kleinste
#
# $f_4(x) =  \log_{a}⁡(x)$
#
# =>
# $f_3(x) = \sqrt[n]{x}$
#
# =>
# $f_1(x) = x^n$
#
# =>
# $f_5(x) = x ^ n∙log⁡(x)$
#
# =>
# $f_2(x) = a^x$
#
# =>
# $f_6(n) = n!$
#
# Grootste
# %%
