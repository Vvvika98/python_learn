'''
Bob only ever answers one of five things:

    "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
    "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
    "Whatever." This is what he answers to anything else.
'''


def response(hey_bob):
    res = hey_bob.strip()
    # print(res)
    if res.isupper() and res.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if res.endswith("?"):
        return "Sure."
    if res.isupper():
        return "Whoa, chill out!"
    if res.isspace() or len(res) == 0:   
        return "Fine. Be that way!"
    return "Whatever."





# print(response("fffbbcbeab?"))  #Sure
# print(response("Okay if like my  spacebar  quite a bit?   ")) #"Sure."!!!!!!!!!!!!!!!!!!!!

# print(response("FCECDFCAAB"))   #Whoa, chill out

# print(response("WHAT'S GOING ON?"))   #Calm down, I know what I'm doing 

# print(response(""))             #"Fine. Be that way!" !!!!!!!!!!!!!!
# print(response("          "))   #Fine. Be that way!

# print(response("Hi there!"))    #Whatever







