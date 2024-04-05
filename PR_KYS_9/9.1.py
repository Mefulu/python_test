import re


def main(a):
    b = (r"do\s*global\s*[raorge\s*.\s*riza\s*]\s*==>\s*@(\w*);\s*end.\s*do\s*global[dima\s*.\s*vetier_614\s*]\s*==>\s+@(\w*);\s*end.\s*")
    res = re.findall(b, a)
    output = [(row[2], row[0:2]) for row in res]
    return output


a = ("<section> do global [raorge . riza ] ==> @'telaes_394'; end. do global[dima . vetier_614 ] ==> @'laar_116'; end. "
     "</section>")
print(main(a))
