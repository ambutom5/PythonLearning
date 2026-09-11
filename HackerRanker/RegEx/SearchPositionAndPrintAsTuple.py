import re

st = re.search("th","Python Program")
if st:
    result = (st.start(),st.end())

else:
    result = (-1,-1)

print(result)
