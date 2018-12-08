def decorate(func):
    print("Je suis dans la fonction 'decorate' et je décore '%s.'" % func.__name__)
    def wrapper(*args, **kwargs):
        print ("Je suis dans la fonction 'wrapper' qui accède aux arguments de '%s'." % func.__name__)
        a = list(args)
        a.reverse()
        print("J'en donne la preuve, je peux les inverser : %s." % ', '.join(a))
        print("Exécution de la fonction '%s'." % func.__name__)

        print("Je peux effectuer, ici, un post-traitement.")
        return func
    return wrapper

# Notre fonction décorée
@decorate
def foobar(*args):
    print( ", ".join(args))

