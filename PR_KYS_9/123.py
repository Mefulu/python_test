import re

a = """||<sect> data array( @'cebi_815'; @'geso'; @'usla_563' ) to 
q(dite_207);</sect>;<sect> data array( @'zaatus_229' ; @'ave'; @'enre' 
)to q(raat); </sect>;||"""
c = r"array\s*\(\s*@'(\w*)'\s*;\s*@'(\w*)'\s*;\s*@'(\w*)'\s*\)\s*to\s*q\((\w*)"
res = re.findall(c, a)
output = [(row[3], row[0:3]) for row in res]
print(output)

b = """||<sect> data array( @'ated'; @'enso_554' ; @'edes_177') to 
q(lazaer);</sect>; <sect> data array( @'rela_539'; @'raradi' ; 
@'maques_294') to q(rive); </sect>; <sect> data array( @'vege_713' 
;@'dier_208' ; @'eraxela' ) to q(erqu_432); </sect>; ||"""
res = re.findall(c, b)
output = [(row[3], row[0:3]) for row in res]
print(output)
