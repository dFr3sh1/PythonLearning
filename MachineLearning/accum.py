def accum(s):
    compteur = 1
    chain_upper_lower = []
    for char in s:
        chain_upper_lower.append((char*compteur).capitalize())
        compteur += 1
    end_chain_upper_lower = '-'.join(chain_upper_lower)
        
    return end_chain_upper_lower

accum("yes")
print(accum("yes"))

# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# def accum(s):
    # return '-'.join((a * i).title() for i, a in enumerate(s, 1))

# def accum(s):
#     output = ""
#     for i in range(len(s)):
#         output+=(s[i]*(i+1))+"-"
#     return output.title()[:-1]

# def accum(s):
#     i = 0
#     result = ''
#     for letter in s:
#         result += letter.upper() + letter.lower() * i + '-'
#         i += 1
#     return result[:len(result)-1]

# def accum(s):
#     return "-".join([((j*(i+1)).capitalize()) for i,j in enumerate(s)])

# def accum(s):
#     str = ""
#     for i in range(0, len(s)):
#         str += s[i].upper()
#         str += s[i].lower()*i
#         if i != len(s)-1:
#             str += "-"
#     return str

# def accum(s):
#     value = ""
#     for i,c in enumerate(s):
#         value += c.upper() + c.lower()*i + "-"
#     return value[:-1]

# def accum(s):
#     a = list(s)
#     res = ""
#     for i, c in enumerate(a):
#         res += c * (i + 1) + "-"
#     return res.strip("-").title()

# def accum(s):
#     counter = 0
#     output = ""
#     for letter in s:
#         output += letter.upper() + letter.lower() * counter + '-'
#         counter += 1
#     return output[:-1]

# def accum(s):
#     return "-".join(c * (i+1) for i, c in enumerate(s)).title()

# accum = lambda s : '-'.join((ch*(i+1)).capitalize() for i,ch in enumerate(s))