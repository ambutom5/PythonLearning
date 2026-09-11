def fun(**kwargs):
    for k, v in kwargs.items():
        print("%s == %s" % (k, v))

fun(s1='Geeks', s2='for', s3='Geeks')